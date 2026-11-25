# MOB: 22. Segurança transversal de aplicativos Mobile

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| MOB-01 | P0 | Login seguro | Verificar identidade no servidor em cada operação sensível. |
| MOB-02 | P0 | Autorização API | Controlar usuário, recurso, função e tenant. |
| MOB-03 | P0 | TLS | Proteger conexões e validar certificados. |
| MOB-04 | P0 | Segredos locais | Utilizar Keychain e Keystore conforme o sistema. |
| MOB-05 | P0 | Chaves no binário | Não embutir credenciais privilegiadas em APK/AAB/IPA. |
| MOB-06 | P0 | Sessão móvel | Expiração, renovação e revogação. |
| MOB-07 | P0 | Logout local e remoto | Limpar estado e revogar acesso. |
| MOB-08 | P1 | Biometria | Usar APIs oficiais e controles adicionais em operações críticas. |
| MOB-09 | P0 | Cache offline | Proteger dados locais e controlar retenção. |
| MOB-10 | P0 | Troca de conta | Não exibir ou reenviar dados de usuário anterior. |
| MOB-11 | P0 | Backup do telefone | Evitar backup indevido de tokens e documentos privados. |
| MOB-12 | P1 | Root/jailbreak | Usar sinais de risco com decisão proporcional. |
| MOB-13 | P1 | Integridade de app | Avaliar Play Integrity e App Attest nos pontos de risco. |
| MOB-14 | P0 | Deep links | Validar identidade, caminho, destino e autorização. |
| MOB-15 | P0 | WebView | Isolar conteúdo e bridges com funções nativas. |
| MOB-16 | P0 | Push | Não enviar informações secretas em payloads. |
| MOB-17 | P1 | Captura de tela | Mitigar exposições conforme a plataforma, sem presumir bloqueio total. |
| MOB-18 | P1 | Clipboard | Não copiar ou reter dados secretos sem necessidade. |
| MOB-19 | P0 | Permissões do aparelho | Solicitar mínimo e lidar com revogação. |
| MOB-20 | P1 | Logs locais | Minimizar dados pessoais e nunca armazenar tokens completos. |
| MOB-21 | P0 | Arquivos mobile | Validar formato, tamanho e autorização. |
| MOB-22 | P0 | Sincronização | Resolver conflitos e segregar contas. |
| MOB-23 | P1 | Versões antigas | Bloquear releases com vulnerabilidades críticas. |
| MOB-24 | P1 | Obfuscação | Usar como defesa complementar, não como autorização. |
| MOB-25 | P0 | Operações financeiras | Nunca confiar em valores calculados exclusivamente no app. |
| MOB-26 | P1 | SDKs externos | Auditar permissões e coleta de terceiros. |
| MOB-27 | P1 | Privacidade local | Reter somente dados necessários. |
| MOB-28 | P1 | Suspensão e retorno | Proteger estado quando aplicativo entra em background. |
| MOB-29 | P1 | Atualização assinada | Distribuir binários íntegros. |
| MOB-30 | P0 | Falha segura | Negar operação se autenticação ou autorização falhar. |
