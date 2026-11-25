# TEC: 26. Riscos por framework e runtime

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| TEC-01 | P0 | React Native | Proteger bridges, deep links, tokens, Secure Storage e SDKs; monitorar renderização, estado e atualizações nativas. |
| TEC-02 | P0 | Expo | Revisar SecureStore, permissões, builds e OTA; compatibilizar JavaScript com módulos nativos. |
| TEC-03 | P0 | Flutter | Auditar plugins e Method Channels, armazenamento local; testar widgets, isolates e memória. |
| TEC-04 | P0 | Kotlin Android | Manifest, intents, WebView, Keystore e lifecycle; testar coroutines, ANR e migração Room. |
| TEC-05 | P0 | Swift/SwiftUI | Keychain, ATS, App Attest e entitlements; testar concorrência e ciclo de vida. |
| TEC-06 | P0 | Electron | Context isolation, sandbox, preload, IPC e NodeIntegration; avaliar vazamentos e auto-update. |
| TEC-07 | P0 | Tauri 2 | Capabilities, plugins Rust e atualizações assinadas; validar comandos e argumentos. |
| TEC-08 | P0 | .NET/WPF/WinUI | DPAPI, registry, permissões, serviços e assinatura; testar UI thread e Windows. |
| TEC-09 | P0 | Qt/C++ | Tratar segurança de memória e DLLs; testar concorrência e crashes nativos. |
| TEC-10 | P1 | Rust Desktop | Revisar FFI, comandos e unsafe; detectar deadlock e erros de lógica. |
| TEC-11 | P0 | Capacitor/Ionic | Controlar plugins, WebView, permissões e mensagens entre web e sistema. |
| TEC-12 | P1 | PWA | Revisar Service Worker, cache, origem, sessão e estado offline. |
