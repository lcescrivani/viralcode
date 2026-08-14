# 22 — AUTENTICAÇÃO E USUÁRIOS

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define a autenticação, identificação e isolamento de usuários no ViralCode.

O objetivo do MVP é possuir uma autenticação simples, segura e suficiente para permitir que cada usuário tenha seus próprios:

```text
perfis
contas sociais
conteúdos
planejamentos
publicações
métricas
aprendizados
```

A arquitetura deverá permitir evolução futura para equipes e organizações sem obrigar o MVP a implementar essa complexidade agora.

---

# 2. Princípio fundamental

O usuário é a raiz de propriedade dos dados do ViralCode.

```text
USUÁRIO
   ↓
PERFIL
   ↓
CONTA SOCIAL
   ↓
CONTEÚDOS
   ↓
PUBLICAÇÕES
   ↓
MÉTRICAS
   ↓
APRENDIZADOS
```

Nenhum usuário deverá conseguir acessar dados pertencentes a outro usuário.

---

# 3. Autenticação do MVP

O MVP utilizará:

```text
e-mail
+
senha
```

O login deverá gerar uma sessão autenticada para utilização da API.

A implementação poderá utilizar token de acesso no padrão:

```text
Authorization: Bearer <token>
```

---

# 4. Não implementar inicialmente

No MVP, não é necessário implementar:

```text
login social com Google
login social com Apple
login social com Facebook
autenticação corporativa
SSO
MFA obrigatório
gestão avançada de organizações
```

Esses recursos poderão ser adicionados posteriormente.

---

# 5. Cadastro

Endpoint definido no contrato da API:

```http
POST /api/v1/usuarios
```

Entrada:

```json
{
  "nome": "Nome do usuário",
  "email": "usuario@exemplo.com",
  "senha": "senha"
}
```

Saída não deverá conter a senha nem o hash da senha.

---

# 6. Regras de cadastro

O sistema deverá validar:

```text
nome obrigatório
e-mail obrigatório
e-mail válido
senha obrigatória
senha com tamanho mínimo
e-mail único
```

---

# 7. E-mail

O e-mail deverá ser armazenado de forma consistente.

Antes de verificar unicidade, o sistema deverá aplicar uma normalização definida pelo serviço.

Exemplo conceitual:

```text
Usuario@Exemplo.com
```

poderá ser tratado como:

```text
usuario@exemplo.com
```

A regra definitiva deverá ser implementada de maneira consistente no cadastro e no login.

---

# 8. Senha

A senha nunca deverá ser armazenada em texto puro.

O banco deverá armazenar:

```text
senha_hash
```

O hash deverá ser produzido por uma biblioteca criptográfica apropriada para armazenamento de senhas.

Não implementar algoritmo criptográfico próprio.

---

# 9. Regras de senha

O MVP deverá exigir uma senha com tamanho mínimo definido na implementação.

A política poderá evoluir posteriormente para exigir:

```text
complexidade
histórico
expiração
MFA
```

Não tornar a política desnecessariamente complexa no MVP.

---

# 10. Login

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
  "token": "...",
  "tipo": "Bearer"
}
```

---

# 11. Token

O token será utilizado para identificar o usuário nas chamadas protegidas.

Exemplo:

```http
Authorization: Bearer eyJ...
```

O conteúdo e mecanismo definitivo do token serão definidos na implementação.

---

# 12. Regra de token

O token não deverá conter dados desnecessários.

O mínimo necessário para identificar o usuário deverá ser suficiente.

Exemplo conceitual:

```text
usuario_id
expiração
```

---

# 13. Expiração

O token deverá possuir prazo de validade.

Não criar tokens permanentes.

A duração exata será definida na implementação conforme o nível de segurança desejado para o MVP.

---

# 14. Logout

No modelo baseado em token, o logout poderá ser tratado no cliente descartando o token.

Caso a implementação utilize sessão revogável ou refresh token, a estratégia deverá ser documentada adicionalmente.

No MVP, não criar uma arquitetura de sessões mais complexa sem necessidade.

---

# 15. Refresh token

Não é obrigatório para a primeira versão.

Se for utilizado, deverá possuir:

```text
expiração
revogação
armazenamento seguro
rotação quando aplicável
```

A decisão será tomada na implementação da autenticação.

---

# 16. Usuário autenticado

Depois da autenticação, as rotas deverão conseguir identificar:

```text
usuario_id
```

A identificação deverá vir da credencial autenticada e não de um campo enviado livremente pelo frontend.

---

# 17. Regra crítica

Não confiar em:

```json
{
  "usuario_id": 999
}
```

enviado pelo cliente para determinar propriedade.

A API deverá obter o usuário autenticado a partir da autenticação.

---

# 18. Isolamento de dados

Exemplo:

```text
Usuário 1
 ├── Perfil 1
 ├── Conta Instagram 1
 └── Conteúdos 1

Usuário 2
 ├── Perfil 2
 ├── Conta Instagram 2
 └── Conteúdos 2
```

Usuário 1 não poderá consultar:

```text
Perfil 2
Conta Instagram 2
Conteúdos 2
```

---

# 19. Autorização

Autenticação responde:

```text
Quem é você?
```

Autorização responde:

```text
Você pode acessar este recurso?
```

O ViralCode deverá implementar os dois conceitos separadamente.

---

# 20. Regra de propriedade

Para recursos pertencentes a um perfil:

```text
recurso
 ↓
perfil_id
 ↓
usuario_id
```

Antes de permitir acesso, o backend deverá verificar essa cadeia de propriedade.

---

# 21. Conta social

Uma conta social deverá pertencer a:

```text
perfil
```

e o perfil deverá pertencer ao:

```text
usuário autenticado
```

Fluxo:

```text
Usuário
   ↓
Perfil
   ↓
Conta Instagram
```

---

# 22. Conteúdo

Conteúdos gerenciados pelo usuário deverão estar associados ao perfil correto.

Não confiar somente no:

```text
conteudo_id
```

recebido pelo cliente.

O serviço deverá verificar se o conteúdo pertence ao contexto do usuário autenticado.

---

# 23. Publicação

Uma publicação deverá estar associada a:

```text
conteúdo
+
conta social
```

E ambos deverão pertencer ao usuário autenticado.

---

# 24. Aprendizado

Aprendizados são dados estratégicos do perfil.

O acesso deverá respeitar:

```text
usuário
 ↓
perfil
 ↓
aprendizado
```

---

# 25. Middleware / dependência

O FastAPI deverá possuir uma forma centralizada de identificar o usuário autenticado.

Conceitualmente:

```python
usuario_atual = obter_usuario_autenticado()
```

As rotas poderão utilizar essa dependência sem implementar novamente a validação do token.

---

# 26. Exemplo de fluxo protegido

```text
Requisição
   ↓
Token
   ↓
Autenticação
   ↓
usuario_id
   ↓
Rota
   ↓
Serviço
   ↓
Validação de propriedade
   ↓
Execução
```

---

# 27. Rotas públicas

Inicialmente poderão ser públicas:

```text
POST /api/v1/usuarios
POST /api/v1/autenticacao/login
GET /health
```

As demais deverão exigir autenticação, salvo decisão explícita posterior.

---

# 28. Rotas protegidas

Exemplos:

```text
GET /api/v1/perfis
POST /api/v1/perfis

GET /api/v1/contas-sociais
GET /api/v1/descobertas

GET /api/v1/conteudos
POST /api/v1/conteudos/gerar

GET /api/v1/planejamento

GET /api/v1/publicacoes

GET /api/v1/aprendizados
```

---

# 29. Erro de autenticação

Quando a credencial estiver ausente ou inválida:

```http
401 Unauthorized
```

Resposta conceitual:

```json
{
  "erro": {
    "codigo": "NAO_AUTENTICADO",
    "mensagem": "É necessário estar autenticado."
  }
}
```

---

# 30. Erro de autorização

Quando o usuário estiver autenticado, mas não possuir acesso:

```http
403 Forbidden
```

Exemplo:

```json
{
  "erro": {
    "codigo": "ACESSO_NEGADO",
    "mensagem": "Você não possui permissão para acessar este recurso."
  }
}
```

---

# 31. Recurso inexistente

Quando o recurso não existir ou não estiver disponível para aquele usuário:

```http
404 Not Found
```

A implementação deverá evitar revelar informações desnecessárias sobre recursos pertencentes a outros usuários.

---

# 32. Tentativas de login

O sistema deverá possuir proteção contra abuso de autenticação.

No MVP, poderá utilizar:

```text
limite de tentativas
```

e:

```text
bloqueio temporário
```

quando necessário.

Não implementar um sistema complexo de detecção de fraude inicialmente.

---

# 33. Mensagens de login

Evitar revelar se um e-mail específico está cadastrado em situações onde isso possa facilitar enumeração de usuários.

Exemplo genérico:

```text
"Credenciais inválidas."
```

em vez de:

```text
"Este e-mail não existe."
```

---

# 34. Recuperação de senha

A recuperação de senha poderá ser implementada após o fluxo básico.

Quando implementada:

```text
solicitação
 ↓
token temporário
 ↓
e-mail
 ↓
nova senha
```

O token deverá possuir expiração e uso único.

---

# 35. E-mail de recuperação

Não armazenar tokens de recuperação em texto puro quando houver uma estratégia segura de armazenamento por hash.

---

# 36. Verificação de e-mail

Não é obrigatória para a primeira versão do MVP.

Poderá ser adicionada posteriormente.

---

# 37. Sessão no frontend

O frontend deverá armazenar a credencial de maneira compatível com a estratégia de segurança escolhida.

Evitar colocar segredos de backend no código do React.

---

# 38. Segredos

Nunca colocar no frontend:

```text
client_secret
senha do banco
chave privada
token de integração
chave secreta do provedor de IA
```

Tudo que for segredo do backend deverá permanecer no ambiente do backend.

---

# 39. Instagram

A autenticação do usuário no ViralCode e a autenticação da conta Instagram são conceitos diferentes.

Fluxo:

```text
USUÁRIO
   ↓
LOGIN VIRALCODE
   ↓
sistema autenticado
   ↓
CONECTAR INSTAGRAM
   ↓
AUTORIZAÇÃO DO INSTAGRAM
```

---

# 40. Token do Instagram

O token obtido para a conta social não deverá ser utilizado como token de autenticação do usuário no ViralCode.

São credenciais diferentes.

```text
Token ViralCode
≠
Token Instagram
```

---

# 41. Armazenamento do token Instagram

O token deverá ser protegido.

A tabela `contas_sociais` poderá possuir:

```text
token_criptografado
token_expira_em
```

A chave utilizada para proteção deverá permanecer fora do banco.

---

# 42. Criptografia

Quando o projeto armazenar credenciais externas, deverá utilizar uma biblioteca de criptografia adequada.

Não criar algoritmo próprio.

---

# 43. Logs de autenticação

Poderão ser registrados:

```text
login realizado
login recusado
logout
conta bloqueada
erro de autenticação
```

Nunca registrar:

```text
senha
senha_hash
token completo
client_secret
```

---

# 44. Auditoria

No MVP, não é necessário criar uma plataforma completa de auditoria.

Entretanto, operações sensíveis poderão ser registradas futuramente:

```text
login
conexão Instagram
desconexão Instagram
publicação
alteração de credenciais
```

---

# 45. Administração

O MVP não precisa de um painel administrativo completo.

Caso exista necessidade operacional, deverá ser criada uma área separada com privilégios específicos.

Não utilizar a conta de usuário comum como administrador por conveniência.

---

# 46. Status do usuário

Estados mínimos:

```text
ATIVO
INATIVO
BLOQUEADO
```

---

# 47. Usuário inativo

Um usuário inativo não deverá conseguir iniciar novas sessões.

Sessões existentes deverão ser tratadas conforme a estratégia de autenticação.

---

# 48. Usuário bloqueado

Um usuário bloqueado não deverá acessar recursos protegidos.

---

# 49. Exclusão

Excluir um usuário não deverá automaticamente apagar de forma irreversível todo o histórico sem uma política definida.

A estratégia de retenção e exclusão deverá ser documentada posteriormente.

---

# 50. Multiusuário futuro

A arquitetura deverá permitir:

```text
Usuário A
   ├── Perfil A1
   └── Perfil A2

Usuário B
   ├── Perfil B1
   └── Perfil B2
```

---

# 51. Equipes futuras

Futuramente poderá existir:

```text
Organização
   ↓
Equipe
   ↓
Usuários
   ↓
Perfis
```

Essa estrutura não faz parte do MVP.

---

# 52. Permissões futuras

Poderão existir papéis como:

```text
ADMINISTRADOR
EDITOR
ANALISTA
VISUALIZADOR
```

Não implementar no MVP sem necessidade.

---

# 53. Banco

A tabela `usuarios` deverá possuir pelo menos:

```text
id
nome
email
senha_hash
ativo
criado_em
atualizado_em
```

---

# 54. Índices

Deverá existir índice/constraint de unicidade para:

```text
email
```

---

# 55. Integridade

Nenhum perfil deverá existir sem:

```text
usuario_id
```

Nenhuma conta social deverá existir sem:

```text
perfil_id
```

---

# 56. Testes de autenticação

Deverão existir testes para:

```text
cadastro
login correto
senha incorreta
e-mail inexistente
token ausente
token inválido
token expirado
usuário inativo
usuário bloqueado
acesso a recurso próprio
acesso a recurso de outro usuário
```

---

# 57. Teste de isolamento

Este é um teste obrigatório.

Cenário:

```text
Usuário A cria Perfil A
Usuário B cria Perfil B
```

Então:

```text
Usuário A tenta acessar Perfil B
```

Resultado esperado:

```text
acesso negado
```

---

# 58. Teste de publicação

Também deverá existir teste garantindo:

```text
Usuário A
   ↓
tenta publicar conteúdo
   ↓
pertencente ao Usuário B
```

Resultado:

```text
acesso negado
```

---

# 59. Regra para IA

Antes de alterar autenticação, uma IA deverá:

1. ler este documento;
2. ler o modelo de dados;
3. ler os contratos da API;
4. preservar isolamento de dados;
5. não expor segredos;
6. não criar autenticação paralela;
7. adicionar testes;
8. atualizar documentação quando necessário.

---

# 60. Estrutura de código

A implementação deverá seguir a estrutura definida:

```text
backend/app/
├── rotas/
│   └── autenticacao.py
│
├── servicos/
│   └── servico_autenticacao.py
│
├── repositorios/
│   └── repositorio_usuario.py
│
├── modelos/
│   └── usuario.py
│
├── esquemas/
│   └── autenticacao.py
│
└── seguranca/
    ├── autenticacao.py
    ├── senhas.py
    └── tokens.py
```

---

# 61. Fluxo de cadastro

```text
React
 ↓
POST /usuarios
 ↓
FastAPI
 ↓
Esquema
 ↓
ServicoAutenticacao
 ↓
validar e-mail
 ↓
gerar hash
 ↓
RepositorioUsuario
 ↓
MySQL
 ↓
resposta
```

---

# 62. Fluxo de login

```text
React
 ↓
POST /autenticacao/login
 ↓
FastAPI
 ↓
ServicoAutenticacao
 ↓
RepositorioUsuario
 ↓
verificar senha
 ↓
gerar token
 ↓
React
```

---

# 63. Fluxo de requisição autenticada

```text
React
 ↓
Bearer Token
 ↓
FastAPI
 ↓
validar token
 ↓
usuario_atual
 ↓
rota
 ↓
serviço
 ↓
validar propriedade
 ↓
executar
```

---

# 64. Regra de simplicidade

O MVP deverá possuir uma autenticação:

```text
simples
segura
testável
documentada
```

Não construir infraestrutura de identidade empresarial antes de existir necessidade.

---

# 65. Critério de sucesso

A autenticação será considerada pronta quando for possível:

```text
cadastrar usuário
      ↓
fazer login
      ↓
receber credencial
      ↓
acessar API protegida
      ↓
identificar usuário
      ↓
acessar seus dados
      ↓
bloquear dados de terceiros
```

---

# 66. Regra final

> **Autenticação identifica o usuário; autorização protege o domínio.**

A segurança do ViralCode não deverá depender de o frontend "esconder" recursos.

Toda proteção importante deverá existir no backend.

O princípio é:

```text
NUNCA CONFIAR NO CLIENTE
```

A API deverá validar sempre:

```text
quem é o usuário
+
o que ele está tentando acessar
+
se ele pode executar a operação
```

**Versão:** 1.0  
**Status:** Documento oficial de Autenticação e Usuários
