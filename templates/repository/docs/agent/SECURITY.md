# Segurança — {{PROJECT_NAME}}

## Classificação

- Criticidade: {{TODO_CRITICALITY}}
- Dados sensíveis: {{TODO_SENSITIVE_DATA}}
- Serviços externos: {{TODO_EXTERNAL_SERVICES}}

## Regras

- Segredos fora do Git.
- Menor privilégio.
- Escrita externa somente com autorização.
- Alterações destrutivas exigem confirmação específica.
- Logs não devem expor dados pessoais ou credenciais.

## Ações bloqueadas sem aprovação

{{TODO_BLOCKED_ACTIONS}}

## Resposta a incidente

1. interromper propagação;
2. preservar evidências sem copiar segredos;
3. revogar ou rotacionar credenciais expostas;
4. comunicar responsável;
5. registrar impacto e correção.
