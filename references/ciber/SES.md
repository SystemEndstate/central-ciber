# SES: 4. Sessões, cookies e JWT

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| SES-01 | P0 | Cookie HttpOnly | Bloquear acesso por JavaScript a cookies de sessão quando aplicável. |
| SES-02 | P0 | Cookie Secure | Enviar cookies de sessão apenas por HTTPS. |
| SES-03 | P0 | SameSite | Definir Lax ou Strict de acordo com o fluxo. |
| SES-04 | P1 | Prefixo __Host- | Usar host-only, Secure e Path=/, sem Domain, quando adequado. |
| SES-05 | P0 | Prazo de validade | Definir expiração de tokens e sessões. |
| SES-06 | P0 | Logout efetivo | Revogar sessão e credenciais de renovação relevantes. |
| SES-07 | P0 | Refresh token | Rotacionar e detectar reuso conforme capacidade do provedor. |
| SES-08 | P1 | Ociosidade | Encerrar sessões inativas conforme sensibilidade. |
| SES-09 | P1 | Duração absoluta | Limitar sessões mesmo com atividade contínua. |
| SES-10 | P0 | Session fixation | Trocar identificador após login/elevação de privilégio quando necessário. |
| SES-11 | P0 | Token em URL ou log | Impedir exposição em histórico, query strings, telemetria e mensagens. |
| SES-12 | P0 | CSRF | Validar origem e usar antifalsificação apropriada para sessões baseadas em cookies. |
| SES-13 | P0 | JWT verificado | Não autorizar com JWT apenas decodificado, sem validação criptográfica. |
| SES-14 | P1 | Revogação antecipada | Bloquear credenciais comprometidas e reavaliar permissões críticas. |
| SES-15 | P0 | Cache compartilhado | Impedir armazenamento cruzado de páginas privadas e Set-Cookie. |
| SES-16 | P1 | Reautenticação | Exigir nova prova de identidade para ações críticas. |
