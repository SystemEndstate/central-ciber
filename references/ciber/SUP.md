# SUP: 9. Supabase: Auth, RLS, Storage e Realtime

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| SUP-01 | P0 | RLS em tabelas expostas | Habilitar RLS nas tabelas protegidas visíveis à API. |
| SUP-02 | P0 | Policies por operação | Definir SELECT, INSERT, UPDATE e DELETE conforme necessidade. |
| SUP-03 | P0 | Grants mínimos | Revisar acesso anon e authenticated por schema, tabela e função. |
| SUP-04 | P0 | Tenant isolation | Limitar linhas e relacionamentos por organização autorizada. |
| SUP-05 | P0 | Chave publicável | Permitir no cliente somente a chave pública, com RLS e grants corretos. |
| SUP-06 | P0 | Secret keys | Manter credenciais privilegiadas no backend. |
| SUP-07 | P0 | service_role | Isolar porque contorna RLS em operações privilegiadas. |
| SUP-08 | P0 | JWT válido | Verificar identidade e claims antes de decisões sensíveis. |
| SUP-09 | P0 | Auth com SSR | Usar getClaims para validação; não autorizar pelo getSession isolado. |
| SUP-10 | P1 | getUser | Consultar o Auth quando dados atuais do usuário forem necessários. |
| SUP-11 | P0 | Views | Auditar security_invoker e impedir bypass indevido de RLS. |
| SUP-12 | P0 | Funções SQL RPC | Revisar SECURITY DEFINER, search_path e EXECUTE. |
| SUP-13 | P0 | Buckets privados | Não publicar documentos confidenciais. |
| SUP-14 | P0 | Storage policies | Autorizar operações em storage.objects por dono e tenant. |
| SUP-15 | P0 | Realtime authorization | Impedir inscrição em canais de outras organizações. |
| SUP-16 | P0 | Edge Functions | Validar identidade e permissão em todos os fluxos. |
| SUP-17 | P1 | OTP e login | Configurar expiração e proteção contra abuso. |
| SUP-18 | P0 | MFA no painel | Exigir MFA para usuários privilegiados do projeto. |
| SUP-19 | P1 | Security Advisor | Triar e resolver alertas relevantes. |
| SUP-20 | P1 | SSL enforcement | Exigir conexões seguras ao PostgreSQL. |
| SUP-21 | P1 | Network restrictions | Restringir conexões diretas quando possível. |
| SUP-22 | P0 | Backup PostgreSQL | Confirmar retenção, PITR e procedimento testado. |
| SUP-23 | P0 | Backup de objetos | Recuperar Storage separadamente dos backups do PostgreSQL. |
| SUP-24 | P1 | Migrações versionadas | Revisar schema, grants, policies e funções em cada mudança. |
| SUP-25 | P0 | Ambientes isolados | Separar projetos, segredos e dados de dev e produção. |
| SUP-26 | P1 | Auditoria | Observar acessos, políticas e ações administrativas. |
| SUP-27 | P1 | Rotação de chaves | Ter processo para chaves comprometidas. |
| SUP-28 | P1 | Data API mínima | Desabilitar Data API quando a arquitetura não exigir acesso direto. |
