# ViralCode

O ViralCode é uma aplicação para descobrir, analisar e transformar dados de conteúdo em decisões editoriais. Esta primeira etapa entrega somente a fundação executável do MVP.

## Tecnologias

- Frontend: React, TypeScript e Vite;
- Backend: Python, FastAPI, Pydantic e SQLAlchemy;
- Banco de dados: MySQL com Alembic;
- Ambiente local: Docker Compose.

## Executar localmente

1. Copie `.env.exemplo` para `.env` e substitua as senhas de exemplo por valores locais seguros.
2. Execute `docker compose up --build`.
3. Acesse o frontend em `http://localhost:5173` e a API em `http://localhost:9000`.
4. Verifique a API em `http://localhost:9000/api/v1/saude`.

## Validação

Com os contêineres ativos, execute:

```text
docker compose exec backend pytest
docker compose exec backend ruff check .
docker compose exec backend alembic upgrade head
docker compose exec frontend npm run lint
docker compose exec frontend npm run build
```

## Estrutura

- `backend/`: API, configuração, banco e migrações;
- `frontend/`: interface React;
- `docs/`: especificação oficial do projeto.

As decisões arquiteturais e o escopo do produto estão em `docs/v1/`.
