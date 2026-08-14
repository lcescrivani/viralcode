from fastapi import APIRouter
from pydantic import BaseModel


class RespostaSaude(BaseModel):
    status: str


roteador_saude = APIRouter(tags=["saude"])


@roteador_saude.get("/saude", response_model=RespostaSaude)
def consultar_saude() -> RespostaSaude:
    """Confirma que a API está disponível, sem expor detalhes internos."""
    return RespostaSaude(status="ok")
