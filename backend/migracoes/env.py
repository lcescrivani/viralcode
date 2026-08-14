from logging.config import fileConfig

from alembic import context

from app.banco.base import Base
from app.configuracoes import obter_configuracoes

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

configuracoes = obter_configuracoes()
config.set_main_option("sqlalchemy.url", configuracoes.url_banco_dados)
target_metadata = Base.metadata


def executar_migracoes_offline() -> None:
    context.configure(
        url=configuracoes.url_banco_dados,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def executar_migracoes_online() -> None:
    conectavel = context.config.attributes.get("connection", None)

    if conectavel is None:
        from sqlalchemy import engine_from_config, pool

        conectavel = engine_from_config(
            config.get_section(config.config_ini_section, {}),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
        )

    with conectavel.connect() as conexao:
        context.configure(connection=conexao, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    executar_migracoes_offline()
else:
    executar_migracoes_online()
