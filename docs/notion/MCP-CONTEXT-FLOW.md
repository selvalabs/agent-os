# MCP e fluxo seletivo de contexto

## Objetivo

Permitir que agentes consultem um Cérebro editorial e uma Biblioteca de Markdowns sem receber o workspace inteiro, sem tratar rascunhos como verdade e sem escrever fora do escopo autorizado.

Este documento usa somente exemplos fictícios. Cada usuário configura seus próprios projetos, agentes, páginas e permissões.

## Modo padrão

Toda integração externa começa em **somente leitura**.

Escrita exige:

1. intenção explícita do humano;
2. página ou banco de destino identificado;
3. campos que serão alterados;
4. conteúdo proposto visível ou revisável;
5. fontes utilizadas;
6. ausência de movimentação ou exclusão destrutiva não solicitada.

## Fluxo de leitura

```text
pedido atual
→ identificar projeto, agente ou domínio
→ abrir Cérebro / START HERE
→ abrir registro do projeto
→ consultar Biblioteca por Projeto + Agente + Tags + Tipo
→ filtrar conteúdo liberado
→ conferir origem, versão e última revisão
→ recuperar somente Markdowns relevantes
→ consultar decisões e fontes aplicáveis
→ seguir para o GitHub quando a informação for operacional
```

## Pacote mínimo de contexto

Para tarefa de código, o contexto ideal contém:

- identificação do projeto;
- propósito e estado;
- URL do repositório;
- START HERE do repositório;
- Markdowns liberados diretamente relacionados;
- decisões relevantes;
- restrições de acesso;
- issue, branch, PR ou handoff atual.

Não inclua automaticamente:

- todas as páginas do projeto;
- toda a Biblioteca;
- documentos de outros agentes ou projetos sem dependência;
- Inbox, Rascunho ou Revisar como regra;
- logs antigos;
- conteúdo duplicado do GitHub;
- páginas, IDs ou URLs de outros workspaces.

## Regras de confiança

Adapte os nomes dos estados, mantendo significados inequívocos:

- **Liberado:** pode orientar a tarefa dentro do escopo indicado;
- **Rascunho:** contexto em construção, não regra aprovada;
- **Inbox:** captura sem triagem;
- **Revisar:** conteúdo potencialmente desatualizado ou conflitante;
- **Arquivado:** histórico, fora dos fluxos ativos.

Antes de usar um item liberado, confira:

- projeto;
- agente ou ferramenta;
- tipo e tags;
- fonte ou GitHub;
- versão;
- última revisão;
- notas e limitações.

Quando houver conflito:

1. identifique as fontes;
2. verifique a hierarquia canônica;
3. registre o conflito;
4. solicite decisão humana quando a precedência não estiver definida.

## Estratégia por camadas

### Camada 1 — Entrada

Leia START HERE e identifique a rota correta.

### Camada 2 — Projeto e agente

Leia registro do projeto, agente aplicável e links canônicos.

### Camada 3 — Memória

Busque Markdowns usando filtros específicos. Não faça dump da Biblioteca.

Exemplos fictícios:

- Projeto = Produto Alpha e Tags = segurança + api;
- Agente = Agente de Código e Tipo = Processo;
- Projeto = Projeto Exemplo e Status = Ativo;
- Tipo = Incidente e Tags = deploy;
- Status = Revisar e Prioridade = Alta.

### Camada 4 — Operação

Use GitHub, issue, PR, código e handoff. O Cérebro deixa de ser fonte principal nessa etapa.

### Camada 5 — Retorno de memória

Depois da execução, avalie se o resultado precisa sobreviver à sessão.

```text
resultado validado
→ gatilho de memória?
   não → encerrar com evidência
   sim → localizar Markdown existente
       → atualizar ou criar Rascunho
       → preencher origem e metadados
       → solicitar revisão humana
       → liberar após aprovação
```

## Gatilhos de escrita na Biblioteca

Há gatilho quando a ação produz:

- processo reutilizável;
- decisão importante;
- incidente e solução validada;
- integração ou configuração relevante;
- runbook de deploy, rollback, backup ou recuperação;
- diagnóstico não trivial;
- regra de segurança;
- aprendizado que evita erro ou retrabalho;
- mudança permanente de operação.

A ausência de gatilho não autoriza criar registro apenas para marcar atividade.

## Escrita permitida com autorização

- criar Markdown em Inbox ou Rascunho;
- atualizar documento existente com nova versão;
- adicionar projeto, agente, tipo, tags e prioridade;
- registrar fonte, GitHub, issue, PR, commit ou arquivo;
- atualizar hash depois de publicação ou indexação;
- alterar para Revisar quando houver dúvida ou envelhecimento;
- atualizar última revisão depois de revisão humana;
- promover para uso somente após aprovação explícita.

## Escrita não permitida por padrão

- mover ou apagar páginas;
- promover conteúdo sem revisão humana;
- substituir decisão existente silenciosamente;
- sobrescrever Markdown extenso sem mostrar a proposta;
- criar duplicata sem buscar item existente;
- copiar documentação operacional inteira do GitHub;
- alterar propriedades ou opções do schema;
- alterar permissões do workspace;
- criar automação bidirecional;
- inserir credenciais ou segredos;
- copiar conteúdo privado para exemplos públicos.

## Procedimento para criar memória

1. busque por slug, título, projeto e tags para evitar duplicata;
2. escolha criar ou atualizar;
3. escreva resumo curto e estrutura reutilizável;
4. preencha documento, slug, status, tipo, formato, projetos, agentes, tags e prioridade;
5. adicione fonte ou GitHub;
6. defina versão e notas;
7. mantenha Rascunho até revisão;
8. informe claramente o que foi registrado.

## Consultas recomendadas

- projeto X + Markdowns liberados de arquitetura;
- projeto X + incidentes de deploy;
- agente Y + processos de operação;
- projeto X + decisões e fontes relacionadas;
- itens Revisar de alta prioridade;
- Markdowns sem origem ou revisão.

Evite consultas abertas como “traga tudo sobre a organização” ou “carregue todo o Cérebro”.

## Rastreabilidade

Quando conteúdo do Cérebro influenciar mudança operacional, registre quando aplicável:

- Markdown ou ID local;
- estado;
- versão e última revisão;
- projeto e agente;
- issue ou PR resultante;
- commit ou versão publicada;
- hash na camada derivada.

Em documentação pública, use somente placeholders. Não publique IDs, URLs ou nomes reais do workspace.

## Falhas e indisponibilidade

Se o Cérebro ou MCP estiver indisponível:

- não invente contexto ausente;
- continue somente com fontes canônicas disponíveis;
- registre a limitação no handoff ou PR;
- não copie conteúdo para locais incorretos como solução silenciosa;
- se houve gatilho de memória, registre pendência em issue para write-back posterior.
