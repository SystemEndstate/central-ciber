# WIN: 25.2. Windows: EXE, MSI e MSIX

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| WIN-01 | P0 | Authenticode | Assinar EXE/MSI/MSIX distribuídos conforme formato. |
| WIN-02 | P0 | MSIX | Validar pacote assinado e integridade quando utilizado. |
| WIN-03 | P1 | SmartScreen | Criar reputação legítima; nunca pedir desativação de proteção. |
| WIN-04 | P0 | DPAPI | Proteger dados locais com APIs criptográficas do Windows. |
| WIN-05 | P0 | NTFS ACL | Restringir acesso a arquivos e diretórios privados. |
| WIN-06 | P0 | DLL Search Order | Evitar busca em diretórios controlados por terceiros. |
| WIN-07 | P0 | UAC | Separar componente elevado do processo normal. |
| WIN-08 | P1 | Registro | Não guardar segredos em claro no registry. |
| WIN-09 | P1 | Windows Services | Utilizar contas de serviço mínimas. |
| WIN-10 | P0 | Named Pipes | Aplicar ACL e validação de cliente. |
| WIN-11 | P0 | localhost | Prevenir chamadas indevidas feitas por navegadores e outros processos. |
| WIN-12 | P1 | Microsoft Defender | Verificar instalador e binários. |
| WIN-13 | P1 | Mitigações nativas | Ativar ASLR, DEP e CFG quando disponíveis. |
| WIN-14 | P1 | Event Log | Registrar eventos com dados mínimos. |
| WIN-15 | P1 | Hibernação | Restaurar sessão e jobs após despertar. |
| WIN-16 | P1 | DPI | Testar escalonamento e monitores de tamanhos diversos. |
| WIN-17 | P1 | Windows Update | Verificar compatibilidade regularmente. |
| WIN-18 | P1 | Instalador temporário | Evitar execução privilegiada com arquivos manipuláveis. |
| WIN-19 | P1 | Usuários locais | Impedir leitura de dados entre contas do Windows. |
| WIN-20 | P0 | Servidor de atualização | Proteger assinatura, metadados e artefatos. |
