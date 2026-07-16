# START HERE — {{PROJECT_NAME}}

Este é o ponto de entrada obrigatório para pessoas e agentes que começam a trabalhar em `{{REPO_SLUG}}`.

Use esta página para localizar somente o contexto necessário. Não carregue toda a documentação do repositório sem necessidade.

## Propósito do projeto

TODO: descrever em poucas linhas o problema resolvido, os usuários e o resultado esperado.

## Estado atual

TODO: informar se o projeto está em descoberta, desenvolvimento, produção, manutenção ou arquivado.

## Ordem mínima de leitura

1. `AGENTS.md` — regras persistentes e comandos essenciais;
2. `docs/agent/ARCHITECTURE.md` — estrutura e responsabilidades;
3. `docs/agent/WORKFLOW.md` — fluxo de implementação e validação;
4. `docs/agent/SECURITY.md` — limites e operações sensíveis;
5. `docs/agent/HANDOFF.md` — estado temporário da frente atual;
6. `docs/agent/DEPLOY.md` e `docs/agent/VPS.md` somente quando a tarefa envolver produção.

## Links canônicos

- Repositório: TODO
- Issue atual: TODO ou não aplicável
- Pull request atual: TODO ou não aplicável
- Ambiente de demonstração: TODO ou não aplicável
- Registro no Cérebro editorial: TODO ou não aplicável
- View da Biblioteca de Markdowns deste projeto: TODO ou não aplicável
- Arquitetura canônica: `docs/agent/ARCHITECTURE.md`
- Handoff atual: `docs/agent/HANDOFF.md`

Não use URLs, IDs ou nomes de um workspace privado em exemplos públicos. Para documentação de demonstração, use `example-org/example-repo` e `https://example.com`.

## Comandos essenciais

- Instalação: `{{INSTALL_COMMAND}}`
- Testes: `{{TEST_COMMAND}}`
- Lint: `{{LINT_COMMAND}}`
- Build: `{{BUILD_COMMAND}}`

## Fontes canônicas

- código, arquitetura e operação: este repositório;
- estado temporário: issue, PR e `docs/agent/HANDOFF.md`;
- memória durável: Biblioteca de Markdowns criada pelo proprietário do projeto;
- políticas e skills compartilhadas: SelvaLabs Agent OS;
- pesquisa e contexto transversal: Cérebro editorial escolhido pelo usuário;
- segredos: gerenciador de segredos, nunca Markdown.

## Memória após ações relevantes

Antes de encerrar uma tarefa, avalie se o trabalho produziu processo, decisão, incidente resolvido, integração, runbook, diagnóstico não trivial ou aprendizado reutilizável.

Quando houver, crie ou atualize um documento na Biblioteca de Markdowns do projeto e relacione:

- projeto aplicável;
- agentes ou ferramentas aplicáveis;
- tipo e tags;
- issue, PR, commit, arquivo ou fonte de origem;
- versão e última revisão;
- estado inicial de rascunho até revisão humana.

Não registre conversas completas, ações triviais, logs brutos, segredos ou conteúdo privado como memória durável.

```text
issue e branch
→ implementação
→ validação
→ pull request ou resultado verificável
→ avaliação de memória
→ criar ou atualizar Markdown
→ revisão
→ liberação para uso
```

## Regras para começar

- preserve alterações existentes;
- abra ou relacione uma issue antes de mudanças relevantes;
- use branch própria;
- consulte somente o contexto necessário;
- valide antes de abrir pull request;
- atualize o handoff quando houver continuidade;
- registre memória quando houver processo ou ação relevante;
- não execute operação destrutiva ou de produção sem autorização explícita;
- não copie contexto privado para documentação pública.

## Checklist para concluir

- [ ] issue e escopo estão identificados;
- [ ] testes ou validação foram executados;
- [ ] pull request ou evidência do resultado existe;
- [ ] handoff foi atualizado quando necessário;
- [ ] gatilho de memória foi avaliado;
- [ ] Markdown foi criado ou atualizado quando aplicável;
- [ ] nenhum segredo ou contexto privado foi registrado.

## Próxima ação

TODO: registrar a próxima ação concreta, pequena e verificável.
