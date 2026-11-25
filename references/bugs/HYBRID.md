# HYBRID: 16. Electron, Tauri e clientes híbridos

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| HYBRID-001 | P0 | Electron preload amplo | Inspecionar funções expostas pelo contextBridge e invocá-las com dados inválidos. | Somente operações necessárias; argumentos e origem validados. |
| HYBRID-002 | P0 | Electron nodeIntegration | Carregar conteúdo remoto em janela de teste. | Node desabilitado e isolamento/sandbox ativos conforme política. |
| HYBRID-003 | P0 | IPC sem validação | Enviar mensagem IPC sintética a handler usando renderer de teste. | Remetente e payload validados antes da ação. |
| HYBRID-004 | P0 | Window.open externo | Solicitar criação de janela ou protocolo externo não confiável. | Navegação bloqueada ou destino validado. |
| HYBRID-005 | P0 | Electron autoUpdater | Servir manifesto assinado inválido em staging. | Instalação rejeitada; app atual preservado. |
| HYBRID-006 | P0 | Tauri capability ampla | Chamar comando fora das permissões da janela de teste. | Operação negada conforme capability configurada. |
| HYBRID-007 | P1 | Tauri command panic | Chamar comando Rust com argumentos extremos. | Erro controlado, sem crash do processo principal. |
| HYBRID-008 | P1 | Plugin nativo não disponível | Desabilitar permissão ou retirar plugin em build de teste. | App reage com fallback ou erro claro. |
| HYBRID-009 | P1 | WebView diferenciado | Comparar Windows WebView2, macOS WKWebView e Linux WebKit. | Funcionalidades e layout compatíveis por plataforma. |
| HYBRID-010 | P0 | CSP rígida | Ativar política mínima e navegar fluxos críticos. | Funciona sem autorizar script arbitrário. |
| HYBRID-011 | P0 | Bundled secret | Inspecionar arquivos ASAR/bundle e configuração de release. | Nenhuma credencial privilegiada embutida. |
| HYBRID-012 | P0 | Arquivo drop/drag | Arrastar arquivo não permitido ou atalho/symlink controlado. | Tratamento respeita extensão, assinatura e caminho. |
| HYBRID-013 | P0 | Menu nativo e UI | Disparar mesma operação por menu, atalho e botão simultaneamente. | Uma única mutação lógica acontece. |
| HYBRID-014 | P1 | Crash processo renderer | Encerrar processo de renderização durante edição. | App preserva dados e recupera janela sem duplicar tarefa. |
| HYBRID-015 | P1 | Crash processo main | Encerrar processo principal no meio de operação. | Recuperação consistente na próxima abertura. |
| HYBRID-016 | P0 | Protocolo customizado | Invocar custom protocol de instalação com parâmetros inválidos. | Roteamento seguro e nenhuma elevação indevida. |
