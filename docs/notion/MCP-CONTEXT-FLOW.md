# MCP e fluxo seletivo de contexto

## Objetivo

Permitir que agentes consultem o Cérebro sem carregar tudo e sem confundir projetos com memória global.

Toda integração começa em **somente leitura**.

## Ordem de consulta

```text
pedido atual
→ identificar se há projeto
→ abrir START HERE do Cérebro
→ abrir registro do projeto, quando aplicável
→ seguir para GitHub e START HERE do repositório
→ consultar conhecimento, decisões e fontes necessárias
→ consultar Biblioteca somente se houver memória global ou de sessão relevante
→ executar
```

A Biblioteca não é etapa obrigatória de toda tarefa.

## Contexto de projeto

Para uma tarefa ligada a um projeto, recupere:

- nome e finalidade;
- estado e responsável;
- repositório;
- START HERE;
- arquitetura;
- ambientes;
- acesso permitido aos agentes;
- decisões e fontes relacionadas;
- issue, PR ou handoff atual.

Esses dados vêm do banco Projetos e do GitHub, não da Biblioteca.

## Contexto da Biblioteca

Consulte a Biblioteca quando precisar de:

- síntese de sessão anterior;
- preferência operacional estável;
- regra global de uso agentic-first;
- aprendizado transversal;
- contexto recorrente sobre agente ou ferramenta;
- padrão identificado em diferentes projetos;
- decisão global necessária para interpretar a tarefa.

## Filtros recomendados

Use filtros como:

- Status = Ativo;
- Escopo = Global ou Transversal;
- Agente/Ferramenta = agente atual;
- Tipo = Síntese de sessão;
- Tags = tema relevante;
- Última revisão dentro do prazo.

`Projeto de origem` pode ajudar na rastreabilidade, mas não deve ser o filtro padrão nem substituir o registro do projeto.

## Não carregar automaticamente

- todo o banco Projetos;
- toda a Biblioteca;
- páginas de outros projetos;
- rascunhos como regras;
- logs antigos;
- transcrições completas;
- documentação duplicada do GitHub;
- conteúdo privado em exemplos públicos.

## Confiança da memória

Antes de usar um Markdown:

1. confirme o status ativo;
2. verifique o escopo;
3. confirme agente ou ferramenta aplicável;
4. confira origem e revisão;
5. verifique conflito com GitHub, projeto ou política canônica;
6. confirme que o conteúdo ainda é global ou transversal.

Fontes específicas do projeto prevalecem para operação daquele projeto.

## Retorno de contexto

Depois da execução:

```text
resultado validado
→ classificar destino
   projeto → banco Projetos
   documentação específica → GitHub
   estado temporário → issue, PR ou HANDOFF
   conhecimento → área 01
   memória global/transversal → Biblioteca
```

## Escrita permitida com autorização

### Projetos

- criar ou atualizar registro do projeto;
- atualizar estado, responsável e links;
- relacionar decisões e fontes;
- registrar última revisão.

### Biblioteca

- criar síntese em Inbox ou Rascunho;
- atualizar memória existente;
- preencher escopo, agente, tags e origem;
- adicionar projeto de origem opcional;
- promover somente depois de revisão humana.

## Escrita não permitida por padrão

- mover ou apagar páginas;
- transformar documentação de projeto em memória global;
- cadastrar projeto dentro da Biblioteca;
- promover Rascunho sem revisão;
- copiar conteúdo integral do GitHub;
- alterar schema ou permissões;
- criar sincronização bidirecional;
- inserir segredos.

## Procedimento de memória

1. confirme que a informação precisa sobreviver a sessões;
2. confirme que não existe destino canônico mais específico;
3. busque memória existente;
4. escreva uma síntese;
5. preencha escopo e origem;
6. use projeto apenas como origem opcional;
7. mantenha Rascunho até revisão.

## Falhas

Se Notion ou MCP estiver indisponível:

- não invente contexto;
- use as fontes canônicas disponíveis;
- registre a limitação na issue, PR ou handoff;
- deixe pendência de write-back apenas quando houver memória global real.
