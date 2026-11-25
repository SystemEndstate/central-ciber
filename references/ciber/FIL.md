# FIL: 11. Uploads, arquivos e downloads

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| FIL-01 | P0 | Armazenamento privado | Dados sigilosos não ficam em buckets públicos. |
| FIL-02 | P0 | Download autorizado | Validar a permissão antes de entregar bytes ou URL. |
| FIL-03 | P0 | URLs assinadas | Escopo e validade mínimos para links temporários. |
| FIL-04 | P0 | Formato real | Conferir tipo de mídia, assinatura e extensão permitida. |
| FIL-05 | P0 | Tamanho e quota | Restringir arquivo individual, quantidade e uso total. |
| FIL-06 | P1 | Antimalware | Analisar arquivos potencialmente perigosos antes do consumo. |
| FIL-07 | P0 | Execução de upload | Nunca executar como código o material enviado pelo usuário. |
| FIL-08 | P0 | Path traversal | Gerar identificadores seguros e validar caminhos. |
| FIL-09 | P1 | Metadados | Remover metadados privados quando necessário. |
| FIL-10 | P1 | Indexação | Impedir indexação de documentos privados. |
| FIL-11 | P0 | Tenant isolation | Negar listagem, leitura, substituição ou exclusão entre clientes. |
| FIL-12 | P1 | Arquivo compactado | Detectar decompression bomb, paths internos e formatos malformados. |
| FIL-13 | P1 | Ciclo de vida | Definir retenção, versionamento e exclusão. |
| FIL-14 | P1 | Auditoria de arquivos | Registrar exportações e compartilhamentos sensíveis. |
| FIL-15 | P1 | Recuperação de objetos | Manter cópias e restauração também do storage. |
