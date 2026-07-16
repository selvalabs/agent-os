# Biblioteca de Markdowns — memória durável dos agentes

## Papel na arquitetura

A **Biblioteca de Markdowns** é um modelo recomendado de memória durável e curada para ambientes agentic-first.

Cada pessoa ou equipe cria sua própria biblioteca. Este repositório fornece estrutura, campos e processos genéricos; não contém linhas, opções, IDs ou conteúdo de uma biblioteca real.

A Biblioteca guarda conhecimento que precisa sobreviver a conversas, sessões, modelos, ferramentas e mudanças de operador. Agentes podem consultá-la para recuperar processos, decisões, políticas, integrações, runbooks, incidentes resolvidos e aprendizados relevantes.

A Biblioteca não substitui:

- o GitHub como fonte canônica de código, arquitetura e operação específica;
- issues e pull requests como histórico da mudança;
- `HANDOFF.md` como estado temporário de uma frente;
- um registro cronológico opcional de atividades;
- um gerenciador de segredos;
- índices, embeddings ou RAG derivados.

## Regra de memory write-back

Ao concluir uma ação relevante, o agente ou responsável deve avaliar se existe memória reutilizável.

Quando houver, deve criar um novo documento ou atualizar um documento existente na Biblioteca de Markdowns do usuário.

```text
issue ou solicitação
→ execução e validação
→ PR, commit ou resultado verificável
→ avaliação de memória
→ criar ou atualizar Markdown
→ preencher origem, projeto, agentes, versão e revisão
→ revisão humana
→ liberação para uso
→ indexação ou RAG derivado, quando aplicável
```

Uma tarefa que descobriu ou alterou um processo relevante não está completamente encerrada enquanto a memória durável correspondente não tiver sido registrada ou explicitamente considerada desnecessária.

## O que deve ser registrado

Crie ou atualize um Markdown quando ocorrer pelo menos um dos seguintes casos:

- criação ou mudança de processo reutilizável;
- instalação ou configuração que precisará ser repetida;
- procedimento de deploy, rollback, backup ou recuperação;
- incidente relevante, causa identificada e solução validada;
- decisão arquitetural ou operacional que afeta trabalhos futuros;
- nova integração, API, MCP, serviço externo ou fluxo de autenticação;
- nova política de segurança, permissão ou proteção;
- comportamento recorrente de agente que precisa de orientação;
- sequência de diagnóstico que resolveu problema não trivial;
- migração de dados, infraestrutura ou versão;
- mudança importante de operação em produção;
- aprendizado que evita repetição de erro ou retrabalho;
- ação que alterou permanentemente o estado de um projeto e exige contexto futuro.

## O que não deve virar memória durável

Não crie um item apenas para registrar:

- conversa completa ou transcrição bruta;
- cada comando executado sem valor reutilizável;
- tentativa temporária que não produziu aprendizado;
- ajuste visual ou textual trivial;
- log bruto de terminal;
- conteúdo já documentado corretamente, sem mudança;
- segredo, token, senha, cookie ou chave;
- estado temporário que pertence ao `HANDOFF.md`;
- detalhes voláteis já canônicos no GitHub;
- conteúdo privado de outro workspace usado como exemplo.

Quando uma ação não merece novo documento, mas altera um processo existente, atualize o Markdown já liberado e incremente sua versão.

## Critério de relevância

Antes de encerrar uma tarefa, responda:

1. outra pessoa ou agente precisará repetir isso?
2. a informação reduz risco, tempo ou ambiguidade no futuro?
3. houve decisão, processo, incidente ou integração relevante?
4. o resultado continuará válido depois desta sessão?
5. a ausência desse registro pode provocar retrabalho ou erro?

Se qualquer resposta for **sim**, existe um gatilho de memória.

## Schema recomendado

Os campos abaixo são recomendações adaptáveis. O usuário define suas próprias opções de projetos, agentes, tags e estados.

| Campo | Uso recomendado |
|---|---|
| Documento | título humano e específico |
| Slug | identificador estável em minúsculas, sem acentos e com hífens |
| Status | ciclo editorial do documento |
| Tipo | natureza do conteúdo |
| Formato | Markdown, MDX, YAML ou Texto |
| Projetos | projetos aos quais a memória se aplica |
| Agentes | agentes ou ferramentas que devem consultá-la |
| Tags | descoberta e recuperação semântica |
| Prioridade | impacto operacional e ordem de revisão |
| Fonte | origem externa, quando existir |
| GitHub | repositório, issue, PR, commit ou arquivo relacionado |
| Versão | versão editorial do documento |
| Última revisão | data da última validação humana |
| Hash de conteúdo | rastreabilidade para sincronização e índice derivado |
| Notas | limitações, observações e escopo adicional |
| Referência derivada | ID opcional em banco, índice ou RAG |

### Exemplo fictício

```text
Documento: Processo — Publicar uma mudança segura
Slug: processo-publicar-mudanca-segura
Status: Rascunho
Tipo: Processo
Projetos: Projeto Exemplo
Agentes: Agente de Código
Tags: github, ci, governança
GitHub: https://github.com/example-org/example-repo/pull/1
Versão: 1
```

## Tipos de memória recomendados

A propriedade `Tipo` pode distinguir:

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

Adapte a lista ao seu ambiente. Não copie opções internas de outro workspace.

## Ciclo editorial recomendado

### Inbox

Material capturado, ainda sem triagem. Não orienta operação automática.

### Rascunho

Documento em construção. Pode ser consultado como contexto, mas não como regra aprovada.

### Ativo ou Aprovado

Documento revisado, aplicável e liberado para uso por agentes dentro do escopo indicado.

### Revisar

Documento possivelmente desatualizado, incompleto ou em conflito. Não deve ser aplicado automaticamente sem validação.

### Arquivado

Documento preservado para histórico, mas removido dos fluxos ativos.

O usuário pode renomear os estados, desde que o significado e as permissões sejam inequívocos.

## Estrutura mínima do corpo

Todo registro operacional deve conter:

```text
Resumo
Quando consultar
Contexto
Processo ou decisão
Entradas necessárias
Passos ou regras
Validação
Resultado esperado
Riscos e limites
Origem verificável
Projetos e agentes aplicáveis
Histórico de versões
```

Para incidentes, acrescente:

```text
Sintoma
Impacto
Causa raiz
Diagnóstico
Correção
Validação
Prevenção
```

## Origem e rastreabilidade

Quando possível, relacione o documento a:

- issue;
- pull request;
- commit;
- tag ou release;
- arquivo canônico;
- fonte externa;
- data da validação;
- responsável pela revisão.

Não copie o conteúdo integral da issue ou PR. Registre a síntese e a origem.

## Views recomendadas

- `Memória liberada` — status ativo ou aprovado;
- `Rascunhos` — conteúdo em criação;
- `Precisa revisar` — revisão vencida ou status Revisar;
- `Por projeto` — agrupada por projeto;
- `Por agente` — filtrada por agente;
- `Processos e runbooks`;
- `Incidentes e aprendizados`;
- `Laboratório` — Inbox e Rascunhos experimentais.

## Leitura por agentes

Antes de usar um Markdown operacionalmente, o agente deve verificar:

1. status liberado;
2. projeto compatível;
3. agente ou ferramenta compatível;
4. origem verificável;
5. versão e data de revisão;
6. ausência de substituto mais recente;
7. inexistência de conflito com GitHub ou políticas superiores.

## Escrita por agentes

O padrão é somente leitura. Escrita exige autorização explícita e deve:

- indicar o destino;
- criar item como Inbox ou Rascunho;
- preencher metadados mínimos;
- preservar conteúdo existente;
- não promover automaticamente para ativo;
- não mover ou excluir páginas;
- não registrar segredos.

## Biblioteca e camada derivada

Um índice, banco ou RAG pode derivar conteúdo da Biblioteca para busca. A camada derivada deve registrar origem, versão e hash, mas não se torna fonte canônica.

## Sanitização para publicação

Ao compartilhar exemplos:

- use projetos e agentes fictícios;
- use `example-org/example-repo`;
- use `https://example.com`;
- remova IDs, links privados e opções reais do workspace;
- não exporte documentos reais da Biblioteca;
- consulte `docs/governance/PUBLIC-SANITIZATION.md`.
