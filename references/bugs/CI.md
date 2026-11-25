# CI: 26. Automação de QA, CI/CD e portões de release

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| CI-001 | P1 | Teste flaky | Executar suíte repetidas vezes com seeds anotados. | Flakiness rastreada; não mascarada por retry indefinido. |
| CI-002 | P1 | Fixture compartilhada | Executar testes paralelos que manipulam mesmo usuário. | Dados isolados por teste; resultado determinístico. |
| CI-003 | P1 | Mock excessivo | Comparar testes mockados com ambiente de integração real. | Contratos e efeitos persistidos também validados. |
| CI-004 | P0 | Teste só happy path | Incluir entrada inválida, negação e falha de dependência. | Cenários negativos cobertos para ações críticas. |
| CI-005 | P0 | Schema alterado | Aplicar migration em build e rodar testes automáticos. | Falha de RLS, grant ou constraint bloqueia pipeline. |
| CI-006 | P1 | Dependência vulnerável | Introduzir dependência de teste com CVE conhecido controlado. | SCA detecta e aplica política de risco. |
| CI-007 | P0 | Segredo no commit | Adicionar token sintético em branch descartável. | Secret scanning bloqueia ou sinaliza imediatamente. |
| CI-008 | P1 | Teste móvel só emulador | Executar suíte crítica também em dispositivos físicos. | Falhas exclusivas de hardware detectáveis. |
| CI-009 | P0 | Windows só debug | Executar smoke no EXE assinado e instalador final. | Build de produção validado, não apenas dev server. |
| CI-010 | P1 | Release com versão errada | Publicar build com versão incompatível no ambiente de teste. | Versionamento e artefatos vinculados ao commit correto. |
| CI-011 | P1 | Feature flag revertida | Ligar/desligar flag em runtime durante fluxo. | Ambos estados são testados e reversão segura. |
| CI-012 | P0 | Migration irreversível | Avaliar publicação com downgrade do serviço. | Estratégia expand/contract ou recuperação validada. |
| CI-013 | P0 | Teste de backup esquecido | Validar restore trimestral em ambiente isolado. | Evidência de integridade e RTO/RPO documentada. |
| CI-014 | P1 | Aprovação sem owner | Tentar liberar alteração crítica sem responsável designado. | Pipeline exige aprovação definida. |
| CI-015 | P1 | Smoke pós-deploy | Injetar erro crítico em ambiente de homologação. | Canary/monitoramento detecta e bloqueia expansão. |
| CI-016 | P0 | Pentest sem autorização | Tentar iniciar varredura fora do escopo autorizado. | Procedimento exige aprovação, limites de carga e alvo permitido. |
