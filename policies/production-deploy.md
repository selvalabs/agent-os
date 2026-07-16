# Política — Deploy de produção

Todo deploy de produção requer:

1. mudança revisada;
2. testes e build aprovados;
3. versão ou commit identificável;
4. backup quando há dados ou migração;
5. plano de rollback;
6. autorização humana;
7. verificação pós-deploy;
8. registro do resultado.

Falha de smoke test deve interromper a progressão e acionar rollback conforme o runbook do projeto.
