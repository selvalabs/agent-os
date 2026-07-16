# START HERE — Meu Cérebro

> Template genérico para importação. Substitua os placeholders e exemplos antes de usar.

## Propósito

Este Cérebro organiza conhecimento, pesquisa, curadoria, decisões transversais, projetos e memória durável para agentes. Código, arquitetura, testes, deploy e estado operacional continuam nos repositórios GitHub.

## Privacidade

- não cole conteúdo de outro workspace;
- não publique nomes, URLs ou IDs privados;
- use exemplos fictícios em capturas e documentação;
- mantenha clientes, projetos internos e agentes privados apenas no seu ambiente.

## Memória central

Crie ou conecte uma **Biblioteca de Markdowns** como memória durável do Cérebro.

Processos, decisões, integrações, incidentes resolvidos, runbooks e aprendizados relevantes podem criar ou atualizar um Markdown nessa Biblioteca.

As áreas abaixo usam views vinculadas da mesma Biblioteca. Evite cópias independentes dos documentos.

## Rotas principais

### 01 — Conhecimento

Formação, estudos, pesquisas, referências, sínteses, glossários e view de Markdowns liberados dos tipos Pesquisa, Manual e Aprendizado.

### 02 — Projetos e Produtos

Catálogo de projetos, responsáveis, repositórios, START HERE, arquitetura, handoff, ambientes e view da Biblioteca filtrada por projeto.

### 03 — Sistema de Agentes

Agentes, ferramentas, repositórios agentic-first, skills, políticas, prompts, templates, compatibilidade, integrações MCP e views da Biblioteca por agente.

### 04 — Operação e Governança

Registro opcional de atividades, decisões, processos, runbooks, incidentes, integrações, publicações, revisões, permissões e view de itens liberados ou a revisar.

### 05 — Laboratório

Hipóteses, experimentos, protótipos, testes de modelos e RAG, propostas de schema, automações e rascunhos ainda não aprovados.

## Registro de atividades versus Biblioteca

- **Registro de atividades:** histórico cronológico opcional do que aconteceu.
- **Biblioteca:** memória temática, curada e reutilizável.

Quando uma atividade revelar processo ou aprendizado durável, consolide-o na Biblioteca.

## Antes de agir

1. identifique o projeto, agente ou domínio;
2. abra o registro correspondente;
3. busque Markdowns relacionados;
4. use operacionalmente somente itens liberados;
5. siga os links para fontes canônicas;
6. use GitHub para contexto operacional;
7. não trate Laboratório ou Rascunho como regra aprovada.

## Depois de uma ação relevante

```text
execução e validação
→ issue, PR, commit ou resultado verificável
→ avaliar se há memória reutilizável
→ criar ou atualizar Markdown
→ preencher projeto, agente, tipo, origem e versão
→ revisão humana
→ liberação para uso
```

Registre processos reutilizáveis, decisões, incidentes resolvidos, integrações, diagnósticos não triviais, deploy, rollback, backup e aprendizados importantes.

Não registre segredos, logs brutos, conversas completas ou ações triviais.

## Fontes canônicas

| Conteúdo | Fonte |
|---|---|
| Memória durável | Biblioteca de Markdowns criada neste workspace |
| Pesquisa e curadoria | Este Cérebro |
| Catálogo de projetos | Este Cérebro |
| Código, arquitetura, testes e deploy | GitHub do projeto |
| Issue, PR e commit | GitHub do projeto |
| Estado temporário | `HANDOFF.md` |
| Registro cronológico opcional | Registro de atividades ou sessões |
| Políticas, skills e templates compartilhados | SelvaLabs Agent OS |
| Busca, embeddings e consultas rápidas | Camada derivada |
| Segredos | Gerenciador de segredos |

## Acesso de agentes

Integrações começam em modo de leitura. Escrita exige intenção explícita, destino definido, conteúdo revisável e preservação das páginas existentes.

## Views recomendadas

- Memória liberada;
- Markdowns a revisar;
- Projetos ativos;
- Markdowns por projeto;
- Markdowns por agente;
- Decisões em revisão;
- Publicações pendentes;
- Laboratório e rascunhos.

## Exemplos fictícios

```text
Projeto: Produto Alpha
Repositório: example-org/product-alpha
Agentes: Agente de Código, Agente de Operações
Ambiente: https://example.com
```

## Responsáveis

- Responsável editorial: definir neste workspace.
- Responsáveis de projeto: definir no catálogo de Projetos.
- Última revisão desta página: preencher após importação.

## Documentação de implementação

A arquitetura, os schemas, o fluxo MCP e as regras da Biblioteca permanecem versionados em `selvalabs-agent-os/docs/notion/`.
