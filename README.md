# SelvaLabs Agent OS

Base reutilizável para preparar novos repositórios para construção e manutenção **agentic-first**, sem transformar `README.md` ou `AGENTS.md` em documentação extensa de máquina.

O Agent OS reúne políticas, skills, templates, bootstrap, validações, handoffs e regras de segurança compartilhadas para operar múltiplos projetos com agentes de forma auditável e reversível.

## Comece aqui

- [`START-HERE.md`](START-HERE.md) — rota mínima para humanos e agentes;
- [`docs/notion/START-HERE.md`](docs/notion/START-HERE.md) — implementação de um Cérebro próprio;
- [`docs/notion/NOTION-BRAIN-ARCHITECTURE.md`](docs/notion/NOTION-BRAIN-ARCHITECTURE.md) — conteúdo recomendado das áreas `01` a `05`;
- [`docs/notion/MARKDOWN-LIBRARY-MEMORY.md`](docs/notion/MARKDOWN-LIBRARY-MEMORY.md) — memória durável e write-back;
- [`docs/governance/PUBLIC-SANITIZATION.md`](docs/governance/PUBLIC-SANITIZATION.md) — proteção contra exposição de workspaces reais;
- [`templates/repository/START-HERE.md`](templates/repository/START-HERE.md) — entrada incluída em novos repositórios.

**Regra:** todo novo repositório e toda raiz de conhecimento preparada pelo Agent OS deve possuir um `START HERE` curto, visível e atualizado.

## Objetivo

Separar cinco responsabilidades:

1. **Cérebro editorial** — conhecimento, curadoria, pesquisa, memória durável e governança;
2. **Repositório do projeto** — código, arquitetura, testes e verdade operacional;
3. **Agent OS** — políticas, skills, templates e validações compartilhadas;
4. **Camada derivada** — busca, índices, embeddings, RAG e rastreabilidade;
5. **Enforcement técnico** — CI, hooks, permissões, sandbox e revisão humana.

## Crie o seu próprio Cérebro

Este repositório não contém o workspace pessoal de nenhum mantenedor. Ele ensina um modelo adaptável para que cada pessoa ou equipe crie a própria estrutura.

A documentação cobre:

- START HERE e navegação seletiva;
- áreas `01` a `05`;
- Biblioteca de Markdowns;
- schemas e views recomendados;
- consulta por MCP em modo de leitura inicial;
- governança e publicação para GitHub;
- memory write-back depois de processos relevantes.

O pacote em `docs/notion-import/` contém páginas genéricas e placeholders. Substitua os exemplos antes de usar.

## Biblioteca de Markdowns

A arquitetura recomenda que o usuário crie uma **Biblioteca de Markdowns** como memória durável e curada.

Ela pode registrar processos reutilizáveis, decisões, políticas, integrações, runbooks, incidentes resolvidos, pesquisas, templates e aprendizados relevantes.

```text
trabalho relevante
→ validação
→ issue, PR, commit ou resultado verificável
→ avaliação de memória
→ criar ou atualizar Markdown
→ revisão humana
→ status liberado para uso
```

As áreas do Cérebro devem usar views vinculadas da mesma biblioteca, evitando bancos paralelos e cópias manuais.

## Estrutura recomendada do Cérebro

```text
Cérebro
├── START HERE
├── Biblioteca de Markdowns
├── 01 — Conhecimento
│   estudos, pesquisas, fontes, sínteses e conhecimento de domínio
├── 02 — Projetos e Produtos
│   catálogo, responsáveis, repositórios e memória por projeto
├── 03 — Sistema de Agentes
│   agentes, skills, políticas, prompts, templates e integrações
├── 04 — Operação e Governança
│   decisões, processos, incidentes, publicações e revisões
└── 05 — Laboratório
    hipóteses, experimentos, protótipos e rascunhos
```

Consulte `docs/notion/NOTION-BRAIN-ARCHITECTURE.md` para a composição completa.

## Princípio central

Documentação que orienta agentes não substitui controles técnicos. Regras críticas também devem ser protegidas por permissões, CI, hooks, sandbox e revisão humana.

O agente recebe uma rota de navegação e recupera somente o contexto necessário. Ele não deve carregar automaticamente todo o workspace, toda a biblioteca ou todos os projetos.

## Estrutura do repositório

```text
selvalabs-agent-os/
├── START-HERE.md
├── AGENTS.md
├── policies/
├── skills/
├── templates/repository/
├── compatibility/
├── docs/
│   ├── notion/
│   ├── notion-import/
│   └── governance/
├── manifests/
├── schemas/
├── scripts/
└── .github/workflows/
```

## Uso inicial

### 1. Validar o Agent OS

```bash
python scripts/validate_agent_os.py .
```

### 2. Preparar um repositório piloto

O bootstrap preserva arquivos existentes por padrão.

```bash
python scripts/bootstrap_repo.py \
  --target /caminho/do/repositorio \
  --project-name "Projeto Exemplo" \
  --repo-slug "projeto-exemplo" \
  --dry-run
```

Depois de revisar:

```bash
python scripts/bootstrap_repo.py \
  --target /caminho/do/repositorio \
  --project-name "Projeto Exemplo" \
  --repo-slug "projeto-exemplo"
```

### 3. Implementar um Cérebro próprio

1. leia `docs/notion/START-HERE.md`;
2. crie uma página raiz com `START HERE` visível;
3. crie ou adapte uma Biblioteca de Markdowns;
4. organize `01` a `05` com views vinculadas;
5. registre projetos usando campos próprios;
6. mantenha integrações MCP em leitura até autorização explícita de escrita.

## Fontes canônicas

| Conteúdo | Fonte canônica |
|---|---|
| Memória durável e reutilizável | Biblioteca de Markdowns criada pelo usuário |
| Pesquisa e curadoria | Cérebro editorial do usuário |
| Catálogo transversal de projetos | Cérebro editorial do usuário |
| Código, arquitetura, testes e deploy | GitHub do projeto |
| Estado temporário | Issue, PR e `HANDOFF.md` |
| Registro cronológico opcional | Registro de atividades ou sessões |
| Políticas e skills compartilhadas | SelvaLabs Agent OS |
| Índices, embeddings e consultas rápidas | Camada derivada |
| Segredos | Gerenciador de segredos; nunca Markdown |

## Fluxo para agentes

```text
pedido atual
→ START HERE do Cérebro
→ registro do projeto
→ Markdowns liberados e relevantes
→ START HERE do repositório
→ issue e branch
→ implementação e validação
→ pull request
→ handoff quando necessário
→ avaliação e registro de memória
```

## Pilotos recomendados

1. **Domínio de conhecimento** — testar curadoria, fontes, revisão e memória;
2. **Projeto de software controlado** — testar START HERE, segurança, handoff, memória e CI;
3. **Operação autorizada** — testar deploy e rollback somente após os dois primeiros pilotos.

## Privacidade e publicação

Exemplos públicos devem ser fictícios. Não inclua nomes reais de clientes, projetos privados, agentes internos, páginas, URLs, IDs ou registros de um workspace particular.

**Não torne público diretamente um repositório privado que já possua histórico, issues ou pull requests com contexto interno.** Gere um snapshot sanitizado e publique-o em um repositório novo, com **histórico limpo ou histórico novo**, sem migrar discussões privadas.

Consulte `docs/governance/PUBLIC-SANITIZATION.md` antes de preparar uma release pública.

## Estado do pacote

Versão inicial de arquitetura e bootstrap. Antes da adoção ampla, execute pilotos, registre aprendizados reutilizáveis e ajuste skills e templates com base em evidências.
