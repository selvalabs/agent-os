---
name: repo-bootstrap
description: Use para preparar um repositório para trabalho com agentes, criando documentação mínima sem sobrescrever arquivos existentes. Não use para reorganizar ou apagar estruturas existentes.
---

# Bootstrap de repositório

## Entrada

- caminho do repositório;
- nome do projeto;
- slug;
- stack e comandos conhecidos;
- classificação de risco.

## Procedimento

1. Inspecione o repositório em modo leitura.
2. Verifique arquivos existentes de agentes.
3. Execute `scripts/bootstrap_repo.py` com `--dry-run`.
4. Revise colisões e placeholders.
5. Execute sem `--dry-run` somente após aprovação.
6. Preencha arquitetura, workflow, segurança e deploy com fatos verificados.
7. Rode `scripts/validate_agent_os.py`.
8. Abra pull request separado.

## Saída

Relatório com arquivos criados, preservados, pendentes e decisões necessárias.
