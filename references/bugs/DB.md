# DB: 08. PostgreSQL, SQL, integridade e concorrência

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| DB-001 | P0 | Lost update | Dois clientes leem e alteram mesmo registro em paralelo. | Conflito detectado ou serialização correta. |
| DB-002 | P0 | Phantom/nonrepeatable | Ler dados durante transações concorrentes sob isolamento configurado. | Invariantes preservados pelo nível de isolamento e estratégia escolhidos. |
| DB-003 | P1 | Deadlock de transação | Executar atualizações em ordem invertida em dois workers. | Deadlock detectado; retry seguro e limitado. |
| DB-004 | P0 | Constraint ausente | Inserir duplicatas ou referências inválidas com SQL de teste. | Constraints impedem estado proibido. |
| DB-005 | P0 | NULL inesperado | Inserir dados ausentes em campos de regra obrigatória. | Banco ou serviço rejeita antes de persistir inconsistência. |
| DB-006 | P0 | Migração forward | Aplicar migração em snapshot anonimizado do schema anterior. | Dados e índices preservados; versão nova opera. |
| DB-007 | P0 | Compatibilidade N/N-1 | Rodar clientes/serviços antigos durante migração expand/contract. | Sem erro de coluna ausente ou perda de escrita. |
| DB-008 | P0 | Rollback de migration | Simular falha no meio da mudança de schema. | Estado documentadamente recuperável; sem migração parcial oculta. |
| DB-009 | P1 | Índice ausente | Executar consultas reais em dados sintéticos volumosos. | Planos e latência dentro do orçamento definido. |
| DB-010 | P1 | Pool exaurido | Gerar concorrência maior que conexões disponíveis. | Fila/timeouts controlados; sem queda generalizada. |
| DB-011 | P1 | Consulta sem paginação | Solicitar exportação/lista extremamente volumosa. | Limite, streaming e orçamento de memória aplicados. |
| DB-012 | P0 | Timezone no banco | Gravar instantes em várias zonas e consultar ordenação. | Sem deslocamento indevido em comparações. |
| DB-013 | P0 | Precisão de decimal | Gravar montantes fracionários e executar somatórios. | Precisão garantida conforme domínio. |
| DB-014 | P2 | Sequência após rollback | Executar transação falha que gera ID sequencial. | Sistema não presume sequência sem lacunas. |
| DB-015 | P0 | Restore íntegro | Restaurar snapshot em ambiente isolado e rodar invariantes. | Dados relacionais e schema validados após restauração. |
| DB-016 | P1 | Soft delete | Excluir lógico e procurar dados em relatórios, joins e índices. | Registros excluídos não reaparecem fora das regras definidas. |
