# API: 7. Backend, APIs e serviços

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| API-01 | P0 | Schemas de entrada | Validar tipo, formato, limite e campos permitidos no backend. |
| API-02 | P0 | SQL injection | Usar consultas parametrizadas e ORMs corretamente. |
| API-03 | P0 | NoSQL injection | Proibir operadores arbitrários fornecidos pelo cliente. |
| API-04 | P0 | Command injection | Não compor comandos shell com entradas não confiáveis. |
| API-05 | P0 | SSRF | Restringir destinos, redirecionamentos, metadados cloud e acesso à rede interna. |
| API-06 | P0 | Mass assignment | Mapear explicitamente campos que cada papel pode editar. |
| API-07 | P0 | Webhook autêntico | Verificar assinatura, timestamp e proteção contra replay. |
| API-08 | P0 | Idempotência | Impedir repetição de pagamentos, pedidos e outras mutações críticas. |
| API-09 | P0 | Rate limiting | Limitar login, OTP, recuperação, IA, exportações e processamento. |
| API-10 | P0 | Quotas | Restringir recursos, chamadas, tokens, armazenamento e custos por cliente. |
| API-11 | P0 | Erros protegidos | Não retornar stack trace, SQL, credenciais e configurações sensíveis. |
| API-12 | P1 | Timeouts | Definir limites para chamadas a serviços externos e banco. |
| API-13 | P1 | Payload limits | Limitar tamanho de JSON, upload, profundidade e complexidade. |
| API-14 | P1 | Desserialização | Evitar execução ou alocação descontrolada ao decodificar objetos. |
| API-15 | P0 | Fluxos financeiros | Conferir saldo, destinatário e transições com transações seguras. |
| API-16 | P1 | Workers e filas | Validar payloads, identidades de serviço e reprocessamento. |
| API-17 | P1 | Respostas externas | Tratar dados de outros sistemas como não confiáveis. |
| API-18 | P1 | GraphQL | Limitar profundidade, complexidade e acesso por resolver. |
| API-19 | P1 | Credenciais de terceiros | Aplicar escopo mínimo, rotação e limite de gastos. |
| API-20 | P0 | Concorrência | Evitar condições de corrida em estoques, saldos e permissões. |
