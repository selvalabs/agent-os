# Workflow — {{PROJECT_NAME}}

## Preparação

1. Ler `AGENTS.md`.
2. Verificar estado do Git.
3. Definir objetivo e fora de escopo.
4. Identificar testes relevantes.

## Implementação

1. Criar branch ou worktree quando adequado.
2. Fazer a menor mudança coerente.
3. Não misturar refatoração ampla com correção pontual.
4. Manter compatibilidade e migração quando necessário.

## Validação

- testes: `{{TEST_COMMAND}}`
- lint: `{{LINT_COMMAND}}`
- build: `{{BUILD_COMMAND}}`
- revisão de diff;
- verificação de segredos e arquivos inesperados.

## Entrega

Registrar o que mudou, evidências, risco residual e próxima ação em `HANDOFF.md` ou no pull request.
