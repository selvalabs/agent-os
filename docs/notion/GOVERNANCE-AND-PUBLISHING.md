# Governança, manutenção e publicação do Cérebro

## Objetivo

Manter o Cérebro útil, confiável e pequeno o suficiente para navegação seletiva. O workspace deve favorecer curadoria, memória durável e rastreabilidade, não acumulação indiscriminada.

Este documento é um modelo genérico. Estados, nomes de campos, projetos e agentes são definidos por cada usuário em seu próprio ambiente.

## Estados recomendados para a Biblioteca

- **Inbox** — captura ainda sem triagem;
- **Rascunho** — documento em construção;
- **Ativo ou Aprovado** — revisado e liberado para uso no escopo indicado;
- **Revisar** — pode estar desatualizado, incompleto ou em conflito;
- **Arquivado** — preservado para histórico, fora dos fluxos ativos.

Agentes não promovem conteúdo para uso ativo sem revisão humana explícita.

## Responsabilidades

### Responsável editorial

- revisa Markdowns, pesquisas e decisões;
- confirma status, versão e última revisão;
- resolve conflitos de fonte;
- aprova publicação para o GitHub;
- define quando item deve ser revisado ou arquivado.

### Responsável do projeto

- mantém links canônicos do projeto;
- confirma arquitetura e estado operacional no GitHub;
- valida impacto de decisões transversais;
- revisa Markdowns operacionais relacionados ao projeto.

### Agente

- consulta contexto seletivamente;
- usa operacionalmente somente Markdowns liberados e aplicáveis;
- indica fontes utilizadas;
- propõe mudanças revisáveis;
- avalia gatilho de memória após ações relevantes;
- cria ou atualiza Rascunho somente com autorização de escrita;
- não altera precedência, aprovação ou permissões silenciosamente.

## Memory write-back

Quando uma ação produzir processo reutilizável, decisão, incidente resolvido, integração, runbook, diagnóstico não trivial ou aprendizado durável, crie ou atualize um Markdown na Biblioteca do usuário.

```text
execução
→ validação
→ issue, PR, commit ou evidência
→ avaliação de memória
→ criar ou atualizar Markdown em Rascunho
→ preencher origem, projeto, agente e versão
→ revisão humana
→ liberação para uso
```

Atualize documento existente quando o assunto já estiver coberto. Evite duplicação por nomes diferentes.

Não transforme logs brutos, conversas completas, ações triviais, segredos ou conteúdo privado em memória pública.

## Fluxo Cérebro → GitHub

```text
Markdown criado ou revisado no Cérebro
→ Rascunho ou Revisar
→ revisão humana
→ aprovação para publicação
→ definição do destino canônico
→ sanitização de nomes, URLs e IDs
→ normalização para Markdown ou código
→ issue
→ branch
→ implementação
→ validação
→ pull request
→ revisão
→ merge
→ registro do commit, versão e hash na Biblioteca privada
→ liberação quando aplicável
```

A publicação nunca é sincronização bidirecional automática. O GitHub passa a ser a fonte canônica do artefato operacional publicado; a Biblioteca preserva descoberta, escopo, origem e versão no ambiente privado.

## Quando publicar no GitHub

Publique quando o conteúdo se tornar:

- política compartilhada;
- skill reutilizável;
- template de repositório;
- runbook operacional que deve acompanhar código ou infraestrutura;
- ADR de projeto;
- documentação técnica versionada;
- regra que exige validação ou enforcement.

Mantenha no Cérebro quando for:

- pesquisa e estudo;
- curadoria editorial;
- memória transversal não vinculada a um único repositório;
- catálogo de projetos;
- hipótese ainda em avaliação;
- planejamento humano;
- decisão ainda não aprovada;
- conteúdo pessoal, de cliente ou organização que não deve ser público.

## Registro de publicação

Cada publicação privada pode registrar:

- Markdown de origem;
- responsável pela aprovação;
- repositório de destino;
- caminho do arquivo;
- issue;
- pull request;
- commit ou tag;
- data;
- versão e hash;
- estado atual;
- item substituído, quando houver.

Não copie esses identificadores para documentação pública sem necessidade. Exemplos públicos usam `example-org/example-repo` e valores fictícios.

## Registro de atividades, HANDOFF e Biblioteca

### Registro de atividades

Histórico cronológico opcional de ações, tentativas, links e próximos passos.

### `HANDOFF.md`

Estado temporário da frente atual: realizado, evidências, riscos, pendências e próxima ação.

### Biblioteca de Markdowns

Memória consolidada, temática e reutilizável.

Quando uma frente termina:

- pendências permanecem em issue;
- estado temporário é atualizado no handoff;
- fatos estáveis vão para documentação canônica do projeto;
- processo, decisão e aprendizado durável vão para a Biblioteca privada.

## Ciclos de revisão

### Semanal

- revisar rascunhos de alta prioridade;
- revisar itens marcados para atualização;
- verificar links quebrados dos projetos ativos;
- confirmar se ações relevantes recentes geraram memória;
- retirar rascunhos abandonados das views principais, sem apagar.

### Mensal

- revisar Markdowns ativos sem origem quando aplicável;
- revisar documentos com data vencida;
- verificar itens duplicados por slug ou tema;
- revisar decisões com prazo vencido;
- revisar acessos de agentes e integrações;
- arquivar projetos e documentos inativos.

### Trimestral

- revisar estrutura, áreas, propriedades e views;
- remover views sem uso;
- confirmar fontes canônicas;
- revisar tipos e tags da Biblioteca;
- avaliar alterações de schema por issue própria;
- revisar política de retenção e arquivamento;
- revisar sanitização antes de releases públicas.

## Arquivamento

Arquivar significa retirar item das views operacionais mantendo histórico e relações.

Antes de arquivar:

1. registrar motivo;
2. apontar substituto, quando houver;
3. preservar origem, versão e data;
4. verificar links canônicos;
5. garantir que agentes não o recuperem como conteúdo ativo.

## Prevenção de acúmulo

- todo Markdown ativo possui projeto ou escopo claro;
- todo documento operacional possui fonte verificável;
- todo item ativo possui versão e última revisão;
- memória existente é atualizada antes de criar duplicata;
- toda view responde a necessidade real;
- páginas órfãs são relacionadas ou arquivadas após revisão;
- conteúdo operacional integral permanece no GitHub;
- a Biblioteca guarda consolidação, não transcrição.

## Mudanças estruturais no Cérebro

Mover áreas, renomear bancos, alterar propriedades, tipos ou relações exige:

- problema documentado em issue;
- impacto previsto;
- plano aditivo ou de migração;
- backup ou exportação quando aplicável;
- responsável;
- validação em piloto;
- aprovação humana antes da execução ampla.

## Publicação pública segura

Não torne público um repositório que já possua histórico, issues ou PRs com contexto privado.

Para publicar um framework derivado de um ambiente privado:

1. produza snapshot sanitizado;
2. revise todos os arquivos;
3. remova URLs, IDs, nomes e conteúdo particular;
4. crie repositório público novo com histórico limpo;
5. use um único commit inicial sanitizado ou histórico reconstituído;
6. não importe issues e PRs privados;
7. execute o validador e revisão manual;
8. somente então altere visibilidade ou publique release.

Consulte `docs/governance/PUBLIC-SANITIZATION.md`.

## Critério de saúde

O Cérebro está saudável quando uma pessoa ou agente consegue:

1. começar pelo START HERE;
2. entender o conteúdo de `01` a `05`;
3. encontrar projeto ativo em poucos passos;
4. recuperar somente Markdowns liberados e relevantes;
5. identificar origem, versão e revisão;
6. seguir para o GitHub sem depender de cópias manuais;
7. rastrear como ação virou memória e mudança operacional;
8. reconhecer conteúdo experimental ou arquivado;
9. separar claramente conteúdo privado de artefatos publicáveis.
