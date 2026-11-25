---
description: Central Ciber — caça a bugs só nos módulos que a mudança atual toca
allowed-tools: Bash, Read, Edit, Write, Grep, Glob
---
Siga a skill `central-ciber`, modo **Caça a bugs no diff (/bugs-diff)**:
1. Veja o diff (`git diff HEAD --stat`) e mapeie os módulos do Vol. 02 que ele toca (ex.: pagamento → PAY; login → AUTH; formulário → WEB/UX).
2. Rode os cenários P0 desses módulos contra o código alterado.
3. Avise, corrija com teste e rode de novo.
