# OFF: 29. Offline, sincronização e conflito

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| OFF-01 | P0 | Cache local | Proteger dados sensíveis e limitar retenção. |
| OFF-02 | P0 | Fila persistente | Preservar operações pendentes após crash. |
| OFF-03 | P0 | Idempotência offline | Não repetir transação crítica ao reconectar. |
| OFF-04 | P0 | Conflitos | Detectar múltiplas edições e definir estratégia de resolução. |
| OFF-05 | P0 | Token expirado | Não sincronizar dados privados sem autorização atual. |
| OFF-06 | P0 | Troca de usuário | Associar fila à identidade correta. |
| OFF-07 | P1 | Reconexão gradual | Usar backoff, jitter e limites. |
| OFF-08 | P1 | Dado obsoleto | Exibir estado de desatualização. |
| OFF-09 | P1 | Upload parcial | Retomar ou recomeçar com integridade verificada. |
| OFF-10 | P0 | Financeiro offline | Nunca considerar movimento confirmado só pelo estado local. |
| OFF-11 | P1 | Disco cheio | Tratar espaço insuficiente sem corromper dados. |
| OFF-12 | P1 | Upgrade offline | Manter compatibilidade e testes de migração. |
| OFF-13 | P1 | Horário do aparelho | Não confiar nele para autorização e contabilidade. |
| OFF-14 | P0 | Exclusões | Não ressuscitar registros removidos durante sync. |
| OFF-15 | P1 | Recuperação do cache | Recriar estado local após corrupção. |
| OFF-16 | P1 | Status das operações | Separar pendente, confirmado, rejeitado e desconhecido. |
