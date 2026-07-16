---
name: safe-repo-change
description: Use para implementar uma mudança de código preservando trabalho existente, limitando escopo e produzindo evidências de validação. Não use para deploy ou alterações destrutivas.
---

# Mudança segura em repositório

1. Leia `AGENTS.md` e a documentação roteada.
2. Inspecione `git status` e não descarte mudanças humanas.
3. Defina objetivo, fora de escopo e critérios de aceite.
4. Faça a menor mudança coerente.
5. Rode testes relevantes.
6. Revise o diff por regressões, segredos e arquivos inesperados.
7. Atualize documentação somente quando o comportamento mudou.
8. Produza handoff com evidências e limitações.
