# FRONT: 04. Frontend JS, React, Next.js e PWA

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| FRONT-001 | P1 | Estado stale | Iniciar atualização, trocar rapidamente de entidade e aguardar resposta. | Resposta anterior não sobrescreve entidade atual. |
| FRONT-002 | P1 | UseEffect em loop | Reproduzir mudança de props que aciona efeito e renderizações repetidas. | Requisições e renderizações permanecem finitas. |
| FRONT-003 | P1 | Component desmontado | Sair da tela antes de requisição resolver. | Cancelamento/limpeza sem efeitos colaterais indevidos. |
| FRONT-004 | P0 | SSR com segredo | Inspecionar HTML inicial, props serializados e bundles de produção. | Nenhuma credencial privilegiada ou dado privado de outra conta. |
| FRONT-005 | P0 | Cache global multi-tenant | Trocar organização sem atualizar o navegador. | Chaves de cache incluem contexto autorizado e invalidam corretamente. |
| FRONT-006 | P0 | Optimistic UI sem rollback | Alterar estado, forçar falha do servidor. | Interface reverte ou marca pendência; nada fica falsamente salvo. |
| FRONT-007 | P1 | Form data inválida | Enviar campos omitidos, null, NaN, strings enormes e Unicode. | Backend valida todos os casos; UI exibe erro adequado. |
| FRONT-008 | P0 | XSS por conteúdo | Exibir conteúdo HTML/Markdown sintético não confiável. | Conteúdo renderizado sem executar código arbitrário. |
| FRONT-009 | P0 | Rotas protegidas por UI | Visitar endereço administrativo diretamente e por API. | Servidor nega acesso não autorizado mesmo sem menu visível. |
| FRONT-010 | P1 | PWA offline stale | Instalar PWA, entrar offline e trocar versão. | Conteúdo atualiza de forma controlada; sem mistura de bundles. |
| FRONT-011 | P0 | Storage entre contas | Entrar A, sair, entrar B e consultar localStorage/IndexedDB. | Sem dados privados ou cache de A disponível para B. |
| FRONT-012 | P1 | Erro de locale no SSR | Alterar fuso/idioma entre cliente e servidor. | Datas e números convergem sem desvio crítico. |
| FRONT-013 | P1 | Renderização de listas | Adicionar e reordenar linhas com valores similares. | Componentes representam IDs corretos, sem estado misturado. |
| FRONT-014 | P0 | Hidratação de sessão | Abrir diretamente uma rota após sessão expirar. | Sem flash de dados sensíveis nem autorização apenas client-side. |
| FRONT-015 | P1 | Erro de chunk antigo | Implantar versão nova com aba antiga aberta. | Falha de chunk tratada; atualização sem perda indevida. |
| FRONT-016 | P1 | CSP quebra feature | Ativar CSP restritiva em staging e percorrer telas críticas. | Scripts legítimos funcionam sem relaxar políticas desnecessárias. |
