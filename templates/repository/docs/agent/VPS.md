# VPS — {{PROJECT_NAME}}

## Escopo

Este documento contém topologia e runbook, nunca credenciais.

## Ambiente

- Provedor: {{TODO_PROVIDER}}
- Identificador não secreto: {{TODO_HOST_ALIAS}}
- Serviço alvo: {{TODO_SERVICE}}
- Diretório do projeto: {{TODO_PROJECT_DIR}}
- Orquestração: {{TODO_ORCHESTRATION}}

## Auditoria somente leitura

{{TODO_READONLY_CHECKS}}

## Operações autorizadas

{{TODO_ALLOWED_OPERATIONS}}

## Operações proibidas sem confirmação específica

- exclusão de volume ou banco;
- alteração global de firewall ou SSH;
- reinício completo do host;
- mudança em serviço fora do escopo;
- impressão de arquivos de segredo.
