# DB: 10. Bancos de dados: controles universais

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| DB-01 | P0 | Conta mínima | Aplicação não usa superusuário para consultas comuns. |
| DB-02 | P0 | Rede privada | Restringir acesso direto e administrativo. |
| DB-03 | P0 | Conexão TLS | Proteger tráfego e conferir certificados. |
| DB-04 | P0 | Dados em repouso | Criptografar volumes, snapshots e backups. |
| DB-05 | P0 | Ambientes separados | Não compartilhar banco de produção com testes. |
| DB-06 | P0 | Isolamento de tenants | Verificar propriedade dos registros e vínculos. |
| DB-07 | P0 | Constraints | Impor integridade com UNIQUE, CHECK, FK e demais restrições. |
| DB-08 | P0 | Transações | Evitar gravação parcial em operações críticas. |
| DB-09 | P1 | Concorrência | Aplicar locks, versionamento ou mutações atômicas. |
| DB-10 | P1 | Consultas limitadas | Evitar consultas que saturam recursos e conexões. |
| DB-11 | P0 | Cópias automáticas | Backups protegidos, atualizados e verificáveis. |
| DB-12 | P0 | Isolamento do backup | Impedir exclusão simultânea de produção e todas as cópias. |
| DB-13 | P1 | Auditoria SQL | Registrar operações privilegiadas e alterações críticas. |
| DB-14 | P0 | Campos confidenciais | Aplicar criptografia adicional conforme sensibilidade. |
| DB-15 | P0 | Dados de teste | Não copiar dados reais sem anonimização e controles adequados. |
| DB-16 | P1 | Retenção | Eliminar dados e cópias conforme obrigações. |
| DB-17 | P0 | Migrações seguras | Versionar, ensaiar e planejar recuperação. |
| DB-18 | P1 | Réplicas | Manter criptografia e permissões equivalentes. |
| DB-19 | P1 | Exclusão de tenant | Remover dados, arquivos e referências conforme política. |
| DB-20 | P1 | Monitoramento DB | Alertar sobre conexões, consultas e acessos anormais. |
