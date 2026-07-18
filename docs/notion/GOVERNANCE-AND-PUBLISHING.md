# Governança, manutenção e publicação do Cérebro

## Objetivo

Manter projetos, conhecimento, decisões e memória em suas fontes corretas, evitando que a Biblioteca vire um depósito geral.

## Responsabilidades

### Responsável do projeto

- mantém o registro no banco Projetos;
- confirma finalidade, estado e responsável;
- mantém links para GitHub, START HERE, arquitetura e ambientes;
- revisa decisões e fontes do projeto;
- garante que contexto específico permaneça em suas fontes canônicas.

### Responsável editorial

- revisa conhecimento, decisões e memória;
- confirma status, escopo, origem e revisão;
- resolve conflitos;
- aprova publicação para o GitHub;
- evita duplicação entre Projetos e Biblioteca.

### Agente

- consulta contexto seletivamente;
- abre o registro do projeto antes de buscar memória global;
- respeita GitHub como fonte operacional;
- classifica o destino antes de escrever;
- cria memória apenas com autorização;
- não promove conteúdo sem revisão humana.

## Governança de projetos

Todo projeto deve possuir:

- estado definido;
- responsável;
- finalidade;
- repositório ou indicação de que não possui código;
- links canônicos;
- data de revisão;
- critério de arquivamento.

Projetos não são itens da Biblioteca.

## Governança da Biblioteca

Estados recomendados:

- **Inbox:** captura sem classificação;
- **Rascunho:** síntese em construção;
- **Ativo:** memória revisada e liberada;
- **Revisar:** conteúdo potencialmente desatualizado;
- **Arquivado:** histórico fora dos fluxos ativos.

Toda memória ativa deve possuir:

- escopo;
- origem;
- agente ou ferramenta aplicável, quando houver;
- última revisão;
- limites de uso.

Projeto de origem é opcional.

## Regra de write-back

```text
sessão ou trabalho concluído
→ validar resultado
→ classificar destino
   projeto → banco Projetos
   específico do repositório → GitHub
   temporário → issue, PR ou HANDOFF
   conhecimento → área 01
   decisão transversal → Decisões
   memória global ou entre sessões → Biblioteca
→ revisar
```

Não use importância como único critério. Um procedimento importante, mas específico de um projeto, continua pertencendo ao projeto.

## Registro de sessões

Um registro cronológico opcional pode conter:

- data;
- ferramenta ou modelo;
- objetivo;
- projeto relacionado;
- resultado;
- links;
- próxima ação.

Apenas a síntese que merece persistir deve ser consolidada na Biblioteca.

## Biblioteca versus outras fontes

| Conteúdo | Fonte |
|---|---|
| Projeto | Banco Projetos |
| Conhecimento | Área 01 |
| Decisão formal | Banco Decisões ou ADR |
| Operação específica | GitHub |
| Continuidade | HANDOFF |
| Sessão cronológica | Registro de sessões |
| Memória entre sessões | Biblioteca |

## Publicação Cérebro → GitHub

Publique no GitHub quando o conteúdo se tornar:

- política compartilhada;
- skill;
- template;
- documentação técnica versionada;
- regra que exige CI ou enforcement;
- ADR ou runbook que deve acompanhar o código.

Fluxo:

```text
conteúdo aprovado no Cérebro
→ definir destino canônico
→ sanitizar
→ issue
→ branch
→ implementação
→ validação
→ pull request
→ merge
→ atualizar origem e versão no Cérebro
```

A Biblioteca pode apontar para o artefato publicado quando a memória global correspondente continuar útil. Não deve copiar a documentação completa.

## Ciclos de revisão

### Semanal

- revisar projetos que mudaram de estado;
- revisar memórias em Rascunho ou Revisar;
- verificar se sessões relevantes produziram sínteses;
- remover capturas sem valor, sem apagar histórico necessário.

### Mensal

- revisar projetos sem responsável ou links;
- revisar memórias ativas sem origem;
- detectar duplicações;
- conferir permissões de agentes;
- arquivar registros inativos.

### Trimestral

- revisar schemas e views;
- confirmar que Projetos e Biblioteca continuam separados;
- revisar tags e tipos de memória;
- revisar retenção e arquivamento;
- revisar sanitização pública.

## Arquivamento

### Projeto

Antes de arquivar:

1. registrar motivo;
2. preservar links e decisões;
3. confirmar estado do repositório;
4. definir substituto, quando houver.

### Memória

Antes de arquivar:

1. registrar motivo;
2. apontar substituto;
3. preservar origem e versão;
4. garantir que agentes não a recuperem como ativa.

## Prevenção de acúmulo

- projeto é registrado uma vez no banco Projetos;
- documentação específica permanece no GitHub;
- a Biblioteca guarda sínteses, não transcrições;
- memória existente é atualizada antes de criar duplicata;
- projeto de origem não é obrigatório;
- toda view responde a uma necessidade real;
- conteúdo volátil não vira memória durável.

## Critério de saúde

O Cérebro está saudável quando uma pessoa ou agente consegue:

1. encontrar o projeto no banco Projetos;
2. seguir para o GitHub correto;
3. identificar o estado temporário da tarefa;
4. consultar conhecimento e decisões sem duplicação;
5. recuperar memória global apenas quando necessária;
6. entender a origem e revisão da memória;
7. distinguir sessão, projeto e memória;
8. publicar artefatos sem expor contexto privado.
