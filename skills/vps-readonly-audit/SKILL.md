---
name: vps-readonly-audit
description: Use para inventariar uma VPS sem alterar serviços, arquivos, firewall, usuários ou containers. Não use para correção, reinício ou deploy.
---

# Auditoria somente leitura de VPS

## Objetivo

Produzir inventário mínimo suficiente para planejar uma mudança segura.

## Verificações

- identificação do host e ambiente;
- espaço, memória e carga;
- serviços e containers relevantes;
- portas e proxy do serviço alvo;
- diretórios e versões do projeto;
- estado de logs sem coletar segredos;
- mecanismo de backup e rollback existente.

## Restrições

Nenhum comando deve alterar estado. Não exiba conteúdo de arquivos de segredo. Registre incertezas e solicite autorização separada para qualquer correção.
