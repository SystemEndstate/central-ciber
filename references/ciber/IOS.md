# IOS: 24. iOS e iPadOS: plataforma e confiabilidade

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| IOS-01 | P0 | Keychain | Guardar credenciais usando accessibility classes adequadas. |
| IOS-02 | P1 | Secure Enclave | Proteger chaves críticas em hardware quando apropriado. |
| IOS-03 | P0 | Data Protection | Definir acesso a arquivos conforme bloqueio e sensibilidade. |
| IOS-04 | P0 | ATS | Preservar App Transport Security e limitar exceções. |
| IOS-05 | P0 | TLS confiável | Verificar certificados e confiança dos servidores. |
| IOS-06 | P0 | Universal Links | Validar associação de domínio e parâmetros. |
| IOS-07 | P0 | URL Schemes | Não aceitar comandos privilegiados de esquemas inseguros. |
| IOS-08 | P0 | WKWebView | Restringir navegação e interfaces nativas. |
| IOS-09 | P1 | Message handlers | Validar conteúdo e origem antes de executar ações. |
| IOS-10 | P0 | App Attest | Verificar atestação no backend nas funções de alto risco. |
| IOS-11 | P1 | DeviceCheck | Utilizar sinais antifraude complementares. |
| IOS-12 | P1 | Face ID/Touch ID | Utilizar LocalAuthentication com fallback seguro. |
| IOS-13 | P0 | Multitarefa | Proteger prévias no alternador de apps. |
| IOS-14 | P1 | Captura de tela | Mitigar exposição conforme APIs, sem prometer bloqueio universal. |
| IOS-15 | P0 | Push confidencial | Evitar segredos nas notificações. |
| IOS-16 | P1 | Permissões | Solicitar câmera, fotos e localização somente quando necessárias. |
| IOS-17 | P1 | Privacy Manifest | Declarar coleta e APIs exigidas quando aplicável. |
| IOS-18 | P1 | ATT | Cumprir regras de consentimento relacionadas a rastreamento. |
| IOS-19 | P1 | App Groups | Isolar dados compartilhados entre extensões. |
| IOS-20 | P0 | Entitlements | Ativar apenas capacidades necessárias. |
| IOS-21 | P0 | iCloud backup | Controlar dados locais incluídos em backup. |
| IOS-22 | P1 | Background Tasks | Tratar cancelamento e suspensão pelo sistema. |
| IOS-23 | P1 | App lifecycle | Recuperar estado após interrupção e fechamento. |
| IOS-24 | P1 | Jetsam | Investigar encerramento por pressão de memória. |
| IOS-25 | P1 | Thread principal | Manter interface responsiva. |
| IOS-26 | P1 | Swift concurrency | Mitigar data races e cancelamentos incorretos. |
| IOS-27 | P0 | Core Data/SQLite/SwiftData | Proteger dados e migrar sem corrupção. |
| IOS-28 | P1 | Crash reports | Simbolicar e analisar falhas por versão. |
| IOS-29 | P1 | TestFlight | Validar em dispositivos reais antes da loja. |
| IOS-30 | P1 | Distribuição | Proteger certificados e perfis do App Store Connect. |
| IOS-31 | P1 | Extensões | Proteger widgets e Share Extensions. |
| IOS-32 | P0 | Troca de conta | Limpar dados específicos do usuário antigo. |
| IOS-33 | P1 | Jailbreak | Utilizar indicador de risco complementar. |
| IOS-34 | P1 | Migrações locais | Evitar quebra em atualizações de esquema. |
| IOS-35 | P1 | Compatibilidade iOS | Testar iPhone, iPad e versões suportadas. |
