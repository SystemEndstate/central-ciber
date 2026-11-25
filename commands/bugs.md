---
description: Central Ciber — caça a bugs no projeto inteiro (Vol. 02); provoca o cenário, corrige e roda de novo
allowed-tools: Bash, Read, Edit, Write, Grep, Glob, Agent
---
Siga a skill `central-ciber`, modo **Caça a bugs (/bugs)**, no repositório atual. $ARGUMENTS pode trazer módulos (ex.: `PAY,AUTH`) ou `--p1`.

Resumo do fluxo:
1. `python ~/.claude/skills/central-ciber/scripts/ciber.py perfil` e `python ~/.claude/skills/central-ciber/scripts/ciber.py backlog --bugs`.
2. Para cada cenário P0 aplicável: o código trata isso?
   - Se não trata, escreva o teste que provoca o cenário, veja falhar, corrija, veja passar.
3. **Avise** o usuário dos bugs achados, **corrija**, **rode de novo** (inclusive o guarda-regressão) e entregue o relatório.
