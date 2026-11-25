# AND: 11. Android: lifecycle, ANR, crashes e dispositivos

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| AND-001 | P1 | Process death | Ativar app, ir ao fundo e matar processo pelo sistema/testes. | Retomada sem dados incoerentes ou operação duplicada. |
| AND-002 | P1 | Rotação de tela | Girar durante preenchimento, upload e navegação. | Estado recuperável e nenhum envio repetido. |
| AND-003 | P1 | ANR por I/O | Executar consulta/sincronização pesada na tela inicial. | Thread principal não fica bloqueada. |
| AND-004 | P1 | Permissão negada | Recusar câmera, microfone, fotos e localização. | Fluxo alternativo ou explicação sem crash. |
| AND-005 | P1 | Permissão revogada | Aceitar permissão, abrir recurso, revogar em configurações. | App reage sem crash ou acesso indevido. |
| AND-006 | P1 | Bateria restrita | Habilitar otimização agressiva e suspender app. | Jobs sobrevivem dentro das garantias Android. |
| AND-007 | P0 | Network handoff | Alternar Wi-Fi/dados durante post crítico. | Retry sem duplicidade; sessão consistente. |
| AND-008 | P1 | Low-memory kill | Submeter app a pressão de memória e voltar. | Estado restaurado sem corrupção. |
| AND-009 | P1 | Notificação duplicada | Enviar mesma push/evento mais de uma vez. | Ação idempotente e sem notificações indevidas. |
| AND-010 | P0 | Deep link inválido | Abrir app link com IDs de outro tenant ou parâmetros quebrados. | Rota rejeitada ou autorizada corretamente. |
| AND-011 | P0 | Intent externo | Enviar intent sintético a componente exportado próprio. | Sem operações privilegiadas por entrada não confiável. |
| AND-012 | P0 | WebView bridge | Carregar conteúdo controlado não confiável na WebView de teste. | JS sem capacidade não autorizada de chamar funções nativas. |
| AND-013 | P0 | Android backup/restore | Restaurar app em outro aparelho de teste. | Credenciais e dados restaurados conforme política segura. |
| AND-014 | P1 | APK antigo vs API | Usar última versão suportada com API atual. | Compatível ou bloqueio de atualização claro. |
| AND-015 | P1 | Teclado e acessibilidade | Usar TalkBack, fontes ampliadas e teclado alternativo. | Fluxo principal utilizável sem campos ocultos. |
| AND-016 | P0 | SQLite migração | Atualizar de versão antiga com DB local pré-populado. | Dados íntegros e schema migrado corretamente. |
| AND-017 | P2 | App em tela dividida | Alternar foco e dimensões continuamente. | Sem perda de contexto ou botões inacessíveis. |
| AND-018 | P0 | Abrir via notificação | Tocar push com app encerrado/conta deslogada. | Roteamento e autenticação corretos. |
