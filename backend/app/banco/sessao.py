from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.configuracoes import Configuracoes, obter_configuracoes


def criar_engine(configuracoes: Configuracoes | None = None) -> Engine:
    configuracoes = configuracoes or obter_configuracoes()
    return create_engine(configuracoes.url_banco_dados, pool_pre_ping=True)


def criar_fabrica_sessoes(
    configuracoes: Configuracoes | None = None,
) -> sessionmaker[Session]:
    return sessionmaker(bind=criar_engine(configuracoes), autoflush=False, autocommit=False)
