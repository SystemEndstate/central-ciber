# PAY: 20. Pagamentos, assinaturas e faturamento

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| PAY-001 | P0 | Webhook pagamento duplicado | Reentregar mesmo evento confirmado duas vezes. | Uma única baixa/crédito no ledger. |
| PAY-002 | P0 | Evento fora de ordem | Entregar cancelamento antes de confirmação no sandbox. | Máquina de estados mantém resultado consistente. |
| PAY-003 | P0 | Timeout após cobrança | Simular ausência de resposta após captura autorizada em sandbox. | Retry consulta evento por ID e não captura novamente. |
| PAY-004 | P0 | Preço no client | Alterar preço enviado pelo frontend em teste. | Servidor recalcula usando catálogo/política confiável. |
| PAY-005 | P0 | Desconto inválido | Aplicar cupom vencido e simultâneo em contas de teste. | Regras verificadas atomicamente. |
| PAY-006 | P0 | Troca de plano simultânea | Executar upgrade e cancelamento ao mesmo tempo. | Estado final definido e cobranças consistentes. |
| PAY-007 | P0 | Reembolso parcial | Testar cenários de reembolso parcial em sandbox. | Saldo, invoice e direitos atualizados corretamente. |
| PAY-008 | P0 | Moeda e centavos | Comparar BRL e outras moedas simuladas com frações. | Precisão e arredondamento corretos por moeda. |
| PAY-009 | P1 | Falha na emissão fiscal | Pagamento aprovado e emissão de documento falha. | Fluxo de compensação/retry rastreável. |
| PAY-010 | P0 | Renovação atrasada | Receber evento de cobrança horas depois do vencimento. | Direitos do assinante obedecem política documentada. |
| PAY-011 | P0 | Pagamento recusado | Simular cartão recusado e retry automático do provedor. | Sem concessão indevida de acesso. |
| PAY-012 | P0 | Falha de conciliação | Inserir cenário de evento faltante em ambiente de homologação. | Reconciliação identifica desvio e evita estado silencioso. |
| PAY-013 | P0 | Alterar recebedor | Usuário tenta modificar destinatário de pagamento fora de permissão. | Mudança negada e auditada. |
| PAY-014 | P0 | Fuso de assinatura | Testar datas de corte em UTC e timezone local. | Cobrança e renovação no instante contratado. |
| PAY-015 | P0 | Crédito sem pagamento | Criar tentativa de acesso com retorno de UI falso positivo. | Backend não libera benefício sem confirmação verificável. |
| PAY-016 | P0 | Transferência duplicada | Executar duas requisições simultâneas com chave idempotente. | Uma operação efetiva; status consistente para ambas. |
