# AGENTS.md

## Missão

Manter o SelvaLabs Agent OS pequeno, auditável, reutilizável e seguro para múltiplos repositórios.

## Ordem de leitura

1. `START-HERE.md`
2. `docs/architecture/SPEC-AGENT-OS.md`
3. `docs/notion/START-HERE.md` quando a tarefa envolver o Cérebro
4. `docs/notion/MARKDOWN-LIBRARY-MEMORY.md` quando envolver memória
5. `docs/governance/CANONICAL-SOURCES.md`
6. `docs/governance/SECURITY-MODEL.md`
7. arquivo relacionado em `policies/`, `skills/` ou `templates/`

## Regras persistentes

- Preserve alterações humanas existentes.
- Não apague, mova ou renomeie estruturas sem pedido explícito.
- Não grave credenciais em Markdown.
- Prefira mudanças pequenas e revisáveis por pull request.
- Mantenha `AGENTS.md` como roteador.
- Toda operação de produção exige preflight, aprovação, rollback e verificação.
- Serviços externos começam em leitura.
- Todo espaço deve possuir `START HERE` visível.
- Projetos vivem no banco Projetos do Cérebro.
- Documentação específica vive no GitHub do projeto.
- Estado temporário vive em issue, PR e handoff.
- A Biblioteca recebe somente memória global, transversal ou necessária entre sessões.
- Projeto de origem em uma memória é opcional e não representa propriedade.
- Documentação pública usa exemplos fictícios.
- Publicações públicas usam snapshot sanitizado e histórico novo.

## Validação

```bash
python scripts/validate_agent_os.py .
```

Quando alterar o bootstrap, teste também com `--dry-run` em diretório temporário.

## Fontes canônicas

- projetos e produtos: banco Projetos do Cérebro;
- conhecimento e curadoria: áreas editoriais do Cérebro;
- memória global e entre sessões: Biblioteca de Markdowns;
- regras locais e operação: repositório consumidor;
- estado temporário: issue, PR e handoff;
- políticas e skills compartilhadas: Agent OS;
- dados derivados: índices e RAG;
- segredos: gerenciador de segredos.

Em conflito, não escolha silenciosamente. Identifique as fontes e solicite decisão humana quando a precedência não estiver definida.
