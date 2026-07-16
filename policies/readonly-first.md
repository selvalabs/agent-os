# Política — Read-only first

## Regra

Conectores externos, Notion, bancos, VPS, provedores e produção começam em modo de leitura.

A escrita exige:

1. pedido humano explícito;
2. objeto e escopo definidos;
3. impacto previsto;
4. plano de reversão quando aplicável;
5. confirmação adicional para exclusão, migração destrutiva ou produção.

## Não fazer

- inferir autorização de escrita a partir de uma pergunta;
- ampliar escopo sem avisar;
- alterar permissões;
- apagar evidências ou logs;
- substituir conteúdo existente quando uma adição resolve.
