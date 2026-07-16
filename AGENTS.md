# AGENTS.md

## Missão

Manter o SelvaLabs Agent OS pequeno, auditável, reutilizável e seguro para múltiplos repositórios.

## Ordem de leitura

1. `START-HERE.md`
2. `docs/architecture/SPEC-AGENT-OS.md`
3. `docs/governance/CANONICAL-SOURCES.md`
4. `docs/governance/SECURITY-MODEL.md`
5. `docs/governance/PUBLIC-SANITIZATION.md`
6. O arquivo relacionado à tarefa em `policies/`, `skills/` ou `templates/`

Não carregue toda a documentação por padrão. Use o `START-HERE.md` para selecionar a rota mínima necessária.

## Regras persistentes

- Preserve alterações humanas existentes.
- Não apague, mova ou renomeie estruturas sem pedido explícito.
- Não grave tokens, senhas, chaves privadas, cookies ou credenciais em Markdown.
- Prefira mudanças pequenas, reversíveis e revisáveis por pull request.
- Não duplique instruções completas entre ferramentas; use adaptadores mínimos.
- Mantenha o `AGENTS.md` como roteador, não como enciclopédia.
- Skills compartilhadas devem possuir `SKILL.md` com `name` e `description`.
- Toda operação de produção deve possuir preflight, aprovação, rollback e verificação.
- Serviços externos começam em modo somente leitura, salvo autorização explícita de escrita.
- Todo novo repositório e toda raiz de conhecimento devem possuir um `START HERE` visível.
- Documentação pública usa exemplos fictícios.
- Não copie nomes, URLs, IDs, registros ou estrutura de workspaces privados para este repositório.
- Antes de publicação pública, use snapshot sanitizado com histórico novo.

## Validação

Antes de concluir uma mudança:

```bash
python scripts/validate_agent_os.py .
```

Quando alterar o bootstrap, teste também em um diretório temporário com `--dry-run` e sem sobrescrever arquivos.

## Fontes canônicas

- Políticas e skills compartilhadas: este repositório.
- Regras locais: repositório consumidor.
- Pesquisa e curadoria: Cérebro editorial criado pelo usuário.
- Memória durável: Biblioteca de Markdowns criada pelo usuário.
- Dados derivados: índices e RAG.
- Segredos: gerenciador de segredos.

Em conflito, não escolha silenciosamente. Pare, identifique as fontes e solicite decisão humana quando a precedência não estiver definida.
