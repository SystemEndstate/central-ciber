"""Central Ciber: segurança (Vol. 01) e caça a bugs (Vol. 02) num repositório.

Uso:
  ciber.py init      [--repo P]                 cria .ciber/ (liga o hook de commit neste repo)
  ciber.py perfil    [--repo P] [--json]        stack detectada + domínios/módulos que se aplicam
  ciber.py scan      [--repo P] [--diff] [--json] [--todas]
                     varredura determinística (sem IA). --diff: só linhas novas/alteradas.
                     exit 1 se houver achado de confiança "alta" (bloqueante)
  ciber.py controles [--dominio X] [--p0] [--repo P --aplicaveis]   lista controles do Vol. 01
  ciber.py cenarios  [--modulo X]  [--p0] [--repo P --aplicaveis]   lista cenários do Vol. 02
  ciber.py backlog   [--repo P] [--bugs] [--render]   cria/atualiza .ciber/backlog.json (+ .md)
  ciber.py status    ID STATUS [--evidencia "..."] [--repo P]   ok|falha|pendente|manual|bloqueado|na|inconclusivo
  ciber.py ignorar   FINGERPRINT --motivo "..." [--repo P]      aceita um achado (falso positivo)
  ciber.py release   [--repo P]                   gate: scan sem "alta" + nenhum P0 em falha/pendente

Exit: 0 ok · 1 achado bloqueante / gate reprovado · 2 erro de uso
"""
import argparse
import base64
import datetime
import fnmatch
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")
STATUS = ("ok", "falha", "pendente", "manual", "bloqueado", "na", "inconclusivo")
SKIP_DIRS = ("node_modules/", "vendor/", "dist/", "build/", ".next/", "coverage/", ".git/", "graphify-out/",
             ".claude/", ".ciber/", ".regressao/", "Pods/", ".gradle/", "target/", "__pycache__/", ".venv/", "venv/")
TEXT_EXT = (".go", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".vue", ".svelte", ".py", ".rb", ".php", ".java",
            ".kt", ".kts", ".swift", ".m", ".cs", ".rs", ".sql", ".json", ".yaml", ".yml", ".toml", ".xml", ".plist",
            ".env", ".sh", ".ps1", ".html", ".gradle", ".properties", ".conf", ".ini", ".tf", ".dart")
TEXT_NAMES = ("Dockerfile", "docker-compose.yml", "docker-compose.yaml", "Containerfile", ".env")


# ---------- utilidades ----------

def run(cmd, cwd, timeout=120):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                           timeout=timeout)
        return r.returncode, r.stdout
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return 1, ""


def repo_root(path):
    code, out = run(["git", "rev-parse", "--show-toplevel"], path)
    return os.path.normpath(out.strip()) if code == 0 and out.strip() else None


def cdir(root):
    return os.path.join(root, ".ciber")


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


def tracked(root):
    _, out = run(["git", "ls-files", "-co", "--exclude-standard"], root)
    return [f.replace("\\", "/") for f in out.splitlines() if f.strip()]


def is_test(path):
    p = path.lower()
    return bool(re.search(r"(_test\.go|\.test\.|\.spec\.|/tests?/|/__tests__/|/e2e/|/fixtures?/|/testdata/|/mocks?/)", p))


def is_text(path):
    b = os.path.basename(path)
    return b in TEXT_NAMES or b.startswith(".env") or path.lower().endswith(TEXT_EXT)


def skip(path):
    p = "/" + path
    return any(("/" + d) in p for d in SKIP_DIRS)


def read(root, f):
    try:
        with open(os.path.join(root, f), encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return ""


# ---------- perfil ----------

def perfil(root):
    files = [f for f in tracked(root) if not skip(f)]
    names = {os.path.basename(f) for f in files}
    pkgs = ""
    for f in files:
        b = os.path.basename(f)
        if b in ("package.json", "go.mod", "requirements.txt", "pyproject.toml", "Gemfile", "pubspec.yaml",
                 "build.gradle", "build.gradle.kts", "Podfile", "Cargo.toml", "composer.json") or f.endswith(".csproj"):
            pkgs += read(root, f).lower() + "\n"
    has = lambda *ws: any(w in pkgs for w in ws)
    anyf = lambda pat: any(fnmatch.fnmatch(f, pat) for f in files)
    sql = [f for f in files if f.endswith(".sql")]
    stack = {
        "frontend_web": has('"react"', '"vue"', '"svelte"', '"next"', '"vite"', "@angular/core", '"nuxt"'),
        "backend": "go.mod" in names or has("express", "fastify", "@nestjs", "django", "flask", "fastapi", "rails",
                                             "laravel", "spring-boot", "koa", "hono"),
        "postgres": bool(sql) or has("pgx", "lib/pq", '"pg"', "psycopg", "postgres", "prisma"),
        "supabase": anyf("supabase/*") or has("@supabase/", "supabase") or
                    any("auth.uid()" in read(root, f) or "supabase" in f.lower() for f in sql[:400]),
        "aws": has("aws-sdk", "@aws-sdk/", "boto3", "aws-cdk", "github.com/aws/") or anyf("*.tf") or
               "serverless.yml" in names or "template.yaml" in names,
        "containers": "Dockerfile" in names or any(n.startswith("docker-compose") for n in names) or
                      any(n.startswith("Dockerfile") for n in names),
        "android": anyf("*AndroidManifest.xml") or has("com.android.application"),
        "ios": anyf("*Info.plist") or "Podfile" in names or anyf("*.xcodeproj/*"),
        "capacitor": has("@capacitor/"),
        "react_native": has('"react-native"', '"expo"'),
        "flutter": "pubspec.yaml" in names,
        "electron": has('"electron"'),
        "tauri": has("@tauri-apps/", "tauri"),
        "dotnet_desktop": any(f.endswith(".csproj") for f in files) and has("winexe", "usewpf", "usewindowsforms", "winui"),
        "pagamentos": has("stripe", "asaas", "mercadopago", "pagarme", "pagseguro", "efipay", "gerencianet") or
                      any(re.search(r"(payment|pagamento|billing|pix|checkout|asaas|stripe)", f, re.I) for f in files),
        "ia": has("openai", "@anthropic-ai", "anthropic", "langchain", "openrouter", "@modelcontextprotocol",
                  "google-generativeai", "ollama"),
        "uploads": any(re.search(r"(upload|storage|media|bucket|s3)", f, re.I) for f in files),
        "offline_pwa": anyf("*sw.js") or anyf("*service-worker*") or has("workbox", "vite-plugin-pwa", "localforage",
                                                                          "dexie", "@capacitor/preferences"),
        "realtime": has("socket.io", '"ws"', "gorilla/websocket", "nhooyr.io/websocket", "pusher") or
                    any(re.search(r"(realtime|websocket|sse)", f, re.I) for f in files),
    }
    mobile = stack["android"] or stack["ios"] or stack["capacitor"] or stack["react_native"] or stack["flutter"]
    desktop = stack["electron"] or stack["tauri"] or stack["dotnet_desktop"]
    v1 = ["CORE", "DEV", "MON", "PRIV", "BUG", "UX", "TST", "QA", "REL", "POL"]
    v2 = ["DISC", "OBS", "CI", "UX"]
    web = stack["frontend_web"] or stack["backend"]
    if web:
        v1 += ["ID", "SES", "ROT", "WEB", "API"]
        v2 += ["AUTH", "API", "NET", "PERF"]
    if stack["frontend_web"]:
        v2 += ["WEB", "FRONT", "I18N"]
    if stack["backend"]:
        v2 += ["BACK"]
    if stack["postgres"]:
        v1 += ["DB"]; v2 += ["DB"]
    if stack["supabase"]:
        v1 += ["SUP"]; v2 += ["SUP"]
    if stack["aws"]:
        v1 += ["AWS"]; v2 += ["AWS"]
    if stack["containers"] or stack["backend"]:
        v1 += ["INF"]
    if stack["uploads"]:
        v1 += ["FIL"]; v2 += ["FILE"]
    if stack["ia"]:
        v1 += ["AI"]; v2 += ["AI"]
    if stack["pagamentos"]:
        v2 += ["PAY"]
    if mobile or stack["offline_pwa"]:
        v1 += ["OFF"]; v2 += ["OFF"]
    if mobile:
        v1 += ["MOB", "LAB", "TEC"]
    if stack["android"] or stack["capacitor"] or stack["react_native"] or stack["flutter"]:
        v1 += ["AND"]; v2 += ["AND"]
    if stack["ios"] or stack["capacitor"] or stack["react_native"] or stack["flutter"]:
        v1 += ["IOS"]; v2 += ["IOS"]
    if desktop:
        v1 += ["DESK", "WIN", "MAC", "LIN", "TEC", "LAB"]; v2 += ["WIN", "MAC", "LNX", "HYBRID", "INSTALL"]
    return {"stack": stack, "dominios_ciber": sorted(set(v1)), "modulos_bugs": sorted(set(v2))}


# ---------- regras do scan ----------
# confianca: "alta" = bloqueia commit (quase sem falso positivo); "revisar" = o Claude confere

R = []


def rule(id_, controles, pri, conf, desc, pattern, files=None, flags=re.I, no_tests=True, unless=None, frontend=False):
    R.append({"id": id_, "controles": controles, "prioridade": pri, "confianca": conf, "descricao": desc,
              "re": re.compile(pattern, flags), "files": files, "no_tests": no_tests,
              "unless": re.compile(unless, re.I) if unless else None, "frontend": frontend})


PLACEHOLDER = r"(example|exemplo|changeme|your[_-]|<|\$\{|xxx|placeholder|dummy|fake|test)"
# segredos
rule("segredo-aws", ["CORE-09", "DEV-03"], "P0", "alta", "Chave de acesso AWS no código", r"\bAKIA[0-9A-Z]{16}\b", flags=0)
rule("segredo-chave-privada", ["CORE-09", "DEV-03"], "P0", "alta", "Chave privada no repositório",
     r"-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----", flags=0)
rule("segredo-token", ["CORE-09", "DEV-03"], "P0", "alta", "Token/chave de API real no código",
     r"\b(sk_live_[0-9A-Za-z]{20,}|rk_live_[0-9A-Za-z]{20,}|ghp_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9_]{40,}|"
     r"xox[baprs]-[A-Za-z0-9-]{20,}|sk-ant-[A-Za-z0-9_-]{30,}|sk-or-v1-[a-f0-9]{40,}|sk-proj-[A-Za-z0-9_-]{30,}|"
     r"sb_secret_[A-Za-z0-9_-]{20,}|AIza[0-9A-Za-z_-]{35}_SECRET|\$aact_[A-Za-z0-9_]{30,})", flags=0,
     unless=PLACEHOLDER)
rule("supabase-service-no-front", ["SUP-06", "SUP-07", "WEB-06"], "P0", "alta",
     "Chave service_role/secret do Supabase referenciada no código do frontend",
     r"(service_role|SERVICE_ROLE_KEY|sb_secret_|SUPABASE_SECRET)", frontend=True, unless=r"(//|#|--)\s*nunca|never")
rule("env-publica-secreta", ["WEB-06", "CORE-09"], "P0", "alta",
     "Variável pública de bundle (VITE_/NEXT_PUBLIC_/EXPO_PUBLIC_/REACT_APP_) carregando segredo",
     r"\b(VITE|NEXT_PUBLIC|EXPO_PUBLIC|REACT_APP|PUBLIC)_[A-Z0-9_]*(SECRET|SERVICE_ROLE|PRIVATE|PASSWORD|SENHA)[A-Z0-9_]*",
     flags=0)
# transporte
rule("tls-desligado", ["WEB-02", "MOB-03", "CORE-01"], "P0", "alta", "Verificação de certificado TLS desligada",
     r"(InsecureSkipVerify\s*:\s*true|rejectUnauthorized\s*:\s*false|NODE_TLS_REJECT_UNAUTHORIZED\s*=\s*['\"]?0|"
     r"verify\s*=\s*False|ServerCertificateValidationCallback\s*=.*true|setHostnameVerifier\(.*ALLOW_ALL)")
rule("android-cleartext", ["AND-11", "MOB-03"], "P0", "alta", "Android permite HTTP sem TLS",
     r'android:usesCleartextTraffic\s*=\s*"true"|cleartextTrafficPermitted\s*=\s*"true"', files=["*.xml"])
rule("android-debuggable", ["AND-15", "REL-07"], "P0", "alta", "Build Android debuggable",
     r'android:debuggable\s*=\s*"true"', files=["*AndroidManifest.xml"])
rule("android-allowbackup", ["AND-14", "MOB-11"], "P0", "revisar",
     "allowBackup=true: tokens e dados privados podem ir para o backup", r'android:allowBackup\s*=\s*"true"',
     files=["*AndroidManifest.xml"])
rule("android-exported", ["AND-02"], "P0", "revisar", "Componente Android exportado: confirmar que precisa ser público",
     r'android:exported\s*=\s*"true"', files=["*AndroidManifest.xml"])
rule("ios-ats-off", ["IOS-04", "MOB-03"], "P0", "alta", "iOS ATS desligado (NSAllowsArbitraryLoads)",
     r"NSAllowsArbitraryLoads</key>\s*<true\s*/>", files=["*.plist"], flags=re.S)
rule("capacitor-cleartext", ["MOB-03", "TEC-11"], "P0", "alta", "Capacitor com cleartext: true",
     r"cleartext\s*:\s*true", files=["capacitor.config.*"])
rule("capacitor-navegacao-livre", ["MOB-14", "MOB-15", "TEC-11"], "P0", "revisar",
     "WebView do Capacitor navega para qualquer domínio", r"allowNavigation\s*:\s*\[[^\]]*['\"]\*['\"]",
     files=["capacitor.config.*"])
# electron
rule("electron-node", ["TEC-06", "DESK-19"], "P0", "alta", "Electron com nodeIntegration ligado",
     r"nodeIntegration\s*:\s*true")
rule("electron-isolation", ["TEC-06", "DESK-19"], "P0", "alta", "Electron sem contextIsolation",
     r"contextIsolation\s*:\s*false")
rule("electron-websecurity", ["TEC-06"], "P0", "alta", "Electron com webSecurity desligado", r"webSecurity\s*:\s*false")
# sessão / auth
rule("jwt-sem-verificar", ["SES-13", "ID-02", "SUP-08"], "P0", "revisar",
     "JWT lido sem verificar assinatura: confirmar que não decide autorização",
     r"(ParseUnverified\(|jwt\.decode\([^)]*verify_signature['\"]?\s*:\s*False|jwt_decode\(|"
     r"\bjwt\.decode\((?![^)]*verify))", unless=r"jwt\.verify")
rule("cookie-sem-flag", ["SES-01", "SES-02"], "P0", "revisar", "Cookie de sessão sem HttpOnly/Secure",
     r"(HttpOnly\s*:\s*false|httpOnly\s*:\s*false|Secure\s*:\s*false|secure\s*:\s*false)")
rule("token-localstorage", ["WEB-11"], "P0", "revisar", "Token/sessão gravado em localStorage",
     r"localStorage\.setItem\([^)]*(token|jwt|session|auth|refresh)", no_tests=True)
rule("hash-senha-fraco", ["ID-04"], "P0", "alta", "Senha com hash fraco (MD5/SHA1)",
     r"((md5|sha1)\W.{0,40}(password|senha)|(password|senha).{0,40}\W(md5|sha1)\b)")
rule("random-inseguro", ["ID-09"], "P0", "revisar", "Token/código gerado com aleatório não criptográfico",
     r"(Math\.random\(\).{0,60}(token|otp|code|codigo|senha|password|secret|reset)|"
     r"(token|otp|code|codigo|senha|password|secret|reset).{0,60}Math\.random\(\))")
# injeção
rule("sql-concatenado", ["API-02", "CORE-10"], "P0", "revisar",
     "SQL montado com texto interpolado: confirmar que nada vem do usuário",
     r"(Sprintf\(\s*\"[^\"]*\b(SELECT|INSERT|UPDATE|DELETE|WHERE|ORDER BY)\b[^\"]*%[sv]|"
     r"\.(query|raw|execute|unsafe)\(\s*`[^`]*\b(SELECT|INSERT|UPDATE|DELETE|WHERE)\b[^`]*\$\{|"
     r"execute\(\s*f[\"'][^\"']*\b(SELECT|INSERT|UPDATE|DELETE)\b)")
rule("comando-shell", ["API-04", "DESK-10"], "P0", "revisar", "Comando de shell montado dinamicamente",
     r"(exec\.Command\(\s*\"(sh|bash|cmd|powershell)\"\s*,\s*\"(-c|/c|-Command)\"|"
     r"child_process.{0,40}\bexec(Sync)?\(\s*`[^`]*\$\{|\bexecSync\(\s*`[^`]*\$\{|shell\s*=\s*True)")
rule("eval", ["API-14", "WEB-04"], "P0", "revisar", "eval/new Function com conteúdo dinâmico",
     r"(\beval\(\s*[a-zA-Z_]|new Function\()", files=["*.js", "*.ts", "*.tsx", "*.jsx", "*.mjs"])
rule("xss-html", ["WEB-04", "WEB-14", "AI-15"], "P0", "revisar", "HTML cru injetado no DOM: confirmar sanitização",
     r"(dangerouslySetInnerHTML|v-html=|\.innerHTML\s*=|document\.write\()",
     unless=r"(DOMPurify|sanitize|purify|escapeHtml)")
# api / backend
rule("cors-aberto", ["WEB-07"], "P0", "revisar", "CORS liberado para qualquer origem",
     r"(AllowOrigins\s*:\s*\[\]string\{\s*\"\*\"|Access-Control-Allow-Origin\"?\s*,\s*\"\*\"|"
     r"origin\s*:\s*['\"]\*['\"]|AllowAllOrigins\s*:\s*true|allow_origins\s*=\s*\[\s*['\"]\*['\"])")
rule("erro-vazado", ["API-11", "BUG-09"], "P0", "revisar", "Erro interno devolvido ao cliente (err.Error()/stack)",
     r"((c|ctx)\.(JSON|String|AbortWithStatusJSON)\([^)]*err\.Error\(\)|http\.Error\([^,]+,\s*err\.Error\(\)|"
     r"res\.(status\(\d+\)\.)?(json|send)\([^)]*(err|error)\.stack)", files=["*.go", "*.js", "*.ts"])
rule("log-segredo", ["MON-05", "SES-11"], "P0", "revisar", "Log pode gravar senha/token",
     r"(log|logger|console|slog|zap|logrus)\.\w*\([^)]*\b(password|senha|access_token|refresh_token|authorization|"
     r"secret|apikey|api_key)\b(?!\s*[:=]\s*['\"]\*)", unless=r"(mask|redact|\*\*\*)")
rule("dinheiro-float", ["BUG-16", "API-15"], "P0", "revisar",
     "Valor monetário em float: usar inteiro em centavos ou decimal",
     r"(\b(price|amount|total|valor|preco|saldo|balance|fee|taxa|subtotal)\w*\s+float(32|64)\b|"
     r"parseFloat\([^)]*(price|amount|valor|preco|total|saldo)|"
     r"\b(price|amount|valor|preco|saldo|balance)\w*\s*:\s*f(32|64)\b)", files=["*.go", "*.ts", "*.tsx", "*.js", "*.rs"])
rule("modo-debug", ["API-11", "REL-07"], "P0", "revisar", "Modo debug ligado no código",
     r"(gin\.SetMode\(gin\.DebugMode\)|app\.run\([^)]*debug\s*=\s*True|^DEBUG\s*=\s*True)", flags=re.M)
rule("sourcemap-prod", ["OBS-007", "WEB-06"], "P1", "revisar", "Sourcemap publicado em produção",
     r"sourcemap\s*:\s*true", files=["vite.config.*", "next.config.*", "webpack.config.*"])
# infra
rule("docker-segredo", ["INF-06"], "P0", "alta", "Segredo gravado na imagem Docker",
     r"^\s*(ENV|ARG)\s+\w*(PASSWORD|SECRET|TOKEN|API_KEY|PRIVATE_KEY)\w*[= ]\s*\S{6,}", files=["Dockerfile*", "Containerfile*"],
     flags=re.M | re.I, unless=PLACEHOLDER)
rule("porta-banco-exposta", ["INF-03", "CORE-07"], "P0", "revisar",
     "Porta de banco/cache publicada para todas as interfaces",
     r"^\s*-\s*['\"]?(5432|6379|3306|27017|9200|11211):\d+", files=["docker-compose*.yml", "docker-compose*.yaml", "compose*.yml"],
     flags=re.M)
# supabase / sql
rule("grant-anon-tudo", ["SUP-03"], "P0", "alta", "GRANT ALL para anon", r"GRANT\s+ALL[^;]*\bTO\s+[^;]*\banon\b",
     files=["*.sql"])
rule("policy-true", ["SUP-02", "SUP-04"], "P0", "revisar", "Policy RLS liberando tudo (USING/CHECK true)",
     r"CREATE\s+POLICY[^;]*(USING|WITH\s+CHECK)\s*\(\s*true\s*\)", files=["*.sql"], flags=re.I | re.S)


def frontend_file(path):
    p = path.lower()
    if re.search(r"(^|/)(backend|server|api|supabase/functions|functions|cmd|internal|migrations)/", p):
        return False
    return p.endswith((".tsx", ".jsx", ".vue", ".svelte")) or \
        bool(re.search(r"(^|/)(frontend|web|client|apps|src|app|pages|components)/", p)) and \
        p.endswith((".ts", ".js", ".mjs"))


def scan_file(root, f, text, lines_ok):
    out = []
    base = os.path.basename(f)
    for r in R:
        if r["files"] and not any(fnmatch.fnmatch(base, g) or fnmatch.fnmatch(f, g) for g in r["files"]):
            continue
        if r["no_tests"] and is_test(f):
            continue
        if r["frontend"] and not frontend_file(f):
            continue
        if r["unless"] and r["unless"].search(text):
            continue
        for m in r["re"].finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            if lines_ok is not None and line not in lines_ok:
                continue
            src = text.splitlines()[line - 1] if text else ""
            if "ciber-ignore" in src:
                continue
            out.append(finding(r, f, line, src))
    out += jwt_service_role(f, text, lines_ok)
    return out


def finding(r, f, line, src):
    norm = re.sub(r"\s+", " ", src.strip())[:200]
    fp = hashlib.sha1(f"{r['id']}|{f}|{norm}".encode()).hexdigest()[:12]
    return {"regra": r["id"], "controles": r["controles"], "prioridade": r["prioridade"],
            "confianca": r["confianca"], "descricao": r["descricao"], "arquivo": f, "linha": line,
            "trecho": norm, "fingerprint": fp}


JWT = re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.(eyJ[A-Za-z0-9_-]{10,})\.[A-Za-z0-9_-]{10,}")


def jwt_service_role(f, text, lines_ok):
    out = []
    for m in JWT.finditer(text):
        try:
            payload = base64.urlsafe_b64decode(m.group(1) + "=" * (-len(m.group(1)) % 4)).decode("utf-8", "replace")
        except (ValueError, UnicodeError):
            continue
        if '"service_role"' in payload:
            line = text.count("\n", 0, m.start()) + 1
            if lines_ok is None or line in lines_ok:
                out.append(finding({"id": "supabase-service-role-jwt", "controles": ["SUP-06", "SUP-07", "CORE-09"],
                                    "prioridade": "P0", "confianca": "alta",
                                    "descricao": "JWT service_role do Supabase escrito no código"}, f, line, m.group(0)[:20] + "…"))
    return out


def rls_check(root, files, lines_by_file):
    """Supabase: tabela criada em schema exposto sem ENABLE ROW LEVEL SECURITY em nenhuma migração."""
    sql = sorted(f for f in files if f.endswith(".sql") and not is_test(f))
    created, enabled = {}, set()
    cre = re.compile(r"CREATE\s+TABLE\s+(IF\s+NOT\s+EXISTS\s+)?((\"?(\w+)\"?)\.)?\"?(\w+)\"?", re.I)
    ena = re.compile(r"ALTER\s+TABLE\s+(ONLY\s+)?(IF\s+EXISTS\s+)?((\"?(\w+)\"?)\.)?\"?(\w+)\"?\s+ENABLE\s+ROW\s+LEVEL\s+SECURITY", re.I)
    drops = set()
    for f in sql:
        t = read(root, f)
        for m in cre.finditer(t):
            schema = (m.group(4) or "public").lower()
            if schema in ("public",):
                created.setdefault(m.group(5).lower(), (f, t.count("\n", 0, m.start()) + 1, m.group(0)))
        for m in ena.finditer(t):
            enabled.add(m.group(6).lower())
        for m in re.finditer(r"DROP\s+TABLE\s+(IF\s+EXISTS\s+)?((\w+)\.)?\"?(\w+)\"?", t, re.I):
            drops.add(m.group(4).lower())
    out = []
    for tbl, (f, line, src) in created.items():
        if tbl in enabled or tbl in drops or tbl == "schema_migrations":
            continue
        lo = lines_by_file.get(f) if lines_by_file is not None else None
        if lines_by_file is not None and (lo is None or line not in lo):
            continue
        out.append(finding({"id": "supabase-sem-rls", "controles": ["SUP-01", "CORE-08"], "prioridade": "P0",
                            "confianca": "alta", "descricao": f"Tabela public.{tbl} sem ROW LEVEL SECURITY"},
                           f, line, src))
    # SECURITY DEFINER sem search_path fixo
    fn = re.compile(r"CREATE\s+(OR\s+REPLACE\s+)?FUNCTION.*?(\$\w*\$).*?\2[^;]*;", re.I | re.S)
    for f in sql:
        t = read(root, f)
        for m in fn.finditer(t):
            body = m.group(0)
            if re.search(r"SECURITY\s+DEFINER", body, re.I) and not re.search(r"SET\s+search_path", body, re.I):
                line = t.count("\n", 0, m.start()) + 1
                lo = lines_by_file.get(f) if lines_by_file is not None else None
                if lines_by_file is not None and (lo is None or line not in lo):
                    continue
                out.append(finding({"id": "security-definer-sem-search-path", "controles": ["SUP-12"],
                                    "prioridade": "P0", "confianca": "alta",
                                    "descricao": "Função SECURITY DEFINER sem SET search_path"}, f, line,
                                   body.splitlines()[0]))
    return out


def env_tracked(files):
    out = []
    for f in files:
        b = os.path.basename(f)
        if re.fullmatch(r"\.env(\.[\w-]+)?", b) and not re.search(r"(example|sample|template|dist|defaults?)$", b):
            out.append(finding({"id": "env-versionado", "controles": ["CORE-09", "DEV-03"], "prioridade": "P0",
                                "confianca": "alta", "descricao": "Arquivo .env com segredos versionado no git"},
                               f, 1, b))
    return out


def dockerfile_root(root, files):
    out = []
    for f in files:
        if re.fullmatch(r"(Dockerfile|Containerfile)(\.[\w-]+)?", os.path.basename(f)):
            t = read(root, f)
            if t and not re.search(r"^\s*USER\s+(?!root\b)\S+", t, re.M | re.I):
                out.append(finding({"id": "container-root", "controles": ["INF-05"], "prioridade": "P0",
                                    "confianca": "revisar", "descricao": "Contêiner roda como root (sem USER)"},
                                   f, 1, "sem instrução USER"))
    return out


def changed_lines(root):
    _, d = run(["git", "diff", "-U0", "HEAD", "--no-color"], root)
    res, cur = {}, None
    for line in d.splitlines():
        if line.startswith("+++ "):
            p = line[4:].strip()
            cur = None if p == "/dev/null" else p[2:] if p.startswith("b/") else p
        elif line.startswith("@@") and cur:
            m = re.search(r"\+(\d+)(?:,(\d+))?", line)
            start, n = int(m.group(1)), int(m.group(2) or 1)
            res.setdefault(cur, set()).update(range(start, start + n))
    _, u = run(["git", "ls-files", "--others", "--exclude-standard"], root)
    for f in u.splitlines():
        res[f.replace("\\", "/")] = None  # arquivo novo: todas as linhas
    return res


def ignored_set(root):
    p = os.path.join(cdir(root), "ignorar.json")
    try:
        with open(p, encoding="utf-8") as f:
            return {x["fingerprint"] for x in json.load(f)}
    except (OSError, ValueError):
        return set()


def do_scan(root, diff=False):
    allf = [f for f in tracked(root) if not skip(f) and is_text(f)]
    if diff:
        ch = changed_lines(root)
        targets = [f for f in allf if f in ch]
        lines_by_file = {f: ch[f] for f in targets}  # None = arquivo novo, todas as linhas
    else:
        targets, lines_by_file = allf, None
    out = []
    for f in targets:
        t = read(root, f)
        if not t or len(t) > 2_000_000:
            continue
        out += scan_file(root, f, t, None if lines_by_file is None else lines_by_file[f])
    lbf = None if not diff else {f: (v if v is not None else set(range(1, 10 ** 6))) for f, v in lines_by_file.items()}
    out += rls_check(root, allf, lbf) if perfil_cache(root)["stack"]["supabase"] else []
    out += env_tracked(targets)
    out += dockerfile_root(root, targets)
    ign = ignored_set(root)
    seen, res = set(), []
    for x in out:
        if x["fingerprint"] in ign or x["fingerprint"] in seen:
            continue
        seen.add(x["fingerprint"])
        res.append(x)
    order = {"alta": 0, "revisar": 1}
    res.sort(key=lambda x: (order[x["confianca"]], x["prioridade"], x["arquivo"], x["linha"]))
    return res


_PERFIL = {}


def perfil_cache(root):
    if root not in _PERFIL:
        _PERFIL[root] = perfil(root)
    return _PERFIL[root]


# ---------- backlog ----------

def bl_path(root):
    return os.path.join(cdir(root), "backlog.json")


def bl_load(root):
    try:
        with open(bl_path(root), encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {"itens": {}}


def bl_save(root, bl):
    os.makedirs(cdir(root), exist_ok=True)
    with open(bl_path(root), "w", encoding="utf-8") as f:
        json.dump(bl, f, ensure_ascii=False, indent=1)
    render(root, bl)


def render(root, bl):
    it = bl["itens"]
    L = ["# Backlog de segurança e qualidade", "",
         f"Atualizado em {datetime.date.today().isoformat()}. Fonte da verdade: `.ciber/backlog.json` "
         "(editar com `ciber.py status`).", ""]
    cnt = {}
    for v in it.values():
        cnt[v["status"]] = cnt.get(v["status"], 0) + 1
    L.append("Resumo: " + ", ".join(f"{k} {v}" for k, v in sorted(cnt.items())))
    for vol, title in (("ciber", "Vol. 01: controles de segurança"), ("bugs", "Vol. 02: cenários de bug")):
        rows = [(k, v) for k, v in it.items() if v["vol"] == vol]
        if not rows:
            continue
        L += ["", f"## {title}", "", "| ID | Pri | Item | Status | Evidência | Data |", "|---|---|---|---|---|---|"]
        prio = {"falha": 0, "pendente": 1, "inconclusivo": 2, "manual": 3, "bloqueado": 4, "ok": 5, "na": 6}
        rows.sort(key=lambda kv: (prio.get(kv[1]["status"], 9), kv[1]["prioridade"], kv[0]))
        for k, v in rows:
            ev = (v.get("evidencia") or "").replace("|", "/")
            L.append(f"| {k} | {v['prioridade']} | {v['titulo']} | {v['status']} | {ev} | {v.get('data', '')} |")
    with open(os.path.join(cdir(root), "backlog.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


def cmd_backlog(root, a):
    pf = perfil_cache(root)
    bl = bl_load(root)
    n = 0
    for c in load("controles.json")["controles"]:
        if c["dominio"] in pf["dominios_ciber"] and c["id"] not in bl["itens"]:
            bl["itens"][c["id"]] = {"vol": "ciber", "prioridade": c["prioridade"], "titulo": c["controle"],
                                    "status": "pendente"}
            n += 1
    if a.bugs:
        for c in load("cenarios.json")["cenarios"]:
            if c["modulo"] in pf["modulos_bugs"] and c["id"] not in bl["itens"]:
                bl["itens"][c["id"]] = {"vol": "bugs", "prioridade": c["prioridade"], "titulo": c["bug"],
                                        "status": "pendente"}
                n += 1
    bl_save(root, bl)
    print(f"Backlog: {len(bl['itens'])} itens ({n} novos). Ver .ciber/backlog.md")
    return 0


def cmd_status(root, a):
    if a.status not in STATUS:
        print(f"status inválido; use: {', '.join(STATUS)}", file=sys.stderr)
        return 2
    bl = bl_load(root)
    ids = [x.strip() for x in a.id.split(",") if x.strip()]
    for i in ids:
        if i not in bl["itens"]:
            src = {c["id"]: ("ciber", c["prioridade"], c["controle"]) for c in load("controles.json")["controles"]}
            src.update({c["id"]: ("bugs", c["prioridade"], c["bug"]) for c in load("cenarios.json")["cenarios"]})
            if i not in src:
                print(f"ID desconhecido: {i}", file=sys.stderr)
                return 2
            v, p, t = src[i]
            bl["itens"][i] = {"vol": v, "prioridade": p, "titulo": t}
        bl["itens"][i].update({"status": a.status, "data": datetime.date.today().isoformat()})
        if a.evidencia:
            bl["itens"][i]["evidencia"] = a.evidencia
    bl_save(root, bl)
    print(f"{', '.join(ids)} -> {a.status}")
    return 0


# ---------- comandos ----------

def report(res, diff, max_por_regra=5):
    alta = [x for x in res if x["confianca"] == "alta"]
    rev = [x for x in res if x["confianca"] == "revisar"]
    if not res:
        return "Central Ciber: nenhum achado" + (" nas linhas alteradas." if diff else ".")
    L = []
    if alta:
        L.append(f"VULNERABILIDADE: {len(alta)} achado(s) bloqueante(s).")
    L.append(f"Central Ciber: {len(alta)} bloqueante(s), {len(rev)} para revisar.")
    grupos = {}
    for x in alta + rev:
        grupos.setdefault((x["confianca"], x["regra"]), []).append(x)
    for (conf, regra), xs in grupos.items():
        tag = "BLOQUEIA" if conf == "alta" else "revisar"
        x0 = xs[0]
        L.append(f"[{tag}] {x0['prioridade']} {x0['descricao']} ({', '.join(x0['controles'])}): {len(xs)}")
        for x in xs[:max_por_regra]:
            L.append(f"  - {x['arquivo']}:{x['linha']} fp={x['fingerprint']}  {x['trecho'][:120]}")
        if len(xs) > max_por_regra:
            L.append(f"  ... +{len(xs) - max_por_regra} (lista completa em .ciber/ultimo-scan.json)")
    return "\n".join(L)


def cmd_scan(root, a):
    res = do_scan(root, diff=a.diff)
    os.makedirs(cdir(root), exist_ok=True)
    out = {"data": datetime.datetime.now().isoformat(timespec="seconds"), "diff": a.diff, "achados": res}
    with open(os.path.join(cdir(root), "ultimo-scan.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    if a.json:
        print(json.dumps(out, ensure_ascii=False))
    else:
        print(report(res, a.diff))
    return 1 if any(x["confianca"] == "alta" for x in res) else 0


def cmd_perfil(root, a):
    pf = perfil_cache(root)
    if a.json:
        print(json.dumps(pf, ensure_ascii=False))
        return 0
    on = [k for k, v in pf["stack"].items() if v]
    nc = sum(1 for c in load("controles.json")["controles"] if c["dominio"] in pf["dominios_ciber"])
    nb = sum(1 for c in load("cenarios.json")["cenarios"] if c["modulo"] in pf["modulos_bugs"])
    print("Stack: " + ", ".join(on))
    print(f"Vol. 01 (segurança): {nc} controles em {', '.join(pf['dominios_ciber'])}")
    print(f"Vol. 02 (caça a bugs): {nb} cenários em {', '.join(pf['modulos_bugs'])}")
    return 0


def lista(root, a, arq, chave, campo_dom, fmt):
    items = load(arq)[chave]
    if a.aplicaveis:
        pf = perfil_cache(root)
        doms = pf["dominios_ciber"] if chave == "controles" else pf["modulos_bugs"]
        items = [x for x in items if x[campo_dom] in doms]
    dom = getattr(a, "dominio", None) or getattr(a, "modulo", None)
    if dom:
        ds = {d.strip().upper() for d in dom.split(",")}
        items = [x for x in items if x[campo_dom] in ds]
    if a.p0:
        items = [x for x in items if x["prioridade"] == "P0"]
    for x in items:
        print(fmt(x))
    print(f"({len(items)} itens)")
    return 0


def cmd_ignorar(root, a):
    p = os.path.join(cdir(root), "ignorar.json")
    try:
        with open(p, encoding="utf-8") as f:
            cur = json.load(f)
    except (OSError, ValueError):
        cur = []
    last = {}
    try:
        with open(os.path.join(cdir(root), "ultimo-scan.json"), encoding="utf-8") as f:
            last = {x["fingerprint"]: x for x in json.load(f)["achados"]}
    except (OSError, ValueError):
        pass
    x = last.get(a.fingerprint, {})
    cur.append({"fingerprint": a.fingerprint, "motivo": a.motivo, "regra": x.get("regra"),
                "arquivo": x.get("arquivo"), "data": datetime.date.today().isoformat()})
    os.makedirs(cdir(root), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(cur, f, ensure_ascii=False, indent=1)
    print(f"Ignorado {a.fingerprint}: {a.motivo}")
    return 0


def cmd_init(root, a):
    os.makedirs(cdir(root), exist_ok=True)
    cp = os.path.join(cdir(root), "config.json")
    if not os.path.exists(cp):
        with open(cp, "w", encoding="utf-8") as f:
            json.dump({"hook_commit": True, "bloquear": "alta"}, f, indent=2)
    gi = os.path.join(cdir(root), ".gitignore")
    if not os.path.exists(gi):
        with open(gi, "w", encoding="utf-8") as f:
            f.write("ultimo-scan.json\n")
    print(f"Central Ciber ligada em {root}.")
    return cmd_perfil(root, a)


def cmd_release(root, a):
    res = do_scan(root)
    alta = [x for x in res if x["confianca"] == "alta"]
    bl = bl_load(root)["itens"]
    p0 = {k: v for k, v in bl.items() if v["prioridade"] == "P0" and v["status"] in ("falha", "pendente", "inconclusivo")}
    print(report(res, False))
    if not bl:
        print("Backlog vazio: rode a auditoria (/ciber) antes do release.")
    if p0:
        print(f"P0 em aberto no backlog: {len(p0)} -> " + ", ".join(sorted(p0)[:30]) + (" ..." if len(p0) > 30 else ""))
    ok = not alta and not p0 and bool(bl)
    print("RELEASE: APROVADO" if ok else "RELEASE: BLOQUEADO")
    return 0 if ok else 1


def main():
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description="Central Ciber")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sp = {}
    for n in ("init", "perfil", "scan", "controles", "cenarios", "backlog", "status", "ignorar", "release"):
        sp[n] = sub.add_parser(n)
        sp[n].add_argument("--repo", default=os.getcwd())
        sp[n].add_argument("--json", action="store_true")
    sp["scan"].add_argument("--diff", action="store_true")
    for n, k in (("controles", "--dominio"), ("cenarios", "--modulo")):
        sp[n].add_argument(k)
        sp[n].add_argument("--p0", action="store_true")
        sp[n].add_argument("--aplicaveis", action="store_true")
    sp["backlog"].add_argument("--bugs", action="store_true", help="inclui os cenários do Vol. 02")
    sp["status"].add_argument("id")
    sp["status"].add_argument("status")
    sp["status"].add_argument("--evidencia", default="")
    sp["ignorar"].add_argument("fingerprint")
    sp["ignorar"].add_argument("--motivo", required=True)
    a = ap.parse_args()
    root = repo_root(a.repo) if a.cmd not in ("controles", "cenarios") or a.aplicaveis else None
    if a.cmd not in ("controles", "cenarios") and not root:
        print("Não é um repositório git.", file=sys.stderr)
        return 2
    if a.cmd == "controles":
        return lista(root, a, "controles.json", "controles", "dominio",
                     lambda x: f"{x['id']} {x['prioridade']} {x['controle']}: {x['exigencia']}")
    if a.cmd == "cenarios":
        return lista(root, a, "cenarios.json", "cenarios", "modulo",
                     lambda x: f"{x['id']} {x['prioridade']} {x['bug']} | provocar: {x['como_provocar']} | "
                               f"esperado: {x['esperado']}")
    return {"init": cmd_init, "perfil": cmd_perfil, "scan": cmd_scan, "backlog": cmd_backlog,
            "status": cmd_status, "ignorar": cmd_ignorar, "release": cmd_release}[a.cmd](root, a)


if __name__ == "__main__":
    sys.exit(main())
