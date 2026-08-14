# 08 — API REST DO VIRALCODE

**Versão:** 0.1  
**Status:** Documento inicial  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode  
**Backend:** FastAPI  
**Formato:** REST + JSON  
**Versão da API:** v1

---

## 1. Objetivo deste documento

Este documento define o contrato inicial da API REST do ViralCode.

A API será o ponto de comunicação entre:

```text
React
  ↓
API ViralCode
  ↓
Serviços
  ↓
Repositórios / Provedores
```

O objetivo é garantir que:

- frontend e backend tenham contratos claros;
- agentes de IA não inventem endpoints diferentes;
- regras de negócio não fiquem nas rotas;
- a API possa evoluir sem quebrar clientes existentes;
- todas as APIs sejam documentadas em português.

---

# 2. Princípios da API

A API deverá seguir:

- REST;
- HTTP;
- JSON;
- versionamento;
- nomes em português;
- respostas previsíveis;
- erros padronizados;
- validação de entrada;
- documentação automática do FastAPI.

---

# 3. URL base

A API deverá utilizar:

```text
/api/v1
```

Exemplos:

```text
/api/v1/saude
/api/v1/buscas
/api/v1/conteudos
```

---

# 4. Versionamento

A primeira versão será:

```text
v1
```

Portanto:

```text
/api/v1/...
```

Uma nova versão deverá ser criada quando houver alteração incompatível com clientes existentes.

Não criar `v2` apenas para pequenas melhorias compatíveis.

---

# 5. Padrão de nomes

Os recursos utilizarão português.

Exemplos:

```text
/buscas
/conteudos
/autores
/metricas
```

Evitar:

```text
/searches
/contents
/authors
/metrics
```

---

# 6. Métodos HTTP

Utilizar os métodos HTTP de acordo com a operação.

### GET

Consulta.

### POST

Criação ou execução de operação.

### PUT

Substituição completa quando necessária.

### PATCH

Atualização parcial.

### DELETE

Exclusão quando aplicável.

No MVP, a maior parte das operações será:

```text
GET
POST
```

---

# 7. Endpoint de saúde

## `GET /api/v1/saude`

Objetivo:

Verificar se a API está funcionando.

Resposta:

```json
{
  "status": "ok"
}
```

---

# 8. Endpoint de saúde completo

Poderá futuramente existir:

```text
GET /api/v1/saude/detalhada
```

Com informações como:

```json
{
  "status": "ok",
  "banco_de_dados": "ok",
  "provedor": "ok"
}
```

Essa versão não é obrigatória no primeiro MVP.

---

# 9. Criar uma busca

## `POST /api/v1/buscas`

Executa uma pesquisa de conteúdos.

### Requisição

```json
{
  "termo": "casamento",
  "plataforma": "instagram",
  "visualizacoes_minimas": 1000000,
  "periodo_dias": 90
}
```

---

# 10. Campos da busca

| Campo | Tipo | Obrigatório | Descrição |
|---|---|---:|---|
| termo | string | Sim | Termo ou nicho pesquisado |
| plataforma | string | Sim | Plataforma da pesquisa |
| visualizacoes_minimas | inteiro | Sim | Mínimo de visualizações |
| periodo_dias | inteiro | Não | Período em dias |

---

# 11. Validações da busca

O backend deverá validar:

### `termo`

Não pode ser vazio.

Exemplo inválido:

```json
{
  "termo": ""
}
```

### `plataforma`

Deve ser uma plataforma suportada.

Inicialmente:

```text
instagram
```

### `visualizacoes_minimas`

Deve ser maior ou igual a zero.

### `periodo_dias`

Quando informado, deve ser maior que zero.

---

# 12. Resposta da busca

Exemplo:

```json
{
  "id": 123,
  "termo": "casamento",
  "plataforma": "instagram",
  "visualizacoes_minimas": 1000000,
  "periodo_dias": 90,
  "quantidade_resultados": 3,
  "resultados": [
    {
      "posicao": 1,
      "conteudo": {
        "id": 100,
        "plataforma": "instagram",
        "identificador_externo": "abc123",
        "tipo": "reel",
        "url": "https://...",
        "legenda": "Exemplo",
        "data_publicacao": "2026-08-10T12:00:00"
      },
      "autor": {
        "id": 20,
        "nome_usuario": "perfil_exemplo",
        "nome": "Perfil Exemplo",
        "url_perfil": "https://..."
      },
      "metricas": {
        "visualizacoes": 18000000,
        "curtidas": 820000,
        "comentarios": 12000
      }
    }
  ]
}
```

---

# 13. Regra importante sobre métricas

Os campos de métricas que não forem fornecidos pelo provedor poderão ser `null`.

Exemplo:

```json
{
  "visualizacoes": 18000000,
  "curtidas": 820000,
  "comentarios": null
}
```

Não transformar automaticamente:

```text
null
```

em:

```text
0
```

porque significam situações diferentes.

---

# 14. Listar buscas

## `GET /api/v1/buscas`

Retorna pesquisas realizadas.

Exemplo:

```text
GET /api/v1/buscas?limite=20&pagina=1
```

Resposta:

```json
{
  "pagina": 1,
  "limite": 20,
  "total": 2,
  "resultados": [
    {
      "id": 123,
      "termo": "casamento",
      "plataforma": "instagram",
      "data_criacao": "2026-08-13T20:00:00"
    }
  ]
}
```

A paginação poderá ser simplificada no MVP.

---

# 15. Consultar uma busca

## `GET /api/v1/buscas/{id}`

Retorna uma busca específica.

Exemplo:

```text
GET /api/v1/buscas/123
```

Resposta:

```json
{
  "id": 123,
  "termo": "casamento",
  "plataforma": "instagram",
  "visualizacoes_minimas": 1000000,
  "periodo_dias": 90,
  "quantidade_resultados": 37
}
```

---

# 16. Resultados de uma busca

## `GET /api/v1/buscas/{id}/resultados`

Retorna os conteúdos encontrados por uma busca.

Exemplo:

```text
GET /api/v1/buscas/123/resultados
```

A resposta deverá manter a posição do ranking original.

---

# 17. Listar conteúdos

## `GET /api/v1/conteudos`

Permite consultar conteúdos armazenados.

Filtros futuros:

```text
plataforma
autor
data_publicacao
visualizacoes_minimas
tipo
```

No MVP, apenas filtros necessários deverão ser implementados.

---

# 18. Consultar conteúdo

## `GET /api/v1/conteudos/{id}`

Retorna um conteúdo específico.

Exemplo:

```text
GET /api/v1/conteudos/100
```

Resposta:

```json
{
  "id": 100,
  "plataforma": "instagram",
  "identificador_externo": "abc123",
  "tipo": "reel",
  "url": "https://...",
  "legenda": "Exemplo",
  "data_publicacao": "2026-08-10T12:00:00",
  "autor": {
    "id": 20,
    "nome_usuario": "perfil_exemplo"
  },
  "metrica_atual": {
    "visualizacoes": 18000000,
    "curtidas": 820000,
    "comentarios": 12000,
    "data_coleta": "2026-08-13T22:00:00"
  }
}
```

---

# 19. Histórico de métricas

## `GET /api/v1/conteudos/{id}/metricas`

Retorna o histórico de métricas de um conteúdo.

Exemplo:

```text
GET /api/v1/conteudos/100/metricas
```

Resposta:

```json
{
  "conteudo_id": 100,
  "metricas": [
    {
      "visualizacoes": 100000,
      "curtidas": 5000,
      "comentarios": 100,
      "data_coleta": "2026-08-13T10:00:00"
    },
    {
      "visualizacoes": 500000,
      "curtidas": 25000,
      "comentarios": 800,
      "data_coleta": "2026-08-13T18:00:00"
    }
  ]
}
```

---

# 20. Consultar autor

## `GET /api/v1/autores/{id}`

Retorna informações de um autor.

Exemplo:

```json
{
  "id": 20,
  "plataforma": "instagram",
  "identificador_externo": "perfil123",
  "nome_usuario": "perfil_exemplo",
  "nome": "Perfil Exemplo",
  "url_perfil": "https://..."
}
```

---

# 21. Contrato de erro

Todos os erros da API deverão possuir estrutura consistente.

Formato recomendado:

```json
{
  "erro": {
    "codigo": "TERMO_INVALIDO",
    "mensagem": "O termo de pesquisa não pode ser vazio."
  }
}
```

---

# 22. Categorias de erro

As categorias principais serão:

```text
ERRO_VALIDACAO
ERRO_NEGOCIO
ERRO_AUTENTICACAO
ERRO_AUTORIZACAO
ERRO_PROVEDOR
ERRO_BANCO_DADOS
ERRO_INTERNO
```

Nem todas serão necessárias no MVP.

---

# 23. Erros de validação

Exemplo:

```http
400 Bad Request
```

Resposta:

```json
{
  "erro": {
    "codigo": "DADOS_INVALIDOS",
    "mensagem": "Visualizações mínimas deve ser maior ou igual a zero."
  }
}
```

---

# 24. Erros do provedor

Se a SocialKit estiver indisponível:

```http
502 Bad Gateway
```

Exemplo:

```json
{
  "erro": {
    "codigo": "PROVEDOR_INDISPONIVEL",
    "mensagem": "Não foi possível consultar a fonte de conteúdos."
  }
}
```

Não expor:

- chave da API;
- URL interna;
- stack trace;
- detalhes secretos.

---

# 25. Erro de limite do provedor

Se o provedor retornar limite de requisições:

```http
429 Too Many Requests
```

Resposta:

```json
{
  "erro": {
    "codigo": "LIMITE_PROVEDOR",
    "mensagem": "O limite temporário de consultas foi atingido."
  }
}
```

---

# 26. Erro interno

Erro inesperado:

```http
500 Internal Server Error
```

Resposta pública:

```json
{
  "erro": {
    "codigo": "ERRO_INTERNO",
    "mensagem": "Ocorreu um erro inesperado."
  }
}
```

Detalhes técnicos deverão aparecer apenas nos logs apropriados.

---

# 27. Status HTTP

Uso esperado:

| Situação | HTTP |
|---|---:|
| Sucesso | 200 |
| Criado | 201 |
| Dados inválidos | 400 |
| Não autenticado | 401 |
| Sem permissão | 403 |
| Não encontrado | 404 |
| Conflito | 409 |
| Limite | 429 |
| Erro do provedor | 502 |
| Erro interno | 500 |

Nem todos serão utilizados inicialmente.

---

# 28. Paginação

Listagens deverão utilizar paginação quando houver potencial de grande volume.

Formato inicial:

```text
?page=1&limite=20
```

Resposta:

```json
{
  "pagina": 1,
  "limite": 20,
  "total": 100,
  "resultados": []
}
```

A implementação poderá começar simples.

---

# 29. Ordenação

A ordenação deverá ser explícita quando necessário.

Exemplo:

```text
?ordenar_por=visualizacoes&ordem=desc
```

No MVP, o ranking de uma busca deverá ser:

```text
visualizações DESC
```

---

# 30. Filtros

Filtros deverão utilizar nomes em português.

Exemplos:

```text
?plataforma=instagram
?tipo=reel
?visualizacoes_minimas=1000000
```

Evitar nomes diferentes para o mesmo conceito.

---

# 31. Respostas JSON

Todas as respostas da API de negócio deverão utilizar JSON.

O backend não deverá devolver HTML para operações normais.

---

# 32. Datas na API

As datas deverão utilizar formato ISO 8601.

Exemplo:

```text
2026-08-13T22:30:00
```

Quando houver necessidade de indicar fuso:

```text
2026-08-13T22:30:00-03:00
```

A estratégia definitiva de timezone será definida na implementação.

---

# 33. Identificadores

IDs internos serão retornados como números ou outro tipo definido pelo backend.

Exemplo:

```json
{
  "id": 123
}
```

Identificadores externos serão mantidos em campo separado:

```json
{
  "id": 123,
  "identificador_externo": "abc123"
}
```

---

# 34. Contrato do frontend

O React deverá consumir somente a API do ViralCode.

Não deverá acessar:

```text
MySQL
SocialKit
outras APIs externas
```

diretamente.

Fluxo:

```text
React
  ↓
FastAPI
  ↓
Serviços
```

---

# 35. API e regras de negócio

As rotas não deverão conter regras complexas.

Errado:

```text
Rota
 ├── chama SocialKit
 ├── normaliza
 ├── remove duplicados
 ├── salva banco
 └── monta ranking
```

Correto:

```text
Rota
  ↓
Serviço de Busca
  ├── Provedor
  ├── Normalização
  ├── Deduplicação
  ├── Persistência
  └── Ranking
```

---

# 36. Contrato com o provedor

A API pública do ViralCode não deverá expor o formato da SocialKit.

Exemplo externo:

```json
{
  "externalField": "...",
  "someMetric": 123
}
```

deverá ser convertido para:

```json
{
  "identificador_externo": "...",
  "visualizacoes": 123
}
```

O contrato público pertence ao ViralCode.

---

# 37. Idempotência

Operações que possam ser repetidas deverão evitar criação duplicada.

Exemplo:

```text
mesma busca
+
mesmo conteúdo
```

não deve gerar múltiplos conteúdos iguais.

A regra de unicidade do banco ajuda nesse controle.

---

# 38. Timeout

Chamadas externas deverão possuir timeout.

Nenhuma requisição à SocialKit deverá permanecer indefinidamente aberta.

O valor concreto será definido na implementação e poderá variar conforme a operação.

---

# 39. Retry

Retentativas automáticas não deverão ser adicionadas indiscriminadamente.

Poderão ser utilizadas para erros temporários, como:

```text
timeout
erro de conexão
erro temporário do provedor
```

Não repetir automaticamente erros permanentes.

---

# 40. Logs

A API deverá registrar informações úteis para diagnóstico.

Exemplos:

```text
busca iniciada
busca concluída
provedor consultado
quantidade de resultados
erro de provedor
erro de banco
```

Nunca registrar:

- chaves;
- tokens;
- senhas;
- segredos.

---

# 41. Autenticação futura

A autenticação completa não é obrigatória no MVP.

No futuro, poderá existir:

```text
POST /api/v1/autenticacao/entrada
POST /api/v1/autenticacao/cadastro
POST /api/v1/autenticacao/saida
```

A solução de autenticação será definida antes da implementação.

---

# 42. Usuários e perfis futuros

Quando houver autenticação:

```text
GET /api/v1/usuario
GET /api/v1/perfis
POST /api/v1/perfis
PATCH /api/v1/perfis/{id}
```

Esses endpoints não fazem parte do MVP inicial.

---

# 43. Plataformas futuras

A API deverá ser preparada para novas plataformas.

Exemplo futuro:

```text
GET /api/v1/plataformas
```

Mas o frontend não deverá precisar conhecer detalhes internos de cada provedor.

---

# 44. API futura de análise

Quando o Motor de Inteligência for implementado:

```text
GET /api/v1/conteudos/{id}/analise
POST /api/v1/conteudos/{id}/analisar
```

Poderá retornar:

```json
{
  "tema": "casamento",
  "hook": "...",
  "emocao": "identificação",
  "estrutura": "...",
  "cta": "..."
}
```

Essa API é futura.

---

# 45. API futura de criação

Exemplo conceitual:

```text
POST /api/v1/ideias
POST /api/v1/conteudos/gerar
POST /api/v1/roteiros/gerar
```

Entradas futuras:

```text
perfil
objetivo
tema
plataforma
formato
padrões
```

---

# 46. API futura de publicação

Exemplo:

```text
POST /api/v1/publicacoes
POST /api/v1/publicacoes/{id}/publicar
GET /api/v1/publicacoes/{id}
```

Essa camada ficará isolada do Motor de Criação.

---

# 47. API futura de desempenho

Exemplo:

```text
GET /api/v1/publicacoes/{id}/desempenho
GET /api/v1/conteudos/{id}/desempenho
```

Poderá retornar métricas consolidadas.

---

# 48. API futura de aprendizado

Exemplo conceitual:

```text
GET /api/v1/perfis/{id}/inteligencia
GET /api/v1/perfis/{id}/padroes
```

Essa camada será desenvolvida somente depois que houver dados suficientes.

---

# 49. Documentação automática

FastAPI deverá disponibilizar documentação automática.

A aplicação deverá permitir acesso à documentação durante desenvolvimento.

A documentação automática não substitui este arquivo.

Este documento representa as decisões arquiteturais e de contrato do projeto.

---

# 50. Testes da API

Cada endpoint deverá possuir testes apropriados.

Prioridade:

### P0

```text
GET /api/v1/saude
POST /api/v1/buscas
GET /api/v1/buscas/{id}
GET /api/v1/buscas/{id}/resultados
```

### P1

```text
GET /api/v1/conteudos/{id}
GET /api/v1/conteudos/{id}/metricas
```

### P2

Demais endpoints.

---

# 51. Mock do provedor

Os testes da API não deverão depender exclusivamente da SocialKit real.

Fluxo:

```text
Teste
  ↓
Serviço
  ↓
Provedor falso/mock
  ↓
Resposta controlada
```

Isso permite testar:

- sucesso;
- resultado vazio;
- erro;
- timeout;
- limite;
- dados incompletos.

---

# 52. Resultado vazio

Uma pesquisa sem resultados não deverá ser tratada necessariamente como erro.

Resposta possível:

```json
{
  "id": 123,
  "quantidade_resultados": 0,
  "resultados": []
}
```

HTTP:

```text
200
```

---

# 53. Dados incompletos

Se o provedor retornar um conteúdo sem uma métrica secundária, o sistema deverá preservar o conteúdo quando possível.

Exemplo:

```text
visualizações disponíveis
curtidas indisponíveis
comentários indisponíveis
```

O conteúdo ainda poderá ser válido para o ranking.

---

# 54. Limite de resultados

O MVP deverá possuir limite razoável para evitar consultas excessivamente grandes.

O valor exato será definido na implementação.

O objetivo é evitar:

- consumo excessivo do provedor;
- respostas muito grandes;
- lentidão;
- custo desnecessário.

---

# 55. Segurança da API

A API deverá:

- validar entradas;
- limitar payloads;
- não expor segredos;
- tratar erros;
- evitar SQL direto vindo do usuário;
- controlar CORS;
- utilizar HTTPS em produção.

---

# 56. CORS

Durante desenvolvimento, o frontend local deverá ser autorizado.

Em produção, o CORS deverá ser limitado aos domínios autorizados.

Não utilizar:

```text
allow_origins=["*"]
```

indiscriminadamente em produção.

---

# 57. Rate limiting futuro

O MVP pode não precisar de rate limiting próprio.

No futuro, poderá existir limitação por:

- usuário;
- organização;
- plano;
- IP;
- endpoint.

Especialmente importante para endpoints que consomem APIs externas.

---

# 58. Compatibilidade

Alterações compatíveis poderão ser feitas dentro da mesma versão.

Exemplo:

Adicionar um campo:

```json
{
  "visualizacoes": 1000000,
  "compartilhamentos": 10000
}
```

pode ser compatível.

Já alterar:

```text
visualizacoes
```

para:

```text
views
```

quebraria o contrato e não deve ocorrer sem versionamento adequado.

---

# 59. Regra para agentes de inteligência artificial

Antes de criar um endpoint:

1. verificar se ele já existe;
2. verificar se o recurso já está documentado;
3. verificar se pertence ao MVP;
4. reutilizar endpoints existentes quando apropriado;
5. manter nomes em português;
6. manter o contrato consistente;
7. criar teste;
8. atualizar este documento se houver alteração relevante.

---

# 60. Regra de simplicidade

Não criar endpoints para todas as funcionalidades futuras.

A API inicial deverá ser pequena.

Fluxo mínimo:

```text
saude
buscas
conteudos
metricas
```

A API crescerá junto com o produto.

---

# 61. Contrato mínimo do MVP

Os endpoints prioritários são:

```text
GET  /api/v1/saude

POST /api/v1/buscas

GET  /api/v1/buscas

GET  /api/v1/buscas/{id}

GET  /api/v1/buscas/{id}/resultados

GET  /api/v1/conteudos/{id}

GET  /api/v1/conteudos/{id}/metricas
```

Esse conjunto é suficiente para construir o primeiro fluxo funcional.

---

# 62. Fluxo completo do MVP pela API

```text
React
  │
  │ POST /api/v1/buscas
  ▼
FastAPI
  │
  ▼
Serviço de Busca
  │
  ▼
SocialKit
  │
  ▼
Normalização
  │
  ▼
MySQL
  │
  ▼
Resposta JSON
  │
  ▼
React
  │
  ▼
Ranking
```

---

# 63. Regra final

> **A API é o contrato entre o frontend e o domínio do ViralCode.**

Ela deve ser:

- simples;
- previsível;
- versionada;
- documentada;
- testável;
- independente do provedor externo;
- escrita em português;
- preparada para evolução.

No MVP, a API precisa fazer apenas o necessário para provar:

```text
Pesquisar
   ↓
Encontrar
   ↓
Armazenar
   ↓
Consultar
   ↓
Exibir
```

**Versão atual:** 0.1  
**Status:** Contrato inicial da API REST do ViralCode
