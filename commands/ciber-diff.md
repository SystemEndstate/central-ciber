---
description: Central Ciber — revisa a segurança só do que a mudança atual afeta; corrige e roda de novo
allowed-tools: Bash, Read, Edit, Write, Grep, Glob
---
Siga a skill `central-ciber`, modo **Diff (/ciber-diff)**:
1. `python ~/.claude/skills/central-ciber/scripts/ciber.py scan --diff`.
2. Revise os controles dos domínios que o diff toca (ex.: mexeu em upload, revise FIL; em rota, revise ROT/API).
3. Avise o que achou, corrija, rode de novo até ficar limpo e reporte em poucas linhas.
