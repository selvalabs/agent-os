# START HERE — SelvaLabs Agent OS

Este é o ponto de entrada para humanos e agentes que começam a trabalhar com o SelvaLabs Agent OS.

Não carregue toda a documentação de uma vez. Localize somente o contexto necessário para a tarefa atual.

## O que é o Agent OS

O SelvaLabs Agent OS é uma base reutilizável para preparar repositórios para construção e manutenção agentic-first. Ele fornece políticas, skills, templates, validações, handoffs e regras de segurança compartilhadas.

Ele não contém o Cérebro pessoal de nenhum mantenedor. A documentação ensina cada usuário a criar a própria estrutura.

## Comece pela sua necessidade

| Necessidade | Leia primeiro |
|---|---|
| Entender a arquitetura completa | `docs/architecture/SPEC-AGENT-OS.md` |
| Criar um Cérebro próprio | `docs/notion/START-HERE.md` |
| Entender as áreas 01–05 | `docs/notion/NOTION-BRAIN-ARCHITECTURE.md` |
| Criar memória durável | `docs/notion/MARKDOWN-LIBRARY-MEMORY.md` |
| Criar um novo repositório | `templates/repository/START-HERE.md` e `scripts/bootstrap_repo.py` |
| Entender fontes canônicas | `docs/governance/CANONICAL-SOURCES.md` |
| Entender segurança e permissões | `docs/governance/SECURITY-MODEL.md` |
| Sanitizar conteúdo público | `docs/governance/PUBLIC-SANITIZATION.md` |
| Gerar distribuição com histórico limpo | `docs/release/PUBLIC-RELEASE.md` e `scripts/build_public_snapshot.py` |
| Encontrar capacidade reutilizável | `skills/` |
| Aplicar regras compartilhadas | `policies/` |

## Regra START HERE

Todo espaço preparado pelo Agent OS deve possuir uma entrada `START HERE` curta e visível.

Ela deve:

1. explicar o propósito do espaço;
2. indicar a ordem mínima de leitura;
3. apontar fontes canônicas;
4. separar contexto estável de estado temporário;
5. impedir navegação por tentativa e erro;
6. orientar leitura seletiva, não carregamento integral.

## Memória durável

A arquitetura recomenda que cada usuário crie sua própria **Biblioteca de Markdowns** como memória durável e curada.

Processos, decisões, incidentes, integrações, runbooks e aprendizados relevantes devem criar ou atualizar um Markdown nessa biblioteca.

```text
execução relevante
→ validação
→ issue, PR, commit ou resultado verificável
→ avaliação de memória
→ criar ou atualizar Markdown
→ revisão
→ liberação para uso
```

Não registre conversas completas, ações triviais, logs brutos ou segredos como memória.

## Fontes canônicas

- memória durável: **Biblioteca de Markdowns criada pelo usuário**;
- conhecimento e curadoria: **Cérebro editorial do usuário**;
- código, arquitetura e operação: **GitHub do projeto**;
- estado temporário: **issue, PR e `HANDOFF.md`**;
- políticas, skills e templates compartilhados: **SelvaLabs Agent OS**;
- busca, embeddings e consultas rápidas: **camada derivada**;
- segredos: **gerenciador de segredos**, nunca Markdown.

## Princípios obrigatórios

- comece em leitura ao acessar serviços externos;
- preserve conteúdo humano existente;
- prefira mudanças aditivas, pequenas e reversíveis;
- não duplique documentação operacional do GitHub no Cérebro;
- use views vinculadas em vez de copiar Markdowns;
- não transforme `AGENTS.md` ou `START-HERE.md` em enciclopédias;
- use issue, branch, PR, validação e revisão para mudanças compartilhadas;
- avalie o gatilho de memória antes de encerrar ações relevantes;
- use exemplos fictícios em documentação pública;
- não copie nomes, URLs, IDs ou conteúdo de workspaces reais;
- publique snapshots de repositórios privados em um novo repositório, sem importar histórico, issues ou pull requests.

## Fluxo recomendado

1. leia este arquivo;
2. escolha a rota correspondente;
3. consulte somente os documentos necessários;
4. abra ou relacione uma issue;
5. execute a mudança em branch própria;
6. valide e abra pull request;
7. atualize o handoff quando houver continuidade;
8. registre memória quando houver processo ou aprendizado reutilizável.
