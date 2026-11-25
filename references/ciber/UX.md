# UX: 28. UX segura e prevenção de erros / 29. Offline, sincronização e conflito

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| UX-01 | P0 | Exclusão segura | Confirmar exatamente o recurso e o efeito destrutivo. |
| UX-02 | P0 | Revisão financeira | Exibir destinatário, valor e custos antes de efetivar. |
| UX-03 | P0 | Sucesso verdadeiro | Somente confirmar após commit/resposta válida. |
| UX-04 | P0 | Duplo clique | Evitar efeitos repetidos no servidor, além do bloqueio visual. |
| UX-05 | P1 | Estado de loading | Indicar progresso e lidar com espera prolongada. |
| UX-06 | P1 | Erros úteis | Orientar sem divulgar stack trace ou dados privados. |
| UX-07 | P1 | Recuperação amigável | Permitir nova tentativa segura em operações reversíveis. |
| UX-08 | P0 | Formulário resiliente | Preservar rascunho não sensível sem duplicar envio. |
| UX-09 | P1 | Acessibilidade | Suportar leitor de tela, teclado, contraste e toque. |
| UX-10 | P1 | Contraste | Garantir leitura em diferentes ambientes. |
| UX-11 | P1 | Dark/light mode | Manter controles visíveis e estados legíveis. |
| UX-12 | P1 | Fonte ampliada | Ajustar layout sem esconder ações. |
| UX-13 | P1 | Responsividade | Testar monitores, orientação e redimensionamento. |
| UX-14 | P1 | Navegação pós-logout | Impedir acesso a conteúdo privado via histórico/cache. |
| UX-15 | P0 | Identidade ativa | Indicar claramente usuário e tenant ativos. |
| UX-16 | P1 | Permissões de dispositivo | Explicar necessidade e tratar recusa. |
| UX-17 | P1 | Biometria falhou | Oferecer recuperação segura quando permitida. |
| UX-18 | P1 | Sessão expirada | Solicitar login mantendo somente rascunhos autorizados. |
| UX-19 | P0 | Dados confidenciais | Mascarar campos e evitar apresentação desnecessária. |
| UX-20 | P1 | Estado da conexão | Diferenciar offline, timeout e falha do servidor. |
| UX-21 | P1 | Dados antigos | Exibir quando informação não foi sincronizada. |
| UX-22 | P1 | Operações pendentes | Mostrar fila, estado e conflitos. |
| UX-23 | P0 | Permissão refletida | Interface não simula autorização inexistente. |
| UX-24 | P1 | Desfazer | Oferecer reversão quando tecnicamente segura. |
| UX-25 | P1 | Releases | Explicar atualizações obrigatórias e mudanças críticas. |
| UX-26 | P1 | Notificações privadas | Não mostrar conteúdo sensível indevidamente. |
| UX-27 | P1 | Recuperação de acesso | Oferecer fluxo claro e resistente a engenharia social. |
| UX-28 | P1 | Localização | Tratar moeda, número, idioma e fuso corretamente. |
| UX-29 | P1 | Tela vazia | Prevenir white screen sem feedback. |
| UX-30 | P1 | Consistência de transação REGRA DE NEGÓCIO Nenhuma operação foi Servidor ainda não confirmou; Estado validado no backend; Consultar estado real antes Exibir motivo seguro e orientação e conflito gerar dados duplicados, corrupção CONTROLE / RISCO | Manter significado e estado dos controles nas plataformas. iniciada. não mostrar sucesso. identificador de operação registrado. de repetir para evitar duplicidade. de recuperação. ou confusão de identidade. EXIGÊNCIA / EVIDÊNCIA |
