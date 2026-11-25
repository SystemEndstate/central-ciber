# AI: 16. Segurança de IA, LLM e agentes

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| AI-01 | P0 | Prompt injection | Tratar arquivos, sites e conteúdo recuperado como dados não confiáveis. |
| AI-02 | P0 | Permissão fora do LLM | Não usar instruções de prompt como controle de autorização. |
| AI-03 | P0 | Tools com escopo | Restringir cada ferramenta ao mínimo necessário. |
| AI-04 | P0 | Isolamento tenant | Filtrar consultas e ações de agentes por cliente. |
| AI-05 | P0 | RAG autorizado | Consultar apenas documentos permitidos ao usuário. |
| AI-06 | P0 | Chaves de modelos | Manter credenciais dos provedores no servidor. |
| AI-07 | P0 | Quotas de tokens | Limitar consumo por usuário, tenant e modelo. |
| AI-08 | P0 | Teto de custos | Impedir loops e chamadas ilimitadas. |
| AI-09 | P0 | Saída validada | Nunca executar SQL/comandos gerados sem validação independente. |
| AI-10 | P0 | Aprovação humana | Requerer confirmação para ações irreversíveis e de alto risco. |
| AI-11 | P1 | Redação de dados | Mascarar informações antes de envio quando possível. |
| AI-12 | P1 | Retenção por provedores | Verificar uso, armazenamento e termos das APIs externas. |
| AI-13 | P1 | Auditoria de agentes | Registrar ferramenta, autorização, custo e resultado. |
| AI-14 | P1 | MCP e plugins | Validar servidores, permissões e fontes conectadas. |
| AI-15 | P1 | HTML gerado | Sanitizar links e conteúdo exibido de modelos. |
| AI-16 | P1 | Prompt sem segredos | Nunca inserir senhas e chaves em system prompt. |
| AI-17 | P1 | Sandbox | Isolar execução de código, parser e arquivos. |
| AI-18 | P1 | Cache de contexto | Impedir vazamento entre contas, embeddings e memória. |
| AI-19 | P1 | Loop de agente | Limitar ações, duração e recursos. |
| AI-20 | P2 | Red teaming | Testar injeção indireta, exfiltração e abuso de ferramentas. |
