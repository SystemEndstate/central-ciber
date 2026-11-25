# WIN: 13. Windows EXE: processos, instaladores e ambiente

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| WIN-001 | P1 | Instalação sem admin | Instalar como usuário padrão no caminho suportado. | Funciona ou explica necessidade de elevação legítima. |
| WIN-002 | P0 | Instalador interrompido | Encerrar instalação no meio em VM descartável. | Sistema permanece recuperável; sem restos privilegiados inseguros. |
| WIN-003 | P1 | Desinstalação interrompida | Interromper remoção e reinstalar. | Sem registro corrompido que impeça reparo. |
| WIN-004 | P0 | EXE assinado alterado | Corromper cópia de binário em laboratório. | Verificação de integridade falha; não executa atualização. |
| WIN-005 | P1 | DLL ausente | Remover dependência não essencial em instalação de teste. | Erro orienta reparação; não trava sem diagnóstico. |
| WIN-006 | P0 | DLL hijacking | Colocar DLL de teste em caminho não confiável permitido no laboratório. | Carregamento é restrito a locais esperados. |
| WIN-007 | P0 | Named pipe acesso | Conectar processo local não autorizado a pipe de teste. | Pipe rejeita ações privadas ou privilegiadas. |
| WIN-008 | P0 | Servidor localhost | Enviar requests simulados de origem/processo não autorizado. | Endpoints locais autenticados e com proteção contra abuse. |
| WIN-009 | P0 | Duas instâncias | Abrir mesmo app simultaneamente e editar documento. | Bloqueios/controle de concorrência evitam corrupção. |
| WIN-010 | P1 | Registro sem permissão | Executar app com HKLM somente leitura. | Operações de usuário não exigem gravação privilegiada. |
| WIN-011 | P1 | DPI 200% | Testar 100/125/150/200% e dois monitores com escalas diferentes. | Textos e controles íntegros e acionáveis. |
| WIN-012 | P1 | Sleep/hibernate | Suspender notebook durante sync/upload e retomar. | Conexões e estado se recuperam de modo consistente. |
| WIN-013 | P1 | Antivírus quarantena | Simular arquivo dependente bloqueado em VM de teste. | Erro recuperável e sem recomendação de desativar AV. |
| WIN-014 | P0 | Atualização com app aberto | Atualizar versão com janelas e serviços ativos. | Transição segura, sem mistura de versões. |
| WIN-015 | P0 | Multiusuário Windows | Alternar contas locais e ler caches/configs por usuário. | Dados privados e credenciais isolados por conta. |
| WIN-016 | P0 | Crash dump | Provocar crash controlado e inspecionar dump/logs. | Dados confidenciais não expostos sem necessidade. |
| WIN-017 | P1 | Tray encerramento | Fechar janela e verificar processos que permanecem ativos. | Comportamento claro; logout/saída corretos. |
| WIN-018 | P1 | File locking | Editar arquivo enquanto antivírus ou outro processo o mantém aberto. | Erro tratado sem corrupção ou loop infinito. |
