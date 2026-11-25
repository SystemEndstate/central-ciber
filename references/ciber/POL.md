# POL: 33. Política de publicação e manutenção

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| POL-01 | P0 | Exploração crítica | Bloquear lançamento até mitigação efetiva. |
| POL-02 | P0 | Falha entre tenants | Bloquear publicação. |
| POL-03 | P0 | Dupla cobrança | Bloquear publicação. |
| POL-04 | P0 | Perda irreversível de dados | Bloquear publicação. |
| POL-05 | P1 | Crash no fluxo principal | Corrigir antes de liberação ampla. |
| POL-06 | P2 | Bug puramente visual | Priorizar conforme impacto de uso e acessibilidade. |
| POL-07 | P0 | Atualização sem assinatura | Bloquear distribuição. |
| POL-08 | P0 | Backup sem teste | Não considerar plano de recuperação validado. |
| POL-09 | P0 | Testes automáticos falham | Bloquear deploy automático até análise formal. |
| POL-10 | P0 | Incidente em produção | Decidir contenção, rollback e comunicação. |
| POL-11 | P1 | Indicador de crash | Acompanhar usuários e sessões sem crashes. |
| POL-12 | P1 | Indicador de ANR/hangs | Acompanhar desempenho por versão e plataforma. |
| POL-13 | P1 | Vulnerabilidades abertas | Registrar severidade, idade, responsável e mitigação. |
| POL-14 | P1 | Transações falhas | Monitorar erro, reconciliação e duplicidade. |
| POL-15 | P1 | Sincronização | Monitorar sucesso e conflitos offline. |
| POL-16 | P1 | Upgrade | Medir porcentagem de atualizações bem-sucedidas. |
| POL-17 | P1 | Detecção e resolução | Medir tempo de detectar e corrigir incidentes. |
| POL-18 | P1 | RPO/RTO | Verificar metas de continuidade após testes de restauração. |
| POL-19 | P1 | Regressão | Acompanhar problemas introduzidos por releases. |
| POL-20 | P1 | Cobertura funcional | Medir testes para invariantes e regras críticas. |
