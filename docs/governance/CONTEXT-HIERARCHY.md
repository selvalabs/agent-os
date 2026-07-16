# Hierarquia de contexto

## Objetivo

Carregar apenas o contexto necessário, com precedência previsível e baixo custo de tokens.

## Camadas

1. **Organização:** segurança, compliance e limites inegociáveis.
2. **Operador:** preferências pessoais não compartilhadas.
3. **Agent OS:** políticas e capacidades reutilizáveis.
4. **Repositório:** `AGENTS.md` e documentação operacional.
5. **Diretório:** instruções próximas do código afetado.
6. **Skill:** procedimento carregado sob demanda.
7. **Tarefa:** handoff, issue, PR e pedido atual.

## Regras

- O contexto global deve ser curto.
- Procedimentos extensos pertencem a skills ou runbooks.
- Fatos temporários pertencem a handoffs.
- Fatos estáveis e revisados podem ir para `MEMORY.md`.
- Memória automática da ferramenta é auxiliar e deve ser verificada antes de virar regra.
- Instruções contraditórias devem ser eliminadas, não acumuladas.
