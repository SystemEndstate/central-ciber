# PERF: 22. Performance, uso de recursos e estabilidade prolongada

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| PERF-001 | P1 | Memória cresce por navegação | Abrir/fechar tela 300 vezes sob profiler. | Heap retorna a patamar estável aceitável. |
| PERF-002 | P1 | Alto uso de CPU | Repetir busca ou renderização com muitos dados. | CPU e responsividade dentro dos orçamentos. |
| PERF-003 | P1 | Banco com volume realista | Carregar registros sintéticos com distribuição parecida com produção. | Consultas mantêm SLO definido. |
| PERF-004 | P0 | 1000 requisições concorrentes | Fazer rampa controlada com tráfego sintético autorizado. | Sem corrupção; limites e falha controlada. |
| PERF-005 | P1 | Upload paralelo | Enviar múltiplos arquivos grandes com quotas. | Uso de memória e disco controlado. |
| PERF-006 | P1 | ANR/hang | Executar tarefa pesada na thread principal e coletar trace. | UI permanece responsiva; trabalho pesado isolado. |
| PERF-007 | P1 | Gargalo de conexão | Estourar pool de teste de maneira controlada. | Fila, timeouts e alertas adequados. |
| PERF-008 | P1 | Bateria Android/iOS | Executar sessão prolongada com GPS/network em dispositivo real. | Consumo dentro de orçamento de produto. |
| PERF-009 | P1 | GPU e rendering | Animar listas e gráficos grandes em aparelhos fracos. | Frames e UI seguem metas de fluidez. |
| PERF-010 | P1 | Cold start desktop | Iniciar app a frio e quente com perfil limpo. | Tempo e atividade de inicialização monitorados. |
| PERF-011 | P1 | Startup mobile | Medir primeiro frame e tela utilizável em aparelhos suportados. | SLO de inicialização cumprido. |
| PERF-012 | P1 | Crash após horas | Executar soak test 8-24h com eventos reais sintéticos. | Sem crescimento de recursos, deadlock ou crash crítico. |
| PERF-013 | P1 | Cancelamento de job | Cancelar tarefa longa antes e após fase irreversível. | Recursos liberados e estado final correto. |
| PERF-014 | P1 | Fila sob surto | Adicionar rajada de mensagens de teste maior que vazão normal. | Backpressure evita colapso; DLQ operacional. |
| PERF-015 | P1 | Corpo gigante | Enviar payload máximo contratado e logo acima do limite. | Processamento controlado; excesso rejeitado. |
| PERF-016 | P1 | Métrica falsa positiva | Simular perda de telemetria com serviço saudável. | Monitoramento distingue dados ausentes de performance boa. |
