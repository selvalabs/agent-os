# Contrato de sincronização

## Regra de propriedade

Sincronização é unidirecional por artefato. A direção depende da fonte canônica.

## Notion para GitHub

Aplicável a pesquisa, políticas editoriais e materiais aprovados.

1. selecionar conteúdo com estado publicável;
2. exportar Markdown normalizado;
3. adicionar metadados de origem;
4. abrir pull request;
5. validar links, estrutura e segredos;
6. realizar merge após revisão;
7. registrar hash e versão.

## GitHub para Notion

Aplicável a índice e descoberta, não a reedição automática do conteúdo operacional.

1. capturar título, repositório, caminho, versão e resumo;
2. criar ou atualizar registro de catálogo;
3. apontar para a fonte original;
4. não substituir o arquivo GitHub a partir da cópia indexada.

## Índice derivado

Supabase ou RAG recebe cópias após publicação. Deve ser reconstruível a partir das fontes canônicas.

## Falhas

- conflito de hash: bloquear;
- fonte ausente: marcar órfão;
- versão regressiva: rejeitar;
- conteúdo com provável segredo: bloquear e solicitar revisão;
- erro de importação: preservar origem e logar sem editar silenciosamente.
