# LAB: 30.2. Cenários físicos e de plataforma

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| LAB-01 | P0 | Android sem internet | Cadastro interrompido não gera perda ou duplicidade. |
| LAB-02 | P1 | Android sem câmera | Permissão negada não causa crash. |
| LAB-03 | P1 | Android processo encerrado | Estado retorna de maneira segura. |
| LAB-04 | P1 | Android troca de rede | Reconexão sem envio duplicado. |
| LAB-05 | P1 | Android baixo desempenho | Sem ANR persistente nem travamento principal. |
| LAB-06 | P1 | Android gira tela | Rascunho e operação conservam integridade. |
| LAB-07 | P0 | Android deep link hostil | Nenhuma função privilegiada por parâmetro. |
| LAB-08 | P1 | iOS sem Face ID | Fluxo alternativo apropriado. |
| LAB-09 | P0 | iOS suspenso durante envio | Retomada e estado consistentes. |
| LAB-10 | P1 | iOS sob pressão de memória | Sem corrupção após encerramento. |
| LAB-11 | P1 | iOS reinstalado | Credenciais e caches tratados conforme política. |
| LAB-12 | P1 | iOS bloqueado | Classes de proteção e background corretos. |
| LAB-13 | P0 | iOS Universal Link inválido | Operação privilegiada não é executada. |
| LAB-14 | P1 | Windows sem admin | Aplicativo opera sem elevação indevida. |
| LAB-15 | P0 | Windows upgrade interrompido | Release anterior recuperada. |
| LAB-16 | P1 | Windows antivírus restringe | Falha controlada e diagnosticável. |
| LAB-17 | P1 | Windows app duplo | Não corrompe dados locais. |
| LAB-18 | P1 | Windows arquivo config inválido | Recuperação sem revelar segredos. |
| LAB-19 | P0 | macOS assinatura inválida | Distribuição não burla Gatekeeper. |
| LAB-20 | P1 | macOS permissão revogada | Funcionalidade falha com segurança. |
| LAB-21 | P1 | Linux sem permissão | Nenhuma escrita parcial indevida. |
| LAB-22 | P1 | Linux biblioteca ausente | Erro identificável e fluxo seguro. |
| LAB-23 | P0 | Logout A/login B | Nenhum dado local/cached de A é exposto a B. |
| LAB-24 | P0 | Pagamento API indisponível | Nenhuma cobrança duplicada ou falso sucesso. |
| LAB-25 | P0 | Banco fora do ar | Falha segura, sem confirmação falsa. |
| LAB-26 | P1 | Contrato API alterado | Clientes oficialmente suportados continuam funcionais. |
