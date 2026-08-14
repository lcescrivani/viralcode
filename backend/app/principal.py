from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.configuracoes import obter_configuracoes
from app.rotas.saude import roteador_saude


@asynccontextmanager
async def ciclo_de_vida(_aplicacao: FastAPI):
    obter_configuracoes()
    yield


def criar_aplicacao() -> FastAPI:
    aplicacao = FastAPI(
        title="ViralCode",
        version="0.1.0",
        description="API do ViralCode.",
        lifespan=ciclo_de_vida,
    )
    aplicacao.include_router(roteador_saude, prefix="/api/v1")
    return aplicacao


aplicacao = criar_aplicacao()
