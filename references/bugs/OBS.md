# OBS: 25. Logs, observabilidade, alertas e resposta

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| OBS-001 | P1 | Trace sem correlação | Reproduzir pedido atravessando frontend, API, worker e banco. | Correlation ID permite seguir evento entre serviços. |
| OBS-002 | P1 | Erro sem contexto | Provocar exceção e abrir observabilidade. | Registro inclui versão, rota, tenant pseudonimizado e ação. |
| OBS-003 | P0 | PII no stack trace | Gerar erro com CPF/email fictícios em payload. | Logs e ferramentas mascaram dados conforme política. |
| OBS-004 | P1 | Alertas desabilitados | Simular indisponibilidade sintética. | Alerta atinge responsável em prazo definido. |
| OBS-005 | P1 | Alerta ruidoso | Disparar flapping intermitente durante teste. | Deduplicação e escalonamento funcionam. |
| OBS-006 | P1 | Crash sem símbolos | Publicar build de teste e provocar crash. | dSYM/sourcemap/PDB disponíveis para diagnóstico protegido. |
| OBS-007 | P1 | Sourcemap público | Verificar política de distribuição de maps e debug artifacts. | Artefatos são acessíveis só conforme política de segurança. |
| OBS-008 | P1 | Métricas sem versão | Forçar regressão após atualização de app. | Dashboards segmentam por build/OS/dispositivo. |
| OBS-009 | P0 | Logs alteráveis | Tentar apagar trilha com identidade operacional de teste. | Eventos críticos preservados conforme controles de auditoria. |
| OBS-010 | P1 | Perda de evento | Induzir pane na pipeline de logs em staging. | Buffer/fallback ou alarme identifica lacuna. |
| OBS-011 | P1 | Bug marcado resolvido | Reabrir fluxo após correção e disparar teste de regressão. | Ticket registra verificação em build e ambiente exatos. |
| OBS-012 | P2 | Bug duplicado | Criar dois tickets com mesma assinatura de falha. | Triagem agrupa mantendo evidências separadas. |
| OBS-013 | P1 | Runbook de falha | Simular dependência externa indisponível em tabletop. | Equipe segue passos documentados de contenção/recuperação. |
| OBS-014 | P0 | Rollback manual | Ensaiar rollback de versão em staging sem acesso root direto. | Procedimento atende RTO e preserva dados. |
| OBS-015 | P0 | Métrica de sucesso errada | Gerar requisição 200 com operação não persistida em teste. | Instrumentação mede sucesso de negócio, não só HTTP 200. |
