# 05 — PILHA TECNOLÓGICA DO VIRALCODE

**Versão:** 0.1  
**Status:** Documento inicial  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo deste documento

Este documento registra as tecnologias adotadas para o ViralCode.

Seu objetivo é evitar decisões inconsistentes durante o desenvolvimento e orientar agentes de inteligência artificial sobre quais tecnologias utilizar.

A regra é:

> **Não trocar uma tecnologia definida neste documento sem uma decisão explícita e documentada.**

---

# 2. Visão geral da pilha

A pilha tecnológica inicial é:

```text
┌───────────────────────────────┐
│           FRONTEND            │
│      React + TypeScript       │
└───────────────┬───────────────┘
                │
                │ HTTP / JSON
                ▼
┌───────────────────────────────┐
│           BACKEND             │
│       Python + FastAPI        │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│          SERVIÇOS             │
│       Regras de negócio       │
└───────────────┬───────────────┘
                │
        ┌───────┴────────┐
        ▼                ▼
┌───────────────┐  ┌────────────────┐
│ REPOSITÓRIOS  │  │   PROVEDORES   │
└───────┬───────┘  └────────┬───────┘
        │                   │
        ▼                   ▼
┌───────────────┐      APIs externas
│  SQLALCHEMY   │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│     MYSQL     │
└───────────────┘
```

---

# 3. Frontend

## Tecnologia

> React

O frontend será responsável pela interface do ViralCode.

---

## 3.1 Linguagem

> TypeScript

O uso de TypeScript será obrigatório no frontend.

Objetivos:

- segurança de tipos;
- melhor manutenção;
- melhor experiência de desenvolvimento;
- redução de erros;
- contratos claros com a API.

---

## 3.2 Ferramenta de desenvolvimento

A ferramenta recomendada para iniciar o frontend é:

> Vite

A decisão poderá ser revista posteriormente se houver uma necessidade concreta.

---

## 3.3 Responsabilidades do frontend

O React deverá cuidar de:

- interface;
- navegação;
- formulários;
- estados da interface;
- carregamento;
- mensagens de erro;
- apresentação dos resultados;
- filtros;
- paginação futura;
- comunicação com a API.

---

## 3.4 O que o frontend não deve fazer

O frontend não deverá:

- acessar diretamente o MySQL;
- acessar diretamente a SocialKit;
- possuir chaves secretas;
- implementar regras de negócio críticas;
- calcular informações que deveriam ser responsabilidade do backend.

Fluxo correto:

```text
React
  ↓
API ViralCode
  ↓
Backend
```

---

# 4. Backend

## Tecnologia

> Python

Python será a linguagem principal do backend.

---

# 5. Framework da API

## Tecnologia

> FastAPI

FastAPI será responsável pela API REST do ViralCode.

---

## 5.1 Responsabilidades

FastAPI será utilizado para:

- endpoints REST;
- validação de dados;
- esquemas de entrada e saída;
- documentação automática;
- tratamento de requisições;
- respostas HTTP;
- dependências da aplicação.

---

## 5.2 Documentação da API

FastAPI fornecerá documentação automática da API.

Os contratos públicos da API deverão também ser documentados em:

```text
docs/08_API.md
```

---

# 6. Validação de dados

## Tecnologia

> Pydantic

Pydantic será utilizado para validação e definição dos dados de entrada e saída da API.

Exemplo conceitual:

```text
Requisição
   ↓
Esquema Pydantic
   ↓
Validação
   ↓
Serviço
```

---

# 7. Banco de dados

## Tecnologia

> MySQL

MySQL será o banco de dados relacional principal do ViralCode.

Motivos:

- maturidade;
- ampla utilização;
- facilidade de hospedagem;
- bom suporte em VPS;
- integração com Python;
- compatibilidade com SQLAlchemy.

---

# 8. ORM

## Tecnologia

> SQLAlchemy

SQLAlchemy será utilizado como camada de acesso e mapeamento objeto-relacional.

Responsabilidades:

- modelos;
- consultas;
- relacionamentos;
- transações;
- persistência.

---

# 9. Migrações

## Tecnologia

> Alembic

Alembic será utilizado para controlar alterações estruturais no banco.

Regra:

> **Alterações de estrutura do banco devem ser representadas por migrations.**

Evitar alterações manuais não documentadas.

---

# 10. Comunicação frontend/backend

O padrão inicial será:

```text
HTTP
+
JSON
+
REST
```

Exemplo:

```text
POST /api/v1/buscas
```

Resposta:

```json
{
  "id": 1,
  "quantidade": 37,
  "resultados": []
}
```

Os contratos serão detalhados em `08_API.md`.

---

# 11. Integrações externas

As integrações externas serão encapsuladas na camada de provedores.

Primeiro provedor planejado:

> SocialKit

Arquitetura:

```text
Serviço
   ↓
Provedor
   ↓
Cliente HTTP
   ↓
API externa
```

---

# 12. Cliente HTTP

O backend precisará de um cliente HTTP para conversar com serviços externos.

A biblioteca específica deverá ser definida durante a implementação inicial, priorizando:

- suporte assíncrono quando necessário;
- timeout;
- tratamento de erros;
- reutilização de conexões;
- facilidade de teste.

A escolha da biblioteca deverá ser registrada se representar uma decisão relevante.

---

# 13. Configuração

Configurações sensíveis e específicas do ambiente deverão ficar fora do código.

Exemplo conceitual:

```text
.env
```

Variáveis esperadas:

```text
AMBIENTE
BANCO_DADOS_URL
CHAVE_SOCIALKIT
NIVEL_LOG
```

Os nomes definitivos serão definidos durante a implementação.

---

# 14. Segredos

Nunca colocar no código:

```python
CHAVE_API = "..."
```

O correto será:

```text
Variável de ambiente
        ↓
Configuração
        ↓
Aplicação
```

O arquivo `.env` não deverá ser versionado.

Deverá existir um arquivo de exemplo, como:

```text
.env.exemplo
```

sem valores secretos reais.

---

# 15. Ambiente local

O desenvolvimento inicial será realizado localmente.

O ambiente deverá possuir:

```text
React
Python
FastAPI
MySQL
```

O objetivo é que qualquer desenvolvedor consiga reproduzir o ambiente.

---

# 16. Docker

Docker poderá ser utilizado para padronização do ambiente.

A configuração prevista poderá conter:

```text
Frontend
Backend
MySQL
```

Exemplo conceitual:

```text
docker-compose.yml
```

Não criar contêineres adicionais sem necessidade.

---

# 17. Desenvolvimento local versus produção

O projeto deverá separar configurações de:

```text
Desenvolvimento
Teste
Produção
```

O mesmo código deverá poder ser executado em ambientes diferentes através de configuração.

---

# 18. VPS

A produção futura será hospedada em:

> VPS da Hostinger

A aplicação não deverá possuir dependência estrutural de recursos exclusivos da Hostinger.

Isso mantém a possibilidade de migração futura.

---

# 19. Servidor web futuro

Na produção, poderá ser utilizado:

> Nginx

Fluxo previsto:

```text
Internet
   ↓
Nginx
   ↓
Aplicação
```

O Nginx poderá posteriormente cuidar de:

- HTTPS;
- domínio;
- encaminhamento;
- arquivos estáticos;
- proxy reverso.

---

# 20. Execução do backend

O backend FastAPI deverá ser executado por um servidor apropriado para produção.

Durante o desenvolvimento poderá utilizar um servidor de desenvolvimento.

A configuração específica será documentada na implantação.

---

# 21. Testes

O projeto deverá possuir testes automatizados.

Para o backend, a ferramenta principal prevista será:

> pytest

Os testes deverão cobrir principalmente:

- serviços;
- regras de negócio;
- repositórios;
- API;
- integrações isoladas por mocks.

---

# 22. Testes do frontend

Os testes do frontend serão definidos conforme as primeiras telas forem implementadas.

A prioridade inicial será:

1. funcionamento da interface;
2. integração com a API;
3. componentes críticos;
4. testes automatizados onde houver benefício real.

Não criar uma estrutura de testes excessivamente complexa antes da necessidade.

---

# 23. Formatação e qualidade de código

O projeto deverá utilizar ferramentas automáticas de qualidade.

No backend, poderão ser utilizados:

- Ruff;
- formatador compatível;
- verificadores de tipos quando aplicável.

No frontend, poderão ser utilizados:

- ESLint;
- Prettier;
- verificadores TypeScript.

As ferramentas exatas e suas configurações deverão ser mantidas no projeto.

---

# 24. Controle de versão

O código será versionado com:

> Git

Repositório remoto poderá ser utilizado posteriormente conforme a estratégia de desenvolvimento.

---

# 25. Estrutura de ambientes

Conceitualmente:

```text
DESENVOLVIMENTO
       ↓
TESTES
       ↓
PRODUÇÃO
```

No início, o foco será:

```text
DESENVOLVIMENTO LOCAL
```

---

# 26. Arquitetura tecnológica do MVP

A combinação oficial é:

```text
Frontend
React
TypeScript
Vite

Backend
Python
FastAPI
Pydantic

Persistência
MySQL
SQLAlchemy
Alembic

Qualidade
pytest
Ruff
ESLint
Prettier

Infraestrutura
Docker
Docker Compose

Controle de versão
Git
```

Algumas ferramentas são recomendadas e poderão ser ajustadas durante a implementação, desde que a decisão seja registrada quando relevante.

---

# 27. O que não faz parte da pilha inicial

Não adicionar automaticamente:

- Kubernetes;
- microsserviços;
- Kafka;
- Redis;
- Elasticsearch;
- filas distribuídas;
- múltiplos bancos;
- GraphQL;
- arquitetura serverless;
- infraestrutura em nuvem complexa.

Essas tecnologias podem ser avaliadas futuramente caso exista uma necessidade real.

---

# 28. Cache

Nenhuma tecnologia de cache é obrigatória no MVP.

Se houver necessidade, uma solução como Redis poderá ser avaliada.

A decisão deverá ser baseada em:

- volume;
- latência;
- custo;
- frequência das consultas;
- carga da API externa.

Não adicionar Redis apenas por antecipação.

---

# 29. Filas

Nenhuma fila é obrigatória no MVP.

Se o processamento passar a exigir tarefas em segundo plano, poderá ser introduzida uma solução apropriada.

A necessidade poderá surgir principalmente em:

- análise de muitos vídeos;
- geração de conteúdo;
- publicação;
- coleta de métricas;
- processamento em lote.

---

# 30. Inteligência artificial

O uso de inteligência artificial será incorporado quando entrar a camada de inteligência/criação.

O provedor de IA não deve ficar diretamente acoplado às regras de negócio.

Arquitetura futura:

```text
Serviço de Inteligência
        ↓
Provedor de IA
        ↓
Modelo de IA
```

Isso permitirá trocar de provedor futuramente.

---

# 31. Armazenamento de arquivos

O MVP não precisa obrigatoriamente de um sistema próprio de armazenamento de arquivos.

Se futuramente houver necessidade de armazenar:

- vídeos;
- imagens;
- áudios;
- thumbnails;
- arquivos gerados;

poderá ser adotado armazenamento de objetos.

A decisão será tomada quando existir necessidade real.

---

# 32. Banco vetorial

Não utilizar banco vetorial no MVP.

Um banco vetorial poderá ser considerado futuramente para:

- busca semântica;
- similaridade;
- recuperação de conhecimento;
- inteligência de conteúdo;
- recomendações.

Só deverá ser introduzido quando houver um caso de uso comprovado.

---

# 33. Observabilidade

No MVP:

- logs básicos;
- tratamento de erros;
- identificação de falhas.

Futuramente:

- métricas;
- alertas;
- monitoramento;
- rastreamento distribuído;
- dashboards operacionais.

---

# 34. Escalabilidade

A estratégia será crescimento gradual.

```text
MVP simples
   ↓
Otimização
   ↓
Cache
   ↓
Processamento assíncrono
   ↓
Filas
   ↓
Trabalhadores
   ↓
Escala horizontal
```

Não começar pela arquitetura de escala máxima.

---

# 35. Dependências

As dependências deverão ser mantidas de forma controlada.

Regras:

- evitar bibliotecas desnecessárias;
- evitar dependências abandonadas;
- preferir bibliotecas maduras;
- fixar versões quando apropriado;
- atualizar periodicamente;
- remover dependências não utilizadas.

---

# 36. Compatibilidade

O projeto deverá definir versões mínimas suportadas para:

- Python;
- Node.js;
- npm;
- MySQL.

As versões concretas serão registradas quando o ambiente inicial for configurado.

Agentes de IA não devem atualizar versões principais automaticamente sem avaliar impacto.

---

# 37. Estrutura de código em português

O ViralCode utilizará nomenclatura em português.

Exemplo:

```python
class ServicoBusca:
    ...

class RepositorioConteudo:
    ...

def buscar_conteudos():
    ...

def salvar_conteudo():
    ...
```

Evitar:

```python
class SearchService:
    ...

class ContentRepository:
    ...

def search_content():
    ...
```

---

# 38. Exceções de nomenclatura

Nomes próprios de tecnologias não serão traduzidos.

Exemplos:

```text
React
FastAPI
Python
SQLAlchemy
MySQL
Docker
Alembic
Git
```

Esses nomes permanecerão conforme suas denominações oficiais.

---

# 39. API em português

Os endpoints também utilizarão português.

Exemplo:

```text
/api/v1/buscas
/api/v1/conteudos
/api/v1/autores
/api/v1/metricas
```

Evitar:

```text
/api/v1/searches
/api/v1/contents
/api/v1/authors
```

A documentação da API também será integralmente em português.

---

# 40. Banco em português

Tabelas e colunas deverão seguir o mesmo padrão.

Exemplo:

```text
conteudos
autores
metricas_conteudo
buscas
perfis
nichos
```

Evitar:

```text
contents
authors
content_metrics
searches
profiles
niches
```

---

# 41. Regra de consistência

A mesma entidade deverá possuir o mesmo nome em todas as camadas.

Exemplo:

```text
Conteúdo
   ↓
Conteudo
   ↓
conteudos
   ↓
ConteudoSchema
   ↓
/conteudos
```

Evitar nomes diferentes para representar a mesma entidade.

---

# 42. Princípio de tecnologia mínima

A pergunta para qualquer nova tecnologia será:

> **Precisamos realmente dela agora?**

Se a resposta for não, não adicionar.

Isso reduz:

- complexidade;
- manutenção;
- custos;
- vulnerabilidades;
- dependências;
- tempo de desenvolvimento.

---

# 43. Regra para agentes de inteligência artificial

Antes de adicionar uma biblioteca ou tecnologia, o agente deverá:

1. verificar se já existe solução no projeto;
2. avaliar se a tecnologia é realmente necessária;
3. considerar custo de manutenção;
4. considerar compatibilidade;
5. evitar dependências desnecessárias;
6. respeitar o padrão em português;
7. registrar decisões importantes.

---

# 44. Stack oficial inicial

A stack oficial do ViralCode é:

```text
REACT
   +
TYPESCRIPT
   +
FASTAPI
   +
PYTHON
   +
PYDANTIC
   +
SQLALCHEMY
   +
MYSQL
   +
ALEMBIC
   +
DOCKER
   +
GIT
```

Ferramentas auxiliares:

```text
Vite
pytest
Ruff
ESLint
Prettier
```

---

# 45. Regra final

> **A melhor tecnologia para o ViralCode é aquela que resolve o problema atual com o menor nível de complexidade possível, sem impedir a evolução futura.**

O MVP não precisa da tecnologia mais sofisticada.

Precisa da tecnologia adequada.

**Versão atual:** 0.1  
**Status:** Pilha tecnológica inicial do ViralCode
