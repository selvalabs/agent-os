# START HERE — Crie o seu Cérebro

Esta é a porta de entrada para criar, revisar ou operar um Cérebro editorial dentro da arquitetura SelvaLabs Agent OS.

O Cérebro mantém conhecimento humano, pesquisa, curadoria, decisões transversais e memória durável para agentes sem duplicar a verdade operacional dos repositórios.

## Princípio de privacidade

Este guia usa somente estruturas e exemplos genéricos. Ao aplicar o modelo:

- crie seus próprios nomes, projetos, agentes e tags;
- não publique URLs, IDs ou conteúdo do workspace real;
- mantenha dados privados apenas no seu ambiente;
- use `docs/governance/PUBLIC-SANITIZATION.md` antes de compartilhar templates ou exemplos.

## Banco central de memória

Crie ou adapte uma **Biblioteca de Markdowns** como banco canônico de memória durável.

Ela pode registrar processos, decisões, políticas, integrações, runbooks, incidentes resolvidos, pesquisas, templates e aprendizados que precisam sobreviver a conversas e sessões.

As áreas `01` a `05` devem usar views vinculadas da mesma Biblioteca, filtradas por projeto, agente, tipo, tags e status. Evite bibliotecas paralelas.

Consulte `MARKDOWN-LIBRARY-MEMORY.md` para os gatilhos de registro.

## Estrutura recomendada

```text
Cérebro
├── START HERE
├── Biblioteca de Markdowns
├── 01 — Conhecimento
├── 02 — Projetos e Produtos
├── 03 — Sistema de Agentes
├── 04 — Operação e Governança
└── 05 — Laboratório
```

A Biblioteca pode permanecer como banco de acesso rápido na raiz. Dentro das áreas, use views vinculadas e filtros.

## Conteúdo das áreas

### 01 — Conhecimento

- estudos e materiais de formação;
- pesquisas técnicas ou de domínio;
- fontes, referências e sínteses;
- glossários e manuais conceituais;
- view da Biblioteca para pesquisas, manuais e aprendizados liberados;
- fila de conteúdo em revisão.

Não recebe código, logs, estado de PR ou comandos operacionais voláteis.

### 02 — Projetos e Produtos

- projetos ativos, incubados, em manutenção, pausados e arquivados;
- finalidade, público, responsável e resultado esperado;
- repositório canônico;
- `START-HERE.md`, arquitetura e handoff;
- ambientes e nível de acesso dos agentes;
- decisões e conhecimento relacionados;
- view da Biblioteca filtrada pelo projeto.

A página do projeto aponta para fontes canônicas; não copia documentação operacional do GitHub.

### 03 — Sistema de Agentes

- registro de agentes e ferramentas;
- responsabilidades, permissões e limites;
- repositórios preparados pelo Agent OS;
- catálogo de skills, políticas, prompts e templates;
- compatibilidade entre agentes;
- integrações MCP e fontes canônicas;
- views da Biblioteca por agente e tipo de documento.

Use exemplos neutros, como `Agente de Código`, `Agente de Operações` e `Agente de Pesquisa`.

### 04 — Operação e Governança

- registro opcional de atividades ou sessões;
- decisões transversais;
- processos e runbooks;
- incidentes, causas, correções e prevenção;
- deploy, rollback, backup e recuperação consolidados;
- integrações implantadas;
- publicações Cérebro → GitHub;
- revisões, responsáveis e permissões;
- views da Biblioteca para operação ativa e itens a revisar.

O registro de atividades é cronológico. A Biblioteca é temática e reutilizável. Quando a execução revelar um processo, decisão, incidente ou aprendizado relevante, crie ou atualize um Markdown na Biblioteca.

### 05 — Laboratório

- hipóteses, experimentos e protótipos;
- testes de modelos, RAG e embeddings;
- propostas de schema;
- integrações futuras;
- automações em validação;
- rascunhos de skills, políticas e processos;
- view da Biblioteca filtrada por Inbox ou Rascunho experimental.

Conteúdo do Laboratório não orienta operação automaticamente. Depois de validação e revisão, ele pode ser promovido à Biblioteca para uso ativo.

Consulte `NOTION-BRAIN-ARCHITECTURE.md` para o detalhamento completo.

## Componentes mínimos

Comece com:

1. **Biblioteca de Markdowns** — memória durável e curada;
2. **Projetos** — catálogo de projetos e repositórios;
3. **Decisões** — decisões transversais com rastreabilidade;
4. **Fontes** — referências e origens.

Adicione bancos extras somente quando houver volume, responsável e uso real.

## Registro de projeto

Cada projeto deve identificar:

- nome, estado e responsável;
- finalidade e stack resumida;
- repositório canônico;
- `START-HERE.md`, arquitetura e handoff;
- nível de acesso dos agentes;
- view da Biblioteca filtrada pelo projeto.

Exemplo público:

```text
Nome: Projeto Exemplo
Repositório: example-org/example-repo
Agentes: Agente de Código, Agente de Operações
Ambiente: https://example.com
```

Código, testes, deploy e estado operacional permanecem no GitHub.

## Fluxo de consulta

O acesso ao Cérebro começa em leitura.

```text
pedido atual
→ START HERE do Cérebro
→ identificar projeto e agente
→ abrir registro do projeto
→ buscar Markdowns liberados e relacionados
→ recuperar somente decisões e conhecimento necessários
→ abrir START HERE do repositório
→ executar no GitHub
```

Use operacionalmente somente documentos liberados, com escopo compatível, origem verificável e revisão aceitável.

## Regra após ações relevantes

Ao concluir uma mudança, avalie o gatilho de memória.

Crie ou atualize um Markdown quando houver processo reutilizável, decisão importante, incidente resolvido, integração relevante, procedimento de deploy/rollback/backup, diagnóstico não trivial, política nova, aprendizado durável ou mudança permanente de operação.

Não registre conversas completas, segredos, logs brutos, tentativas sem aprendizado ou ações triviais.

```text
issue e branch
→ implementação
→ validação
→ PR ou resultado verificável
→ avaliação de memória
→ criar ou atualizar Markdown
→ revisão
→ liberação para uso
```

## Schema recomendado

A Biblioteca pode usar:

- Documento;
- Slug;
- Status;
- Tipo;
- Formato;
- Projetos;
- Agentes;
- Tags;
- Prioridade;
- Fonte ou GitHub;
- Versão;
- Última revisão;
- Hash de conteúdo;
- Notas.

Esses campos são recomendações. Adapte as opções ao seu workspace sem copiar valores reais para documentação pública.

## Fontes canônicas

| Conteúdo | Sistema canônico |
|---|---|
| Memória durável | Biblioteca de Markdowns do usuário |
| Pesquisa e curadoria | Cérebro editorial do usuário |
| Catálogo de projetos | Cérebro editorial do usuário |
| Código, arquitetura, testes e deploy | GitHub do projeto |
| Issue, PR e commit | GitHub do projeto |
| Estado temporário | `HANDOFF.md` no GitHub |
| Registro cronológico opcional | Registro de atividades ou sessões |
| Políticas, skills e templates compartilhados | SelvaLabs Agent OS |
| Embeddings e busca rápida | Camada derivada |
| Credenciais | Gerenciador de segredos |

## Publicação editorial

Conteúdo do Cérebro só se transforma em política, skill, documentação técnica ou template compartilhado após revisão humana, normalização Markdown, issue, branch, PR, validação, merge e atualização de origem e versão.

Antes de publicar, substitua nomes reais, URLs, IDs e exemplos do workspace por placeholders neutros.

## Checklist mínimo

- [ ] existe `Cérebro/START HERE`;
- [ ] a Biblioteca foi criada ou adaptada;
- [ ] `01` a `05` possuem função e conteúdo definidos;
- [ ] as áreas usam views vinculadas;
- [ ] existe view de memória liberada e de itens a revisar;
- [ ] projetos apontam para GitHub e `START-HERE.md`;
- [ ] integrações externas começam em leitura;
- [ ] ações relevantes passam por avaliação de memória;
- [ ] o fluxo Cérebro → GitHub usa issue, branch, PR e validação;
- [ ] exemplos públicos são fictícios;
- [ ] nenhuma página existente foi removida ou movida automaticamente.

## Documentos relacionados

1. `NOTION-BRAIN-ARCHITECTURE.md` — conteúdo detalhado das áreas;
2. `MARKDOWN-LIBRARY-MEMORY.md` — memória e write-back;
3. `DATABASE-SCHEMAS.md` — propriedades, relações e views;
4. `MCP-CONTEXT-FLOW.md` — acesso seletivo e seguro;
5. `GOVERNANCE-AND-PUBLISHING.md` — manutenção e publicação;
6. `../governance/PUBLIC-SANITIZATION.md` — sanitização para publicação.
