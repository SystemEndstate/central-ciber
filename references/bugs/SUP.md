# SUP: 09. Supabase: Auth, RLS, Realtime e Storage

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| SUP-001 | P0 | RLS SELECT cruzado | Com JWT de tenant A consultar linha pertencente a B. | Nenhuma linha privada de B retorna. |
| SUP-002 | P0 | RLS INSERT cruzado | Criar registro com user_id/tenant_id de outro usuário. | Inserção negada pela policy e grants. |
| SUP-003 | P0 | RLS UPDATE cruzado | Alterar PK, owner ou tenant_id de linha própria para B. | Atualização negada; propriedade permanece consistente. |
| SUP-004 | P0 | RLS DELETE cruzado | Excluir linha de B usando token de A. | Exclusão negada. |
| SUP-005 | P0 | Tabela nova sem RLS | Criar tabela em schema exposto e rodar inspeção automatizada. | Deploy bloqueia falta de política/grants adequados. |
| SUP-006 | P0 | View ignora RLS | Consultar views que fazem join de dados privados. | Views e definer/invoker não vazam linhas entre tenants. |
| SUP-007 | P0 | Função SECURITY DEFINER | Invocar função SQL de teste com role de baixo privilégio. | Permissões, search_path e autorização interna adequadas. |
| SUP-008 | P0 | Chave de servidor vazada | Inspecionar bundle e variáveis públicas de staging. | Chave secret/service_role ausente do cliente. |
| SUP-009 | P0 | Storage listagem cruzada | Listar prefixos privados com JWT de outra organização. | Objetos externos não aparecem. |
| SUP-010 | P1 | URL assinada longa | Gerar link privado e avaliar escopo/validade/cancelamento. | Acesso dura somente o necessário e segue política estabelecida. |
| SUP-011 | P0 | Realtime canal privado | Inscrever cliente A em canal privado de B. | Assinatura rejeitada; sem eventos cruzados. |
| SUP-012 | P0 | Edge Function sem JWT | Invocar função diretamente sem sessão ou assinatura exigida. | Função valida autenticidade e autorização necessárias. |
| SUP-013 | P0 | Tokens SSR stale | Abrir SSR com sessão expirada e chamar API. | Identidade verificada, não apenas dados de cookie. |
| SUP-014 | P1 | Trigger falha | Inserir registro que aciona trigger com erro simulado. | Transação e estado final ficam consistentes. |
| SUP-015 | P0 | Migração de policy | Atualizar regras RLS e rodar testes pgTAP/cliente. | Nenhuma regressão entre perfis/tenants. |
| SUP-016 | P0 | Restore de Storage | Restaurar banco e simular objeto privado ausente. | Processo inclui estratégia de restauração dos objetos separadamente. |
