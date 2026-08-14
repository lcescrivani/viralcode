# 34 — CONTRATOS DA API REST

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define os contratos REST do backend do ViralCode.

Ele estabelece:

```text
rotas
métodos HTTP
autenticação
entrada
saída
status HTTP
erros
paginação
filtros
identificação
```

O objetivo é permitir que:

```text
React
   ↓
API REST
   ↓
FastAPI
   ↓
Serviços
```

trabalhem com contratos claros e estáveis.

---

# 2. Princípio fundamental

A API será:

```text
REST
JSON
versionada
autenticada
documentada
```

Prefixo inicial:

```text
/api/v1
```

---

# 3. Idioma

Os nomes das rotas, campos de negócio, esquemas e códigos internos deverão seguir o padrão definido para o projeto:

```text
Português
```

Exemplo:

```http
GET /api/v1/perfis
```

e não:

```http
GET /api/v1/profiles
```

---

# 4. Exceção — termos técnicos

Alguns nomes técnicos poderão permanecer no padrão internacional quando forem parte do protocolo ou biblioteca.

Exemplos:

```text
HTTP
JSON
JWT
OAuth
URL
HTTPS
GET
POST
PUT
PATCH
DELETE
```

---

# 5. Estrutura de URL

Padrão:

```text
/api/v1/{recurso}
```

Exemplo:

```text
/api/v1/perfis
```

---

# 6. Recursos principais

A API deverá contemplar inicialmente:

```text
autenticacao
usuarios
perfis
contas-sociais
descobertas
conteudos
analises
insights
aprendizados
publicacoes
metricas
ia
administracao
```

Nem todos precisarão ser implementados simultaneamente no MVP.

---

# 7. Autenticação

Endpoints públicos iniciais:

```http
POST /api/v1/autenticacao/cadastro
POST /api/v1/autenticacao/login
```

Endpoints protegidos deverão utilizar o mecanismo de autenticação definido no documento de segurança.

---

# 8. Cabeçalho de autenticação

Quando utilizado token:

```http
Authorization: Bearer <token>
```

---

# 9. Correlation ID

As requisições deverão suportar:

```http
X-Correlation-ID
```

Quando o cliente não enviar, o backend poderá gerar um.

---

# 10. Resposta de sucesso

As respostas deverão possuir JSON consistente.

Exemplo:

```json
{
  "dados": {
    "id": 1,
    "nome": "Perfil Casamento"
  }
}
```

---

# 11. Resposta de lista

Exemplo:

```json
{
  "dados": [],
  "paginacao": {
    "pagina": 1,
    "por_pagina": 20,
    "total": 100,
    "total_paginas": 5
  }
}
```

---

# 12. Resposta de erro

Formato recomendado:

```json
{
  "erro": {
    "codigo": "CONTEUDO_NAO_ENCONTRADO",
    "mensagem": "Conteúdo não encontrado.",
    "correlation_id": "abc123"
  }
}
```

---

# 13. Códigos de erro

Os códigos deverão ser estáveis e legíveis.

Exemplos:

```text
AUTENTICACAO_INVALIDA
ACESSO_NEGADO
RECURSO_NAO_ENCONTRADO
DADOS_INVALIDOS
INSTAGRAM_NAO_CONECTADO
INSTAGRAM_INDISPONIVEL
INSTAGRAM_REAUTENTICACAO_NECESSARIA
IA_INDISPONIVEL
IA_RESPOSTA_INVALIDA
PUBLICACAO_DUPLICADA
PUBLICACAO_FALHOU
ERRO_INTERNO
```

---

# 14. Status HTTP

Usar códigos HTTP adequados.

```text
200 OK
201 Created
204 No Content
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
422 Unprocessable Entity
429 Too Many Requests
500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
```

---

# 15. Regra

Não retornar:

```text
200
```

quando uma operação falhou.

---

# 16. Paginação

Listagens deverão utilizar:

```text
pagina
por_pagina
```

Exemplo:

```http
GET /api/v1/conteudos?pagina=1&por_pagina=20
```

O modelo poderá evoluir para paginação por cursor quando houver necessidade.

---

# 17. Limites

A API deverá possuir limite máximo para:

```text
por_pagina
```

evitando solicitações gigantes.

---

# 18. Ordenação

Quando disponível:

```text
ordenar_por
ordem
```

Exemplo:

```http
GET /api/v1/conteudos?ordenar_por=criado_em&ordem=desc
```

Os campos permitidos deverão ser controlados pelo backend.

---

# 19. Filtros

Filtros deverão utilizar nomes claros.

Exemplo:

```http
GET /api/v1/conteudos?status=APROVADO
```

---

# 20. Cadastro

Endpoint:

```http
POST /api/v1/autenticacao/cadastro
```

Entrada:

```json
{
  "nome": "Nome do usuário",
  "email": "usuario@exemplo.com",
  "senha": "senha"
}
```

Resposta:

```json
{
  "dados": {
    "id": 1,
    "nome": "Nome do usuário",
    "email": "usuario@exemplo.com"
  }
}
```

---

# 21. Login

Endpoint:

```http
POST /api/v1/autenticacao/login
```

Entrada:

```json
{
  "email": "usuario@exemplo.com",
  "senha": "senha"
}
```

Resposta conceitual:

```json
{
  "dados": {
    "token": "..."
  }
}
```

A implementação definitiva poderá utilizar outro mecanismo de sessão.

---

# 22. Usuário atual

Endpoint:

```http
GET /api/v1/usuarios/me
```

Resposta:

```json
{
  "dados": {
    "id": 1,
    "nome": "Nome",
    "email": "usuario@exemplo.com"
  }
}
```

---

# 23. Atualizar usuário

Endpoint:

```http
PATCH /api/v1/usuarios/me
```

Entrada:

```json
{
  "nome": "Novo nome"
}
```

---

# 24. Listar perfis

Endpoint:

```http
GET /api/v1/perfis
```

Filtros futuros poderão incluir:

```text
status
nicho
```

---

# 25. Criar perfil

Endpoint:

```http
POST /api/v1/perfis
```

Entrada:

```json
{
  "nome": "Perfil Casamento",
  "descricao": "Conteúdo sobre casamento",
  "nicho": "casamento",
  "subnicho": "restauracao de casamentos",
  "publico_alvo": "casais",
  "posicionamento": "especialista",
  "tom_de_voz": "direto e acolhedor",
  "objetivo": "crescimento"
}
```

---

# 26. Consultar perfil

Endpoint:

```http
GET /api/v1/perfis/{perfil_id}
```

---

# 27. Atualizar perfil

Endpoint:

```http
PATCH /api/v1/perfis/{perfil_id}
```

---

# 28. Excluir/arquivar perfil

A operação deverá seguir a estratégia de exclusão definida no domínio.

Não assumir exclusão física.

---

# 29. Contas sociais

Listar:

```http
GET /api/v1/contas-sociais
```

---

# 30. Iniciar conexão Instagram

Endpoint conceitual:

```http
GET /api/v1/contas-sociais/instagram/conectar
```

A resposta poderá redirecionar ou retornar a URL oficial de autorização conforme a implementação OAuth.

---

# 31. Callback Instagram

Endpoint conceitual:

```http
GET /api/v1/contas-sociais/instagram/callback
```

O callback deverá validar:

```text
state
código
conta
resultado
```

antes de persistir a conexão.

---

# 32. Consultar contas sociais

Resposta:

```json
{
  "dados": [
    {
      "id": 10,
      "plataforma": "INSTAGRAM",
      "identificador_externo": "123456",
      "nome_externo": "@perfil",
      "status": "CONECTADA"
    }
  ]
}
```

Nunca retornar credenciais.

---

# 33. Desconectar conta

Endpoint:

```http
DELETE /api/v1/contas-sociais/{conta_social_id}
```

A operação deverá validar propriedade.

---

# 34. Iniciar descoberta

Endpoint:

```http
POST /api/v1/descobertas
```

Entrada conceitual:

```json
{
  "perfil_id": 1,
  "tema": "casamento",
  "palavras_chave": [
    "casamento",
    "relacionamento"
  ],
  "filtros": {
    "minimo_visualizacoes": 1000000
  }
}
```

Os filtros efetivamente suportados dependerão das capacidades da integração oficial.

---

# 35. Resultado da descoberta

Resposta conceitual:

```json
{
  "dados": {
    "id": 100,
    "status": "CONCLUIDA",
    "quantidade_encontrada": 20
  }
}
```

---

# 36. Listar conteúdos

Endpoint:

```http
GET /api/v1/conteudos
```

Filtros possíveis:

```text
perfil_id
origem
tipo
status
tema
data
```

---

# 37. Consultar conteúdo

Endpoint:

```http
GET /api/v1/conteudos/{conteudo_id}
```

---

# 38. Criar conteúdo manual

Endpoint:

```http
POST /api/v1/conteudos
```

Entrada mínima:

```json
{
  "perfil_id": 1,
  "tipo": "REEL",
  "origem": "MANUAL",
  "titulo": "Título"
}
```

---

# 39. Atualizar conteúdo

Endpoint:

```http
PATCH /api/v1/conteudos/{conteudo_id}
```

---

# 40. Analisar conteúdo

Endpoint:

```http
POST /api/v1/conteudos/{conteudo_id}/analisar
```

Resposta síncrona inicial poderá ser:

```json
{
  "dados": {
    "analise_id": 50,
    "status": "CONCLUIDA"
  }
}
```

Se o processamento se tornar assíncrono, o contrato poderá retornar:

```text
PROCESSANDO
```

e um identificador de execução.

---

# 41. Consultar análise

Endpoint:

```http
GET /api/v1/analises/{analise_id}
```

---

# 42. Listar análises

Endpoint:

```http
GET /api/v1/analises
```

Filtros:

```text
perfil_id
conteudo_id
status
```

---

# 43. Gerar conteúdo

Endpoint:

```http
POST /api/v1/conteudos/gerar
```

Entrada conceitual:

```json
{
  "perfil_id": 1,
  "tipo": "REEL",
  "objetivo": "engajamento",
  "tema": "comunicacao no casamento"
}
```

O backend deverá buscar contexto adicional:

```text
perfil
padrões
insights
aprendizados
```

---

# 44. Resultado da geração

Exemplo:

```json
{
  "dados": {
    "conteudo_id": 100,
    "status": "GERADO"
  }
}
```

---

# 45. Aprovar conteúdo

Endpoint:

```http
POST /api/v1/conteudos/{conteudo_id}/aprovar
```

---

# 46. Arquivar conteúdo

Endpoint:

```http
POST /api/v1/conteudos/{conteudo_id}/arquivar
```

---

# 47. Insights

Listar:

```http
GET /api/v1/insights
```

Criar manualmente não é requisito inicial.

---

# 48. Consultar insight

Endpoint:

```http
GET /api/v1/insights/{insight_id}
```

---

# 49. Aprendizados

Listar:

```http
GET /api/v1/aprendizados
```

---

# 50. Consultar aprendizado

Endpoint:

```http
GET /api/v1/aprendizados/{aprendizado_id}
```

---

# 51. Publicações

Listar:

```http
GET /api/v1/publicacoes
```

Filtros:

```text
perfil_id
conteudo_id
conta_social_id
status
data
```

---

# 52. Criar publicação

Endpoint:

```http
POST /api/v1/publicacoes
```

Entrada:

```json
{
  "conteudo_id": 100,
  "conta_social_id": 10
}
```

---

# 53. Agendar publicação

Endpoint:

```http
POST /api/v1/publicacoes
```

Entrada:

```json
{
  "conteudo_id": 100,
  "conta_social_id": 10,
  "agendado_para": "2026-08-20T18:00:00"
}
```

---

# 54. Publicar imediatamente

A API poderá utilizar o mesmo recurso de publicação com:

```text
agendado_para = null
```

ou endpoint específico, caso isso deixe o contrato mais claro.

A decisão final será tomada na implementação.

---

# 55. Consultar publicação

Endpoint:

```http
GET /api/v1/publicacoes/{publicacao_id}
```

---

# 56. Cancelar publicação

Endpoint:

```http
POST /api/v1/publicacoes/{publicacao_id}/cancelar
```

Somente estados canceláveis deverão aceitar a operação.

---

# 57. Métricas

Listar métricas:

```http
GET /api/v1/metricas
```

Filtros:

```text
conteudo_id
publicacao_id
periodo
tipo
```

---

# 58. Coletar métricas

Endpoint conceitual:

```http
POST /api/v1/publicacoes/{publicacao_id}/coletar-metricas
```

A operação utilizará o conector da plataforma.

---

# 59. Execuções de IA

Para usuários comuns, a API poderá disponibilizar apenas informações necessárias ao histórico de suas operações.

Endpoint:

```http
GET /api/v1/ia/execucoes
```

---

# 60. Detalhes da execução IA

Endpoint:

```http
GET /api/v1/ia/execucoes/{execucao_id}
```

Não retornar chaves ou segredos.

---

# 61. Administração

Prefixo:

```text
/api/v1/admin
```

---

# 62. Usuários administrativos

Endpoint:

```http
GET /api/v1/admin/usuarios
```

---

# 63. Consultar usuário administrativo

Endpoint:

```http
GET /api/v1/admin/usuarios/{usuario_id}
```

---

# 64. Bloquear usuário

Endpoint:

```http
POST /api/v1/admin/usuarios/{usuario_id}/bloquear
```

---

# 65. Desbloquear usuário

Endpoint:

```http
POST /api/v1/admin/usuarios/{usuario_id}/desbloquear
```

---

# 66. Perfis administrativos

Endpoint:

```http
GET /api/v1/admin/perfis
```

---

# 67. Contas sociais administrativas

Endpoint:

```http
GET /api/v1/admin/contas-sociais
```

---

# 68. Conteúdos administrativos

Endpoint:

```http
GET /api/v1/admin/conteudos
```

Filtros:

```text
usuario_id
perfil_id
origem
tipo
status
```

---

# 69. Publicações administrativas

Endpoint:

```http
GET /api/v1/admin/publicacoes
```

---

# 70. Execuções de IA administrativas

Endpoint:

```http
GET /api/v1/admin/ia/execucoes
```

Filtros:

```text
usuario_id
perfil_id
tipo
modelo
status
periodo
```

---

# 71. Logs administrativos

Endpoint:

```http
GET /api/v1/admin/logs
```

Filtros:

```text
nivel
evento
correlation_id
usuario_id
periodo
```

O acesso deverá ser protegido.

---

# 72. Auditoria administrativa

Endpoint:

```http
GET /api/v1/admin/auditoria
```

Filtros:

```text
administrador_id
acao
entidade
entidade_id
periodo
```

---

# 73. Dashboard administrativo

Endpoint:

```http
GET /api/v1/admin/dashboard
```

Resposta conceitual:

```json
{
  "dados": {
    "usuarios": 100,
    "perfis": 120,
    "contas_sociais": 95,
    "conteudos": 1500,
    "publicacoes": 300,
    "erros_24h": 4,
    "execucoes_ia_24h": 800
  }
}
```

---

# 74. Health

Endpoint:

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

# 75. Health detalhado

Endpoint futuro:

```http
GET /health/detalhado
```

Poderá verificar:

```text
API
MySQL
dependências essenciais
```

Não deverá expor segredos.

---

# 76. Convenção de recursos

Usar substantivos:

```text
/perfis
/conteudos
/publicacoes
```

Evitar verbos desnecessários:

```text
/getPerfis
/criarConteudo
```

---

# 77. Ações específicas

Ações de negócio que não se encaixem naturalmente em CRUD poderão utilizar:

```text
POST /recurso/{id}/acao
```

Exemplos:

```text
/conteudos/{id}/aprovar
/conteudos/{id}/analisar
/publicacoes/{id}/cancelar
```

---

# 78. PATCH x PUT

Preferir:

```text
PATCH
```

para alterações parciais.

Exemplo:

```http
PATCH /api/v1/perfis/10
```

---

# 79. DELETE

Usar `DELETE` somente quando a operação representar efetivamente remoção/desvinculação.

Não assumir que todo DELETE significa exclusão física.

---

# 80. Idempotência

Operações com efeito externo deverão possuir proteção contra repetição.

Especialmente:

```text
publicação
conexão
operações externas
```

---

# 81. Chave de idempotência

Quando necessário, poderá ser utilizado:

```http
Idempotency-Key: <valor>
```

A necessidade e implementação serão definidas para cada operação.

---

# 82. Timeouts

A API não deverá esperar indefinidamente integrações externas.

---

# 83. Processamento assíncrono

No MVP, operações pequenas poderão ser síncronas.

Quando houver processamento longo:

```text
POST
 ↓
202 Accepted
 ↓
id da execução
 ↓
GET status
```

poderá ser utilizado.

---

# 84. Exemplo de operação assíncrona

```json
{
  "dados": {
    "execucao_id": 123,
    "status": "PROCESSANDO"
  }
}
```

---

# 85. Compatibilidade

Alterações incompatíveis deverão resultar em nova versão da API:

```text
/api/v2
```

Não quebrar silenciosamente:

```text
/api/v1
```

---

# 86. Campos adicionais

A API poderá adicionar campos compatíveis sem necessariamente criar nova versão.

Remover ou alterar significado de campos exige avaliação de compatibilidade.

---

# 87. Validação

FastAPI/Pydantic deverá validar:

```text
tipos
formatos
obrigatoriedade
enum
tamanho
```

antes da execução da regra de negócio.

---

# 88. Regra de negócio

Validação de formato:

```text
Pydantic
```

Regra de negócio:

```text
Serviço
```

Exemplo:

```text
"agendado_para deve estar no futuro"
```

é regra de negócio.

---

# 89. Erros de validação

Resposta poderá seguir:

```json
{
  "erro": {
    "codigo": "DADOS_INVALIDOS",
    "mensagem": "Dados inválidos.",
    "campos": {
      "email": "E-mail inválido."
    },
    "correlation_id": "abc123"
  }
}
```

---

# 90. Segurança

Toda rota deverá ser classificada como:

```text
PÚBLICA
AUTENTICADA
ADMINISTRATIVA
```

---

# 91. Regra de propriedade

Para recursos do usuário:

```text
usuario autenticado
+
recurso pertence ao usuário
```

deverá ser verificado no backend.

---

# 92. Não confiar em IDs enviados

Exemplo:

```json
{
  "perfil_id": 999
}
```

não significa que o usuário tenha acesso ao perfil 999.

---

# 93. Rate limiting

Priorizar proteção em:

```text
login
cadastro
geração IA
descoberta
análise
publicação
```

---

# 94. Documentação automática

O FastAPI poderá gerar documentação OpenAPI.

A documentação deverá ser mantida coerente com os contratos oficiais.

---

# 95. Tags

As rotas deverão ser organizadas por grupos.

Exemplo:

```text
Autenticação
Usuários
Perfis
Contas Sociais
Conteúdos
Análises
Publicações
Métricas
IA
Administração
```

---

# 96. Exemplos

Endpoints importantes deverão possuir exemplos de:

```text
request
response
erro
```

quando isso ajudar o desenvolvimento.

---

# 97. Contrato como fonte de verdade

Antes de implementar frontend e backend, consultar este documento.

Não criar contratos diferentes em cada camada.

---

# 98. Regra para agentes de IA

Antes de criar endpoint:

1. verificar se o recurso já existe;
2. verificar se a rota já existe;
3. verificar request;
4. verificar response;
5. verificar autenticação;
6. verificar autorização;
7. verificar erro;
8. verificar testes;
9. atualizar este documento.

---

# 99. Regra contra duplicação

Não criar:

```text
GET /conteudos-do-usuario
```

se:

```text
GET /conteudos
```

já puder resolver a necessidade através do usuário autenticado.

---

# 100. Critério de sucesso

A API estará adequadamente definida quando:

```text
React sabe o que enviar
+
FastAPI sabe o que receber
+
FastAPI sabe o que responder
+
erros possuem contrato
+
autorização é clara
+
integrações são isoladas
```

---

# 101. Arquitetura resumida

```text
                         REACT
                           │
                           ▼
                    /api/v1/*
                           │
                        FASTAPI
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           ROTAS        SERVIÇOS      ESQUEMAS
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        REPOSITÓRIOS   CONECTORES    PROVEDOR IA
              │            │            │
              ▼            ▼            ▼
            MYSQL       INSTAGRAM       IA
```

---

# 102. Regra final

> **A API é o contrato entre o frontend e o coração do ViralCode. Ela deve ser simples para o cliente, rigorosa no backend e estável o suficiente para permitir que o sistema evolua sem quebrar o que já funciona.**

O padrão oficial será:

```text
/api/v1
   ↓
autenticação
   ↓
recurso
   ↓
serviço
   ↓
persistência / integração
   ↓
resposta padronizada
```

**Versão:** 1.0  
**Status:** Documento oficial dos Contratos da API REST
