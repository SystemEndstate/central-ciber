"""Registra (ou remove) o hook da Central Ciber e os comandos curtos no ~/.claude.

Uso:
  python install.py              instala hook de commit + /ciber /ciber-diff /ciber-release /bugs /bugs-diff
  python install.py --uninstall
Faz backup do settings.json antes de mexer. Rodar de novo não duplica.
Comando com o mesmo nome que já seja seu não é sobrescrito.
"""
import json
import os
import shutil
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
HOOK = os.path.join(HERE, "hook.py")
SETTINGS = os.path.join(os.path.expanduser("~"), ".claude", "settings.json")
CMD_SRC = os.path.join(os.path.dirname(HERE), "commands")
CMD_DST = os.path.join(os.path.expanduser("~"), ".claude", "commands")
MARK = "Central Ciber"


def ours(path):
    try:
        with open(path, encoding="utf-8") as f:
            return MARK in f.read(300)
    except OSError:
        return False


def commands(uninstall):
    done = []
    for name in sorted(os.listdir(CMD_SRC)):
        dst = os.path.join(CMD_DST, name)
        if uninstall:
            if ours(dst):
                os.remove(dst)
            continue
        if os.path.exists(dst) and not ours(dst):
            print(f"Pulei /{name[:-3]}: já existe um comando seu com esse nome.")
            continue
        os.makedirs(CMD_DST, exist_ok=True)
        shutil.copy(os.path.join(CMD_SRC, name), dst)
        done.append("/" + name[:-3])
    return done


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    uninstall = "--uninstall" in sys.argv
    s = {}
    if os.path.exists(SETTINGS):
        with open(SETTINGS, encoding="utf-8") as f:
            s = json.load(f)
        shutil.copy(SETTINGS, f"{SETTINGS}.bak-{time.strftime('%Y%m%d-%H%M%S')}")
    pre = s.setdefault("hooks", {}).setdefault("PreToolUse", [])
    for e in [e for e in pre if "central-ciber" in json.dumps(e) and "hook.py" in json.dumps(e)]:
        pre.remove(e)
    if not uninstall:
        pre.append({"matcher": "Bash|PowerShell", "hooks": [{
            "type": "command", "command": sys.executable, "args": [HOOK], "timeout": 120,
            "statusMessage": "Central Ciber procurando vulnerabilidade no commit..."}]})
    os.makedirs(os.path.dirname(SETTINGS), exist_ok=True)
    with open(SETTINGS, "w", encoding="utf-8") as f:
        json.dump(s, f, ensure_ascii=False, indent=2)
    cmds = commands(uninstall)
    print("Hook e comandos removidos." if uninstall else
          f"Hook instalado ({sys.executable} {HOOK}).\nComandos: {' '.join(cmds)}\n"
          "No Claude Code, abra um repositório e rode /ciber.")


if __name__ == "__main__":
    main()
