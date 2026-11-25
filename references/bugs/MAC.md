# MAC: 14. macOS: apps, permissões e distribuição

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| MAC-001 | P0 | Notarização | Distribuir build de teste sem/ com notarização conforme canal. | Processo de distribuição e Gatekeeper comportam-se como esperado. |
| MAC-002 | P0 | Assinatura quebrada | Alterar um arquivo do .app assinado em cópia de teste. | Verificação de assinatura detecta adulteração. |
| MAC-003 | P0 | Keychain bloqueado | Negar acesso a item seguro em conta de teste. | App pede autenticação ou falha de modo controlado. |
| MAC-004 | P1 | Permissão de arquivos | Revogar acesso à pasta Documentos durante importação. | Operação aborta sem corromper arquivo. |
| MAC-005 | P1 | Microfone negado | Negar gravação de áudio em fluxo suportado. | Interface orienta; app não entra em crash loop. |
| MAC-006 | P1 | Sleep/wake | Suspender Mac durante conexão e retomar. | Sockets/sessões reconectam sem duplicar ações. |
| MAC-007 | P1 | Múltiplos Spaces | Mover janela entre áreas de trabalho e monitores. | Foco, modais e coordenadas permanecem funcionais. |
| MAC-008 | P1 | Menu bar fechada | Fechar janela principal com helper/menu bar ativo. | Estado e processos cumprem política de saída. |
| MAC-009 | P0 | Atualização notarizada | Instalar atualização assinada em máquina de teste. | Binário final mantém assinatura/entitlements e abre corretamente. |
| MAC-010 | P0 | App sandbox diretório | Tentar importar/exportar arquivo fora do escopo concedido. | Acesso pede autorização, sem bypass. |
| MAC-011 | P1 | Migração Intel->ARM | Transferir base local de uma versão para outra arquitetura. | Dados e plugins compatíveis, sem perda. |
| MAC-012 | P1 | Crash em release | Provocar falha controlada no build assinado. | Relatório simbolicado com versão e contexto disponíveis. |
| MAC-013 | P1 | Quick Look/preview | Pré-visualizar arquivo malformado suportado. | Parser isolado, sem execução ou travamento prolongado. |
| MAC-014 | P0 | Logout e re-login | Trocar usuário da aplicação mantendo app aberto. | Sem reaproveitar Keychain/cache incorretamente. |
| MAC-015 | P0 | Deep link macOS | Abrir custom URL com IDs inválidos e esquemas inesperados. | Nenhuma ação de alto privilégio sem validação. |
| MAC-016 | P1 | Desinstalação | Remover app e verificar arquivos residuais conforme política. | Dados/credenciais tratados de forma documentada. |
