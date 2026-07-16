# Modelo de segurança

## Níveis de risco

| Nível | Exemplos | Controle mínimo |
|---|---|---|
| Baixo | leitura de código e documentação | registro da fonte |
| Médio | edição local, testes e criação de branch | diff e validação |
| Alto | merge, alteração de banco e acesso à infraestrutura | aprovação explícita |
| Crítico | deploy, migração destrutiva e uso de segredos | aprovação, backup, rollback e auditoria |

## Orientação versus enforcement

- Markdown explica intenção e contexto.
- Skills padronizam procedimentos.
- CI e hooks verificam condições.
- Permissões e sandbox limitam capacidade.
- Revisão humana autoriza ações de alto impacto.

## Privacidade de documentação

A publicação de documentação também possui risco operacional.

- exemplos públicos usam placeholders;
- URLs, IDs e nomes privados não entram no repositório público;
- conteúdo de clientes ou workspaces internos permanece fora do GitHub público;
- snapshots públicos são revisados antes do commit;
- repositórios privados com histórico sensível não devem apenas trocar de visibilidade;
- a versão pública deve usar histórico novo ou completamente sanitizado;
- issues e pull requests privados não são migrados automaticamente.

Consulte `PUBLIC-SANITIZATION.md`.

## Princípios

- menor privilégio;
- somente leitura como padrão externo;
- credenciais nunca em documentação;
- nenhuma ação destrutiva implícita;
- nenhuma ocultação de falha;
- logs com dados mínimos necessários;
- revogação e rotação após suspeita de exposição;
- contexto privado nunca usado diretamente como exemplo público;
- publicação pública tratada como release de segurança.
