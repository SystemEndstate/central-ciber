# INSTALL: 17. Instalação, atualização, distribuição e rollback

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| INSTALL-001 | P0 | Manifest inválido | Servir manifesto com versão ou hash incorreto em ambiente de teste. | Atualizador rejeita manifesto inválido. |
| INSTALL-002 | P0 | Pacote adulterado | Modificar byte de instalador/cópia de atualização de teste. | Assinatura/hash inválidos impedem aplicação. |
| INSTALL-003 | P0 | Download interrompido | Derrubar conexão no meio do download. | Retomada ou reinício controlado; pacote parcial nunca executado. |
| INSTALL-004 | P1 | Disco sem espaço | Reduzir espaço e iniciar instalação. | Aviso antecipado ou rollback limpo sem corrupção. |
| INSTALL-005 | P0 | Instalação parcial | Interromper processo entre cópia e ativação de executável. | Versão antiga ainda abre ou mecanismo de reparo é funcional. |
| INSTALL-006 | P0 | Atualização com DB local | Atualizar app com milhões de linhas sintéticas offline. | Migração preserva integridade e é recuperável. |
| INSTALL-007 | P0 | Upgrade de N-2 | Atualizar de versão antiga suportada diretamente para a atual. | Todas as migrações necessárias executadas. |
| INSTALL-008 | P0 | Downgrade incompatível | Tentar voltar versão após schema irreversível. | Downgrade bloqueado claramente ou migração reversa segura. |
| INSTALL-009 | P1 | Canal beta/estável | Instalar beta e depois versão estável. | Dados não são migrados incorretamente entre canais. |
| INSTALL-010 | P0 | Rollback de serviço | Reverter backend enquanto clientes atuais continuam ativos. | Contrato e schema suportam a transição. |
| INSTALL-011 | P0 | Update em duas instâncias | Abrir app em duas instâncias enquanto atualiza. | Nenhum processo executa combinação inválida de arquivos. |
| INSTALL-012 | P1 | Permissão negada no destino | Retirar permissão de escrita durante upgrade. | Falha segura e instalação íntegra. |
| INSTALL-013 | P1 | Certificado expirado | Testar pacote assinado com configuração de validação apropriada. | Regras de assinatura/carimbo de tempo interpretadas corretamente. |
| INSTALL-014 | P0 | Update obrigatório | Abrir app antigo vulnerável sem conectividade. | Política de acesso explicita e executável pelo backend. |
| INSTALL-015 | P1 | Desinstalar após upgrade | Instalar várias versões e remover a atual. | Sem serviços órfãos nem dados indevidamente removidos. |
| INSTALL-016 | P0 | Dispositivo reinicia | Reiniciar VM durante fase controlada do upgrade. | Recuperação consistente na próxima inicialização. |
