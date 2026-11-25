# QA: 30. Tipos de testes: qualidade, AppSec e resiliência

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| QA-01 | P0 | Unitários | Regras e funções de negócio testadas com JUnit, XCTest, Jest, Vitest ou equivalentes. |
| QA-02 | P0 | Integração | Validar banco, APIs, fila, storage e terceiros. |
| QA-03 | P0 | End-to-end | Validar fluxo real com Playwright, Maestro, Espresso e XCUITest. |
| QA-04 | P1 | Contrato API | Conferir compatibilidade entre cliente e servidor. |
| QA-05 | P0 | Regressão | Impedir que correção quebre fluxos existentes. |
| QA-06 | P0 | Autorização | Testar acesso positivo e negativo por tenant/role. |
| QA-07 | P0 | SAST | Analisar vulnerabilidades no código-fonte. |
| QA-08 | P1 | DAST | Testar aplicação em execução em ambiente controlado. |
| QA-09 | P1 | Mobile security testing | Executar verificações alinhadas ao MASTG; revisar falsos positivos. |
| QA-10 | P1 | Fuzzing | Enviar entradas malformadas e inesperadas a parsers. |
| QA-11 | P1 | Property-based testing | Verificar invariantes com muitos casos gerados. |
| QA-12 | P1 | Performance | Medir latência, CPU, energia e memória. |
| QA-13 | P1 | Carga e stress | Validar degradação segura em concorrência elevada. |
| QA-14 | P1 | Soak testing | Detectar memory leaks após execução prolongada. |
| QA-15 | P1 | Failure testing | Simular queda de rede, fila, serviço e processo. |
| QA-16 | P0 | Upgrade e rollback | Testar migração, interrupção e retorno. |
| QA-17 | P0 | Restauração | Recuperar backup em ambiente isolado. |
| QA-18 | P1 | Acessibilidade | Testar TalkBack, VoiceOver, teclado e Narrator. |
| QA-19 | P1 | Regressão visual | Comparar layouts, fontes e responsividade. |
| QA-20 | P1 | Pentest independente | Executar avaliação autorizada por especialista. |
