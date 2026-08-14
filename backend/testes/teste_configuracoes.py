from app.configuracoes import Configuracoes


def testar_configuracoes_montam_url_do_banco() -> None:
    configuracoes = Configuracoes(
        ambiente="teste",
        url_publica_api="http://teste.local",
        origens_permitidas="http://teste.local,http://frontend.local",
        banco_host="mysql",
        banco_porta=3306,
        banco_nome="viralcode_teste",
        banco_usuario="usuario_teste",
        banco_senha="senha_teste",
    )

    assert configuracoes.lista_origens_permitidas == [
        "http://teste.local",
        "http://frontend.local",
    ]
    assert configuracoes.url_banco_dados == (
        "mysql+pymysql://usuario_teste:senha_teste@mysql:3306/viralcode_teste"
    )
