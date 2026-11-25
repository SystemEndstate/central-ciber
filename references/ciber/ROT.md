# ROT: 5. Rotas, endpoints e autorização

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| ROT-01 | P0 | Rota privada | Validar autenticação no servidor em toda rota protegida. |
| ROT-02 | P0 | Autorização de objeto | Conferir a propriedade e o direito ao registro solicitado. |
| ROT-03 | P0 | Autorização funcional | Rejeitar execução de métodos reservados a papéis superiores. |
| ROT-04 | P0 | Isolamento tenant | Associar toda operação à organização corretamente autorizada. |
| ROT-05 | P0 | Campos protegidos | Nunca permitir edição indevida de role, owner_id, balance e tenant_id. |
| ROT-06 | P0 | Negação por padrão | Negar métodos e rotas não explicitamente permitidos. |
| ROT-07 | P0 | GET protegido | Aplicar autorização também nas leituras de dados privados. |
| ROT-08 | P0 | Escritas protegidas | Verificar autenticação, papel, objeto e estado para POST, PATCH e DELETE. |
| ROT-09 | P0 | IDs manipulados | Trocar UUID ou slug não pode conceder acesso. |
| ROT-10 | P0 | Resposta mínima | Não expor campos internos ou confidenciais desnecessários. |
| ROT-11 | P0 | Admin APIs | Reforçar MFA, autorização, auditoria e reautenticação. |
| ROT-12 | P1 | APIs internas | Utilizar identidade de serviço e redes protegidas. |
| ROT-13 | P1 | Inventário de rotas | Manter lista de endpoints, métodos, escopo, permissões e proprietário. |
| ROT-14 | P1 | Versionamento | Remover versões vulneráveis ou exigir atualizações seguras. |
| ROT-15 | P0 | Exportação | Filtrar relatórios e exports pelo escopo autorizado. |
| ROT-16 | P0 | WebSocket | Autorizar assinatura de canais e alterações de permissão. |
| ROT-17 | P0 | RPC e Server Actions | Tratar ações invocáveis como APIs externas. |
| ROT-18 | P1 | Busca e paginação | Limitar volume, custo e complexidade das consultas. |
