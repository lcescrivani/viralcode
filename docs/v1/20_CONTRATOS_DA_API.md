# 20 — CONTRATOS DA API

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define o contrato inicial entre:

```text
React
  ↓
API REST
  ↓
FastAPI
  ↓
Serviços
```

O objetivo é garantir que frontend e backend possam evoluir de forma independente sem quebrar a comunicação.

---

# 2. Princípio fundamental

A API será responsável por expor capacidades do sistema.

Ela não deverá conter a regra de negócio completa.

Arquitetura:

```text
React
   ↓
Rotas FastAPI
   ↓
Serviços
   ↓
Repositórios / Conectores
```

---

# 3. Tecnologia

Backend:

```text
FastAPI
```

Frontend:

```text
React
```

Comunicação:

```text
HTTP
JSON
REST
```

Banco:

```text
MySQL
```

---

# 4. Idioma

A API do ViralCode deverá utilizar português do Brasil como padrão conceitual.

Exemplos:

```text
/perfis
/conteudos
/publicacoes
/aprendizados
```

Campos:

```text
nome
descricao
status
criado_em
atualizado_em
```

---

# 5. Exceções

Algumas nomenclaturas poderão permanecer em inglês quando forem exigidas por:

```text
HTTP
OAuth
JWT
JSON
bibliotecas
protocolos
plataformas externas
```

Essas exceções não devem contaminar desnecessariamente o domínio interno.

---

# 6. URL base

Desenvolvimento:

```text
http://localhost:9000
```

Produção:

```text
https://api.<dominio-do-viralcode>
```

O domínio definitivo será definido no documento de infraestrutura.

---

# 7. Versionamento

A API deverá possuir versão.

Exemplo:

```text
/api/v1
```

Todas as rotas públicas do MVP deverão utilizar:

```text
/api/v1
```

---

# 8. Formato padrão

As requisições e respostas utilizarão:

```text
application/json
```

quando não houver necessidade de envio de arquivo.

---

# 9. Identificadores

Os recursos deverão possuir identificadores únicos.

Exemplo:

```json
{
  "id": 123
}
```

A tecnologia e formato definitivo do identificador serão definidos na implementação do banco.

---

# 10. Datas

As APIs deverão utilizar formato ISO 8601.

Exemplo:

```text
2026-08-13T23:30:00-03:00
```

O backend deverá manter consistência de fuso horário.

---

# 11. Paginação

Listagens poderão utilizar:

```text
pagina
tamanho
```

Exemplo:

```text
GET /api/v1/conteudos?pagina=1&tamanho=20
```

A implementação poderá evoluir para cursor quando houver necessidade.

---

# 12. Resposta paginada

Modelo:

```json
{
  "itens": [],
  "pagina": 1,
  "tamanho": 20,
  "total": 100
}
```

---

# 13. Erros

As respostas de erro deverão possuir estrutura consistente.

Exemplo:

```json
{
  "erro": {
    "codigo": "CONTEUDO_NAO_ENCONTRADO",
    "mensagem": "Conteúdo não encontrado.",
    "detalhes": null
  }
}
```

---

# 14. Códigos HTTP

Utilizar códigos HTTP de acordo com a situação.

Exemplos:

```text
200 → sucesso
201 → criado
204 → sem conteúdo
400 → requisição inválida
401 → não autenticado
403 → não autorizado
404 → não encontrado
409 → conflito
422 → validação
429 → limite
500 → erro interno
502 → falha de integração externa
503 → serviço indisponível
```

---

# 15. Autenticação

As rotas protegidas deverão exigir autenticação.

Exemplo conceitual:

```text
Authorization: Bearer <token>
```

O mecanismo definitivo será definido no documento de autenticação.

---

# 16. Usuários

### Criar usuário

```http
POST /api/v1/usuarios
```

Exemplo:

```json
{
  "nome": "Leonardo",
  "email": "usuario@exemplo.com",
  "senha": "********"
}
```

Resposta:

```json
{
  "id": 1,
  "nome": "Leonardo",
  "email": "usuario@exemplo.com"
}
```

A senha nunca deverá aparecer na resposta.

---

# 17. Login

```http
POST /api/v1/autenticacao/login
```

Resposta conceitual:

```json
{
  "token": "...",
  "tipo": "Bearer"
}
```

---

# 18. Perfil

### Listar perfis

```http
GET /api/v1/perfis
```

### Criar perfil

```http
POST /api/v1/perfis
```

Exemplo:

```json
{
  "nome": "Perfil de Casamento",
  "nicho_id": 1,
  "publico": "Casais",
  "posicionamento": "Relacionamentos",
  "tom_de_voz": "Direto e acolhedor"
}
```

---

# 19. Consultar perfil

```http
GET /api/v1/perfis/{id}
```

---

# 20. Alterar perfil

```http
PUT /api/v1/perfis/{id}
```

---

# 21. Nichos

### Listar

```http
GET /api/v1/nichos
```

### Criar

```http
POST /api/v1/nichos
```

No MVP, o cadastro poderá ser simples.

---

# 22. Contas sociais

### Listar contas

```http
GET /api/v1/contas-sociais
```

### Iniciar conexão Instagram

```http
GET /api/v1/contas-sociais/instagram/conectar
```

A resposta poderá redirecionar o usuário para o fluxo oficial de autenticação.

---

# 23. Retorno da conexão

O provedor externo retornará informações para uma rota de callback.

Exemplo:

```http
GET /api/v1/contas-sociais/instagram/callback
```

O tratamento exato deverá seguir o mecanismo oficial de autenticação escolhido.

---

# 24. Status da conta social

```http
GET /api/v1/contas-sociais/{id}
```

Resposta:

```json
{
  "id": 1,
  "plataforma": "instagram",
  "nome_usuario": "@perfil",
  "status": "CONECTADA"
}
```

Nunca retornar token.

---

# 25. Desconectar conta

```http
DELETE /api/v1/contas-sociais/{id}
```

O comportamento deverá preservar histórico de publicações e métricas quando necessário.

---

# 26. Descoberta

### Iniciar descoberta

```http
POST /api/v1/descobertas
```

Exemplo:

```json
{
  "perfil_id": 1,
  "plataforma": "instagram",
  "nicho": "casamento",
  "tema": "dialogo",
  "visualizacoes_minimas": 1000000
}
```

---

# 27. Resultado da descoberta

```http
GET /api/v1/descobertas/{id}
```

Resposta conceitual:

```json
{
  "id": 10,
  "status": "CONCLUIDA",
  "itens": [
    {
      "conteudo_id": 123,
      "plataforma": "instagram",
      "autor": "@perfil",
      "url": "...",
      "visualizacoes": 1500000
    }
  ]
}
```

---

# 28. Importante sobre descoberta

A API do ViralCode não deverá prometer ao frontend que toda pesquisa textual será atendida diretamente pelo Instagram.

A resposta deverá representar o que a estratégia de descoberta conseguiu obter.

Estados possíveis:

```text
CONCLUIDA
SEM_RESULTADOS
PARCIAL
ERRO
```

---

# 29. Conteúdos

### Listar

```http
GET /api/v1/conteudos
```

Filtros futuros:

```text
perfil_id
origem
tipo
status
tema
```

---

# 30. Consultar conteúdo

```http
GET /api/v1/conteudos/{id}
```

---

# 31. Conteúdo externo

O frontend poderá consultar informações normalizadas:

```json
{
  "id": 123,
  "origem": "EXTERNO",
  "plataforma": "instagram",
  "autor": "@perfil",
  "url": "...",
  "data_publicacao": "2026-08-10T19:00:00-03:00"
}
```

---

# 32. Análise

### Solicitar análise

```http
POST /api/v1/conteudos/{id}/analisar
```

Resposta:

```json
{
  "id": 50,
  "conteudo_id": 123,
  "status": "CONCLUIDA"
}
```

---

# 33. Consultar análise

```http
GET /api/v1/conteudos/{id}/analise
```

---

# 34. Padrões

### Listar padrões

```http
GET /api/v1/padroes
```

Filtros:

```text
perfil_id
tipo
status
```

---

# 35. Insights

```http
GET /api/v1/insights
```

Filtros futuros:

```text
perfil_id
tema
confianca
status
```

---

# 36. Planejamento

### Listar calendário

```http
GET /api/v1/planejamento
```

Filtros:

```text
perfil_id
data_inicio
data_fim
status
```

---

# 37. Criar item de planejamento

```http
POST /api/v1/planejamento
```

Exemplo:

```json
{
  "perfil_id": 1,
  "data_planejada": "2026-08-20",
  "horario_planejado": "19:00",
  "tema": "dialogo",
  "formato": "REEL",
  "objetivo": "IDENTIFICACAO",
  "prioridade": "ALTA"
}
```

---

# 38. Alterar planejamento

```http
PUT /api/v1/planejamento/{id}
```

---

# 39. Cancelar planejamento

```http
DELETE /api/v1/planejamento/{id}
```

Quando necessário, o backend poderá preservar o histórico através do status:

```text
CANCELADO
```

em vez de exclusão física.

---

# 40. Criação de conteúdo

### Gerar conteúdo

```http
POST /api/v1/conteudos/gerar
```

Exemplo:

```json
{
  "perfil_id": 1,
  "tema": "dialogo",
  "formato": "REEL",
  "objetivo": "IDENTIFICACAO"
}
```

Resposta:

```json
{
  "conteudos": [
    {
      "id": 201,
      "titulo": "...",
      "hook": "...",
      "roteiro": "...",
      "cta": "..."
    }
  ]
}
```

---

# 41. Regra de geração

A geração deverá respeitar:

```text
perfil
nicho
tom de voz
aprendizados
padrões
objetivo
formato
```

---

# 42. Aprovação

### Aprovar conteúdo

```http
POST /api/v1/conteudos/{id}/aprovar
```

Resposta:

```json
{
  "id": 201,
  "status": "APROVADO"
}
```

---

# 43. Rejeição

No MVP poderá existir:

```http
POST /api/v1/conteudos/{id}/rejeitar
```

Exemplo:

```json
{
  "motivo": "Precisa de um hook mais forte."
}
```

---

# 44. Publicação

### Publicar

```http
POST /api/v1/publicacoes
```

Exemplo:

```json
{
  "conteudo_id": 201,
  "conta_social_id": 1
}
```

---

# 45. Resultado da publicação

```json
{
  "id": 500,
  "status": "PUBLICANDO"
}
```

Ou:

```json
{
  "id": 500,
  "status": "PUBLICADO",
  "url_publicacao": "..."
}
```

---

# 46. Consultar publicação

```http
GET /api/v1/publicacoes/{id}
```

---

# 47. Desempenho

### Consultar desempenho

```http
GET /api/v1/desempenho/publicacoes/{id}
```

Resposta:

```json
{
  "publicacao_id": 500,
  "atual": {
    "visualizacoes": 100000,
    "curtidas": 5000,
    "comentarios": 300
  }
}
```

---

# 48. Atualizar métricas

```http
POST /api/v1/desempenho/publicacoes/{id}/atualizar
```

A atualização deverá utilizar o conector da plataforma.

---

# 49. Histórico de métricas

```http
GET /api/v1/desempenho/publicacoes/{id}/historico
```

---

# 50. Aprendizados

### Listar

```http
GET /api/v1/aprendizados
```

Filtros:

```text
perfil_id
tipo
escopo
status
confianca
```

---

# 51. Consultar aprendizado

```http
GET /api/v1/aprendizados/{id}
```

---

# 52. Evidências

O frontend poderá consultar as evidências relacionadas:

```http
GET /api/v1/aprendizados/{id}/evidencias
```

---

# 53. IA

As execuções de IA não deverão ser necessariamente expostas diretamente ao usuário.

Quando necessário para diagnóstico:

```http
GET /api/v1/ia/execucoes/{id}
```

deverá possuir proteção adequada.

---

# 54. Health check

A API deverá possuir:

```http
GET /health
```

Resposta:

```json
{
  "status": "ok"
}
```

---

# 55. Health detalhado

Futuramente:

```http
GET /health/detalhado
```

Poderá verificar:

```text
API
Banco
serviços essenciais
```

Não retornar segredos.

---

# 56. Estrutura padrão de sucesso

Não é obrigatório envolver todas as respostas em um campo `dados`.

O projeto poderá retornar diretamente o recurso quando isso deixar o contrato mais simples.

Exemplo:

```json
{
  "id": 1,
  "nome": "Perfil"
}
```

---

# 57. Validação

O FastAPI deverá validar:

```text
tipos
campos obrigatórios
tamanho
valores permitidos
formatos
```

---

# 58. Erros de validação

Exemplo:

```json
{
  "erro": {
    "codigo": "DADOS_INVALIDOS",
    "mensagem": "Existem campos inválidos.",
    "detalhes": [
      {
        "campo": "visualizacoes_minimas",
        "mensagem": "Deve ser maior ou igual a zero."
      }
    ]
  }
}
```

---

# 59. Idempotência

Operações sensíveis poderão aceitar uma chave de idempotência.

Exemplo:

```text
Idempotency-Key
```

Especialmente:

```text
publicação
```

Isso deverá ser implementado antes de permitir ações que possam gerar duplicidade.

---

# 60. Integrações externas

Erros vindos de Instagram ou IA deverão ser traduzidos para códigos internos.

Exemplo:

```text
INSTAGRAM_AUTENTICACAO_INVALIDA
```

em vez de expor diretamente a resposta interna da plataforma.

---

# 61. Segurança

Nunca retornar:

```text
senha
senha_hash
token
client_secret
segredos
```

---

# 62. Logs

As requisições poderão ser registradas com:

```text
método
rota
usuário
tempo
status
correlation_id
```

Nunca registrar credenciais.

---

# 63. Correlation ID

As requisições deverão possuir um identificador de rastreamento quando necessário.

Exemplo:

```text
X-Correlation-ID
```

Isso facilitará diagnóstico entre:

```text
API
serviço
conector
IA
```

---

# 64. Documentação automática

O FastAPI deverá gerar documentação OpenAPI.

Interfaces esperadas:

```text
/docs
/openapi.json
```

O acesso em produção poderá ser protegido conforme a estratégia de segurança.

---

# 65. Compatibilidade

Mudanças incompatíveis deverão exigir nova versão da API.

Exemplo:

```text
/api/v1
```

para:

```text
/api/v2
```

Não quebrar silenciosamente contratos existentes.

---

# 66. Regras para o frontend

O React não deverá:

```text
acessar MySQL
chamar Instagram diretamente
conter token do Instagram
conter chave secreta da IA
implementar regra de negócio crítica
```

Tudo deverá passar pela API.

---

# 67. Regras para o backend

As rotas não deverão:

```text
acessar SQL diretamente
chamar API externa diretamente
conter prompts gigantes
implementar toda a regra de negócio
```

Preferir:

```text
Rota
 ↓
Serviço
 ↓
Conector/Repositório
```

---

# 68. Fluxo completo da API

```text
React
  ↓
FastAPI
  ↓
Autenticação
  ↓
Rota
  ↓
Serviço
  ↓
┌──────────────┬───────────────┐
↓              ↓               ↓
Repositório   Conector       IA
↓              ↓               ↓
MySQL        Instagram       Modelo
```

---

# 69. Contrato da descoberta

Fluxo:

```text
POST /descobertas
        ↓
ServicoDescoberta
        ↓
Conector
        ↓
Instagram
        ↓
normalização
        ↓
MySQL
        ↓
GET /descobertas/{id}
```

---

# 70. Contrato da criação

```text
POST /conteudos/gerar
        ↓
ServicoCriacao
        ↓
Aprendizados
        ↓
Prompts
        ↓
IA
        ↓
Conteúdo
        ↓
MySQL
```

---

# 71. Contrato da publicação

```text
POST /publicacoes
        ↓
ServicoPublicacao
        ↓
validar
        ↓
ConectorInstagram
        ↓
Instagram
        ↓
Publicacao
```

---

# 72. Contrato do desempenho

```text
POST /desempenho/publicacoes/{id}/atualizar
        ↓
ServicoDesempenho
        ↓
ConectorInstagram
        ↓
Instagram
        ↓
MetricasPublicacao
        ↓
MySQL
```

---

# 73. Contrato do aprendizado

O aprendizado poderá ser atualizado internamente:

```text
Desempenho
   ↓
ServicoAprendizado
   ↓
Evidências
   ↓
Aprendizado
```

No MVP, não é necessário permitir que o usuário edite diretamente o aprendizado.

---

# 74. Regra de domínio

A API não deverá permitir:

```text
publicar conteúdo não aprovado
```

quando essa regra estiver ativa no MVP.

---

# 75. Regra de perfil

Uma conta social deverá pertencer a um perfil autorizado pelo usuário.

Não permitir acesso cruzado.

---

# 76. Regra de isolamento

Um usuário deverá acessar somente:

```text
seus perfis
suas contas
seus conteúdos
suas publicações
seus aprendizados
```

---

# 77. Regra de transação

Operações que alteram múltiplas entidades deverão utilizar transação quando necessário.

Exemplo:

```text
aprovar conteúdo
+
criar publicação
```

A estratégia transacional deverá ser definida no serviço.

---

# 78. Não expor detalhes internos

Não retornar ao frontend:

```text
stack trace
SQL
tokens
segredos
resposta completa de erro externo
```

---

# 79. Limites

Rotas sensíveis poderão possuir limites de requisição.

Exemplo:

```text
geração de IA
descoberta
publicação
```

O mecanismo definitivo será definido na infraestrutura.

---

# 80. MVP

As rotas prioritárias serão:

```text
POST /autenticacao/login

GET  /perfis
POST /perfis

GET  /contas-sociais
GET  /contas-sociais/instagram/conectar
GET  /contas-sociais/instagram/callback

POST /descobertas
GET  /descobertas/{id}

GET  /conteudos
GET  /conteudos/{id}
POST /conteudos/{id}/analisar
POST /conteudos/gerar
POST /conteudos/{id}/aprovar

POST /publicacoes
GET  /publicacoes/{id}

GET  /desempenho/publicacoes/{id}
POST /desempenho/publicacoes/{id}/atualizar

GET /aprendizados

GET /planejamento
POST /planejamento
PUT /planejamento/{id}
```

---

# 81. Rotas que podem ficar para depois

```text
campanhas
experimentos
A/B
múltiplas redes
faturamento
equipes
administração avançada
webhooks complexos
```

---

# 82. Testes de API

Cada rota importante deverá possuir testes para:

```text
sucesso
dados inválidos
não autenticado
sem permissão
não encontrado
conflito
erro externo
```

---

# 83. Contrato como fonte de verdade

Quando frontend e backend divergirem:

```text
este documento
+
OpenAPI
```

deverão ser utilizados para resolver a definição do contrato.

---

# 84. Regra para agentes de IA

Antes de alterar uma API:

1. ler este documento;
2. verificar o modelo de dados;
3. verificar o serviço correspondente;
4. preservar o padrão de resposta;
5. preservar os códigos de erro;
6. não colocar regra de negócio na rota;
7. não expor credenciais;
8. atualizar OpenAPI;
9. atualizar testes;
10. atualizar este documento se o contrato mudar.

---

# 85. Arquitetura

```text
                         REACT
                           │
                           ▼
                      API REST
                           │
                           ▼
                        FASTAPI
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          SERVIÇOS     AUTENTICAÇÃO    VALIDAÇÃO
             │
      ┌──────┼──────────────┐
      ▼      ▼              ▼
 REPOSITÓRIO CONECTOR       IA
      │      │              │
      ▼      ▼              ▼
   MYSQL  INSTAGRAM      PROVEDOR IA
```

---

# 86. Regra final

> **A API é o contrato entre a interface e o domínio do ViralCode. Ela deve ser simples, previsível, versionada e independente dos detalhes internos de banco, Instagram ou provedor de IA.**

O objetivo do MVP é possuir uma API pequena, mas capaz de sustentar o ciclo principal:

```text
DESCOBRIR
   ↓
ANALISAR
   ↓
CRIAR
   ↓
APROVAR
   ↓
PUBLICAR
   ↓
MEDIR
   ↓
APRENDER
```

**Versão:** 1.0  
**Status:** Documento oficial dos Contratos da API
