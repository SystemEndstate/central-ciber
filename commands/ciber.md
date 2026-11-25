---
description: Central Ciber — auditoria de segurança completa do projeto; acha, avisa, corrige e roda de novo
allowed-tools: Bash, Read, Edit, Write, Grep, Glob, Agent
---
Siga a skill `central-ciber`, modo **Auditoria (/ciber)**, no repositório atual (ou em $ARGUMENTS, se for um caminho; `--p1` inclui os P1).

Resumo do fluxo:
1. `python ~/.claude/skills/central-ciber/scripts/ciber.py init` (se não houver `.ciber/`), depois `perfil` e `backlog`.
2. `python ~/.claude/skills/central-ciber/scripts/ciber.py scan`, mais a revisão dos controles P0 aplicáveis, domínio por domínio.
3. **Avise** o usuário com a lista curta do que foi achado.
4. **Corrija** cada falha (sem quebrar o que funciona), **rode de novo** até não sobrar falha corrigível.
5. Atualize o backlog e entregue o relatório final.
