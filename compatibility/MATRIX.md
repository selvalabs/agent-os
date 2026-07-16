# Matriz de compatibilidade

| Mecanismo | Uso canônico | Estratégia |
|---|---|---|
| `AGENTS.md` | orientação compartilhada | arquivo principal curto |
| `CLAUDE.md` | adaptador Claude | importar `AGENTS.md` |
| regras por caminho | contexto específico | manter próximo do código |
| skills | procedimento reutilizável | carregar sob demanda |
| hooks | enforcement de ciclo | usar em regras determinísticas |
| MCP | acesso a sistemas | menor privilégio e leitura inicial |
| memória automática | aprendizado auxiliar | revisar antes de promover |
| handoff | continuidade da tarefa | temporário e verificável |
