# DESK: 25. Desktop: Windows, macOS e Linux / 25.2. Windows: EXE, MSI e MSIX

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| DESK-01 | P0 | Assinatura | Assinar binário e instalador conforme o sistema. |
| DESK-02 | P0 | Origem oficial | Distribuir apenas por canais confiáveis. |
| DESK-03 | P0 | Integridade | Verificar assinatura e hash de pacote. |
| DESK-04 | P0 | Atualizador | Autenticar manifesto e pacote antes de aplicar. |
| DESK-05 | P0 | Atualização atômica | Evitar instalação parcial. |
| DESK-06 | P1 | Rollback | Prever retorno compatível com dados persistidos. |
| DESK-07 | P0 | Secrets locais | Usar DPAPI, Keychain ou secret service apropriado. |
| DESK-08 | P0 | Arquivos privados | Aplicar permissões de usuário e isolamento. |
| DESK-09 | P0 | Configurações | Não gravar tokens e senhas em JSON/YAML em claro. |
| DESK-10 | P0 | Comandos do SO | Não concatenar argumentos não confiáveis em shell. |
| DESK-11 | P0 | Argument injection | Validar todos os parâmetros externos. |
| DESK-12 | P0 | Path traversal | Verificar caminhos ao gravar e extrair arquivos. |
| DESK-13 | P0 | Symlink attacks | Evitar trocas de destino e TOCTOU em arquivos sensíveis. |
| DESK-14 | P0 | Library hijack | Restringir fontes de DLLs e bibliotecas. |
| DESK-15 | P0 | IPC | Autenticar chamadas entre processos. |
| DESK-16 | P0 | Serviço local | Proteger portas localhost e sockets. |
| DESK-17 | P1 | Privilégios | Evitar UAC/sudo para ações corriqueiras. |
| DESK-18 | P0 | Elevação controlada | Validar pedidos feitos a processos privilegiados. |
| DESK-19 | P0 | WebView | Isolar conteúdo web de recursos do SO. |
| DESK-20 | P0 | Protocolos externos | Validar URLs e targets antes de abrir. |
| DESK-21 | P1 | Memória nativa | Mitigar use-after-free e buffers inseguros. |
| DESK-22 | P1 | Logs locais | Não persistir tokens e dados privados desnecessários. |
| DESK-23 | P1 | Clipboard | Evitar manter credenciais sem necessidade. |
| DESK-24 | P1 | Início automático | Documentar e restringir autostart. |
| DESK-25 | P1 | Background/tray | Encerrar processos e sessões quando apropriado. |
| DESK-26 | P0 | Logout no desktop | Apagar caches e credenciais da conta. |
| DESK-27 | P1 | Múltiplas instâncias | Evitar escrita concorrente e corrupção. |
| DESK-28 | P1 | Instalador seguro | Proteger locais temporários e arquivos privilegiados. |
| DESK-29 | P1 | Desinstalação | Remover serviços e tratar dados locais. |
| DESK-30 | P1 | Crash dumps | Proteger dumps contra exposição de dados. |
| DESK-31 | P1 | Atualização do SO | Testar compatibilidade após patches. |
| DESK-32 | P1 | Plugins | Isolar extensões e suas permissões. |
| DESK-33 | P1 | Antivírus/EDR | Testar distribuição e minimizar falsos positivos. |
| DESK-34 | P1 | Instalação offline | Definir comportamento seguro sem conectividade. |
| DESK-35 | P0 | Cache multi-tenant EXE, MSI e MSIX e o mecanismo de atualização CONTROLE / RISCO | Impedir vazamento via dados locais e temporários. devem compor a mesma cadeia de confiança. EXIGÊNCIA / EVIDÊNCIA |
