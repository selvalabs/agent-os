# Política de sanitização para publicação

## Objetivo

Garantir que o SelvaLabs Agent OS possa ser publicado e reutilizado sem expor informações de workspaces, projetos, clientes ou operadores usados durante seu desenvolvimento.

## Regra principal

Este repositório documenta **como criar e estruturar um Cérebro próprio**. Ele não deve descrever, reproduzir ou espelhar o Cérebro real de nenhuma pessoa ou organização.

## Conteúdo permitido

- arquitetura genérica;
- propriedades e schemas recomendados;
- placeholders;
- exemplos fictícios;
- fluxos de issue, branch, pull request e validação;
- modelos de START HERE, AGENTS.md, handoff, políticas e skills;
- conceitos de memória durável, RAG, MCP, governança e fontes canônicas;
- nomes públicos do próprio framework e de tecnologias abertas.

## Conteúdo proibido

- nomes reais de clientes, produtos privados ou projetos internos;
- apelidos de agentes usados em um workspace privado;
- títulos reais de páginas ou bancos pessoais;
- URLs, IDs, slugs, hashes ou identificadores de um workspace privado;
- estrutura acadêmica, familiar, comercial ou operacional de um mantenedor;
- credenciais, segredos, números de telefone, e-mails privados ou dados pessoais;
- incidentes reais que permitam identificar infraestrutura ou clientes;
- cópias de conteúdo da Biblioteca de Markdowns de uma pessoa ou organização.

## Padrão de exemplos

Use nomes neutros:

- `Projeto Exemplo`;
- `Produto Alpha`;
- `Agente de Código`;
- `Agente de Operações`;
- `Workspace Exemplo`;
- `Biblioteca de Markdowns`;
- `Registro de Atividades`;
- `example-org/example-repo`;
- `https://example.com`.

## Biblioteca de Markdowns

O repositório pode ensinar um schema recomendado para uma Biblioteca de Markdowns. Deve deixar claro que:

1. o usuário cria a própria biblioteca;
2. os campos são recomendações adaptáveis;
3. as opções de projetos, agentes e tags são preenchidas pelo usuário;
4. nenhuma linha, opção ou identificador de uma biblioteca real pertence ao código público;
5. exemplos devem ser fictícios.

## Pacote de importação

Arquivos em `docs/notion-import/` devem:

- criar estrutura vazia ou baseada em placeholders;
- nunca presumir páginas já existentes;
- não mencionar conteúdo de um workspace particular;
- usar migração aditiva e não destrutiva;
- orientar o usuário a substituir exemplos antes de usar em produção.

## Revisão antes da publicação

Antes de tornar o repositório público ou lançar uma versão:

1. revisar README, START HERE, documentação e templates;
2. verificar exemplos, URLs e nomes próprios;
3. confirmar que nenhuma configuração privada foi copiada;
4. executar o validador;
5. revisar o diff completo da release;
6. somente então criar tag ou alterar a visibilidade.

## Regra para contribuições futuras

Toda contribuição deve ser escrita como documentação de produto reutilizável. Contexto real usado para descobrir um padrão deve ser abstraído antes do commit.
