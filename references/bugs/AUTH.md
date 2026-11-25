# AUTH: 05. Usuários, autenticação, sessão e autorização

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| AUTH-001 | P0 | Sessão expirada | Manter janela aberta até o vencimento e tentar salvar alteração. | Reautenticação segura; operação não é atribuída a sessão inválida. |
| AUTH-002 | P0 | Logout incompleto | Sair e reenviar chamada API com credencial de teste antiga. | Revogação respeita política de segurança documentada. |
| AUTH-003 | P0 | Conta desativada | Desativar usuário ainda autenticado e tentar operação sensível. | Servidor recusa segundo latência de revogação estipulada. |
| AUTH-004 | P0 | Alteração de role | Reduzir papel admin para viewer durante sessão ativa. | Próxima ação sensível verifica privilégios atuais. |
| AUTH-005 | P0 | Tentativa IDOR | Trocar ID de documento de A pelo de B em request próprio. | Leitura/escrita cruzada negada. |
| AUTH-006 | P0 | Troca de tenant | Alternar organização sem reiniciar cliente e repetir operação. | Dados, cache e permissões são atualizados conjuntamente. |
| AUTH-007 | P1 | Refresh simultâneo | Disparar várias chamadas ao expirar access token. | Renovação coordenada; sem logout em cascata ou token perdido. |
| AUTH-008 | P1 | Login em duas sessões | Criar sessões em dois dispositivos e revogar uma. | Política de revogação aplicada sem encerrar sessão errada. |
| AUTH-009 | P0 | Redefinição repetida | Usar link de redefinição já consumido. | Token não pode ser reutilizado. |
| AUTH-010 | P1 | Enumeração de conta | Comparar mensagens para e-mails existentes e fictícios. | Não revela existência de contas indevidamente. |
| AUTH-011 | P0 | MFA interrompido | Fechar app durante verificação MFA e tentar operação protegida. | Autenticação permanece incompleta até prova válida. |
| AUTH-012 | P0 | Cookie em cross-site | Executar ação com contexto cross-site em ambiente autorizado. | Proteções CSRF e SameSite conforme arquitetura. |
| AUTH-013 | P0 | Impersonação administrativa | Iniciar e encerrar acesso assistido a conta de teste. | Consentimento/justificativa, escopo e trilha auditável. |
| AUTH-014 | P1 | Conta sem e-mail verificado | Tentar ações que exigem confirmação de titularidade. | Ações críticas bloqueadas até condição exigida. |
| AUTH-015 | P0 | Revogação de convite | Aceitar convite que acabou de ser cancelado. | Convite inválido e acesso não concedido. |
| AUTH-016 | P0 | Permissão em função RPC | Invocar RPC/Server Action sem passar pelo frontend. | Backend ou banco aplica regra de autorização independente. |
