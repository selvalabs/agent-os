# Biblioteca de Markdowns — memória global e de sessões

## Papel na arquitetura

A Biblioteca de Markdowns é um repositório de memória durável para agentes.

Seu objetivo é preservar sínteses que precisam ser recuperadas em conversas ou sessões futuras, independentemente da ferramenta, modelo ou operador utilizado.

A Biblioteca não registra projetos e não substitui:

- o banco `Projetos` no Cérebro;
- a página própria de cada projeto;
- o GitHub como fonte de código e operação específica;
- issues e pull requests;
- `HANDOFF.md`;
- bancos de conhecimento, fontes ou decisões;
- um gerenciador de segredos.

## Pergunta principal

Antes de criar um Markdown, pergunte:

> Esta informação precisa ser lembrada por agentes em sessões futuras e possui valor global, transversal ou recorrente?

Se a resposta for não, use outro destino.

## Classificação de destino

| Conteúdo | Destino correto |
|---|---|
| Cadastro, estado e links de um projeto | Banco Projetos |
| Código, arquitetura e operação específica | GitHub do projeto |
| Mudança em andamento | Issue ou PR |
| Continuidade de uma frente | `HANDOFF.md` |
| Pesquisa e conhecimento editorial | Área 01 |
| Decisão transversal formal | Banco Decisões |
| Memória global, transversal ou entre sessões | Biblioteca |
| Hipótese ainda não validada | Laboratório |

## O que deve ser registrado

A Biblioteca pode receber:

- síntese de uma sessão do ChatGPT com valor futuro;
- contexto global que o agente deve recuperar em outras conversas;
- preferência operacional estável;
- regra de colaboração entre humanos e agentes;
- padrão recorrente observado em diferentes projetos;
- aprendizado transversal que evita erro ou retrabalho;
- decisão global que afeta vários contextos;
- comportamento recorrente de agente ou ferramenta;
- contexto reutilizável sobre MCPs, modelos e integrações;
- diagnóstico cuja lógica se aplica além de um projeto específico;
- convenção agentic-first compartilhada;
- memória consolidada depois de várias sessões relacionadas.

## O que não deve ser registrado

Não crie memória para:

- cadastrar ou descrever um projeto;
- copiar README, arquitetura ou documentação técnica de projeto;
- registrar cada tarefa executada;
- guardar estado atual de branch, PR, deploy ou incidente aberto;
- copiar conversa completa;
- guardar log bruto;
- registrar comando isolado sem valor transversal;
- documentar ajuste visual ou textual trivial;
- duplicar informação já canônica no GitHub;
- guardar segredo, token, senha, cookie ou chave;
- armazenar conteúdo de outro workspace em exemplos públicos.

## Memória específica de projeto

Uma descoberta feita em um projeto não deve ir automaticamente para a Biblioteca.

Use esta regra:

```text
serve apenas para este projeto
→ página do projeto ou GitHub

surgiu neste projeto, mas orienta outros projetos ou sessões
→ Biblioteca, com projeto de origem opcional
```

O campo de projeto, quando existir, representa **origem ou aplicabilidade**, não propriedade do conteúdo.

## Memory write-back

```text
sessão ou trabalho relevante
→ validar o resultado
→ verificar a fonte canônica
→ perguntar se existe memória global/transversal
   não → encerrar na fonte correta
   sim → localizar memória existente
       → atualizar ou criar Rascunho
       → registrar síntese e origem
       → revisão humana
       → liberar para consulta futura
```

## Gatilhos

Existe gatilho de memória quando:

1. outra sessão precisará desse contexto;
2. diferentes agentes devem aplicar a mesma regra;
3. a informação vale para mais de um projeto;
4. houve uma decisão global;
5. foi identificado um padrão recorrente;
6. a ausência do contexto pode causar erro futuro;
7. o conhecimento não possui outra fonte canônica mais adequada.

Um processo específico de deploy não é global apenas por ser importante. Se pertence a um único repositório, deve permanecer nele.

## Schema recomendado

| Campo | Uso |
|---|---|
| Documento | título específico da memória |
| Slug | identificador estável |
| Status | Inbox, Rascunho, Ativo, Revisar ou Arquivado |
| Tipo de memória | natureza da síntese |
| Escopo | Global, Transversal, Agente, Ferramenta ou Sessão |
| Agentes/Ferramentas | consumidores previstos |
| Tags | recuperação semântica |
| Sessão de origem | data, título ou referência da conversa |
| Fonte | documento, conversa, decisão ou origem externa |
| Projeto de origem | relação opcional |
| GitHub | referência opcional, não cópia do conteúdo |
| Versão | versão editorial |
| Última revisão | validação humana mais recente |
| Notas | limites e condições de uso |

`Projeto de origem` não deve ser campo obrigatório.

## Tipos de memória

Tipos sugeridos:

- Síntese de sessão;
- Contexto global;
- Aprendizado transversal;
- Preferência operacional;
- Decisão global;
- Padrão recorrente;
- Contexto de agente;
- Contexto de ferramenta;
- Integração transversal;
- Diagnóstico reutilizável;
- Política de memória;
- Handoff consolidado entre sessões.

Evite tipos que transformem a Biblioteca em um espelho da documentação técnica dos projetos.

## Estrutura mínima do corpo

```text
Resumo
Quando consultar
Escopo
Contexto de origem
Memória consolidada
Como aplicar
Limites
Fontes e referências
Agentes ou ferramentas aplicáveis
Projeto de origem opcional
Histórico de versões
```

### Síntese de sessão

```text
Objetivo da sessão
Decisões relevantes
Contexto que deve persistir
Aprendizados reutilizáveis
O que foi descartado por ser temporário
Fontes canônicas atualizadas
Próxima consulta recomendada
```

Não inclua transcrição integral.

## Ciclo editorial

- **Inbox:** captura ainda não classificada;
- **Rascunho:** síntese em construção;
- **Ativo:** revisado e liberado para consulta;
- **Revisar:** pode estar desatualizado ou conflitante;
- **Arquivado:** preservado apenas para histórico.

Agentes não promovem conteúdo para Ativo sem autorização humana.

## Views recomendadas

- `Memória ativa`;
- `Sínteses de sessões`;
- `Global e transversal`;
- `Por agente ou ferramenta`;
- `Precisa revisar`;
- `Sem fonte`;
- `Projeto de origem`, apenas para rastreabilidade opcional.

Não use `Por projeto` como navegação principal da Biblioteca.

## Leitura por agentes

Antes de usar uma memória, verifique:

1. status ativo;
2. escopo compatível;
3. agente ou ferramenta aplicável;
4. origem verificável;
5. data de revisão;
6. ausência de conflito com uma fonte canônica;
7. se o conteúdo ainda é realmente global ou transversal.

## Escrita por agentes

O padrão é somente leitura. Escrita autorizada deve:

- buscar memória existente antes de criar outra;
- registrar uma síntese, não uma transcrição;
- manter o item em Rascunho;
- preencher origem e escopo;
- usar projeto apenas como referência opcional;
- não mover ou excluir páginas;
- não registrar segredos;
- não transformar documentação específica em memória global.

## Camada derivada

Um índice ou RAG pode derivar conteúdo da Biblioteca. A camada derivada deve manter origem, versão e data de revisão, mas não se torna fonte canônica.
