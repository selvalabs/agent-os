# Segurança — {{PROJECT_NAME}}

## Classificação

- Criticidade: {{TODO_CRITICALITY}}
- Dados sensíveis: {{TODO_SENSITIVE_DATA}}
- Serviços externos: {{TODO_EXTERNAL_SERVICES}}

## Controles obrigatórios

Preencha cada linha com a implementação local, o teste e o comando de validação. Use nomes de variáveis e placeholders; nunca registre valores reais.

| Controle | Decisão local | Teste/evidência |
|---|---|---|
| Escopo de autorização | TODO | TODO |
| Configuração fail-closed | TODO | TODO |
| Limites contra abuso | TODO | TODO |
| Fronteira de ingress | TODO | TODO |
| Higiene de secrets | TODO | TODO |

## Regras

- Segredos fora do Git.
- Menor privilégio e autorização por recurso.
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
