from fastapi.testclient import TestClient

from app.configuracoes import obter_configuracoes
from app.principal import aplicacao


def testar_consulta_de_saude_retorna_status_ok(monkeypatch) -> None:
    variaveis = {
        "AMBIENTE": "teste",
        "URL_PUBLICA_API": "http://teste.local",
        "BANCO_HOST": "mysql",
        "BANCO_PORTA": "3306",
        "BANCO_NOME": "viralcode_teste",
        "BANCO_USUARIO": "usuario_teste",
        "BANCO_SENHA": "senha_teste",
    }
    for nome, valor in variaveis.items():
        monkeypatch.setenv(nome, valor)

    obter_configuracoes.cache_clear()

    with TestClient(aplicacao) as cliente:
        resposta = cliente.get("/api/v1/saude")

    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok"}
