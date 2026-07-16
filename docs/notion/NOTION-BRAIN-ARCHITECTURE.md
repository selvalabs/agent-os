# Arquitetura de um Cérebro editorial

## Princípio

O Cérebro é o plano editorial, de conhecimento e de memória durável do ecossistema. Ele organiza contexto humano, pesquisa, curadoria, decisões transversais, registros reutilizáveis e navegação entre projetos.

Não é banco operacional, repositório de código, secret manager nem substituto do GitHub.

Este documento ensina uma estrutura genérica. Cada pessoa ou equipe deve criar o próprio workspace e preencher os exemplos com seus dados privados.

## Estrutura recomendada

A **Biblioteca de Markdowns** é o banco canônico de memória. As áreas `01` a `05` usam views vinculadas e filtros desse mesmo banco; não criam cópias independentes dos documentos.

```text
Cérebro
├── START HERE
├── Biblioteca de Markdowns
├── 01 — Conhecimento
│   ├── Formação e estudos
│   ├── Pesquisas em andamento
│   ├── Referências e fontes
│   ├── Sínteses aprovadas
│   └── View da Biblioteca: pesquisas, manuais e conhecimento liberado
├── 02 — Projetos e Produtos
│   ├── Projetos ativos
│   ├── Projetos em incubação
│   ├── Projetos em manutenção
│   ├── Projetos arquivados
│   └── Páginas de projeto com views filtradas da Biblioteca
├── 03 — Sistema de Agentes
│   ├── Registro de agentes e ferramentas
│   ├── Registro de repositórios agentic-first
│   ├── Catálogo de skills
│   ├── Políticas globais
│   ├── Prompts e templates
│   ├── Fontes canônicas
│   ├── Compatibilidade e integrações MCP
│   └── View da Biblioteca: skills, políticas, prompts e manuais
├── 04 — Operação e Governança
│   ├── Registro de atividades ou sessões
│   ├── Decisões
│   ├── Processos e runbooks
│   ├── Incidentes e aprendizados
│   ├── Publicações Cérebro → GitHub
│   ├── Revisões periódicas
│   ├── Responsáveis e permissões
│   └── View da Biblioteca: operação, decisões e itens a revisar
└── 05 — Laboratório
    ├── Hipóteses
    ├── Experimentos
    ├── Protótipos
    ├── Integrações futuras
    ├── Testes de RAG, modelos e automações
    └── View da Biblioteca: Inbox e Rascunhos experimentais
```

## Biblioteca de Markdowns

A Biblioteca é a memória durável utilizada por humanos, agentes, automações e futuras camadas de RAG.

Ela deve permanecer única. As cinco áreas apresentam views filtradas por projeto, agente, tipo, tags e status.

Documentos liberados para operação usam o estado definido pelo usuário para conteúdo aprovado, por exemplo `Ativo`. Itens em captura, rascunho ou revisão não devem ser aplicados automaticamente.

Consulte `MARKDOWN-LIBRARY-MEMORY.md` para os gatilhos de registro e o ciclo editorial.

## START HERE

É a entrada obrigatória. Explica onde cada tipo de informação vive, apresenta as views principais, aponta fontes canônicas e impede navegação por tentativa e erro.

Também aponta para a Biblioteca de Markdowns e explica que ações e processos relevantes podem produzir memória durável.

## 01 — Conhecimento

### Finalidade

Organizar conteúdo que ajuda a compreender assuntos, domínios e problemas, independentemente da execução imediata de um projeto.

### Conteúdo esperado

- formação e estudos;
- pesquisas em andamento;
- estudos técnicos e conceituais;
- referências externas;
- sínteses aprovadas;
- glossários e vocabulários;
- documentação temática;
- conhecimento de domínio necessário aos projetos.

### Views recomendadas

- `Conhecimento liberado` — itens aprovados dos tipos Pesquisa, Manual ou Aprendizado;
- `Em revisão` — rascunhos e itens que precisam de validação;
- `Por domínio` — agrupada por Tags;
- `Por projeto` — filtrada por Projetos;
- `Formação` — conteúdo acadêmico ou profissional separado da memória operacional.

### Não pertence aqui

- código;
- comandos operacionais voláteis;
- estado atual de branch ou PR;
- logs de execução;
- regras de agentes ainda não aprovadas.

## 02 — Projetos e Produtos

### Finalidade

Ser o catálogo transversal dos produtos, sistemas, estudos aplicados e repositórios.

### Conteúdo esperado

- registro de cada projeto;
- finalidade, público e resultado esperado;
- estado: incubação, ativo, manutenção, pausado ou arquivado;
- responsável humano;
- GitHub canônico;
- `START-HERE.md` do repositório;
- arquitetura e documentação canônica;
- ambiente de demonstração ou produção;
- nível de acesso permitido aos agentes;
- relações com conhecimento, decisões e fontes;
- view da Biblioteca filtrada pelo projeto.

### Estrutura mínima da página de projeto

```text
Resumo
Estado
Responsável
Repositório canônico
START HERE do repositório
Arquitetura
Ambientes
Acesso permitido aos agentes
Decisões relevantes
Conhecimento relacionado
Memória do projeto
Última revisão
```

### Exemplo público

```text
Projeto: Produto Alpha
Repositório: example-org/product-alpha
Agentes: Agente de Código, Agente de Operações
Ambiente: https://example.com
```

### Regra

O Cérebro mostra mapa, contexto e relações. Código, testes, deploy, runbooks técnicos e estado operacional detalhado permanecem no GitHub. A página usa links e views da Biblioteca, não cópias manuais.

## 03 — Sistema de Agentes

### Finalidade

Organizar como agentes, modelos e ferramentas trabalham nos projetos.

### Conteúdo esperado

- registro de agentes e ferramentas;
- responsabilidades e limites de cada agente;
- repositórios preparados pelo Agent OS;
- catálogo editorial de skills;
- políticas globais;
- prompts e templates aprovados;
- compatibilidade entre ferramentas;
- integrações MCP;
- fontes canônicas e permissões.

### Exemplos neutros

- Agente de Código;
- Agente de Pesquisa;
- Agente de Operações;
- Agente de Suporte;
- Orquestrador de Workflows.

A implementação canônica de skills, políticas e templates compartilhados continua no GitHub do Agent OS.

## 04 — Operação e Governança

### Finalidade

Organizar como o sistema é mantido, revisado e evoluído com rastreabilidade.

### Conteúdo esperado

- registro cronológico opcional de atividades ou sessões;
- decisões transversais;
- processos e runbooks;
- incidentes, causas, correções e prevenção;
- procedimentos consolidados de deploy, rollback, backup e recuperação;
- integrações implantadas;
- publicações do Cérebro para GitHub;
- ciclos de revisão;
- responsáveis, papéis e permissões;
- itens que precisam de atualização.

### Diferença entre registro cronológico e memória

- **Registro de atividades:** relata o que aconteceu em ordem temporal.
- **Biblioteca de Markdowns:** consolida conhecimento temático, curado e reutilizável.

Quando uma sessão revelar um processo ou aprendizado durável, ele deve ser consolidado na Biblioteca.

## 05 — Laboratório

### Finalidade

Separar exploração de conhecimento aprovado e operação ativa.

### Conteúdo esperado

- hipóteses;
- experimentos;
- protótipos;
- testes de modelos, RAG e embeddings;
- propostas de schema;
- integrações futuras;
- automações em validação;
- rascunhos de skills, políticas e processos.

Itens desta área não orientam operação automaticamente. Depois de evidência e revisão, podem ser promovidos para uso ativo.

## Modelo de navegação

A navegação deve começar por views orientadas a intenção:

- `Começar um projeto`;
- `Retomar projeto ativo`;
- `Encontrar conhecimento liberado`;
- `Revisar decisões pendentes`;
- `Publicar no GitHub`;
- `Consultar skills e políticas`;
- `Revisar memória desatualizada`.

Evite uma home composta apenas por dezenas de links sem contexto.

## Camadas de contexto

1. **Entrada:** START HERE do Cérebro.
2. **Orientação:** registro do projeto.
3. **Memória:** Markdowns liberados e diretamente relacionados.
4. **Conhecimento:** decisões e pesquisas relacionadas.
5. **Operação:** GitHub e START HERE do repositório.
6. **Estado temporário:** issue, branch, PR e handoff.

Essa ordem reduz contexto excessivo e mantém a informação próxima de sua fonte correta.

## O que não deve ser duplicado no Cérebro

- código-fonte;
- arquivos completos de configuração;
- comandos que mudam frequentemente;
- runbooks extensos de deploy já versionados;
- conteúdo integral de issues e pull requests;
- logs de execução;
- credenciais;
- cópias manuais de políticas e skills canônicas;
- nomes, IDs, URLs ou registros de outro workspace usados como exemplo público.

Use links, relações, resumos aprovados e metadados de origem.

## Evolução do workspace

Comece com poucos bancos e views. Adicione novos componentes somente quando houver:

- volume recorrente;
- responsável definido;
- necessidade real de relações ou filtros;
- regra de arquivamento;
- fonte canônica inequívoca.

A arquitetura deve crescer a partir do uso, não da tentativa de prever todos os cenários.

## Sanitização para compartilhamento

Antes de exportar templates, capturas ou exemplos:

1. substitua nomes reais por placeholders;
2. remova URLs e IDs privados;
3. remova clientes, produtos e agentes internos;
4. confirme que nenhum conteúdo da Biblioteca foi copiado;
5. revise `docs/governance/PUBLIC-SANITIZATION.md`.
