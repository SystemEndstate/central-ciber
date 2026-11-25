# ID: 3. Identidade, login e usuários

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| ID-01 | P0 | Provedor de identidade | Preferir Cognito ou Supabase Auth a autenticação improvisada. |
| ID-02 | P0 | Verificação de tokens | Validar assinatura, emissor, audiência, expiração e claims relevantes. |
| ID-03 | P0 | Identidade do usuário | Nunca confiar no ID enviado pelo dispositivo sem autenticação correspondente. |
| ID-04 | P0 | Armazenamento de senhas | Se gerenciado diretamente, usar Argon2id e parâmetros adequados; nunca texto puro. |
| ID-05 | P0 | Força bruta | Limitar tentativas, aplicar atrasos e identificar ataques distribuídos. |
| ID-06 | P0 | MFA dos operadores | Exigir MFA de administradores e de quem acessa produção. |
| ID-07 | P1 | MFA de clientes | Oferecer MFA e exigir proteção adicional em operações de risco. |
| ID-08 | P1 | Passkeys | Priorizar WebAuthn/FIDO2 quando viável para resistência a phishing. |
| ID-09 | P0 | Recuperação de senha | Tokens únicos e curtos, uso único e expiração no servidor. |
| ID-10 | P0 | Alteração de e-mail | Solicitar reautenticação ou confirmação segura. |
| ID-11 | P1 | Enumeração de usuários | Evitar respostas que revelem a existência de contas. |
| ID-12 | P0 | Escalada de privilégios | Proibir autoatribuição de funções como owner e admin. |
| ID-13 | P0 | Conta suspensa | Impedir operações depois da desativação, considerando latência de revogação. |
| ID-14 | P1 | Lista de dispositivos | Permitir consultar e encerrar sessões ativas. |
| ID-15 | P1 | Anomalias de acesso | Detectar alterações suspeitas de dispositivo, padrão e localização. |
| ID-16 | P1 | OAuth/OIDC seguro | Verificar state, nonce quando aplicável, PKCE e redirect URI. |
