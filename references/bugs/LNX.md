# LNX: 15. Linux: permissões, pacotes e dependências

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| LNX-001 | P1 | Dependência ausente | Executar pacote em distro mínima suportada. | Dependência declarada ou erro de instalação acionável. |
| LNX-002 | P0 | Pacote quebrado | Interromper instalação apt/rpm em VM. | Gerenciador consegue reparar; sem scripts perigosos persistentes. |
| LNX-003 | P1 | Executar sem root | Abrir app como usuário padrão em ambiente limpo. | Fluxos normais funcionam sem sudo. |
| LNX-004 | P1 | Diretório read-only | Revogar permissão temporária sobre pasta de dados de teste. | Aplicação avisa e preserva dados anteriores. |
| LNX-005 | P0 | Symlink manipulado | Apontar arquivo de entrada para caminho fora de diretório de teste. | App valida destino e escopo antes de manipular arquivo. |
| LNX-006 | P0 | Socket Unix | Criar cliente local não autorizado e conectar ao socket. | Permissões/autorização impedem acesso indevido. |
| LNX-007 | P1 | Wayland/X11 | Executar os dois backends de janela quando suportados. | Teclado, clipboard, resize e captura funcionam conforme política. |
| LNX-008 | P1 | DPI/font fallback | Testar escalas e fontes ausentes. | UI não some nem perde legibilidade. |
| LNX-009 | P1 | Biblioteca incompatível | Testar versões glibc/OpenSSL suportadas. | Build informa limites e funciona em ambientes declarados. |
| LNX-010 | P1 | systemd restart | Reiniciar serviço de apoio durante operação pendente. | Fila e estado se recuperam corretamente. |
| LNX-011 | P1 | Flatpak permission | Revogar portal de pasta/câmera e repetir ação. | App lida com recusa sem forçar bypass. |
| LNX-012 | P0 | Atualização no pacote | Instalar versão nova com cache da versão antiga. | Migração e operação consistentes. |
| LNX-013 | P0 | Espaço em disco cheio | Limitar filesystem de teste e iniciar escrita. | Arquivo atual permanece íntegro; falha explícita. |
| LNX-014 | P1 | Signals de término | Enviar SIGTERM ao processo de teste durante atividade. | Shutdown respeita grace period e persistência. |
| LNX-015 | P0 | Múltiplas sessões | Abrir app com dois usuários Linux separados. | Dados privados e configs não ficam compartilhados. |
| LNX-016 | P1 | Crash report | Provocar crash em build de teste e coletar coredump restrito. | Símbolos e telemetria adequados sem expor segredos. |
