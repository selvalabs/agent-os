# START HERE — Crie o seu Cérebro

Esta é a porta de entrada para criar ou operar um Cérebro editorial dentro da arquitetura SelvaLabs Agent OS.

O Cérebro organiza projetos, conhecimento, decisões, fontes, agentes e memória reutilizável. Cada tipo de informação possui um destino próprio.

## Separação obrigatória

| Informação | Destino canônico |
|---|---|
| Projeto, produto, estado, responsável e links | `02 — Projetos e Produtos` |
| Conhecimento, pesquisa e formação | `01 — Conhecimento` |
| Agentes, ferramentas e permissões | `03 — Sistema de Agentes` |
| Governança, decisões e revisões | `04 — Operação e Governança` |
| Hipóteses e experimentos | `05 — Laboratório` |
| Memória global, transversal ou necessária entre sessões | Biblioteca de Markdowns |
| Código e operação específica | GitHub do projeto |
| Estado temporário | Issue, PR e `HANDOFF.md` |

A Biblioteca de Markdowns **não é o lugar onde os projetos são registrados**.

## Estrutura recomendada

```text
Cérebro
├── START HERE
├── 01 — Conhecimento
├── 02 — Projetos e Produtos
│   └── Banco Projetos
├── 03 — Sistema de Agentes
├── 04 — Operação e Governança
├── 05 — Laboratório
└── Biblioteca de Markdowns
```

A Biblioteca fica na raiz por ser transversal. Ela não precisa aparecer dentro de cada página de projeto.

## 01 — Conhecimento

Use para:

- formação e estudos;
- pesquisas;
- fontes e referências;
- sínteses e glossários;
- conhecimento de domínio.

Conhecimento específico pode ser relacionado a um projeto, mas continua sendo conhecimento, não memória de sessão.

## 02 — Projetos e Produtos

Este é o catálogo canônico dos projetos.

Cada projeto deve registrar:

- nome e finalidade;
- estado e responsável;
- usuários ou público;
- resultado esperado;
- stack resumida;
- repositório canônico;
- `START-HERE.md`;
- arquitetura;
- ambientes;
- acessos permitidos aos agentes;
- decisões e fontes relacionadas;
- última revisão.

A página do projeto serve como mapa. Código, testes, deploy, runbooks técnicos e detalhes operacionais ficam no GitHub.

### Relação opcional com a Biblioteca

Uma memória da Biblioteca pode mencionar o projeto em que surgiu. Essa relação indica apenas:

- origem;
- exemplo de aplicação;
- escopo opcional.

Ela não transforma a Biblioteca em documentação do projeto.

## 03 — Sistema de Agentes

Use para:

- agentes, modelos e ferramentas;
- funções, permissões e limites;
- integrações MCP;
- repositórios preparados pelo Agent OS;
- catálogo e links para políticas, skills, prompts e templates.

A implementação canônica das políticas e skills compartilhadas permanece no GitHub do Agent OS.

## 04 — Operação e Governança

Use para:

- decisões transversais;
- responsáveis e permissões;
- revisões periódicas;
- publicações Cérebro → GitHub;
- registro cronológico opcional de sessões ou atividades;
- regras de retenção e arquivamento.

O registro cronológico conta o que aconteceu. A Biblioteca recebe apenas a síntese reutilizável que precisa sobreviver à sessão.

## 05 — Laboratório

Use para hipóteses, experimentos, protótipos e propostas ainda não aprovadas.

Um experimento não deve virar memória ativa automaticamente. Depois de validação, classifique o resultado:

- específico de projeto → projeto ou GitHub;
- conhecimento editorial → área 01;
- regra ou aprendizado global → Biblioteca;
- política ou skill compartilhada → Agent OS.

## Biblioteca de Markdowns

A Biblioteca é memória para agentes, não catálogo de projetos.

Ela registra principalmente:

- sínteses relevantes de sessões do ChatGPT;
- decisões globais que precisam ser recuperadas depois;
- preferências operacionais estáveis;
- aprendizados transversais;
- contexto sobre agentes, ferramentas e integrações;
- padrões recorrentes entre projetos;
- regras de uso agentic-first não pertencentes a um único repositório.

Não registre:

- cadastro ou documentação completa de projeto;
- código e arquitetura específica;
- status atual de branch, PR ou deploy;
- conversa completa;
- log bruto;
- ajustes triviais;
- segredos.

## Fluxo de consulta

```text
pedido atual
→ START HERE do Cérebro
→ identificar projeto, domínio e agente
→ abrir o registro do projeto quando aplicável
→ consultar GitHub para contexto específico
→ consultar Biblioteca somente se houver memória global ou de sessão relevante
→ executar usando as fontes canônicas
```

A consulta à Biblioteca não é obrigatória para toda tarefa.

## Fluxo de write-back

```text
sessão ou trabalho concluído
→ validar o resultado
→ classificar o conteúdo
   projeto → página do projeto
   operação específica → GitHub
   estado temporário → issue, PR ou HANDOFF
   conhecimento → área 01
   memória global/transversal → Biblioteca
→ revisar antes de liberar
```

## Schema mínimo recomendado

### Projetos

- Nome;
- Slug;
- Estado;
- Tipo;
- Responsável;
- Repositório;
- START HERE;
- Arquitetura;
- Ambientes;
- Acesso de agentes;
- Decisões;
- Fontes;
- Última revisão.

### Biblioteca

- Documento;
- Slug;
- Status;
- Tipo de memória;
- Escopo;
- Agentes ou ferramentas;
- Tags;
- Sessão ou fonte de origem;
- Projeto de origem opcional;
- GitHub opcional;
- Versão;
- Última revisão;
- Notas.

## Checklist

- [ ] existe `Cérebro/START HERE`;
- [ ] projetos vivem no banco Projetos;
- [ ] a Biblioteca não contém cadastros de projetos;
- [ ] GitHub permanece canônico para operação específica;
- [ ] estado temporário usa issue, PR e handoff;
- [ ] a Biblioteca recebe somente memória global, transversal ou de sessão relevante;
- [ ] integrações começam em leitura;
- [ ] exemplos públicos são fictícios;
- [ ] segredos não entram em Markdown.
