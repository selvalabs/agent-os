# Schemas recomendados para um Cérebro

Este documento propõe bancos independentes e complementares. Projetos não devem ser armazenados na Biblioteca de Markdowns.

## 1. Projetos

### Função

Registrar os projetos, produtos, sistemas e iniciativas do Cérebro.

### Propriedades recomendadas

| Propriedade | Tipo sugerido | Uso |
|---|---|---|
| Nome | Title | nome do projeto |
| Slug | Text | identificador estável |
| Estado | Select | Incubação, Ativo, Manutenção, Pausado, Arquivado |
| Tipo | Select | Produto, Sistema, Biblioteca, Infraestrutura, Estudo ou Laboratório |
| Finalidade | Text | problema e objetivo |
| Público/Usuários | Text | quem utiliza ou se beneficia |
| Resultado esperado | Text | entrega ou impacto esperado |
| Responsável | Person/Text | responsável humano |
| Stack | Multi-select/Text | tecnologias principais |
| Repositório | URL | GitHub canônico |
| START HERE | URL | entrada do repositório |
| Arquitetura | URL | documento canônico |
| Ambientes | Text/URL | demonstração, homologação ou produção |
| Acesso de agentes | Select | Sem acesso, Leitura, Escrita revisada, Operação autorizada |
| Decisões | Relation | decisões relacionadas |
| Fontes | Relation | fontes relacionadas |
| Última revisão | Date | revisão do registro |

### Views recomendadas

- Projetos ativos;
- Incubação;
- Manutenção;
- Precisam de revisão;
- Agentic-first;
- Arquivados.

### Página do projeto

```text
Resumo
Finalidade
Estado
Responsável
Usuários
Resultado esperado
Stack
Repositório
START HERE
Arquitetura
Ambientes
Acesso dos agentes
Decisões
Fontes
Próxima revisão
```

A página não precisa de view da Biblioteca.

## 2. Biblioteca de Markdowns

### Função

Registrar memória global, transversal ou necessária entre sessões para humanos e agentes.

### Propriedades recomendadas

| Propriedade | Tipo sugerido | Uso |
|---|---|---|
| Documento | Title | título da memória |
| ID | Unique ID | identificador interno |
| Slug | Text | identificador estável |
| Status | Select/Status | Inbox, Rascunho, Ativo, Revisar, Arquivado |
| Tipo de memória | Select | natureza da síntese |
| Escopo | Select | Global, Transversal, Agente, Ferramenta, Sessão |
| Agentes/Ferramentas | Multi-select/Relation | consumidores previstos |
| Tags | Multi-select | recuperação temática |
| Sessão de origem | Text/URL | conversa, data ou referência |
| Fonte | URL/Text | origem verificável |
| Projeto de origem | Relation | opcional; indica onde surgiu |
| GitHub | URL | referência opcional |
| Prioridade | Select | ordem de revisão |
| Versão | Number | versão editorial |
| Última revisão | Date | validação humana |
| Notas | Text | limites e condições |
| Referência derivada | Text | ID opcional em índice ou RAG |
| Criado | Created time | criação |
| Editado | Last edited time | edição |

`Projeto de origem` é opcional e não deve ser usado para montar o projeto.

### Tipos de memória recomendados

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
- Handoff consolidado entre sessões.

### Views recomendadas

- Memória ativa;
- Sínteses de sessões;
- Global e transversal;
- Por agente ou ferramenta;
- Precisa revisar;
- Sem fonte;
- Projeto de origem, apenas para rastreabilidade.

Não use `Por projeto` como view central.

## 3. Decisões

### Função

Registrar decisões transversais ou editoriais com rastreabilidade.

| Propriedade | Tipo sugerido | Uso |
|---|---|---|
| Decisão | Title | título curto |
| Estado | Select | Proposta, Aprovada, Rejeitada, Substituída, Arquivada |
| Escopo | Select | Global, Projeto, Produto, Arquitetura, Editorial |
| Responsável | Person/Text | decisor |
| Data | Date | data da decisão |
| Projetos | Relation | projetos afetados, quando houver |
| Artefato operacional | URL | ADR, issue ou PR |
| Revisar em | Date | reavaliação |
| Memória relacionada | Relation | opcional, apenas se houver valor entre sessões |

Uma decisão específica de projeto não precisa virar memória global.

## 4. Fontes

| Propriedade | Tipo sugerido | Uso |
|---|---|---|
| Fonte | Title | nome legível |
| Tipo | Select | Documento, Site, Livro, Vídeo, Repositório, Norma, Dataset |
| URL | URL | localização |
| Autor/Origem | Text | autor ou organização |
| Confiabilidade | Select | Primária, Secundária, Contextual, Não verificada |
| Estado | Select | Ativa, Indisponível, Substituída, Arquivada |
| Projetos | Relation | projetos relacionados |
| Consultada em | Date | última consulta |
| Observações | Text | limites e escopo |

## 5. Registro de sessões

Pode ser uma página ou banco cronológico opcional.

Campos úteis:

- data;
- ferramenta ou modelo;
- objetivo;
- projeto relacionado, quando houver;
- links;
- resultado;
- próxima ação;
- memória consolidada, quando houver.

O registro de sessão não substitui a Biblioteca. A Biblioteca recebe somente a síntese selecionada.

## Relações recomendadas

```text
Projetos ↔ Decisões
Projetos ↔ Fontes
Biblioteca ↔ Agentes/Ferramentas
Biblioteca ↔ Projeto de origem (opcional)
Biblioteca ↔ Decisão global (opcional)
```

Evite tornar `Projetos ↔ Biblioteca` uma relação obrigatória.

## Template de memória

```text
Resumo
Quando consultar
Escopo
Sessão ou fonte de origem
Memória consolidada
Como aplicar
Limites
Agentes ou ferramentas
Projeto de origem opcional
Histórico de versões
```

## Regras de qualidade

- projetos vivem no banco Projetos;
- a Biblioteca guarda sínteses globais ou entre sessões;
- documentação específica permanece no GitHub;
- estado temporário permanece em issue, PR ou handoff;
- relações opcionais indicam origem, não propriedade;
- toda memória ativa possui escopo, origem e revisão;
- agentes não promovem conteúdo sem revisão humana;
- exemplos públicos são fictícios;
- segredos nunca entram no Cérebro.
