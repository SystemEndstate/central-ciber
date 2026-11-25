# Método: regras gerais dos dois volumes

Fontes:
- Vol. 01, *Central de Cybersegurança para SaaS e Apps* v2.0: 676 controles; prioridades P0 369, P1 303, P2 4.
- Vol. 02, *Manual de Caça a Bugs e Confiabilidade* v1.0: 419 cenários (206 P0).

O Vol. 01 descreve as defesas necessárias. O Vol. 02 descreve como estressar o produto para provar que as defesas e as regras de negócio não falham.

## Prioridade

| Nível | Significado | Ação |
|---|---|---|
| P0, crítico/bloqueante | perda ou mistura de dados, fraude, escalada de privilégio, cobrança indevida, corrupção irreversível, falha de atualização sem recuperação | bloqueia o release; corrigir/mitigar de forma verificável; teste de regressão obrigatório |
| P1, alto | obrigatório para produção madura; crashes, ANR, quedas de fluxo | corrigir antes de escalar, ou aceitar formalmente com mitigação e prazo |
| P2, avançado | proteção extra / defeito cosmético | priorizar por ameaça, custo e impacto |

A prioridade é ponto de partida, não determinação normativa (OWASP).

## Regra central

Esconder página, botão, rota ou menu **não é autorização**. Toda leitura, atualização, exportação, upload, mensagem em tempo real e execução de ferramenta precisa ser protegida na camada de dados ou de serviço que executa a operação.

## Invariantes de qualidade

- Operação financeira não duplica efeito.
- Uma conta não acessa dados de outra.
- Dado confirmado não some sem causa autorizada.
- Upgrade não deixa o app inutilizável.
- Falha de rede não gera confirmação falsa.

## Status de um controle ou cenário

| Status | Quando usar |
|---|---|
| `ok` | atendido, com evidência verificável (arquivo:linha, teste, config) |
| `falha` | não atendido; evidência do desvio |
| `pendente` | ainda não avaliado |
| `manual` | depende de ação fora do código (console AWS/Supabase, MFA, backup, loja) |
| `bloqueado` | pré-requisito ausente: ambiente, dispositivo ou risco não autorizado |
| `na` | não se aplica, com justificativa |
| `inconclusivo` | avaliado sem evidência suficiente; repetir |

## Regra de ambiente

Nunca provocar corrupção, exaustão de recursos, falha de pagamento ou ataque em **produção** sem aprovação expressa, janela, limite de carga e plano de parada/rollback. Testes rodam local, em staging ou em sandbox, com contas e dados sintéticos. Pentest e varredura somente em ativos próprios ou autorizados.

## Laboratório mínimo (SaaS multi-tenant)

- **Usuários:**
  - U-A1 editor;
  - U-A2 visualizador;
  - U-B1 admin de outra organização;
  - U-INATIVO desativado.
- **Organizações:** Tenant A e Tenant B, cada um com projetos, faturas e documentos próprios.
- **Ambiente:** staging com proxy de latência, queda de rede, banco isolado e backup de teste.
- **Instrumentação:** logs estruturados, trace ID, crash reports, sem PII.

## Supabase: exemplo de RLS por dono

```sql
ALTER TABLE public.documents ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON public.documents FROM anon, authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.documents TO authenticated;
CREATE POLICY documents_select ON public.documents FOR SELECT TO authenticated
  USING (user_id = (SELECT auth.uid()));
CREATE POLICY documents_insert ON public.documents FOR INSERT TO authenticated
  WITH CHECK (user_id = (SELECT auth.uid()));
CREATE POLICY documents_update ON public.documents FOR UPDATE TO authenticated
  USING (user_id = (SELECT auth.uid())) WITH CHECK (user_id = (SELECT auth.uid()));
CREATE POLICY documents_delete ON public.documents FOR DELETE TO authenticated
  USING (user_id = (SELECT auth.uid()));
```

O que testar e o resultado esperado:
- A lê ou edita documento próprio: permitido.
- A lê, altera ou exclui documento de B: negado ou sem linhas retornadas.
- A insere documento com `user_id` de B: negado.
- Anônimo consulta documentos: negado.

Revise também grants, views (`security_invoker`), RPC e `SECURITY DEFINER` (com `search_path` fixo).

## Estados seguros de transação (UI)

| Estado | Como tratar |
|---|---|
| Não enviada | nada foi iniciado |
| Pendente | o servidor não confirmou; **não mostrar sucesso** |
| Confirmada | validada no backend; ID da operação registrado |
| Não confirmada | consultar o estado real antes de repetir |
| Falha definitiva | motivo seguro + caminho de recuperação |

## Playbooks (Vol. 02)

**A. Bug intermitente:**
1. Congelar o contexto: build, flags, commit, tenant, SO, latência e dados.
2. Rodar de 20 a 100 vezes com seed fixa.
3. Variar uma dimensão por vez: concorrência, rede, ordem dos eventos, conta.
4. Comparar UI, request, banco e fila.
5. Escrever um teste que falha antes da correção e passa depois, rodando no CI.

**B. Vazamento entre clientes:**
1. Preparar dois tenants com dados próprios.
2. Executar GET/POST/PATCH/DELETE legítimos com A.
3. Repetir trocando o alvo para um objeto de B.
4. Verificar status, resposta, rowcount, evento e dado persistido.
5. Automatizar a matriz papel × tenant × recurso × método.

**C. Duplicidade financeira/webhook:**
1. Gerar um pedido sintético.
2. Cortar a resposta depois de persistir.
3. Reenviar e inverter a ordem dos eventos.
4. Conferir o ledger.
5. O resultado tem que ser único em todas as tentativas.

**D. Crash nativo/ANR:**
1. Reproduzir em build release.
2. Coletar a evidência oficial (logcat/vitals, crash report/MetricKit).
3. Segmentar a causa: thread de UI, memória, lifecycle, plugin, filesystem.
4. Reduzir a um gatilho mínimo.
5. Conferir a integridade do estado ao reabrir.

**E. Atualização interrompida:**
1. Partir de VM limpa com versão N-2.
2. Interromper com: rede, reboot, disco cheio, permissão.
3. Verificar a assinatura.
4. Confirmar que a versão anterior abre ou que existe reparo.
5. Validar a migração.

**F. Sync offline:**
1. Fazer edições conflitantes em dois clientes.
2. Mudar a ordem de reconexão e a conta.
3. Simular timeout pós-commit.
4. Reconciliar A, B, banco e auditoria.
5. Documentar a política: tombstones, versões, idempotência.

## Modelo de ticket de bug

Campos:
- ID/título: `BUG-AAAA-0001 — [plataforma] [fluxo] falha`;
- resumo (sem inferir causa);
- ambiente/build/commit;
- persona/tenant;
- pré-condições;
- passos;
- esperado;
- real;
- frequência;
- impacto;
- evidências (trace ID, request redigido, log);
- causa raiz confirmada;
- plano de correção;
- teste de regressão (falha antes, passa depois);
- aceite.

O bug só fecha quando:
1. foi reproduzido na versão anterior;
2. o teste de regressão passa no build novo;
3. os impactos vizinhos foram observados.

## Release gates

**Vol. 01 (REL/POL).** Bloqueia publicação quando houver:
- P0 explorável aberto;
- falha entre tenants;
- dupla cobrança;
- perda irreversível de dados;
- atualização sem assinatura;
- testes automáticos falhando;
- backup sem teste de restauração.

**Vol. 02 (G1–G16):**

| Gate | Condição |
|---|---|
| G1 | nenhum P0 aplicável aberto sem mitigação |
| G2 | testes de autorização por usuário/tenant versionados |
| G3 | pagamento, idempotência e reconciliação exercitados em sandbox |
| G4 | migrações testadas com dados sintéticos realistas |
| G5 | restore de backup com RTO/RPO medidos |
| G6 | E2E dos fluxos principais |
| G7 | crashes/ANR priorizados; build release em dispositivo real |
| G8 | instalador/updater assinado e testado contra interrupção |
| G9 | offline, troca de conta e sync sem corrupção |
| G10 | scanners de segredo, dependências e código no pipeline |
| G11 | observabilidade com correlation ID e dono dos alertas |
| G12 | rollback, feature flags e comunicação de incidente praticados |
| G13 | performance e limites testados |
| G14 | acessibilidade, idiomas e layouts essenciais testados |
| G15 | matriz de SO/dispositivos documentada |
| G16 | evidências ligadas ao commit publicado |

## Cadência

| Quando | O que rodar |
|---|---|
| A cada commit | unitários, contrato, lint, análise estática, scan de segredos |
| A cada PR | integração, autorização, regressões afetadas |
| Antes de publicar | E2E, dispositivo real, migrações, instalador/update, smoke do build assinado, restore |
| Depois de publicar | canary, métricas por versão, crash rate, alertas |
| Periódico | caos controlado, restore trimestral, pentest, threat modeling, revisão de permissões (mensal) |

## Ferramentas de referência

| Área | Ferramentas |
|---|---|
| Código | Semgrep, CodeQL |
| Segredos | Gitleaks, TruffleHog |
| Dependências | Dependabot, Snyk, Trivy |
| Web | Playwright, OWASP ZAP, axe-core |
| Banco | pgTAP, `supabase test db`, EXPLAIN ANALYZE |
| Carga | k6, Locust, toxiproxy |
| Mobile | MobSF, Maestro, Espresso, XCUITest |
| Observabilidade | Sentry, OpenTelemetry |

Nenhum checklist torna o produto invulnerável. Isto não substitui pentest formal, análise jurídica de LGPD (incidente: em regra, comunicar ANPD e titulares em 3 dias úteis, Res. CD/ANPD 15/2024) nem revisão de arquitetura.
