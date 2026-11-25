---
description: Central Ciber — portão de release; qualquer P0 aberto bloqueia a publicação
allowed-tools: Bash, Read, Edit, Write, Grep, Glob
---
Siga a skill `central-ciber`, modo **Release (/ciber-release)**:
1. Rode `python ~/.claude/skills/central-ciber/scripts/ciber.py release`.
2. **BLOQUEADO:** liste o que falta.
   - O que for corrigível no código: corrija e rode de novo.
   - O que for ação manual (console, MFA, backup, loja): passo a passo para o usuário.
3. **APROVADO:** resumo dos release gates (Vol. 01 REL/POL e Vol. 02 G1–G16) com o que tem evidência e o que não se aplica.
