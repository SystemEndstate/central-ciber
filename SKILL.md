---
name: central-ciber
description: Auditoria de cybersegurança (676 controles, Vol. 01) e caça a bugs (419 cenários, Vol. 02) para SaaS, APIs, Supabase/AWS, Android/iOS e desktop. Acha a vulnerabilidade ou o bug, avisa, corrige e roda de novo até ficar limpo. Use quando o usuário pedir auditoria de segurança, pentest do próprio código, "tem vulnerabilidade?", "caça bugs", checklist de release, RLS/Supabase, IDOR/tenant, LGPD técnica, antes de publicar app ou loja, quando o commit for bloqueado pela Central Ciber, ou pelos comandos /ciber, /ciber-diff, /ciber-release, /bugs, /bugs-diff.
---

# Central Ciber

Duas habilidades sobre o mesmo repositório:

| Habilidade | Fonte | Pergunta que responde |
|---|---|---|
| **Ciber** | Vol. 01, 676 controles, 31 domínios (`references/ciber/<DOMÍNIO>.md`) | "A defesa existe e está certa?" |
| **Caça a bugs** | Vol. 02, 419 cenários, 26 módulos (`references/bugs/<MÓDULO>.md`) | "Se eu provocar a falha, o produto aguenta?" |

Regras gerais, prioridades, playbooks, ticket e release gates: `references/metodo.md`. Leia antes do primeiro uso.

Script: `python ~/.claude/skills/central-ciber/scripts/ciber.py <comando> [--repo <raiz>]`

| Comando | Para quê |
|---|---|
| `init` | liga a Central Ciber no repo (`.ciber/`, hook de commit passa a valer) |
| `perfil` | stack detectada e quais domínios/módulos se aplicam |
| `scan [--diff]` | varredura determinística (segredos, RLS, TLS, Android/iOS, Electron, CORS, SQL, XSS, dinheiro em float…). `alta` = bloqueia; `revisar` = você confere |
| `controles --aplicaveis [--dominio X] [--p0]` | lista controles do Vol. 01 |
| `cenarios --aplicaveis [--modulo X] [--p0]` | lista cenários do Vol. 02 |
| `backlog [--bugs]` | cria/atualiza `.ciber/backlog.json` e `.md` com os itens aplicáveis |
| `status ID[,ID] <status> --evidencia "arquivo:linha / teste / motivo"` | marca um item: `ok`, `falha`, `pendente`, `manual`, `bloqueado`, `na` ou `inconclusivo` |
| `ignorar <fp> --motivo "..."` | aceita um achado do scan como falso positivo (fica registrado) |
| `release` | portão: nenhum `alta` no scan e nenhum P0 em `falha`/`pendente`/`inconclusivo` |

## O ciclo (vale para todos os modos)

**ACHAR → AVISAR → CORRIGIR → RODAR DE NOVO**, até não sobrar nada corrigível.

1. **Achar:**
   - Rode o script (`scan`) e revise os controles/cenários aplicáveis no código (`references/...`).
   - Cada achado precisa de evidência `arquivo:linha` ou de um teste que reproduz.
   - Sem evidência, o status é `inconclusivo`, não `falha`.
2. **Avisar:** antes de mexer, mostre ao usuário a lista curta com ID, prioridade, onde está, risco e o que vai fazer. Não espere resposta, a não ser nos casos de parada abaixo.
3. **Corrigir:**
   - Comece pelos P0, depois os P1 (só se pedido ou em `--p1`).
   - Corrija a **causa**, não o sintoma.
   - Para cada correção de bug ou vulnerabilidade de lógica (IDOR, tenant, idempotência, validação), escreva um teste que **falha antes e passa depois**.
   - Siga a skill `guarda-regressao` se estiver instalada: `gate.py check` depois de cada lote de correções, para não quebrar outra coisa.
4. **Rodar de novo:**
   - Rode de novo o `scan` e os testes da área.
   - Achado que continua: tente outra abordagem, no máximo 3 voltas por item. Depois disso, marque `falha` com o motivo e siga.
5. **Registrar:**
   - `status` para cada item avaliado (`ok` com evidência, `falha`, `manual` com passo a passo, `na` com justificativa).
   - Falso positivo do scan: `ignorar` com motivo.

**Pare e pergunte** quando:
- a correção muda comportamento de negócio visível (ex.: endurecer uma regra que hoje bloqueia usuários legítimos);
- exige migração destrutiva ou irreversível em dados;
- envolve produção, custo, contas externas (console AWS/Supabase, MFA, lojas) ou deploy.

Nesses casos: status `manual`, passo a passo e opções.

**Nunca:**
- testar contra produção;
- rodar carga, caos ou pentest fora de ambiente autorizado;
- usar dados reais de clientes;
- "corrigir" desligando o teste ou o controle;
- commitar segredo.

## Modo Auditoria (`/ciber`)

1. `init` (se não houver `.ciber/`), `perfil`, `backlog`.
2. `scan`:
   - todo `alta` é falha P0 confirmada;
   - para cada `revisar`, abra o trecho e decida: falha, ok ou falso positivo.
3. Revisão por domínio, só P0 por padrão (P1 com `--p1`):
   - Abra `references/ciber/<DOM>.md` de cada domínio aplicável e verifique cada controle no código.
   - Projeto grande: um subagente por grupo de domínios (ex.: ROT+API+ID+SES / SUP+DB+FIL / MOB+AND+IOS+TEC / INF+DEV+MON+PRIV), cada um devolvendo `ID | status | evidência | correção sugerida`.
   - Decisão fechada em lote ("este controle se aplica a este projeto?"): use o Jev (`decide_many`) se disponível.
4. Prioridade de verificação nos P0:
   - autorização no servidor por objeto e tenant (ROT-02/04, CORE-03/04);
   - RLS e grants (SUP);
   - segredos (CORE-09);
   - validação de entrada e SQL (API);
   - webhooks e idempotência (API-07/08);
   - uploads (FIL);
   - sessão e JWT (SES);
   - dinheiro (API-15, BUG-16).
5. Ciclo **avisar → corrigir → rodar de novo**.
6. Relatório final (formato abaixo).

## Modo Diff (`/ciber-diff`)

1. `scan --diff`.
2. Mapeie os arquivos alterados para domínios:
   - rota/handler → ROT, API;
   - migração SQL → SUP, DB;
   - upload → FIL;
   - login → ID, SES;
   - manifest/plist/capacitor → MOB, AND, IOS;
   - Dockerfile/compose → INF.
3. Revise só os P0 desses domínios no código alterado.
4. Avisar, corrigir, rodar de novo.

## Modo Release (`/ciber-release`)

1. `release`.
2. **BLOQUEADO:**
   - corrija o que for código;
   - para o que for operação (backup testado, MFA, assinatura, loja), dê o passo a passo e marque `manual`.
3. Confira os gates de `references/metodo.md` (Vol. 01 REL/POL e Vol. 02 G1–G16) e diga quais têm evidência.

## Modo Caça a bugs (`/bugs`, `/bugs-diff`)

1. `perfil` e `backlog --bugs`. Em `/bugs-diff`, só os módulos que o diff toca.
2. Para cada cenário P0 aplicável (`cenarios --aplicaveis --p0`), leia "como provocar" e "resultado esperado", e ache no código o caminho que o cenário exercita.
3. Classifique:
   - **ok:** o código trata, com evidência (`arquivo:linha` do lock, da chave de idempotência, do teste existente…);
   - **falha:** o caminho não trata.
     1. Escreva um teste automatizado que provoca o cenário (unitário, integração com banco de teste, ou E2E/Playwright quando for UI) e veja ele falhar.
     2. Corrija.
     3. Veja o teste passar.
     4. Rode a regressão.
   - **bloqueado:** precisa de dispositivo real, VM, loja ou sandbox de terceiro. Registre o ticket (modelo em `metodo.md`) com os passos para o usuário executar.
4. Use os playbooks A–F de `metodo.md` para casos difíceis: intermitente, vazamento entre tenants, duplicidade financeira, crash, update interrompido, sync offline.
5. Ambiente: banco/schema de teste e contas sintéticas (Tenant A/B, usuários A1/A2/B1/inativo). Se o projeto tiver regras próprias de teste (CLAUDE.md, memória), elas valem.

## Hook de commit

Em repo com `.ciber/config.json`, todo `git commit` feito pelo Claude passa por `scan --diff` (só as linhas novas):
- `alta` nega o commit e avisa o usuário. O Claude corrige, roda de novo e commita.
- `revisar` entra como contexto para conferir.
- Saída de emergência, só com motivo: `# ciber-ok <motivo>` no fim do comando.

## Relatório final

```
Central Ciber: <modo> em <repo>
Achados: <n> (P0 <n>, P1 <n>) | Corrigidos: <n> | Rodado de novo: limpo / <n> restantes
Corrigido: ID — o que era — onde — teste que prende
Manual (precisa de você): ID — passo a passo curto
Pendente/inconclusivo: <n> (ver .ciber/backlog.md)
Release: APROVADO / BLOQUEADO (motivo)
```

Limite: isto é uma auditoria técnica de código e configuração. Não substitui pentest formal, análise jurídica de LGPD nem revisão de arquitetura (ver o fim de `metodo.md`).
