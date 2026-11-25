# UX: 03. UX, acessibilidade e percepção de estado

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| UX-001 | P0 | Sucesso falso | Simular timeout do servidor após clicar em confirmar. | UI não afirma sucesso sem comprovante válido da operação. |
| UX-002 | P0 | Exclusão equivocada | Selecionar um item, alterar filtro e acionar excluir. | Confirmação e backend apontam o item certo. |
| UX-003 | P1 | Alerta sem solução | Provocar 400/403/409/500 e avaliar mensagem e ação possível. | Mensagem útil, segura e recuperável quando aplicável. |
| UX-004 | P1 | Botão sem estado | Forçar latência em ações importantes. | Há feedback pendente, prevenção de duplicidade e timeout. |
| UX-005 | P1 | Foco perdido | Abrir/fechar diálogo usando teclado e leitor de tela. | Foco permanece previsível e acionável. |
| UX-006 | P1 | Texto truncado | Testar zoom, tradução longa e fonte ampliada. | Informação crítica não desaparece nem muda significado. |
| UX-007 | P1 | Erro só por cor | Testar daltonismo e modos de contraste. | Estados têm texto/ícone além da cor. |
| UX-008 | P1 | Leitor de tela não anuncia | Completar formulário com erro sem usar mouse. | Rótulos e mensagens associadas e anunciadas. |
| UX-009 | P1 | Teclado preso em modal | Usar Tab, Shift+Tab e Escape. | Navegação de foco correta; sem armadilha indevida. |
| UX-010 | P0 | Inconsistência monetária | Alternar localidade e exibir montantes de teste. | Separadores, moedas e arredondamento corretos. |
| UX-011 | P0 | Conta ativa ambígua | Trocar tenant e testar ação destrutiva. | Organização atual clara antes da ação. |
| UX-012 | P1 | Offline disfarçado | Desativar rede com dados em cache visíveis. | UI sinaliza offline, idade dos dados e ações pendentes. |
| UX-013 | P1 | Estado vazio incorreto | Aplicar filtro sem resultados vs erro de API. | Diferencia vazio legítimo, carregamento e falha. |
| UX-014 | P0 | Confirmação insuficiente | Executar transferência em conta de teste. | Resumo mostra destinatário, valor e estado antes do envio. |
| UX-015 | P1 | Interrupção no fluxo | Trocar de janela ou bloquear aparelho durante formulário. | Retomada consistente sem perda inesperada. |
| UX-016 | P1 | Desfazer enganoso | Acionar desfazer após operação irreversível. | UI não promete reversão impossível; explica limites. |
