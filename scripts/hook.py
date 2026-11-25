"""Hook PreToolUse (Bash|PowerShell): Central Ciber antes de `git commit`.

- só age em repo com .ciber/config.json (ligado com `ciber.py init` ou /ciber)
- varre só as linhas novas/alteradas; achado de confiança "alta" nega o commit,
  avisa o usuário e manda o Claude corrigir e rodar de novo (fase "corrigir" da skill)
- achados "revisar" entram como contexto, sem bloquear
- saída de emergência: `# ciber-ok <motivo>` no fim do comando
Qualquer erro termina em silêncio (exit 0): nunca trava o fluxo.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ciber  # noqa: E402

GIT_COMMIT = re.compile(r"\bgit\b(?:\s+-\S+(?:\s+\S+)?)*\s+commit\b")


def out(ctx=None, deny=None, user=None):
    hso = {"hookEventName": "PreToolUse"}
    if deny:
        hso["permissionDecision"] = "deny"
        hso["permissionDecisionReason"] = deny
    if ctx:
        hso["additionalContext"] = ctx
    o = {"hookSpecificOutput": hso}
    if user:
        o["systemMessage"] = user
    print(json.dumps(o, ensure_ascii=False))


def main():
    for s in (sys.stdin, sys.stdout):
        try:
            s.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    data = json.load(sys.stdin)
    cmd = (data.get("tool_input") or {}).get("command", "")
    if not GIT_COMMIT.search(cmd) or os.environ.get("CIBER_OFF"):
        return
    cwd = data.get("cwd") or os.getcwd()
    m = re.search(r"\bgit\s+-C\s+(\"[^\"]+\"|'[^']+'|\S+)", cmd) or \
        re.search(r"(?:^|&&|;)\s*(?:cd|Set-Location)\s+(\"[^\"]+\"|'[^']+'|\S+)", cmd)
    if m:
        p = os.path.expanduser(m.group(1).strip("\"'"))
        cwd = p if os.path.isabs(p) else os.path.join(cwd, p)
    root = ciber.repo_root(cwd)
    if not root or not os.path.exists(os.path.join(ciber.cdir(root), "config.json")):
        return
    if "# ciber-ok" in cmd:
        out(ctx="Central Ciber pulada com `# ciber-ok`. Registre o motivo no backlog com `ciber.py status`.")
        return
    res = ciber.do_scan(root, diff=True)
    if not res:
        return
    rep = ciber.report(res, True)
    alta = [x for x in res if x["confianca"] == "alta"]
    if not alta:
        out(ctx=rep + "\nItens 'revisar' nas linhas alteradas: confira cada um antes de seguir "
                      "(corrija ou aceite com `ciber.py ignorar <fp> --motivo ...`).")
        return
    out(deny=rep + "\n\nCommit bloqueado pela Central Ciber. Siga a skill `central-ciber` (fase \"Corrigir e "
                   "rodar de novo\"): corrija a causa sem desfazer o pedido, rode `ciber.py scan --diff` até não "
                   "sobrar bloqueante, atualize o backlog e faça o commit de novo. Falso positivo: "
                   "`ciber.py ignorar <fp> --motivo \"...\"`.",
        user=f"⛔ Central Ciber: commit bloqueado. {len(alta)} vulnerabilidade(s) nas linhas alteradas. "
             f"Corrigindo e rodando de novo antes de commitar.")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
