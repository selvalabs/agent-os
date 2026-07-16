# Fontes canônicas

## Regra

Todo artefato possui um proprietário e uma única fonte de verdade. Cópias derivadas carregam origem, versão e hash.

## Matriz recomendada

| Classe | Fonte | Cópias permitidas |
|---|---|---|
| Conhecimento e estudos | Cérebro editorial do usuário | Markdown publicado e índice derivado |
| Pesquisa | Cérebro editorial do usuário | Markdown aprovado e índice derivado |
| Memória durável | Biblioteca de Markdowns do usuário | Índice, embeddings e resumos vinculados |
| Instrução do repositório | GitHub do projeto | Índice e links no Cérebro |
| Skill compartilhada | Agent OS | Instalação ou referência |
| Política compartilhada | Agent OS | Adaptadores gerados |
| Handoff | GitHub do projeto | Resumo indexado |
| Segredo | Gerenciador de segredos | Nenhuma cópia em Markdown |

## Cabeçalho de conteúdo derivado

Conteúdo gerado pode registrar:

```yaml
source_system: editorial-system
source_id: "example-id"
source_version: 3
source_hash: "sha256:example"
generated_at: "YYYY-MM-DDTHH:MM:SSZ"
do_not_edit: true
```

Use somente placeholders em documentação pública. IDs, hashes e URLs reais permanecem no ambiente privado.

## Conflito

Quando duas fontes divergem:

1. interromper publicação automática;
2. identificar o proprietário de cada artefato;
3. produzir diff;
4. registrar decisão;
5. atualizar a cópia derivada somente após resolução.

## Privacidade

A matriz pública descreve classes de informação, não a estrutura real de um workspace. Não inclua nomes de projetos, agentes, páginas, bancos, clientes, URLs ou IDs privados.
