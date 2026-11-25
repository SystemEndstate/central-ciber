# DISC: 01. Descoberta, reprodução e triagem

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| DISC-001 | P1 | Bug não reproduzível | Repetir cenário com versão, tenant, usuário, horário, estado e rede anotados. | Passos determinísticos ou hipótese documentada e evidência suficiente. |
| DISC-002 | P1 | Erro intermitente | Executar muitas iterações registrando seeds, IDs de correlação e latência. | Frequência medida; gatilho e variação isolados. |
| DISC-003 | P0 | Produção diferente do staging | Comparar flags, variáveis, migrações, permissões e versões sem expor segredos. | Desvios rastreados e classificados como risco de ambiente. |
| DISC-004 | P1 | Erro após deploy | Relacionar primeira ocorrência com commits, versões e mudanças de schema. | Regressão e janela do defeito identificadas. |
| DISC-005 | P1 | Bug relatado sem detalhes | Solicitar fluxo exato, resultado esperado, tela, horário e versão. | Ticket acionável sem dados pessoais desnecessários. |
| DISC-006 | P0 | Erro em um único tenant | Comparar configurações, volume, roles e histórico do tenant de teste. | Diferença explicada, sem acessar dados reais sem autorização. |
| DISC-007 | P1 | Bug só em dispositivo real | Comparar emulador e dispositivo físico, sistema e fabricante. | Matriz de reprodução registra divergências. |
| DISC-008 | P1 | Erro só em carga | Reproduzir com tráfego sintético, rampa e limites conhecidos. | Ponto de degradação e mecanismo de falha medidos. |
| DISC-009 | P1 | Erro após reinício | Executar fluxo, reiniciar app/serviço e retomar estado. | Persistência e recuperação consistentes. |
| DISC-010 | P1 | Bug regressivo | Executar o mesmo teste na última versão estável e na candidata. | Versão introdutora do defeito identificada. |
| DISC-011 | P1 | Sinal não é causa | Correlacionar logs, traces, banco e cadeia de dependências. | Causa raiz sustentada por evidência, não suposição. |
| DISC-012 | P0 | Correção sem teste | Exigir teste que falha antes da correção e passa depois. | Defeito não retorna silenciosamente. |
| DISC-013 | P1 | Pânico em produção | Simular incidente com owner, freeze de deploy e rollback ensaiado. | Decisões rastreáveis e procedimento operacional acionável. |
| DISC-014 | P0 | Logs confidenciais | Inspecionar dumps, screenshots, headers e payloads de relatório. | Evidência útil, com tokens e dados privados removidos. |
