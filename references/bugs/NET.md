# NET: 21. Rede, DNS, latência e falhas de dependências

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| NET-001 | P1 | DNS intermitente | Bloquear resolução do host em staging por janelas curtas. | Retries limitados e erros compreensíveis. |
| NET-002 | P0 | TLS expirado | Apontar cliente de teste para certificado inválido. | Conexão rejeitada sem bypass de segurança. |
| NET-003 | P1 | Proxy corporativo | Executar no ambiente com proxy permitido e certificado gerenciado. | Política de confiança e diagnósticos claros. |
| NET-004 | P1 | Latência 2-10 s | Adicionar atrasos variáveis a endpoints com dados fictícios. | Timeout/cancelamento e UI dentro de orçamentos. |
| NET-005 | P1 | Perda de pacotes | Simular 5-20% de perda na rede de teste. | Retentativas limitadas e idempotência preservada. |
| NET-006 | P0 | Interrupção após commit | Cortar conexão após aplicação do comando no servidor. | Cliente consulta status e evita reexecutar ação. |
| NET-007 | P1 | Resposta truncada | Interromper streaming JSON/arquivo antes do fim. | Parser rejeita incompleto; sem dados finais falsos. |
| NET-008 | P1 | HTTP 429 | Impor limitação temporária da API. | Cliente respeita Retry-After quando fornecido e orçamento de retries. |
| NET-009 | P1 | HTTP 503 prolongado | Manter dependência indisponível durante fluxo sensível. | Circuit breaker/degradação e alerta funcionam. |
| NET-010 | P0 | Redirecionamento inesperado | Responder 30x para domínio não previsto no cliente de teste. | Credenciais não vazam para destino não autorizado. |
| NET-011 | P1 | WebSocket sem ping | Simular conexão aparentemente ativa sem troca de mensagens. | Heartbeat detecta e recupera conexão. |
| NET-012 | P1 | Mudança de IP | Alternar rede durante upload/login. | Sessões e operações seguem política de segurança sem duplicidade. |
| NET-013 | P1 | API dependência lenta | Simular latência de fornecedor externo acima do SLO. | Isolamento e timeout evitam bloqueio total da aplicação. |
| NET-014 | P1 | Requisição cancelada | Cancelar navegação enquanto backend processa. | Servidor mantém semântica transacional definida. |
| NET-015 | P0 | Relógio cliente divergente | Alterar fuso/hora do dispositivo e validar expiração. | Decisões críticas usam tempo confiável do servidor. |
| NET-016 | P0 | Cache HTTP privado | Forçar proxy a armazenar respostas de contas de teste. | Headers e chaves impedem distribuição cruzada de dados. |
