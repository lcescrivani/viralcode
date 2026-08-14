# 36 — ARQUITETURA DE AUTENTICAÇÃO E AUTORIZAÇÃO

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define como o ViralCode irá identificar usuários e controlar o que cada usuário pode acessar ou executar.

A arquitetura separa claramente:

```text
AUTENTICAÇÃO
→ quem é o usuário?

AUTORIZAÇÃO
→ o que esse usuário pode fazer?
```

---

# 2. Princípio fundamental

Nenhum recurso privado deverá depender somente da interface.

A regra será:

```text
Frontend
→ experiência

Backend
→ autoridade
```

---

# 3. Fluxo geral

```text
USUÁRIO
   ↓
LOGIN
   ↓
AUTENTICAÇÃO
   ↓
IDENTIDADE
   ↓
AUTORIZAÇÃO
   ↓
SERVIÇO
   ↓
RECURSO
```

---

# 4. Autenticação

A autenticação deverá permitir:

```text
cadastro
login
identificação do usuário
expiração de sessão
logout/invalidação
```

---

# 5. Cadastro

Endpoint definido no documento da API:

```http
POST /api/v1/autenticacao/cadastro
```

Entrada:

```json
{
  "nome": "Nome",
  "email": "usuario@exemplo.com",
  "senha": "senha"
}
```

A senha deverá ser transformada em hash antes de ser persistida.

---

# 6. Senha

Nunca armazenar:

```text
senha em texto puro
```

Armazenar somente:

```text
senha_hash
```

utilizando mecanismo seguro de hash de senha.

---

# 7. Login

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

O backend deverá:

```text
localizar usuário
 ↓
verificar status
 ↓
validar senha
 ↓
criar sessão/token
```

---

# 8. Usuário bloqueado

Se o usuário estiver:

```text
BLOQUEADO
```

o login deverá ser recusado.

---

# 9. Usuário pendente

Se houver estado:

```text
PENDENTE
```

o comportamento deverá seguir a regra de negócio definida para o cadastro.

---

# 10. Identidade autenticada

Após autenticação, o backend deverá possuir uma identidade confiável para a requisição.

Exemplo conceitual:

```text
usuario_id = 123
```

Essa identidade deverá vir do mecanismo de autenticação, e não de um campo enviado livremente pelo frontend.

---

# 11. Token

Caso o projeto utilize JWT ou mecanismo equivalente, o token deverá conter somente as informações necessárias.

Não colocar:

```text
senha
token do Instagram
segredo da IA
```

dentro do token.

---

# 12. Expiração

A credencial de autenticação deverá possuir tempo de validade.

Não utilizar sessão infinita como padrão.

---

# 13. Renovação

Caso seja adotado mecanismo de renovação:

```text
token de acesso
+
mecanismo de renovação
```

deverão possuir regras próprias de segurança.

A implementação final deverá escolher uma estratégia consistente.

---

# 14. Armazenamento no frontend

A forma de armazenamento da sessão deverá ser escolhida considerando segurança contra:

```text
XSS
roubo de sessão
exposição de credenciais
```

Não escolher uma solução somente por simplicidade de implementação.

---

# 15. Logout

O logout deverá encerrar ou invalidar a sessão conforme o mecanismo adotado.

---

# 16. Sessão expirada

Quando a API responder:

```http
401 Unauthorized
```

o frontend deverá:

```text
identificar sessão inválida
 ↓
limpar estado de autenticação
 ↓
redirecionar para login
```

---

# 17. Autorização

Depois de identificar o usuário, o backend deverá verificar se ele pode executar a operação.

Exemplo:

```text
usuario 10
 ↓
conteúdo 100
 ↓
conteúdo pertence ao perfil do usuário?
 ↓
SIM → permitido
NÃO → negado
```

---

# 18. Regra de propriedade

Recursos do usuário deverão ser protegidos por propriedade.

Exemplo:

```text
Conteudo
 ↓
Perfil
 ↓
Usuario
```

A API deverá verificar essa cadeia quando necessário.

---

# 19. Não confiar no usuario_id

Nunca aceitar:

```json
{
  "usuario_id": 999
}
```

como prova de propriedade.

A identidade deverá vir da sessão autenticada.

---

# 20. Exemplo de ataque

Usuário A envia:

```text
GET /api/v1/conteudos/500
```

onde o conteúdo 500 pertence ao usuário B.

O backend deverá responder:

```text
403
```

ou:

```text
404
```

conforme a estratégia adotada para não revelar existência de recursos.

---

# 21. Perfis

Um usuário poderá possuir múltiplos perfis.

```text
Usuario
 ├── Perfil A
 ├── Perfil B
 └── Perfil C
```

---

# 22. Conta social

Uma conta social pertence ao contexto autorizado do usuário.

O backend deverá verificar:

```text
ContaSocial
 ↓
Perfil
 ↓
Usuario autenticado
```

---

# 23. Conteúdo

Acesso a conteúdo próprio deverá respeitar:

```text
Conteudo
 ↓
Perfil
 ↓
Usuario
```

---

# 24. Publicação

Antes de publicar:

```text
Conteudo
 ↓
Perfil
 ↓
Usuario
 ↓
ContaSocial
 ↓
usuário possui autorização?
```

---

# 25. Análise

Antes de analisar conteúdo privado:

```text
Conteudo
 ↓
propriedade
 ↓
autorização
 ↓
análise
```

---

# 26. Geração de conteúdo

A geração deverá usar o perfil autenticado e autorizado.

Não permitir que um usuário use:

```text
insights
aprendizados
contexto privado
```

de outro usuário.

---

# 27. Área administrativa

A Área Administrativa possuirá autorização adicional.

```text
USUÁRIO
→ acesso ao próprio contexto

ADMINISTRADOR
→ acesso administrativo autorizado
```

---

# 28. Permissão administrativa

No MVP, poderá existir uma permissão simples:

```text
ADMINISTRADOR
```

A arquitetura deverá permitir expansão futura.

---

# 29. Perfis administrativos futuros

Poderão existir:

```text
ADMINISTRADOR
SUPORTE
OPERADOR
ANALISTA
```

---

# 30. Regra de backend

Toda rota:

```text
/api/v1/admin/*
```

deverá verificar autorização administrativa.

---

# 31. Frontend não é segurança

O frontend poderá ocultar:

```text
menu Administração
```

para usuários comuns.

Mas isso não substitui:

```text
autorização no FastAPI
```

---

# 32. Middleware/dependência

O backend deverá possuir mecanismo centralizado para verificar:

```text
usuário autenticado
```

e:

```text
usuário administrador
```

evitando duplicação em todas as rotas.

---

# 33. Autorização por serviço

Além da rota, serviços críticos deverão respeitar as regras de domínio.

Exemplo:

```text
rota
 ↓
autorização
 ↓
serviço
 ↓
regra de negócio
```

---

# 34. Privilégio mínimo

Cada usuário deverá receber somente o acesso necessário.

---

# 35. Segregação

Não misturar:

```text
dados do usuário
```

com:

```text
dados administrativos
```

sem necessidade.

---

# 36. Tokens do Instagram

O token da rede social não é o mesmo que o token de autenticação do usuário.

São credenciais diferentes:

```text
TOKEN DO USUÁRIO
→ acesso ao ViralCode

TOKEN DO INSTAGRAM
→ acesso autorizado à plataforma social
```

---

# 37. Proteção do token Instagram

O token Instagram deverá:

```text
ser protegido
não aparecer no frontend
não aparecer em logs
não aparecer em respostas comuns da API
```

---

# 38. Chaves de IA

A chave do provedor de IA deverá permanecer no backend.

```text
React
  X
  → chave IA

FastAPI
  ↓
provedor IA
```

---

# 39. Banco

A senha do MySQL jamais deverá estar:

```text
frontend
token
resposta API
```

---

# 40. CORS

A API deverá permitir somente origens necessárias.

---

# 41. HTTPS

Produção deverá utilizar:

```text
HTTPS
```

---

# 42. Proteção contra força bruta

O login deverá considerar:

```text
rate limiting
```

e mecanismos de proteção contra tentativas excessivas.

---

# 43. Rate limiting prioritário

Prioridade:

```text
login
cadastro
geração IA
descoberta
análise
publicação
```

---

# 44. Tentativas de login

O sistema poderá registrar:

```text
sucesso
falha
data
correlation_id
```

sem registrar a senha.

---

# 45. Auditoria

Ações administrativas relevantes deverão ser registradas.

Exemplo:

```text
ADMINISTRADOR
 ↓
BLOQUEOU USUÁRIO
 ↓
AUDITORIA
```

---

# 46. Não registrar segredo

Auditoria e logs nunca deverão conter:

```text
senha
token
client_secret
chave privada
```

---

# 47. Correlation ID

As operações deverão possuir um identificador para rastreamento.

Exemplo:

```text
X-Correlation-ID: 8b71...
```

---

# 48. Controle de acesso a recursos

Toda operação deverá responder à pergunta:

```text
quem está executando?
```

e:

```text
qual recurso está sendo acessado?
```

---

# 49. Ações sensíveis

Operações como:

```text
desconectar Instagram
publicar
cancelar publicação
bloquear usuário
```

deverão possuir validações adicionais quando necessário.

---

# 50. Publicação

A publicação deverá validar:

```text
usuário
perfil
conteúdo
conta social
estado do conteúdo
estado da conta
```

antes de executar.

---

# 51. Idempotência

Operações de publicação deverão possuir proteção contra duplicidade.

---

# 52. Sessão administrativa

Sessões administrativas deverão ter controles adequados e, futuramente, poderão exigir:

```text
2FA
reauthentication
tempo de sessão reduzido
```

---

# 53. MVP

No MVP, implementar:

```text
cadastro
login
logout/invalidação conforme mecanismo
senha com hash
sessão/token
autorização por usuário
autorização administrativa
isolamento de recursos
proteção de credenciais
rate limiting básico
```

---

# 54. Futuro

Posteriormente:

```text
2FA
múltiplos perfis administrativos
gestão avançada de sessões
revogação global
detecção de comportamento suspeito
```

---

# 55. Fluxo de login

```text
Frontend
   ↓
POST /autenticacao/login
   ↓
FastAPI
   ↓
validar usuário
   ↓
validar senha
   ↓
validar status
   ↓
criar sessão/token
   ↓
Frontend
```

---

# 56. Fluxo de requisição protegida

```text
Frontend
   ↓
Authorization
   ↓
FastAPI
   ↓
autenticar
   ↓
identificar usuário
   ↓
autorizar
   ↓
Serviço
   ↓
Recurso
```

---

# 57. Fluxo administrativo

```text
Frontend Admin
   ↓
Authorization
   ↓
FastAPI
   ↓
autenticar
   ↓
verificar ADMINISTRADOR
   ↓
Serviço Administrativo
   ↓
Recurso
   ↓
Auditoria quando aplicável
```

---

# 58. Fluxo de acesso negado

```text
requisição
 ↓
autenticação
 ↓
identidade
 ↓
autorização
 ↓
NEGADO
 ↓
403
```

---

# 59. Usuário não autenticado

```text
requisição
 ↓
sem credencial válida
 ↓
401
```

---

# 60. Recurso inexistente

```text
requisição
 ↓
recurso não encontrado
 ↓
404
```

---

# 61. Recurso de outro usuário

O backend deverá escolher entre:

```text
403
```

ou:

```text
404
```

conforme a estratégia de segurança e exposição de existência do recurso.

A decisão deverá ser consistente em toda a API.

---

# 62. Regra de consistência

Não permitir que uma rota trate:

```text
recurso de outro usuário → 403
```

e outra:

```text
recurso de outro usuário → 200
```

por erro de implementação.

---

# 63. Testes de autorização

Os testes deverão verificar pelo menos:

```text
usuário acessa próprio recurso
usuário não acessa recurso de outro
admin acessa área administrativa
usuário comum não acessa admin
usuário bloqueado não acessa sistema
sessão expirada não acessa recurso
```

---

# 64. Teste crítico

Sempre criar teste para:

```text
IDOR
```

ou seja, tentativa de acessar recurso de outro usuário alterando o identificador.

---

# 65. Exemplo

```text
Usuário A
possui conteúdo 100

Usuário B
tenta:

GET /api/v1/conteudos/100
```

Resultado esperado:

```text
acesso negado
```

---

# 66. Autorização em cascata

Quando necessário:

```text
usuario
 ↓
perfil
 ↓
conta social
 ↓
conteúdo
 ↓
publicação
```

deverá ser validado.

---

# 67. Não duplicar autenticação

A autenticação deverá ser centralizada.

Não criar uma implementação diferente para:

```text
conteúdo
Instagram
publicação
admin
```

---

# 68. Não duplicar autorização

As regras comuns deverão ser reutilizadas.

---

# 69. Exceções

Algumas operações administrativas poderão possuir regras adicionais.

Exemplo:

```text
bloquear usuário
```

---

# 70. Proteção de endpoints internos

Mesmo endpoints que aparentemente serão chamados somente pelo frontend deverão ser protegidos quando manipularem dados privados.

---

# 71. Endpoints públicos

Somente endpoints realmente públicos deverão ser acessíveis sem autenticação.

Exemplo:

```text
POST /autenticacao/cadastro
POST /autenticacao/login
GET /health
```

---

# 72. Health

O endpoint de saúde não deverá retornar:

```text
senha
configuração interna
token
stack trace
```

---

# 73. Ambiente local

No desenvolvimento poderá haver facilidades controladas.

Porém:

```text
atalho local ≠ comportamento de produção
```

---

# 74. Produção

Produção deverá utilizar:

```text
HTTPS
segredos reais protegidos
CORS restrito
rate limiting
autorização
logs seguros
```

---

# 75. Variáveis de ambiente

Segredos deverão vir de configuração segura.

Exemplos:

```text
CHAVE_JWT
BANCO_SENHA
INSTAGRAM_CLIENT_SECRET
CHAVE_PROVEDOR_IA
```

---

# 76. Regra para agentes de IA

Antes de alterar autenticação ou autorização:

1. ler este documento;
2. verificar contratos da API;
3. verificar modelo Usuario;
4. verificar segurança;
5. verificar impacto nas rotas;
6. criar testes;
7. não criar atalhos;
8. atualizar documentação.

---

# 77. Regra contra atalhos perigosos

Nunca resolver um problema de desenvolvimento:

```text
removendo autenticação
desabilitando autorização
aceitando usuario_id enviado pelo cliente
liberando CORS globalmente
colocando segredo no frontend
```

---

# 78. Critério de sucesso

A autenticação e autorização estarão adequadas quando:

```text
usuário consegue entrar
+
usuário só acessa seus recursos
+
admin acessa somente área autorizada
+
usuário comum não acessa admin
+
credenciais ficam protegidas
+
sessões podem expirar
+
operações críticas são rastreáveis
```

---

# 79. Arquitetura resumida

```text
                    REQUISIÇÃO
                         │
                         ▼
                     FASTAPI
                         │
                 ┌───────┴───────┐
                 ▼               ▼
           AUTENTICAÇÃO     CORRELATION ID
                 │
                 ▼
              USUÁRIO
                 │
                 ▼
           AUTORIZAÇÃO
           ┌─────┴─────┐
           ▼           ▼
        USUÁRIO       ADMIN
           │           │
           └─────┬─────┘
                 ▼
              SERVIÇO
                 │
                 ▼
             RECURSO
```

---

# 80. Regra final

> **Autenticação identifica. Autorização protege. O frontend facilita. O backend decide.**

Essa separação deverá permanecer como princípio estrutural do ViralCode.

**Versão:** 1.0  
**Status:** Documento oficial da Arquitetura de Autenticação e Autorização
