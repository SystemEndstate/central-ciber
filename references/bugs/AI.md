# AI: 24. IA, agentes, MCP e automações

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| AI-001 | P0 | Prompt injection indireta | Incluir instrução adversarial em documento sintético de RAG. | Agente não executa ação fora das permissões do usuário. |
| AI-002 | P0 | Acesso RAG cruzado | Perguntar por documento de tenant B usando conta A. | Nenhum trecho privado externo ao escopo é recuperado. |
| AI-003 | P0 | Loop de ferramentas | Criar cenário com ferramenta que sempre falha. | Limites de passos, tempo e custo interrompem execução. |
| AI-004 | P0 | Ferramenta perigosa | Pedir alteração financeira sem autorização fora do modelo. | Backend recusa sem confirmação independente. |
| AI-005 | P1 | JSON malformado do LLM | Retornar objeto com campos ausentes, tipos incorretos e lixo. | Schema rejeita e sistema tenta recuperação limitada. |
| AI-006 | P0 | Alucinação de ID | Modelo retorna ID inexistente ou de outro usuário. | Validação no backend impede mutação incorreta. |
| AI-007 | P1 | Timeout de modelo | Interromper stream da resposta com cobrança registrada. | Status/custo reconciliado; cliente recebe erro apropriado. |
| AI-008 | P0 | Conta sem quota | Gerar solicitações paralelas acima do orçamento. | Quota financeira e limites de tokens respeitados. |
| AI-009 | P1 | Modelo não disponível | Trocar modelo configurado por inexistente/descontinuado. | Fallback permitido ou erro controlado, sem downgrade inseguro. |
| AI-010 | P0 | MCP tools alteradas | Mudar schema de ferramenta em ambiente de teste. | Agente detecta incompatibilidade, não executa com parâmetros errados. |
| AI-011 | P0 | Output HTML | Gerar resposta contendo tags/script de teste. | UI sanitiza saída antes de renderizar. |
| AI-012 | P0 | Histórico trocado | Alternar tenant e reiniciar conversa de agente. | Contexto, arquivos e memória isolados por identidade. |
| AI-013 | P1 | Input arquivo gigante | Enviar anexo acima de limite de extração/contexto. | Sistema limita custo e memória. |
| AI-014 | P0 | Tool call repetida | Modelo chama mesma ferramenta transacional várias vezes. | Idempotência no executor evita efeitos duplicados. |
| AI-015 | P0 | Prompt contém segredo | Inspecionar histórico, tracing e erro de ferramentas de teste. | Tokens e segredos são mascarados e não persistidos indevidamente. |
| AI-016 | P1 | Streaming parcial | Cortar streaming de tokens e enviar nova requisição. | UI e histórico não apresentam resposta parcial como definitiva. |
