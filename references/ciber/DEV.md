# DEV: 13. DevSecOps e cadeia de fornecimento

| ID | Pri | Controle | Exigência / evidência |
|---|---|---|---|
| DEV-01 | P0 | Acesso ao Git | Restringir repositórios e projetos sensíveis. |
| DEV-02 | P0 | MFA da equipe | Proteger contas que acessam código e ambientes. |
| DEV-03 | P0 | Secret scanning | Bloquear publicação de credenciais. |
| DEV-04 | P0 | SAST | Executar análise estática na mudança de código. |
| DEV-05 | P0 | SCA | Monitorar bibliotecas e transitivas vulneráveis. |
| DEV-06 | P1 | DAST | Examinar aplicação em ambiente autorizado. |
| DEV-07 | P1 | SBOM | Manter inventário das dependências. |
| DEV-08 | P0 | Branch protection | Exigir aprovações e checks para produção. |
| DEV-09 | P0 | Revisão humana | Validar alterações sensíveis por outra pessoa. |
| DEV-10 | P0 | CI/CD isolado | Separar execução não confiável de segredos de produção. |
| DEV-11 | P0 | OIDC para deploy | Usar credenciais curtas e federadas. |
| DEV-12 | P1 | Containers analisados | Scan de imagens e bases mínimas. |
| DEV-13 | P1 | Artefatos assinados | Verificar procedência e integridade de builds. |
| DEV-14 | P0 | Infra as Code | Versionar redes, políticas, recursos e secrets references. |
| DEV-15 | P1 | Policy as Code | Bloquear recursos inseguros na pipeline. |
| DEV-16 | P0 | Testes de autorização | Executar por papel, usuário, tenant e estado. |
| DEV-17 | P1 | Threat modeling | Avaliar ameaças de recursos novos. |
| DEV-18 | P1 | Patching de dependências | Acompanhar CVEs e compromissos de correção. |
| DEV-19 | P1 | Ambiente temporário | Nunca expor dados de produção em preview inseguro. |
| DEV-20 | P0 | Aprovação de migrações | Revisar mudanças irreversíveis e de privilégio. |
| DEV-21 | P1 | Código gerado por IA | Revisar e testar como qualquer código não confiável. |
| DEV-22 | P1 | Rollback de release | Preparar retorno com compatibilidade de schema. |
