# INF: 12. Servidores, rede, VPS e contêineres

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| INF-01 | P0 | Firewall | Negar entradas não necessárias. |
| INF-02 | P0 | Administração remota | Restringir SSH e acessos administrativos com identidade forte. |
| INF-03 | P0 | Portas internas | Não expor PostgreSQL, Redis, Docker ou painéis de gestão. |
| INF-04 | P0 | Patches | Manter sistemas e componentes suportados e corrigidos. |
| INF-05 | P0 | Contêiner não root | Evitar root e restringir capabilities e recursos. |
| INF-06 | P0 | Segredos em contêiner | Não inserir credenciais na imagem ou no repositório. |
| INF-07 | P1 | Filesystem | Usar montagens mínimas e somente leitura quando possível. |
| INF-08 | P1 | Segmentação | Separar camadas expostas e internas. |
| INF-09 | P1 | Saídas externas | Restringir tráfego de saída de serviços de risco. |
| INF-10 | P0 | Painéis internos | Proteger EasyPanel, consoles e dashboards com MFA e acesso restrito. |
| INF-11 | P1 | Domínio DNS | Restringir conta de domínio e gestão de DNS. |
| INF-12 | P1 | DNSSEC | Aplicar quando compatível com a zona e provedor. |
| INF-13 | P1 | Subdomínios órfãos | Remover apontamentos que permitam takeover. |
| INF-14 | P1 | DDoS | Preparar absorção, mitigação e runbooks. |
| INF-15 | P1 | Bypass da CDN | Proteger IP/hostname direto da origem. |
| INF-16 | P1 | Hardening | Desativar serviços e interfaces desnecessárias. |
| INF-17 | P1 | Limites de processo | Restringir CPU, memória, conexões e execução. |
| INF-18 | P1 | Segregação de funções | Diferenciar privilégios de deploy, operação, backup e root. |
| INF-19 | P2 | Privilégio temporário | Just-in-time access em funções administrativas. |
| INF-20 | P1 | Segurança de e-mail | Habilitar SPF, DKIM e DMARC do domínio. |
