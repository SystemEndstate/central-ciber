# MON: 14. Logs, alertas e resposta a incidentes

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| MON-01 | P0 | Eventos de login | Registrar êxito, falha, MFA e tentativas suspeitas. |
| MON-02 | P0 | Acessos negados | Monitorar falhas anormais de autorização. |
| MON-03 | P0 | Auditoria administrativa | Registrar permissões, papéis e configurações. |
| MON-04 | P0 | Integridade do log | Proteger contra alteração e exclusão indevidas. |
| MON-05 | P0 | Minimização no log | Nunca armazenar segredos e tokens completos. |
| MON-06 | P1 | Logs estruturados | Incluir correlação, tempo, recurso e tenant quando correto. |
| MON-07 | P1 | Alerta de abuso de login | Detectar padrões de força bruta e credential stuffing. |
| MON-08 | P1 | Mudanças sensíveis | Alertar alterações de acesso e infraestrutura. |
| MON-09 | P1 | Exfiltração | Detectar exportações e leituras em volume anormal. |
| MON-10 | P1 | Métricas API | Observar latência, tráfego e erros. |
| MON-11 | P1 | Integrações | Detectar falhas de webhooks, filas e serviços de terceiros. |
| MON-12 | P1 | Uso financeiro | Alertar picos de cloud, IA e pagamentos. |
| MON-13 | P0 | Plano de incidentes | Documentar contenção, análise, recuperação e comunicação. |
| MON-14 | P0 | Revogação emergencial | Rotacionar chaves, bloquear acesso e interromper recursos. |
| MON-15 | P1 | Evidências | Preservar eventos para análise técnica sem criar novos vazamentos. |
| MON-16 | P1 | Exercícios | Simular sequestro de sessão, ransomware e chave comprometida. |
| MON-17 | P1 | Responsáveis | Associar alertas a pessoas e decisões. |
| MON-18 | P1 | Retenção de logs | Definir prazo e confidencialidade. |
| MON-19 | P1 | Cobertura | Escalonar incidentes críticos fora do horário comercial, se exigido. |
| MON-20 | P1 | Pós-morte técnico | Documentar causa raiz e testar correções. |
