# LIN: 25.3. macOS e Linux: assinatura, isolamento e permissões

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| LIN-01 | P0 | Permissões POSIX | Definir usuário, grupo e modo corretamente. |
| LIN-02 | P0 | Execução sem root | Evitar sudo para funções comuns. |
| LIN-03 | P1 | AppArmor/SELinux | Adotar confinamento quando viável. |
| LIN-04 | P1 | Flatpak | Restringir sandbox e permissões de portals. |
| LIN-05 | P1 | Pacotes Linux | Verificar origem e integridade de AppImage, deb ou rpm. |
| LIN-06 | P1 | systemd hardening | Aplicar restrições e contas mínimas. |
| LIN-07 | P0 | Unix sockets | Proteger por permissões e identidade de cliente. |
| LIN-08 | P1 | Bibliotecas dinâmicas | Evitar diretórios de carregamento não confiáveis. |
| LIN-09 | P1 | Variáveis de ambiente | Nunca confiar em PATH e outros valores controlados pelo usuário. |
| LIN-10 | P1 | Distribuições | Testar versões, bibliotecas e drivers diferentes. |
