# Estratégia de compatibilidade

## Canônico

O arquivo compartilhado no repositório é `AGENTS.md`. Documentos extensos ficam em `docs/agent/` e skills.

## Claude Code

Use `CLAUDE.md` mínimo:

```md
@AGENTS.md
```

Adicione apenas instruções exclusivas do Claude abaixo do import.

## Outros agentes

Quando uma ferramenta exigir arquivo próprio:

1. crie um adaptador pequeno;
2. aponte para a documentação canônica;
3. não copie políticas extensas manualmente;
4. gere o adaptador a partir de manifesto quando possível;
5. valide drift em CI.

## Regra

Arquivos específicos de ferramenta são interfaces, não fontes de verdade. Se a ferramenta não suporta import, mantenha apenas o mínimo indispensável e registre a limitação.
