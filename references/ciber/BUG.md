# BUG: 27. Bugs e causas de vulnerabilidades

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| BUG-01 | P0 | Race condition | Operações simultâneas produzem estado inválido; usar atomicidade e locks/versionamento. |
| BUG-02 | P0 | Double submit | Evitar cobranças ou envios duplicados com idempotência no servidor. |
| BUG-03 | P0 | Bug de autorização | Testar todas as combinações permitidas e proibidas de papéis e objetos. |
| BUG-04 | P0 | Cache cruzado | Associar cache ao escopo exato de usuário e tenant. |
| BUG-05 | P0 | Sync incorreta | Resolver conflitos e evitar sobrescrita silenciosa. |
| BUG-06 | P0 | Upgrade interrompido | Usar atualização transacional e recuperação. |
| BUG-07 | P0 | Migração quebrada | Ensaiar upgrade com cópias anonimizadas e rollback. |
| BUG-08 | P0 | Validação parcial | Usar contratos de entrada e saída consistentes. |
| BUG-09 | P0 | Erro inseguro | Falhar de modo fechado sem expor contexto sensível. |
| BUG-10 | P1 | Memory leak | Executar testes de duração e análise de heap. |
| BUG-11 | P1 | Deadlock | Monitorar locks e impor timeouts e hierarquia. |
| BUG-12 | P1 | UI Freeze/ANR | Evitar bloqueio da thread principal. |
| BUG-13 | P1 | Crash loop | Parar reinicializações infinitas e oferecer recuperação. |
| BUG-14 | P0 | Estado nulo inesperado | Tratar valores ausentes e validar schema. |
| BUG-15 | P1 | Overflow/Underflow | Controlar limites e usar tipos apropriados. |
| BUG-16 | P0 | Precisão monetária | Utilizar decimal ou inteiros em unidade monetária mínima. |
| BUG-17 | P0 | Fusos horários | Guardar instantes canônicos e converter conforme o contexto. |
| BUG-18 | P1 | Relógio adulterado | Usar relógio confiável no servidor para decisões sensíveis. |
| BUG-19 | P0 | Rollback transacional | Garantir que erros não gerem estados parciais. |
| BUG-20 | P0 | Lost update | Conferir versão do registro antes de gravar. |
| BUG-21 | P1 | Retry sem limite | Usar tentativas finitas e backoff com jitter. |
| BUG-22 | P1 | Timeout ausente | Limitar espera por serviços dependentes. |
| BUG-23 | P0 | Confirmação prematura | Exibir sucesso apenas com resposta efetiva do backend. |
| BUG-24 | P1 | Versão incompatível | Manter contratos de API e política de cliente mínimo. |
| BUG-25 | P1 | Dependência quebrada | Fixar/testar versões e acompanhar regressões. |
| BUG-26 | P0 | Falha silenciosa | Observar erros operacionais e reconciliar transações. |
| BUG-27 | P0 | Reprocessamento de eventos | Projetar webhooks e filas para ao menos uma entrega sem duplicação de efeitos. |
| BUG-28 | P1 | UI desatualizada | Distinguir pendente, confirmado e rejeitado. |
| BUG-29 | P0 | Exclusão indevida | Verificar objeto e autorização imediatamente antes da ação. |
| BUG-30 | P1 | Corrupção de arquivos | Usar gravação temporária e troca atômica. |
| BUG-31 | P1 | Unicode e encoding | Tratar normalização e nomes internacionais. |
| BUG-32 | P0 | Parser de arquivo | Isolar parse de XML, PDF, imagens e formatos malformados. |
| BUG-33 | P1 | Paginação incorreta | Usar ordenação estável/cursor para evitar perda ou duplicação. |
| BUG-34 | P0 | Troca de tenant | Limpar estado e revalidar autorização da organização. |
| BUG-35 | P1 | Feature flag | Usar defaults seguros e desligamento rápido. |
| BUG-36 | P1 | Falha de recuperação | Ensaiar retomada após exceção, crash e queda de energia. |
