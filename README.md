# central-ciber

Skill para o [Claude Code](https://claude.com/claude-code) que audita a **segurança** e **caça bugs** no seu projeto e já corrige o que encontra.

Ciclo: **acha → avisa → corrige → roda de novo**, até não sobrar nada corrigível.

*English: a Claude Code skill with 676 security controls (web, APIs, Supabase, AWS, databases, mobile, desktop, AI) and 419 reproducible bug-hunting scenarios. It detects your stack, scans for high-confidence vulnerabilities, reviews the applicable controls, fixes issues with tests, re-runs until clean, tracks a backlog and blocks commits that introduce new vulnerabilities.*

## Duas habilidades

| | Fonte | Conteúdo |
|---|---|---|
| **Ciber** | *Central de Cybersegurança para SaaS e Apps* v2.0 | 676 controles (369 P0) em 31 domínios: identidade, sessões/JWT, rotas e autorização, frontend, APIs, AWS, Supabase (RLS, Storage, Realtime), bancos, uploads, servidores/containers, DevSecOps, logs, LGPD, IA/agentes, mobile, Android, iOS, desktop (Windows/macOS/Linux), frameworks, bugs, UX segura, offline, testes e release |
| **Caça a bugs** | *Manual de Caça a Bugs e Confiabilidade* v1.0 | 419 cenários (206 P0) em 26 módulos, cada um com bug buscado, como provocar e resultado esperado; mais playbooks, modelo de ticket e release gates G1–G16 |

## Comandos

| Comando | O que faz |
|---|---|
| `/ciber` | auditoria de segurança do projeto inteiro: acha, avisa, corrige, roda de novo |
| `/ciber-diff` | o mesmo, só no que a mudança atual afeta |
| `/ciber-release` | portão antes de publicar: qualquer P0 aberto bloqueia |
| `/bugs` | caça a bugs no projeto: provoca cada cenário P0 com teste, corrige o que falhar e roda de novo |
| `/bugs-diff` | caça a bugs só nos módulos que a mudança toca |

**Trava de commit:** em repositórios com a Central Ciber ligada, todo `git commit` feito pelo Claude passa por uma varredura das linhas novas. Vulnerabilidade de alta confiança bloqueia o commit, avisa você e o Claude corrige e roda de novo antes de commitar.

## Como funciona

1. **Perfil:** detecta a stack (React/Next/Vite, Go/Node/Python, Postgres, Supabase, AWS, Docker, Capacitor/React Native/Flutter, Android, iOS, Electron/Tauri, pagamentos, IA…) e escolhe só os domínios e módulos que se aplicam.
2. **Scan determinístico** (sem IA, segundos). Exemplos do que procura:
   - segredos (AWS, Stripe, GitHub, OpenAI/Anthropic/OpenRouter, Supabase `service_role` / `sb_secret_`) e `.env` versionado;
   - tabela Supabase sem RLS, `SECURITY DEFINER` sem `search_path`, `GRANT ALL TO anon`, policy `USING (true)`;
   - TLS desligado; Android `debuggable`/cleartext/`allowBackup`/`exported`; iOS ATS; Capacitor cleartext; Electron `nodeIntegration`/`contextIsolation`;
   - CORS `*`, JWT sem verificação, SQL e shell montados com texto, XSS (`dangerouslySetInnerHTML`/`innerHTML`), token em `localStorage`, erro interno devolvido ao cliente, segredo em log, dinheiro em `float`;
   - Dockerfile como root ou com segredo, porta de banco exposta.

   Cada achado aponta o código do controle (ex.: `SUP-01`).
3. **Revisão por domínio:** o Claude verifica os controles P0 aplicáveis no código, com evidência `arquivo:linha`.
4. **Correção com teste:** cada falha de lógica (IDOR, tenant, idempotência, validação) ganha um teste que falha antes e passa depois. Se a skill `guarda-regressao` estiver instalada, ela garante que a correção não quebre outra parte do sistema.
5. **Backlog:** `.ciber/backlog.md` registra cada item com status (`ok`, `falha`, `manual`, `na`…), evidência e data.

## Instalação

```bash
git clone https://github.com/SystemEndstate/central-ciber ~/.claude/skills/central-ciber
python ~/.claude/skills/central-ciber/scripts/install.py
```

Depois, no Claude Code, abra o projeto e rode `/ciber`. Na primeira vez ele liga a Central Ciber no repositório criando a pasta `.ciber/`.

Se você já tiver um comando com o mesmo nome, ele não é sobrescrito. Desinstalar: `python scripts/install.py --uninstall`.

### Pelo terminal (sem Claude)

```bash
python scripts/ciber.py perfil                      # stack e domínios aplicáveis
python scripts/ciber.py scan                        # varredura completa (exit 1 = vulnerabilidade)
python scripts/ciber.py scan --diff                 # só linhas alteradas
python scripts/ciber.py controles --aplicaveis --p0
python scripts/ciber.py cenarios --modulo PAY
python scripts/ciber.py release                     # portão de publicação
```

Falso positivo: `python scripts/ciber.py ignorar <fp> --motivo "..."` ou um comentário `ciber-ignore` na linha.

## Estrutura

```
SKILL.md                 fluxo dos modos e regras de correção
data/controles.json      676 controles (Vol. 01)
data/cenarios.json       419 cenários (Vol. 02)
references/ciber/*.md    um arquivo por domínio
references/bugs/*.md     um arquivo por módulo
references/metodo.md     prioridades, playbooks, ticket, release gates, cadência
scripts/ciber.py         perfil, scan, backlog, status, release
scripts/hook.py          trava de commit
commands/*.md            /ciber /ciber-diff /ciber-release /bugs /bugs-diff
```

## Limites

- Auditoria técnica de código e configuração. Não substitui pentest formal, análise jurídica de LGPD nem revisão de arquitetura.
- Teste só em ambiente local, staging ou sandbox, com dados sintéticos. Nunca em produção sem autorização.
- O scan é por padrões: `alta` é quase certo; `revisar` precisa de olhar humano ou do Claude.

## Licença

MIT
