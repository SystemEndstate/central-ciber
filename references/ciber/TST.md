# TST: 17. Matriz de testes de invasão e aceite

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| TST-01 | P0 | Rota anônima | Rota privada deve negar acesso sem login. |
| TST-02 | P0 | Token expirado | Credencial vencida não pode autorizar. |
| TST-03 | P0 | JWT adulterado | Assinatura alterada deve ser rejeitada. |
| TST-04 | P0 | Token de outra audiência | API deve rejeitar credencial de outro serviço. |
| TST-05 | P0 | Sessão revogada | Acesso negado conforme política explícita de revogação. |
| TST-06 | P0 | Leitura cruzada | Usuário A não consulta registro de B. |
| TST-07 | P0 | Escrita cruzada | Usuário A não altera registro de B. |
| TST-08 | P0 | Exclusão cruzada | Usuário A não remove registro de B. |
| TST-09 | P0 | Operação admin | Usuário comum não executa função administrativa. |
| TST-10 | P0 | Alteração de role | A elevação indevida de privilégios falha. |
| TST-11 | P0 | Tenant ID falsificado | Troca de parâmetro não muda autorização. |
| TST-12 | P0 | Arquivo privado | Download de outro usuário é negado. |
| TST-13 | P0 | Tipo de arquivo | Formato proibido é rejeitado. |
| TST-14 | P1 | Payload grande | Requisição é interrompida sem degradação sistêmica. |
| TST-15 | P0 | Entrada SQL hostil | Consultas continuam parametrizadas e protegidas. |
| TST-16 | P0 | HTML não confiável | Script não executa no navegador. |
| TST-17 | P0 | Pagamento duplicado | Repetição não cria cobrança extra. |
| TST-18 | P0 | Webhook inválido | Evento sem assinatura válida é rejeitado. |
| TST-19 | P0 | Repetição de webhook | Não produz novos efeitos. |
| TST-20 | P0 | Login repetitivo | Rate limit e alertas funcionam. |
| TST-21 | P0 | SSRF | URL externa não alcança redes privadas e metadados. |
| TST-22 | P0 | Supabase anon | Chave pública não expõe tabelas privadas. |
| TST-23 | P0 | Supabase tenant | JWT de A não dá acesso aos registros de B. |
| TST-24 | P0 | Realtime privado | Inscrição indevida em canal é bloqueada. |
| TST-25 | P0 | Relatório adulterado | Filtros não extraem dados de outra empresa. |
| TST-26 | P1 | Exportação anormal | Quota, autenticação e auditoria atuam. |
| TST-27 | P0 | Cache pós-logout | Nenhuma resposta de outra sessão é apresentada. |
| TST-28 | P0 | Reset reutilizado | Token de recuperação já consumido falha. |
| TST-29 | P0 | Conta desativada | Acesso interrompido no prazo definido. |
| TST-30 | P1 | Banco indisponível | Erro é controlado e não expõe credenciais. |
| TST-31 | P0 | Perda de dados | Backup restaura dentro de RPO/RTO acordados. |
| TST-32 | P0 | Chave vazada | Runbook de rotação e contenção funciona. |
| TST-33 | P0 | Prompt malicioso | Agente não executa ação sem autorização independente. |
| TST-34 | P0 | Abuso de IA | Cotas e alertas impedem consumo descontrolado. |
| TST-35 | P0 | Role alterada | Permissão ativa é reavaliada no intervalo estabelecido. |
| TST-36 | P0 | Restore isolado | Cópia restaurada mantém integridade verificável. |
