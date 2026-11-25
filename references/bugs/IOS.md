# IOS: 12. iOS e iPadOS: crash, memória e ciclo de vida

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| IOS-001 | P1 | Jetsam | Provocar pressão de memória com app em uso/fundo. | Retorno recupera estado; nenhuma perda silenciosa. |
| IOS-002 | P0 | Face ID falha | Cancelar autenticação e testar fallback permitido. | Sem bypass; recuperação de acesso prevista. |
| IOS-003 | P1 | Biometria alterada | Adicionar/remover rosto/digital no aparelho de teste. | Credenciais protegidas respeitam política de invalidação. |
| IOS-004 | P1 | Arquivo protegido bloqueado | Executar tarefa offline com iPhone bloqueado. | App trata indisponibilidade de dados protegidos corretamente. |
| IOS-005 | P0 | Background suspension | Suspender app durante escrita ou upload. | Operação é concluída ou recuperada sem duplicidade. |
| IOS-006 | P0 | Universal Link | Abrir link autorizado, expirado, malformado e de outro tenant. | Destino correto; permissão revalidada no servidor. |
| IOS-007 | P0 | Keychain ao reinstalar | Excluir/reinstalar app e tentar recuperar credenciais antigas. | Comportamento explícito de limpeza/reuso conforme política. |
| IOS-008 | P0 | Push lockscreen | Enviar notificação de cenário sensível com aparelho bloqueado. | Sem vazamento de conteúdo privado na prévia. |
| IOS-009 | P1 | Rotação iPad | Redimensionar Split View/Stage Manager quando aplicável. | Layout funcional e estado persistente. |
| IOS-010 | P1 | Dynamic Type | Aplicar tamanhos de fonte máximos suportados. | Botões e erros críticos acessíveis. |
| IOS-011 | P1 | VoiceOver | Navegar formulários somente pelo leitor de tela. | Rótulos, ordens e alertas adequados. |
| IOS-012 | P1 | Cancelamento async | Sair da tela durante Task/async com resposta atrasada. | Sem atualização de modelo inválido ou crash. |
| IOS-013 | P1 | Crash simbolicado | Provocar exceção de teste em build de distribuição. | Stack simbólica e versão recuperáveis sem dados sensíveis. |
| IOS-014 | P0 | SwiftData/Core Data upgrade | Abrir versão nova com armazenamento local legado. | Migração íntegra e verificável. |
| IOS-015 | P0 | Mudança de conta | Alternar Apple ID/app account conforme cenário suportado. | Dados e sessões do usuário anterior não reaparecem. |
| IOS-016 | P0 | Modo avião no pagamento | Desconectar após confirmação local, antes da resposta remota. | Nenhuma aprovação falsa nem duplicidade em retry. |
| IOS-017 | P1 | Notificação abre app morto | Tocar alerta quando app não está em memória. | Fluxo respeita login e contexto correto. |
| IOS-018 | P1 | Falha TestFlight | Testar build de distribuição, não apenas debug no Xcode. | Mesmas funcionalidades críticas operam em release. |
