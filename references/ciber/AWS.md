# AWS: 8. Infraestrutura AWS: proteção e operações

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| AWS-01 | P0 | Conta root | MFA forte, credenciais de emergência e uso excepcional. |
| AWS-02 | P0 | IAM mínimo | Permissões menores necessárias para pessoas e aplicações. |
| AWS-03 | P0 | Roles temporárias | Preferir STS e federação a chaves permanentes. |
| AWS-04 | P0 | VPC | Separar segmentos de borda, aplicação e dados. |
| AWS-05 | P0 | Security Groups | Permitir apenas portas e origens exigidas. |
| AWS-06 | P0 | RDS privado | Evitar interface pública do banco. |
| AWS-07 | P0 | TLS no RDS | Criptografar e validar certificado de conexão ao banco. |
| AWS-08 | P0 | Criptografia RDS | Proteger dados, snapshots e réplicas em repouso. |
| AWS-09 | P0 | Segredos RDS | Armazenar no Secrets Manager e controlar rotação/acesso. |
| AWS-10 | P1 | RDS Proxy | Considerar pool seguro e escala em ambientes serverless. |
| AWS-11 | P1 | Multi-AZ | Adequar redundância às metas de disponibilidade. |
| AWS-12 | P0 | PITR | Habilitar recuperação em ponto no tempo quando exigida. |
| AWS-13 | P0 | S3 Block Public Access | Bloquear publicação acidental de buckets privados. |
| AWS-14 | P0 | Bucket policies | Restringir identidade, recurso, caminho e ações. |
| AWS-15 | P0 | CloudTrail | Habilitar trilha de gestão e eventos de dados conforme risco. |
| AWS-16 | P1 | GuardDuty | Monitorar atividades suspeitas em contas e regiões aplicáveis. |
| AWS-17 | P1 | Security Hub | Centralizar achados e conformidade. |
| AWS-18 | P1 | AWS Config | Detectar desvios de configuração. |
| AWS-19 | P0 | AWS WAF | Aplicar regras gerenciadas, limites e proteção por rota. |
| AWS-20 | P1 | Controle de egress | Limitar saídas de serviços que processam conteúdo externo. |
| AWS-21 | P1 | Organizations | Segregar produção, desenvolvimento e segurança por conta quando viável. |
| AWS-22 | P1 | SCP | Impor guardrails organizacionais contra ações perigosas. |
| AWS-23 | P1 | CloudWatch | Alertar sobre erros, abusos, latência e mudanças relevantes. |
| AWS-24 | P0 | CI/CD federado | Implantar via OIDC/roles com credenciais efêmeras. |
| AWS-25 | P0 | DynamoDB IAM | Controlar acesso por principal e chaves de partição quando adequado. |
| AWS-26 | P1 | Custos e abuso | Monitorar gasto inesperado e limitar operações financeiramente custosas. |
