# SelvaLabs Agent OS

Base reutilizável para preparar repositórios e workspaces **agentic-first** com navegação clara, contexto seletivo, políticas, skills, bootstrap seguro e validação em CI.

## Comece aqui

- [`START-HERE.md`](START-HERE.md) — rota mínima para humanos e agentes;
- [`docs/notion/START-HERE.md`](docs/notion/START-HERE.md) — implementação de um Cérebro próprio;
- [`docs/notion/NOTION-BRAIN-ARCHITECTURE.md`](docs/notion/NOTION-BRAIN-ARCHITECTURE.md) — conteúdo das áreas `01` a `05`;
- [`docs/notion/MARKDOWN-LIBRARY-MEMORY.md`](docs/notion/MARKDOWN-LIBRARY-MEMORY.md) — memória global, transversal e de sessões;
- [`docs/notion/DATABASE-SCHEMAS.md`](docs/notion/DATABASE-SCHEMAS.md) — schemas recomendados;
- [`docs/governance/PUBLIC-SANITIZATION.md`](docs/governance/PUBLIC-SANITIZATION.md) — proteção contra exposição de contexto privado.

## Separação fundamental

O Agent OS distingue quatro tipos de contexto:

| Contexto | Fonte canônica |
|---|---|
| Projeto, produto, responsáveis, estado e links | `02 — Projetos e Produtos` no Cérebro |
| Código, arquitetura, testes, deploy e operação específica | GitHub do projeto |
| Issue, branch, PR, pendências e continuidade | GitHub e `HANDOFF.md` |
| Memória global, transversal ou necessária entre sessões | Biblioteca de Markdowns |

A **Biblioteca de Markdowns não é um catálogo de projetos** e não substitui a página própria de cada projeto.

## Cérebro editorial

A estrutura recomendada é:

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

### Projetos e Produtos

Cada projeto possui registro próprio com finalidade, estado, responsável, repositório, START HERE, arquitetura, ambientes, acessos, decisões e fontes relacionadas.

O projeto não deve ser montado dentro da Biblioteca. Seu contexto específico permanece na página do projeto e no GitHub correspondente.

### Biblioteca de Markdowns

A Biblioteca é um repositório de memória para agentes. Ela registra sínteses que precisam sobreviver a conversas, sessões, modelos e ferramentas, por exemplo:

- síntese relevante de uma sessão do ChatGPT;
- regra global de uso agentic-first;
- aprendizado transversal aplicável a mais de um projeto;
- preferência operacional estável;
- contexto sobre agentes, ferramentas ou integrações que será reutilizado;
- decisão global que precisa ser recuperada em sessões futuras;
- padrão recorrente identificado em diferentes trabalhos.

Não devem ir para a Biblioteca:

- o cadastro ou a documentação completa de um projeto;
- código, arquitetura ou runbook específico já versionado no GitHub;
- estado atual de branch, PR ou deploy;
- conversa completa ou log bruto;
- ajustes triviais;
- segredos.

Uma memória pode apontar opcionalmente para o projeto em que surgiu, mas essa relação indica apenas **origem ou aplicabilidade**.

## Memory write-back

```text
sessão ou trabalho relevante
→ resultado validado
→ classificar o destino correto
   projeto específico → página do projeto ou GitHub
   estado temporário → issue, PR ou HANDOFF
   memória global/transversal → Biblioteca de Markdowns
→ revisão humana
→ liberação para consulta futura
```

## Estrutura do repositório

```text
agent-os/
├── START-HERE.md
├── AGENTS.md
├── policies/
├── skills/
├── templates/repository/
├── compatibility/
├── docs/
├── manifests/
├── schemas/
├── scripts/
└── .github/workflows/
```

## Uso inicial

Validar o Agent OS:

```bash
python scripts/validate_agent_os.py .
```

Preparar um repositório sem sobrescrever arquivos existentes:

```bash
python scripts/bootstrap_repo.py \
  --target /caminho/do/repositorio \
  --project-name "Projeto Exemplo" \
  --repo-slug "projeto-exemplo" \
  --dry-run
```

## Princípios

- todo espaço possui um `START HERE` visível;
- contexto é recuperado seletivamente;
- projetos e memória global são estruturas distintas;
- GitHub permanece canônico para operação específica;
- integrações externas começam em leitura;
- regras críticas recebem enforcement técnico;
- exemplos públicos são fictícios;
- segredos nunca entram em Markdown.

## Privacidade e publicação

Este repositório ensina cada usuário a criar o próprio Cérebro. Não publique nomes, URLs, IDs, projetos, agentes ou conteúdo de um workspace real.

Não torne público diretamente um repositório privado que possua histórico interno. Gere um snapshot sanitizado e publique-o em um repositório novo com **histórico limpo ou histórico novo**, sem migrar issues e pull requests privados.
