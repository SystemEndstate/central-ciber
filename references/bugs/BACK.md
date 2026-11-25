# BACK: 07. Backend, jobs e regras de negócio

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| BACK-001 | P0 | Regra só no client | Enviar valor inválido diretamente pela API em conta de teste. | Validação de negócio realizada no servidor. |
| BACK-002 | P0 | Saldo negativo indevido | Disparar dois débitos simultâneos sobre mesmo saldo sintético. | Invariantes financeiros preservados atomicamente. |
| BACK-003 | P0 | Transição inválida | Mudar pedido de cancelado para pago sem evento válido. | Máquina de estados recusa transição. |
| BACK-004 | P0 | Job duplicado | Entregar a mesma mensagem duas vezes ao worker. | Efeito de negócio ocorre uma única vez. |
| BACK-005 | P0 | Job fora de ordem | Trocar ordem dos eventos de atualização. | Versão/estado evita regressão indevida. |
| BACK-006 | P0 | Worker morre após gravar | Encerrar worker após commit e antes de ack em staging. | Reentrega não duplica efeito. |
| BACK-007 | P1 | Retries sem backoff | Simular serviço externo indisponível. | Tentativas com limite, jitter e DLQ quando aplicável. |
| BACK-008 | P1 | Timeout sem cancelamento | Simular dependência travada. | Request termina e recursos são liberados. |
| BACK-009 | P0 | Falha em etapa 3 de 4 | Injetar exceção após múltiplas gravações. | Rollback, compensação ou estado recuperável garantido. |
| BACK-010 | P0 | Fuso horário | Testar horário de verão, meia-noite e UTC. | Regras de vencimento baseadas em instantes corretos. |
| BACK-011 | P0 | Arredondamento monetário | Testar centavos, descontos e milhares de itens. | Uso de decimal/inteiros com política financeira correta. |
| BACK-012 | P0 | Limite de quota | Disparar consumo paralelo de limite de tokens/requests. | Quota respeitada mesmo sob concorrência. |
| BACK-013 | P1 | Cache de configuração | Mudar limite por tenant durante operação. | Valores atualizados dentro de política prevista. |
| BACK-014 | P0 | Retry de integração externa | Injetar perda de resposta e reexecução do fluxo. | Idempotência ou reconciliação evita duplicidade. |
| BACK-015 | P0 | Vazamento em erro | Forçar exceção de ORM e observar API e logs. | Sem credenciais, stack privado ou payloads sensíveis em resposta. |
| BACK-016 | P1 | Shutdown em processamento | Reiniciar worker com fila ocupada. | Mensagens não desaparecem; retomada segura. |
