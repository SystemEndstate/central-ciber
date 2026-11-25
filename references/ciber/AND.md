# AND: 23. Android: plataforma e vulnerabilidades

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| AND-01 | P0 | Manifest | Auditar permissões, serviços e componentes declarados. |
| AND-02 | P0 | android:exported | Exportar apenas os componentes que precisam ser públicos. |
| AND-03 | P0 | Content Providers | Restringir leitura e escrita de dados. |
| AND-04 | P0 | Intents externas | Validar entradas e origem quando relevante. |
| AND-05 | P0 | PendingIntent | Configurar mutabilidade e alvo de forma segura. |
| AND-06 | P0 | App Links | Associar e verificar domínio e aplicativo. |
| AND-07 | P0 | Deep Link Hijack | Não expor credenciais em esquemas não verificados. |
| AND-08 | P0 | WebView navegável | Bloquear esquemas e domínios não permitidos. |
| AND-09 | P0 | JavaScriptInterface | Não oferecer funções nativas a conteúdo remoto não confiável. |
| AND-10 | P0 | Acesso a arquivos no WebView | Desativar capacidades desnecessárias e acessos cruzados. |
| AND-11 | P0 | Network Security Config | Evitar cleartext e configurar confiança TLS. |
| AND-12 | P0 | Android Keystore | Proteger chaves e segredos por recursos do sistema. |
| AND-13 | P1 | StrongBox e TEE | Usar proteção em hardware quando disponível. |
| AND-14 | P0 | Backup rules | Excluir credenciais e dados confidenciais quando apropriado. |
| AND-15 | P0 | Release sem debug | Desativar debug e componentes de teste inseguros. |
| AND-16 | P1 | R8 | Reduzir/obfuscar como defesa adicional. |
| AND-17 | P1 | Play Integrity | Validar provas no backend e tratar falsos positivos. |
| AND-18 | P1 | Assinatura do app | Proteger chaves e o fluxo de publicação. |
| AND-19 | P1 | APK alternativo | Controlar distribuição fora da Play Store se suportada. |
| AND-20 | P1 | FLAG_SECURE | Avaliar proteção de telas sensíveis. |
| AND-21 | P1 | Tapjacking | Mitigar abuso por sobreposição em ações críticas. |
| AND-22 | P1 | Acessibilidade | Considerar ameaças sem bloquear acessibilidade legítima. |
| AND-23 | P1 | Notificações | Limitar informações visíveis na tela bloqueada. |
| AND-24 | P0 | Room/SQLite | Proteger dados e testar migrações. |
| AND-25 | P1 | WorkManager | Tarefas resilientes e idempotentes. |
| AND-26 | P1 | Foreground services | Respeitar restrições de execução e bateria. |
| AND-27 | P1 | ANR | Não bloquear thread de UI. |
| AND-28 | P1 | Memory leaks | Detectar referências retidas e crescimento de memória. |
| AND-29 | P1 | Fragmentação | Testar fabricantes, versões e dimensões. |
| AND-30 | P0 | Troca de conta | Limpar caches e jobs vinculados à identidade anterior. |
| AND-31 | P1 | Permissão revogada | Tratar cancelamento/negação em tempo de execução. |
| AND-32 | P1 | Reinstalação | Tratar restauração e chaves locais incompatíveis. |
| AND-33 | P1 | Analytics e SDKs | Auditar dados coletados e permissões. |
| AND-34 | P1 | JNI/NDK | Revisar erros de memória e bibliotecas nativas. |
| AND-35 | P1 | Suporte do SO | Definir versões mínimas ainda seguras. |
