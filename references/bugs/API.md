# API: 06. APIs REST, GraphQL, WebSocket e webhooks

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| API-001 | P1 | JSON inválido | Enviar sintaxe quebrada e campos extras em ambiente de teste. | Resposta 4xx previsível; nenhuma mutação. |
| API-002 | P0 | Tipos inesperados | Trocar string por array, objeto, boolean e null. | Schemas recusam entradas inválidas, sem stack trace público. |
| API-003 | P1 | Parâmetro repetido | Enviar mesmo parâmetro duas vezes com valores diferentes. | Parse consistente e seguro; validação não pode ser contornada. |
| API-004 | P0 | Cabeçalho ausente | Omitir Authorization, Content-Type e outros necessários. | Erro explícito sem crash ou comportamento permissivo. |
| API-005 | P1 | Resposta fora de ordem | Simular latências distintas em chamadas paralelas. | Cliente aplica resposta à operação correta. |
| API-006 | P0 | Timeout após commit | Forçar perda da resposta depois de gravar pedido de teste. | Retry não cria segunda operação; consulta estado por ID. |
| API-007 | P1 | Paginação sob inclusão | Inserir novos registros enquanto lista é paginada. | Sem omissões críticas ou mistura entre tenants. |
| API-008 | P1 | GraphQL complexo | Criar query profundamente aninhada em staging. | Limites de complexidade e recursos aplicados. |
| API-009 | P1 | WebSocket reconectar | Cortar socket durante envio e reconectar. | Estado revalidado; mensagens duplicadas tratadas. |
| API-010 | P0 | WebSocket logout | Encerrar sessão com socket ainda conectado. | Inscrições privadas e autorizações atualizadas ou encerradas. |
| API-011 | P0 | Webhook repetido | Entregar evento válido duas vezes. | Processamento idempotente; resultado único. |
| API-012 | P0 | Webhook fora de ordem | Entregar evento de cancelamento antes de pagamento. | Estado final consistente por versão/ID e regras de negócio. |
| API-013 | P0 | Assinatura de webhook | Enviar evento sintético com assinatura incorreta. | Evento recusado e registrado sem execução. |
| API-014 | P1 | Rate limit errado | Exceder quota com vários usuários e clientes de teste. | Limites por identidade e recurso, sem bloquear contas alheias. |
| API-015 | P1 | API antiga | Executar cliente suportado contra endpoint versionado recente. | Compatibilidade preservada ou migração explícita. |
| API-016 | P0 | Erros 500 mascarados | Gerar exceção controlada no ambiente de teste. | Sem segredos expostos; correlation ID rastreável. |
