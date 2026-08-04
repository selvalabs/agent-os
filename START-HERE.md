# START HERE — SelvaLabs Agent OS

Este é o ponto de entrada para humanos e agentes que trabalham com o SelvaLabs Agent OS.

Não carregue toda a documentação. Identifique primeiro qual tipo de contexto a tarefa exige.

## Rotas principais

| Necessidade | Leia primeiro |
|---|---|
| Entender a arquitetura | `docs/architecture/SPEC-AGENT-OS.md` |
| Criar um Cérebro | `docs/notion/START-HERE.md` |
| Organizar projetos no Notion | `docs/notion/NOTION-BRAIN-ARCHITECTURE.md` |
| Criar memória para agentes | `docs/notion/MARKDOWN-LIBRARY-MEMORY.md` |
| Definir bancos e relações | `docs/notion/DATABASE-SCHEMAS.md` |
| Criar um repositório | `templates/repository/START-HERE.md` |
| Entender fontes canônicas | `docs/governance/CANONICAL-SOURCES.md` |
| Publicar com segurança | `docs/governance/PUBLIC-SANITIZATION.md` |

## Onde cada informação vive

```text
projeto e produto
→ 02 — Projetos e Produtos

código, arquitetura e operação específica
→ GitHub do projeto

estado temporário, pendências e continuidade
→ issue, PR e HANDOFF.md

memória global, transversal ou necessária entre sessões
→ Biblioteca de Markdowns
```

A Biblioteca de Markdowns não registra projetos. Ela registra sínteses reutilizáveis que agentes precisam recuperar em sessões futuras.

## Gatilho de memória

Antes de criar um Markdown, classifique o resultado:

1. é específico de um projeto? Atualize a página do projeto ou o GitHub.
2. é estado temporário? Atualize issue, PR ou `HANDOFF.md`.
3. é global, transversal ou necessário para futuras sessões? Atualize a Biblioteca.
4. é trivial, bruto ou volátil? Não crie memória durável.

```text
sessão ou trabalho relevante
→ validar resultado
→ classificar destino
→ registrar na fonte correta
→ revisar
```

## Fontes canônicas

- catálogo e contexto dos projetos: banco Projetos no Cérebro;
- código e operação específica: GitHub do projeto;
- memória global e transversal: Biblioteca de Markdowns;
- conhecimento e curadoria: áreas editoriais do Cérebro;
- estado temporário: issue, PR e handoff;
- políticas e skills compartilhadas: Agent OS;
- segredos: gerenciador de segredos.

## Princípios obrigatórios

- mantenha um `START HERE` visível;
- preserve conteúdo existente;
- use leitura seletiva;
- não duplique projeto na Biblioteca;
- não copie documentação operacional do GitHub para o Notion;
- use issue, branch, PR e CI;
- comece integrações externas em leitura;
- use exemplos fictícios em conteúdo público;
- nunca grave segredos em Markdown.

## Segurança durante o desenvolvimento

Para mudanças de segurança, leia policies/secure-development.md, o inventário schemas/security-controls.yaml e o worksheet 	emplates/repository/docs/agent/SECURITY.md. Issue e PR devem registrar o teste negativo, o teste positivo e a evidência de não reprodução.
