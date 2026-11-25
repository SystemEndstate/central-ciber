# OFF: 18. Offline, reconexão e sincronização

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| OFF-001 | P0 | Fila perdida | Criar cinco operações offline e matar processo antes de sincronizar. | Fila persiste e retoma sem perder intenções válidas. |
| OFF-002 | P0 | Duplo replay | Reconectar com timeout após servidor já confirmar operação. | Idempotência impede aplicação duplicada. |
| OFF-003 | P0 | Conflito mesma linha | Editar registro em dois dispositivos offline. | Conflito detectado e resolvido conforme regra documentada. |
| OFF-004 | P0 | Mudança de tenant offline | Enfileirar A, entrar B e reconectar. | Eventos de A não são executados como B. |
| OFF-005 | P0 | Token offline vencido | Criar operações antes de expiração e retornar após dias. | Autenticação renovada e autorização atual reavaliada. |
| OFF-006 | P0 | Registro excluído remotamente | Editar offline item já excluído em outro dispositivo. | Tombstone/conflito evita ressuscitação indevida. |
| OFF-007 | P1 | Horário de dispositivo errado | Avançar/recuar relógio local durante edição offline. | Ordenação/versão não depende cegamente de horário controlável. |
| OFF-008 | P1 | Foto parcialmente enviada | Interromper upload multipart no meio. | Retoma ou reinicia sem arquivo corrupto público. |
| OFF-009 | P1 | Fila sem limite | Gerar milhares de ações offline sintéticas. | Limites de armazenamento e UX preservados. |
| OFF-010 | P0 | Falha após upload | Servidor recebe arquivo, mas banco não recebe referência. | Processo reconcilia órfãos e informa estado correto. |
| OFF-011 | P1 | Sync em background | Bloquear app/desktop durante sincronização. | Tarefas persistem conforme garantias do SO; sem falsa confirmação. |
| OFF-012 | P0 | Dados locais corrompidos | Modificar cópia descartável do cache local. | Detecção e reconstrução sem propagação de corrupção remota. |
| OFF-013 | P0 | Reordenação de fila | Alterar ordem dos eventos de edição e exclusão. | Regras de dependência preservam resultado final. |
| OFF-014 | P1 | Rede flapping | Alternar online/offline repetidamente a cada poucos segundos. | Sem tempestade de requisições ou duplicação. |
| OFF-015 | P0 | Versão de schema offline | Voltar online com cliente cuja base local é antiga. | Migração e sync controlados ou atualização exigida. |
| OFF-016 | P0 | Sessão encerrada remotamente | Fazer logout remoto com outro dispositivo ainda offline. | Conteúdo e operações locais respeitam política de bloqueio e retenção. |
