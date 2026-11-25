# AWS: 10. AWS e cloud: falhas, resiliência e custos

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| AWS-001 | P0 | RDS indisponível | Negar temporariamente conexão em staging. | Aplicação informa falha e preserva transações; reconecta. |
| AWS-002 | P1 | Failover de banco | Testar troca de instância/endpoint em ambiente adequado. | Pool recupera sem duplicar operações. |
| AWS-003 | P1 | Lambda timeout | Forçar função a superar timeout com dados sintéticos. | Reentrega e limpeza respeitam idempotência. |
| AWS-004 | P1 | Cold start | Medir primeiras invocações e rajadas. | Latência dentro dos objetivos; timeout de cliente adequado. |
| AWS-005 | P1 | ECS reiniciado | Interromper uma tarefa com requisições ativas. | Sem perda de jobs; recuperação dentro do SLO. |
| AWS-006 | P0 | S3 acesso bloqueado | Remover permissão temporariamente em staging. | Falha tratada, sem publicar bucket nem expor chaves. |
| AWS-007 | P1 | S3 objeto faltante | Apagar objeto de teste referenciado no banco. | Erro controlado; registros órfãos detectáveis e reconciliáveis. |
| AWS-008 | P1 | Credencial rotacionada | Substituir segredo de teste durante tráfego. | Aplicação atualiza credencial sem indisponibilidade indevida. |
| AWS-009 | P0 | IAM negado | Remover permissão de API de serviço em staging. | Erro observável, sem fallback para credenciais privilegiadas. |
| AWS-010 | P1 | Quota cloud | Simular limite de conexões ou concorrência. | Degradação controlada e alerta disparado. |
| AWS-011 | P0 | Fila SQS redelivery | Reentregar evento de teste e variar ordem. | Processamento consistente e DLQ configurada conforme política. |
| AWS-012 | P0 | CloudFront cache | Testar resposta autenticada e alternância de usuários. | Nenhum dado pessoal armazenado e entregue a outra sessão. |
| AWS-013 | P1 | DNS fail | Simular falha de resolução em ambiente de teste. | Retries controlados e comunicação útil para o usuário. |
| AWS-014 | P1 | Custo inesperado | Gerar consumo sintético acima de quota em sandbox. | Proteção de custos/alertas detecta abuso sem interromper outros tenants. |
| AWS-015 | P1 | Região indisponível | Executar tabletop e testes de recuperação regional previstos. | RTO/RPO documentados e realistas. |
| AWS-016 | P1 | Logs inoperantes | Simular falha de envio de telemetria. | Serviço mantém política segura de buffers e não perde eventos críticos silenciosamente. |
