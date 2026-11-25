# CORE: 1. Controles fundamentais de lançamento

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| CORE-01 | P0 | HTTPS e TLS | TLS moderno em todos os acessos; redirecionamento HTTP e HSTS após validação. |
| CORE-02 | P0 | Autenticação segura | Identidade validada no backend; conferir autenticidade de sessão ou token. |
| CORE-03 | P0 | Autorização por recurso | Autorizar cada leitura, escrita e exclusão; nunca confiar na interface. |
| CORE-04 | P0 | Isolamento multi-tenant | Impedir que clientes distintos compartilhem recursos sem autorização expressa. |
| CORE-05 | P0 | Proteção de sessão | Expiração, revogação, logout real e proteção contra reutilização. |
| CORE-06 | P0 | MFA administrativo | Segundo fator resistente a phishing para contas privilegiadas. |
| CORE-07 | P0 | Banco não exposto | Restringir rede e portas administrativas; evitar acesso direto público. |
| CORE-08 | P0 | RLS e grants no Supabase | Aplicar políticas por usuário/tenant e privilégios SQL mínimos. |
| CORE-09 | P0 | Gestão de segredos | Nunca expor chaves privadas no frontend, repositório ou logs. |
| CORE-10 | P0 | Entradas confiáveis | Validar no backend e parametrizar consultas; prevenir injeções. |
| CORE-11 | P0 | Rate limiting | Limitar abuso por rota, identidade e operação. |
| CORE-12 | P1 | WAF e anti-DDoS | Defender a borda e impedir bypass da origem quando aplicável. |
| CORE-13 | P0 | Segurança de arquivos | Validar upload, manter storage privado e autorizar download. |
| CORE-14 | P0 | Criptografia | Proteger trânsito, repouso e campos de maior risco. |
| CORE-15 | P0 | Auditoria | Registrar ações administrativas, autenticação e transações críticas. |
| CORE-16 | P0 | Backups restauráveis | Backup protegido e teste de restauração documentado. |
| CORE-17 | P1 | Dependências | Analisar vulnerabilidades de bibliotecas e imagens. |
| CORE-18 | P0 | CI/CD seguro | Proteger branch, revisão e implantação com credenciais temporárias. |
| CORE-19 | P1 | Monitoramento | Detectar abuso, falhas, custos e atividade suspeita com resposta definida. |
| CORE-20 | P0 | Teste de autorização | Demonstrar isolamento entre usuários e clientes e funções privilegiadas. |
