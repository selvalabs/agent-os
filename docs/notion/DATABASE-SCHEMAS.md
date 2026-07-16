# Schemas recomendados para um Cérebro

Este documento propõe bancos, propriedades, relações e views que podem ser adaptados a qualquer workspace.

Nada aqui representa o schema real de um mantenedor. Cada pessoa ou equipe deve criar suas próprias opções de projetos, agentes, tags, estados e integrações.

## 1. Biblioteca de Markdowns

### Função

Memória durável, curada e reutilizável para humanos, agentes, automações e futuras camadas de RAG.

### Propriedades recomendadas

| Propriedade | Tipo sugerido | Uso |
|---|---|---|
| Documento | Title | título humano e específico |
| ID | Unique ID | identificador interno estável |
| Slug | Text | identificador sem acentos e com hífens |
| Status | Select/Status | Inbox, Rascunho, Ativo, Revisar, Arquivado |
| Tipo | Select | natureza do documento |
| Formato | Select | Markdown, MDX, YAML ou Texto |
| Projetos | Multi-select ou Relation | projetos aos quais se aplica |
| Agentes | Multi-select ou Relation | agentes e ferramentas consumidores |
| Tags | Multi-select | descoberta temática e semântica |
| Prioridade | Select | Alta, Média ou Baixa |
| Fonte | URL | origem externa, quando houver |
| GitHub | URL | repositório, issue, PR, commit ou arquivo relacionado |
| Versão | Number | versão editorial |
| Última revisão | Date | última validação humana |
| Hash de conteúdo | Text | rastreabilidade para sync ou índice derivado |
| Notas | Text | limites, escopo e observações |
| Referência derivada | Text | ID opcional em banco, índice ou RAG |
| Criado | Created time | criação do registro |
| Editado | Last edited time | última edição |

### Tipos recomendados

- Manual;
- Processo;
- Runbook;
- Decisão;
- Política;
- Skill;
- Prompt;
- Template;
- Pesquisa;
- Integração;
- Incidente;
- Aprendizado;
- Handoff consolidado.

Adapte as opções ao seu ambiente. Mudanças de schema devem passar por issue e revisão quando afetarem agentes ou automações.

### Views mínimas

- `Memória ativa` — Status = Ativo;
- `Inbox` — Status = Inbox;
- `Rascunhos` — Status = Rascunho;
- `Revisar` — Status = Revisar;
- `Arquivados` — Status = Arquivado;
- `Por projeto` — agrupada por Projetos;
- `Por agente` — agrupada por Agentes;
- `Alta prioridade` — Prioridade = Alta;
- `Sem origem` — Fonte e GitHub vazios;
- `Revisão vencida` — Última revisão ausente ou vencida.

### Views vinculadas por área

| Área | Filtros principais |
|---|---|
| 01 — Conhecimento | Pesquisa, Manual ou Aprendizado; status liberado |
| 02 — Projetos | projeto atual; excluir arquivados por padrão |
| 03 — Sistema de Agentes | agente atual ou tipos Skill, Política, Prompt e Template |
| 04 — Operação e Governança | Processo, Runbook, Decisão, Integração e Incidente |
| 05 — Laboratório | Inbox, Rascunho e tags de experimento |

### Exemplo fictício

```text
Documento: Manual — Preparar uma release segura
Status: Rascunho
Tipo: Manual
Projetos: Projeto Exemplo
Agentes: Agente de Código
GitHub: https://github.com/example-org/example-repo/pull/1
Versão: 1
```

## 2. Projetos

Registro transversal de produtos, sistemas, estudos aplicados e repositórios.

### Propriedades recomendadas

| Propriedade | Tipo sugerido | Uso |
|---|---|---|
| Nome | Title | nome humano do projeto |
| Slug | Text | identificador estável |
| Estado | Select | Incubação, Ativo, Manutenção, Pausado, Arquivado |
| Tipo | Select | Produto, Biblioteca, Infraestrutura, Estudo, Cliente, Laboratório |
| Responsável | Person/Text | responsável humano |
| Repositório | URL | GitHub canônico |
| START HERE | URL | entrada operacional do repositório |
| Arquitetura | URL | documento canônico no GitHub |
| Handoff | URL | estado temporário da frente |
| Acesso de agentes | Select | Sem acesso, Leitura, Escrita revisada, Operação autorizada |
| Última revisão | Date | revisão humana mais recente |
| Biblioteca | Relation ou linked view | memória relacionada ao projeto |
| Decisões | Relation | decisões relacionadas |
| Fontes | Relation | fontes relacionadas |

### Views mínimas

- `Projetos ativos`;
- `Precisam de revisão`;
- `Agentic-first` — START HERE e repositório preenchidos;
- `Incubação`;
- `Arquivados`.

Toda página de projeto deve incluir uma view vinculada da Biblioteca filtrada pelo projeto.

## 3. Decisões

Decisões transversais ou editoriais que precisam de rastreabilidade.

### Propriedades recomendadas

| Propriedade | Tipo sugerido | Uso |
|---|---|---|
| Decisão | Title | título curto |
| Estado | Select | Proposta, Aprovada, Rejeitada, Substituída, Arquivada |
| Escopo | Select | Organização, Projeto, Produto, Arquitetura, Editorial |
| Responsável | Person/Text | decisor ou mantenedor |
| Data | Date | data da decisão |
| Projetos | Relation | projetos afetados |
| Markdown relacionado | Relation/URL | registro consolidado na Biblioteca |
| Substitui | Relation | decisão anterior |
| Artefato operacional | URL | ADR, issue ou PR no GitHub |
| Revisar em | Date | data para reavaliação |

### Conteúdo da página

- contexto;
- problema;
- alternativas;
- decisão;
- consequências;
- artefato operacional;
- Markdown consolidado;
- critérios de revisão.

Decisões aprovadas e reutilizáveis devem gerar ou atualizar um Markdown na Biblioteca.

## 4. Fontes

Catálogo de documentos, páginas, livros, vídeos, normas, repositórios e outras origens.

### Propriedades recomendadas

| Propriedade | Tipo sugerido | Uso |
|---|---|---|
| Fonte | Title | nome legível |
| Tipo | Select | Documento, Site, Livro, Vídeo, Repositório, Norma, Dataset |
| URL | URL | localização |
| Autor/Origem | Text | autor ou organização |
| Confiabilidade | Select | Primária, Secundária, Contextual, Não verificada |
| Estado | Select | Ativa, Indisponível, Substituída, Arquivada |
| Markdowns | Relation/URL | memórias que usam a fonte |
| Projetos | Relation | projetos relacionados |
| Consultada em | Date | última consulta |
| Observações | Text | limitações e escopo |

## Componentes que podem começar sem banco próprio

### 01 — Conhecimento

Pode usar páginas, fontes e views da Biblioteca. Crie um banco separado somente quando houver volume e processo editorial que não possam ser atendidos pela Biblioteca.

### Registro de atividades

Pode permanecer como página ou banco cronológico opcional. Não substitui a Biblioteca e não precisa duplicar seu schema.

### Sistema de Agentes

Pode usar páginas de navegação e views da Biblioteca filtradas por agentes e tipo. Skills e políticas continuam canônicas no GitHub.

### Laboratório

Pode começar com páginas e views da Biblioteca em Inbox ou Rascunho. Crie banco próprio somente quando experimentos exigirem propriedades e ciclo específicos.

## Bancos opcionais

### Publicações

Crie quando o fluxo Cérebro → GitHub se tornar recorrente. Registre origem, destino, versão, hash ou commit, aprovação e estado.

### Agentes

Crie quando houver volume suficiente para relações, permissões e responsáveis que não possam ser mantidos em páginas simples.

## Relações essenciais

```text
Projetos ↔ Biblioteca de Markdowns
Projetos ↔ Decisões
Projetos ↔ Fontes
Decisões ↔ Biblioteca de Markdowns
Fontes ↔ Biblioteca de Markdowns
```

Evite relações sem uso real. Toda relação deve responder a uma pergunta concreta.

## Template de Markdown operacional

- resumo;
- quando consultar;
- contexto;
- processo, decisão ou aprendizado;
- entradas;
- passos ou regras;
- validação;
- resultado esperado;
- riscos e limites;
- origem verificável;
- projetos e agentes;
- histórico de versões.

Consulte `MARKDOWN-LIBRARY-MEMORY.md` para templates de incidente e decisão.

## Regras de qualidade

- mantenha uma única Biblioteca canônica;
- não use texto livre para dados filtrados com frequência;
- não crie relação sem view ou processo que a utilize;
- mantenha estados pequenos e definidos;
- documentos ativos precisam de origem, escopo, versão e revisão;
- use arquivamento em vez de exclusão automática;
- mudanças de schema exigem revisão;
- revise propriedades e views após os pilotos;
- use apenas exemplos fictícios em documentação pública;
- nunca publique opções reais, IDs ou linhas de um workspace privado.
