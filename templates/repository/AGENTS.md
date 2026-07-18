# AGENTS.md — {{PROJECT_NAME}}

## Missão

Trabalhar neste repositório com mudanças pequenas, verificáveis e compatíveis com a arquitetura existente.

## Leia antes de agir

1. `START-HERE.md`
2. `docs/agent/index.md`
3. `docs/agent/ARCHITECTURE.md`
4. `docs/agent/WORKFLOW.md`
5. `docs/agent/SECURITY.md`
6. `docs/agent/HANDOFF.md`
7. documentação de produção quando aplicável

## Comandos essenciais

- Instalação: `{{INSTALL_COMMAND}}`
- Testes: `{{TEST_COMMAND}}`
- Lint: `{{LINT_COMMAND}}`
- Build: `{{BUILD_COMMAND}}`

## Regras

- Preserve mudanças existentes.
- Não grave segredos.
- Não altere produção sem autorização explícita.
- Não faça force push ou limpeza destrutiva.
- Mostre resultados de testes e limitações.
- Atualize o handoff ao transferir a tarefa.
- Relacione mudanças relevantes a issue e branch própria.
- Mantenha o `START-HERE.md` curto e atual.
- Mantenha contexto específico deste projeto no repositório ou em seu registro no Cérebro.
- Não use a Biblioteca de Markdowns para cadastrar ou documentar este projeto.
- Crie memory write-back somente quando o resultado for global, transversal ou necessário entre sessões.
- Use projeto apenas como origem opcional da memória.
- Não copie contexto privado para exemplos públicos.

## Classificação de contexto

```text
projeto e links
→ registro do projeto no Cérebro

código e operação
→ este repositório

continuidade
→ issue, PR e HANDOFF

memória global ou entre sessões
→ Biblioteca de Markdowns
```

## Contexto compartilhado

Skills e políticas globais pertencem ao SelvaLabs Agent OS. Pesquisa e memória transversal podem viver no Cérebro editorial. Este repositório mantém as fontes canônicas específicas de `{{REPO_SLUG}}`.
