---
name: safe-deploy
description: Use quando houver deploy autorizado e existir documentação específica do projeto, testes, rollback e verificação. Não use sem aprovação humana ou quando o ambiente não estiver identificado.
---

# Deploy seguro

1. Confirme repositório, ambiente e versão.
2. Leia `docs/agent/DEPLOY.md` e `docs/agent/VPS.md`.
3. Verifique testes, build e migrações.
4. Confirme backup e rollback.
5. Apresente plano e obtenha aprovação.
6. Execute somente o runbook documentado.
7. Rode smoke tests.
8. Em falha, interrompa e aplique rollback previsto.
9. Registre versão, horário, resultado e pendências no handoff.
