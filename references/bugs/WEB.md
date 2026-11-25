# WEB: 02. Web: navegação, HTML, CSS e estado

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| WEB-001 | P1 | Página em branco | Abrir rota diretamente, atualizar e usar histórico após login. | Rota carrega ou mostra erro recuperável, nunca branco definitivo. |
| WEB-002 | P1 | Back/forward inconsistente | Navegar entre listagem e detalhe usando botões do navegador. | Estado e URL representam a tela correta. |
| WEB-003 | P1 | Formulário perde dados | Preencher formulário, simular erro 500 e voltar ao estado anterior. | Campos recuperáveis preservados; segredos tratados conforme política. |
| WEB-004 | P0 | Submit duplicado | Clicar duas vezes, pressionar Enter e disparar retry em paralelo. | Uma única alteração lógica confirmada no servidor. |
| WEB-005 | P1 | Scroll/click bloqueados | Abrir modal, fechar via Escape, toque e navegação. | Focus e scrolling restaurados; ações não ficam bloqueadas. |
| WEB-006 | P1 | Layout quebra em zoom | Testar 200% de zoom e largura estreita em browser desktop. | Controles essenciais continuam disponíveis e legíveis. |
| WEB-007 | P1 | Tema quebra formulário | Alternar dark/light e alto contraste no meio do fluxo. | Campos, foco e erros continuam visíveis. |
| WEB-008 | P1 | Hydration mismatch | Recarregar páginas SSR com datas, idioma e valores dinâmicos. | Sem divergência indevida entre HTML do servidor e cliente. |
| WEB-009 | P1 | Evento de navegação perdido | Clicar rapidamente em duas rotas enquanto dados são carregados. | Última rota selecionada vence; dados antigos não reaparecem. |
| WEB-010 | P1 | Busca com resposta fora de ordem | Digitar termos sucessivos sob rede lenta. | Somente resultado do termo atual é exibido. |
| WEB-011 | P2 | Filtro sem reset de página | Ir para a última página e aplicar filtro restritivo. | Paginação volta a página válida, sem lista falsa vazia. |
| WEB-012 | P1 | Upload sem feedback | Enviar arquivo grande em rede degradada. | Progresso e falhas são exibidos; estado não fica eternamente pendente. |
| WEB-013 | P0 | Links externos mal interpretados | Abrir URLs externas e links internos com parâmetros especiais. | Destino e contexto validados; sem execução inesperada. |
| WEB-014 | P0 | Campos ocultos acessíveis | Modificar campos somente pela DevTools em conta de teste. | Backend ignora ou rejeita campos não autorizados. |
| WEB-015 | P1 | Service Worker antigo | Atualizar aplicação com aba e cache antigos ativos. | Versão e cache convergem sem ativos incompatíveis. |
| WEB-016 | P0 | Três abas concorrentes | Editar mesmo registro em duas abas e sair da terceira. | Conflitos e encerramento de sessão tratados corretamente. |
