from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

CAMINHO_RAIZ = Path(__file__).resolve().parents[3]


class Configuracoes(BaseSettings):
    """Carrega e valida a configuração necessária à execução da aplicação."""

    ambiente: str = Field(min_length=1)
    debug: bool = False
    nivel_log: str = "INFO"
    url_publica_api: str = Field(min_length=1)
    origens_permitidas: str = ""
    banco_host: str = Field(min_length=1)
    banco_porta: int = Field(ge=1, le=65535)
    banco_nome: str = Field(min_length=1)
    banco_usuario: str = Field(min_length=1)
    banco_senha: str = Field(min_length=1)

    model_config = SettingsConfigDict(
        env_file=CAMINHO_RAIZ / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def lista_origens_permitidas(self) -> list[str]:
        return [origem.strip() for origem in self.origens_permitidas.split(",") if origem.strip()]

    @property
    def url_banco_dados(self) -> str:
        return (
            f"mysql+pymysql://{self.banco_usuario}:{self.banco_senha}"
            f"@{self.banco_host}:{self.banco_porta}/{self.banco_nome}"
        )


@lru_cache
def obter_configuracoes() -> Configuracoes:
    return Configuracoes()
