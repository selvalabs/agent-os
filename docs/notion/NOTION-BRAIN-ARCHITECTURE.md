# Arquitetura de um Cérebro editorial

## Princípio

O Cérebro organiza contexto humano e agentic-first sem misturar entidades, documentação operacional e memória de sessões.

A regra central é:

```text
projetos vivem em Projetos
operação específica vive no GitHub
estado temporário vive em issues, PRs e handoffs
memória reutilizável vive na Biblioteca de Markdowns
```

## Estrutura recomendada

```text
Cérebro
├── START HERE
├── 01 — Conhecimento
│   ├── Formação e estudos
│   ├── Pesquisas
│   ├── Referências e fontes
│   └── Sínteses e glossários
├── 02 — Projetos e Produtos
│   ├── Banco Projetos
│   ├── Projetos ativos
│   ├── Incubação
│   ├── Manutenção
│   └── Arquivados
├── 03 — Sistema de Agentes
│   ├── Agentes e ferramentas
│   ├── Permissões e limites
│   ├── Skills, políticas e prompts
│   └── Integrações MCP
├── 04 — Operação e Governança
│   ├── Decisões transversais
│   ├── Revisões
│   ├── Publicações
│   └── Registro opcional de sessões
├── 05 — Laboratório
│   ├── Hipóteses
│   ├── Experimentos
│   └── Protótipos
└── Biblioteca de Markdowns
    ├── Memória ativa
    ├── Sínteses de sessões
    ├── Memória transversal
    ├── Por agente ou ferramenta
    └── Revisar
```

## START HERE

A entrada do Cérebro deve explicar:

- onde os projetos são registrados;
- quando seguir para o GitHub;
- quando consultar a Biblioteca;
- onde ficam estado temporário e decisões;
- quais conteúdos não devem ser duplicados.

## 01 — Conhecimento

### Finalidade

Organizar conteúdo editorial usado para compreender domínios e problemas.

### Conteúdo

- estudos;
- pesquisas;
- fontes;
- sínteses;
- glossários;
- conhecimento de domínio.

Conhecimento pode se relacionar com projetos, mas não deve ser tratado como memória de sessão apenas por ter sido usado em um projeto.

## 02 — Projetos e Produtos

### Finalidade

Ser o catálogo canônico dos projetos e produtos.

### Registro mínimo

```text
Nome
Slug
Estado
Tipo
Finalidade
Público ou usuários
Resultado esperado
Responsável
Stack resumida
Repositório
START HERE
Arquitetura
Ambientes
Acesso de agentes
Decisões relacionadas
Fontes relacionadas
Última revisão
```

### Regra

A página do projeto deve ser suficiente para encontrar seu contexto e seguir para suas fontes canônicas.

Ela não depende da Biblioteca de Markdowns e não precisa possuir uma view da Biblioteca.

### Contexto específico

- código, arquitetura, testes e deploy → GitHub;
- pendências e mudanças → issues e PRs;
- continuidade → `HANDOFF.md`;
- decisões do projeto → página de projeto, ADR ou GitHub;
- conhecimento relacionado → área 01 ou banco de Fontes.

## 03 — Sistema de Agentes

### Finalidade

Organizar agentes, modelos, ferramentas e integrações.

### Conteúdo

- responsabilidades;
- permissões;
- limites;
- compatibilidade;
- MCPs;
- catálogo de skills, políticas e prompts;
- links para implementações canônicas.

Memórias sobre comportamento recorrente de agentes podem ir para a Biblioteca quando forem globais ou úteis em sessões futuras.

## 04 — Operação e Governança

### Finalidade

Organizar manutenção e evolução do sistema.

### Conteúdo

- decisões transversais;
- revisões periódicas;
- responsáveis e permissões;
- publicação Cérebro → GitHub;
- regras de retenção;
- registro cronológico opcional de sessões.

### Sessão versus memória

- **Registro de sessão:** sequência cronológica do que ocorreu.
- **Biblioteca:** síntese selecionada e reutilizável.

Uma sessão não deve ser copiada integralmente para a Biblioteca.

## 05 — Laboratório

### Finalidade

Separar exploração de conteúdo aprovado.

Depois de um experimento, classifique o resultado:

| Resultado | Destino |
|---|---|
| Implementação de um projeto | GitHub do projeto |
| Novo projeto ou produto | Banco Projetos |
| Conhecimento editorial | Área 01 |
| Memória global ou transversal | Biblioteca |
| Skill ou política compartilhada | Agent OS |

## Biblioteca de Markdowns

### Finalidade

Ser um repositório de memória durável para agentes e sessões futuras.

### O que registra

- sínteses relevantes de conversas ou sessões;
- decisões globais;
- preferências operacionais estáveis;
- aprendizados transversais;
- padrões recorrentes entre projetos;
- contexto sobre agentes, ferramentas e integrações;
- regras agentic-first que não pertencem a um único projeto.

### O que não registra

- projetos;
- cadastro de produtos;
- documentação técnica completa de um projeto;
- estado atual de uma tarefa;
- conteúdo integral de issues e PRs;
- logs;
- transcrições completas;
- segredos.

### Projeto de origem

Uma memória pode possuir uma relação opcional com um projeto para indicar onde foi descoberta. Essa relação não torna o projeto dependente da Biblioteca.

## Camadas de contexto

1. `START HERE` do Cérebro.
2. Registro do projeto, quando houver projeto.
3. Conhecimento, decisões e fontes relacionadas.
4. GitHub e `START HERE` do repositório.
5. Issue, branch, PR e handoff atuais.
6. Biblioteca apenas quando memória global ou de sessão for útil.

A Biblioteca não deve ser consultada automaticamente em toda tarefa.

## Matriz de classificação

| Pergunta | Destino |
|---|---|
| Isso define ou descreve um projeto? | Projetos e Produtos |
| É implementação específica? | GitHub |
| É estado temporário? | Issue, PR ou handoff |
| É conhecimento editorial? | Conhecimento |
| É uma decisão transversal? | Governança/Decisões |
| Precisa sobreviver a sessões e orientar agentes globalmente? | Biblioteca |
| Ainda é hipótese? | Laboratório |

## Não duplicar

- projetos na Biblioteca;
- código no Notion;
- handoffs na Biblioteca;
- runbooks específicos já versionados;
- transcrições de sessões;
- dados privados em exemplos públicos.

Use relações e links para conectar as estruturas sem fundi-las.
