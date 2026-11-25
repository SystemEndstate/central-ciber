# FILE: 19. Arquivos, armazenamento e mídia

| ID | Pri | Bug buscado | Como provocar | Resultado esperado |
|---|---|---|---|---|
| FILE-001 | P0 | Extensão disfarçada | Enviar conteúdo de formato A com extensão B em staging. | Tipo real validado; processamento inadequado recusado. |
| FILE-002 | P1 | Arquivo enorme | Enviar arquivo acima do limite e diversos arquivos simultâneos. | Quota aplicada antes de esgotar recursos. |
| FILE-003 | P0 | ZIP bomb sintético | Usar arquivo compactado de teste com alta taxa de expansão. | Limites de extração e CPU/memória aplicados. |
| FILE-004 | P0 | Path traversal | Carregar arquivo com nome incluindo ../ e separadores alternativos. | Destino permanece dentro da área autorizada. |
| FILE-005 | P0 | Symlink import | Selecionar link para arquivo externo em sandbox autorizado. | Aplicação valida caminhos reais e permissões. |
| FILE-006 | P1 | PDF malformado | Processar corpus de PDFs de teste truncados/malformados. | Parser isolado; falha sem crash global. |
| FILE-007 | P1 | Imagem danificada | Carregar JPEG/PNG truncado, dimensões extremas ou metadados inválidos. | Sem travamento, corrupção ou consumo ilimitado de memória. |
| FILE-008 | P1 | Upload duplicado | Enviar mesmo arquivo duas vezes com retry automático. | Política clara de deduplicação, versionamento ou duas cópias. |
| FILE-009 | P0 | Permissão de download | Usar link de arquivo de outro tenant. | Download privado negado. |
| FILE-010 | P0 | URL assinada expirada | Solicitar arquivo após expiração. | Acesso negado e renovação autorizada quando aplicável. |
| FILE-011 | P1 | Arquivo órfão | Simular falha do banco após gravação de objeto. | Limpeza ou reconciliação com auditoria. |
| FILE-012 | P0 | Concorrência de nome | Dois usuários salvam arquivo com mesmo nome lógico. | Não sobrescreve conteúdo de outro usuário. |
| FILE-013 | P1 | Arquivo em uso | Editar/exportar arquivo bloqueado por outro processo. | Erro manejado; conteúdo existente íntegro. |
| FILE-014 | P1 | Exportação longa | Exportar dados volumosos com cancelamento no meio. | Job cancelado e artefato parcial não publicado. |
| FILE-015 | P1 | Metadados privados | Exportar imagem/documento com EXIF e dados de teste. | Dados sensíveis removidos quando política exigir. |
| FILE-016 | P1 | Antimalware em falso positivo | Simular rejeição de arquivo aparentemente válido. | Estado do upload e comunicação apropriados sem bypass automático. |
