# Política — Uso seguro de VPS

## Padrão

A primeira sessão é de inventário e somente leitura.

## Antes de escrever

- confirmar host e ambiente;
- identificar serviço, usuário e diretório;
- capturar estado relevante sem segredos;
- verificar backup ou rollback;
- limitar comandos ao serviço alvo;
- obter autorização explícita.

## Proibido sem autorização específica

- apagar volumes, bancos, diretórios ou containers;
- alterar firewall, SSH, usuários ou permissões globais;
- reiniciar a VPS inteira;
- editar vários serviços de uma vez;
- copiar chaves privadas ou variáveis secretas para logs.
