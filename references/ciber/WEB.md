# WEB: 6. Frontend, browser e HTTPS

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| WEB-01 | P0 | TLS atual | Usar TLS 1.2/1.3 conforme política; priorizar TLS 1.3. |
| WEB-02 | P0 | Certificados válidos | Renovar automaticamente e impedir confiança em certificado inválido. |
| WEB-03 | P1 | HSTS | Aplicar depois de confirmar compatibilidade de domínios/subdomínios. |
| WEB-04 | P0 | Proteção contra XSS | Escaping contextual e sanitização de HTML não confiável. |
| WEB-05 | P1 | CSP | Restringir fontes de scripts; usar nonces/hashes quando necessário. |
| WEB-06 | P0 | Segredos no bundle | Não compilar tokens privilegiados e senhas no frontend. |
| WEB-07 | P0 | CORS | Restringir origens; lembrar que CORS não é autorização. |
| WEB-08 | P1 | Frame embedding | Usar frame-ancestors para proteger contra clickjacking. |
| WEB-09 | P1 | Referrer Policy | Evitar propagação de URLs privadas e parâmetros sensíveis. |
| WEB-10 | P1 | MIME sniffing | Aplicar X-Content-Type-Options: nosniff. |
| WEB-11 | P0 | Browser storage | Evitar tokens sensíveis em localStorage se arquitetura melhor estiver disponível. |
| WEB-12 | P0 | Cache privado | Evitar que proxies e CDNs armazenem dados particulares entre usuários. |
| WEB-13 | P1 | Scripts externos | Avaliar provedores, SDKs e dependências frontend. |
| WEB-14 | P1 | Markdown e HTML | Sanitizar saída de renderizadores e conteúdo gerado por IA. |
| WEB-15 | P1 | postMessage | Validar origin, schema e destinatário. |
| WEB-16 | P2 | SRI | Aplicar integridade de sub-recursos externos estáticos quando apropriado. |
