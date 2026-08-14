# 23 — CONFIGURAÇÃO E AMBIENTE

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define como o ViralCode deverá tratar configurações, variáveis de ambiente, segredos e diferenças entre os ambientes de desenvolvimento, teste e produção.

O objetivo é garantir que:

```text
CÓDIGO
≠
CONFIGURAÇÃO
≠
SEGREDOS
≠
DADOS
```

---

# 2. Ambientes

O projeto deverá considerar inicialmente:

```text
DESENVOLVIMENTO
TESTE
PRODUÇÃO
```

Fluxo:

```text
DESENVOLVIMENTO
      ↓
TESTE
      ↓
PRODUÇÃO
```

---

# 3. Regra principal

Nenhuma informação específica de ambiente deverá ser fixada diretamente no código quando puder ser configurada externamente.

Evitar:

```python
senha = "123456"
```

Preferir:

```python
senha = configuracao.banco_senha
```

---

# 4. Arquivo `.env`

No ambiente local poderá existir:

```text
.env
```

Esse arquivo conterá configurações e segredos necessários para execução.

O arquivo:

```text
.env
```

não deverá ser versionado.

---

# 5. Arquivo `.env.example`

O projeto deverá possuir:

```text
.env.example
```

Esse arquivo será versionado e servirá como referência.

Não deverá conter segredos reais.

Exemplo:

```text
BANCO_HOST=localhost
BANCO_PORTA=3306
BANCO_NOME=viralcode
BANCO_USUARIO=viralcode
BANCO_SENHA=

INSTAGRAM_CLIENT_ID=
INSTAGRAM_CLIENT_SECRET=
INSTAGRAM_REDIRECIONAMENTO=

CHAVE_ASSINATURA=
PROVEDOR_IA=
CHAVE_IA=
```

---

# 6. Regra de segurança

Nunca versionar:

```text
.env
tokens
senhas
client_secret
chaves privadas
chaves de API
credenciais do banco
```

---

# 7. Configuração centralizada

O backend deverá possuir uma camada central de configuração.

Estrutura:

```text
backend/app/configuracoes/
├── ambiente.py
├── banco.py
└── aplicacao.py
```

A implementação poderá consolidar esses arquivos posteriormente se isso simplificar o projeto.

---

# 8. Configuração da aplicação

Exemplos:

```text
NOME_APLICACAO
AMBIENTE
MODO_DEBUG
NIVEL_LOG
URL_API
URL_FRONTEND
```

---

# 9. Configuração do banco

Exemplos:

```text
BANCO_HOST
BANCO_PORTA
BANCO_NOME
BANCO_USUARIO
BANCO_SENHA
```

A aplicação deverá montar a conexão através dessas configurações.

---

# 10. Banco de desenvolvimento

Exemplo:

```text
Host: localhost
Porta: 3306
Banco: viralcode
```

Os valores reais deverão estar no ambiente local.

---

# 11. Banco de teste

O banco de teste deverá ser separado do banco de desenvolvimento.

Exemplo:

```text
viralcode_teste
```

Nunca executar testes destrutivos contra o banco de produção.

---

# 12. Banco de produção

A produção deverá possuir:

```text
credenciais próprias
banco próprio
acesso protegido
backup próprio
```

Não reutilizar credenciais de desenvolvimento.

---

# 13. Instagram

A integração deverá possuir configuração própria.

Exemplos:

```text
INSTAGRAM_CLIENT_ID
INSTAGRAM_CLIENT_SECRET
INSTAGRAM_REDIRECIONAMENTO
```

Os nomes definitivos poderão ser ajustados conforme o mecanismo oficial de integração escolhido.

---

# 14. Regra importante sobre Instagram

As configurações deverão refletir o mecanismo de autenticação efetivamente utilizado.

Não criar variáveis para endpoints, permissões ou credenciais que não sejam necessárias.

A configuração deverá ser revisada após a POC da integração do Instagram.

---

# 15. Provedor de IA

O projeto deverá utilizar uma abstração para o provedor de IA.

Configurações conceituais:

```text
PROVEDOR_IA
MODELO_IA
CHAVE_IA
URL_IA
```

Nem todas serão obrigatórias para todos os provedores.

---

# 16. Regra de abstração

O código de negócio não deverá depender diretamente do nome do fornecedor.

Preferir:

```text
ServicoCriacao
      ↓
ProvedorIA
```

em vez de:

```text
ServicoCriacao
      ↓
FornecedorX
```

---

# 17. Chave de assinatura

Se a autenticação utilizar tokens assinados, deverá existir uma configuração secreta.

Exemplo:

```text
CHAVE_ASSINATURA
```

Essa chave nunca deverá aparecer no código ou no Git.

---

# 18. Ambiente

A aplicação deverá saber em qual ambiente está sendo executada.

Exemplo:

```text
AMBIENTE=desenvolvimento
```

ou:

```text
AMBIENTE=teste
```

ou:

```text
AMBIENTE=producao
```

---

# 19. Debug

O modo de depuração deverá ser controlado por configuração.

Desenvolvimento:

```text
MODO_DEBUG=true
```

Produção:

```text
MODO_DEBUG=false
```

Nunca ativar debug de produção por conveniência.

---

# 20. Logs

O nível de log poderá variar por ambiente.

Exemplo:

```text
desenvolvimento → DEBUG
teste           → INFO
produção        → INFO
```

O nível definitivo será ajustado conforme observabilidade.

---

# 21. Segredos

Segredos deverão ser fornecidos pelo ambiente.

Exemplos:

```text
senha do banco
chave de assinatura
segredo Instagram
chave de IA
```

---

# 22. Nunca colocar segredos no frontend

O React poderá receber configurações públicas necessárias para funcionamento da interface.

Nunca deverá receber:

```text
senha do banco
client_secret
chave secreta de IA
chave de criptografia
token privado
```

---

# 23. Configurações públicas

Algumas configurações poderão ser públicas, por exemplo:

```text
URL pública da API
nome da aplicação
versão
ambiente
```

Mesmo assim, não expor informações internas desnecessárias.

---

# 24. URL da API

O frontend deverá utilizar uma configuração para saber onde está a API.

Desenvolvimento:

```text
http://localhost:8000
```

Produção:

```text
https://api.<dominio-do-viralcode>
```

---

# 25. URL do frontend

O backend poderá precisar conhecer a origem autorizada do frontend.

Exemplo:

```text
URL_FRONTEND=http://localhost:3000
```

Em produção:

```text
URL_FRONTEND=https://<dominio-do-viralcode>
```

---

# 26. CORS

O backend deverá configurar CORS explicitamente.

No desenvolvimento poderá permitir:

```text
http://localhost:3000
```

ou a porta utilizada pelo frontend.

Em produção deverá permitir somente as origens necessárias.

Evitar:

```text
allow_origins=["*"]
```

em produção para rotas autenticadas sem uma justificativa clara.

---

# 27. Redirecionamento do Instagram

O endereço utilizado no fluxo OAuth deverá ser configurado por ambiente.

Exemplo:

```text
INSTAGRAM_REDIRECIONAMENTO=http://localhost:8000/api/v1/contas-sociais/instagram/callback
```

Em produção deverá utilizar HTTPS e o domínio oficial.

---

# 28. Configuração de timeout

Integrações externas deverão possuir timeouts configuráveis ou definidos por constantes seguras.

Exemplo conceitual:

```text
TEMPO_LIMITE_INSTAGRAM
TEMPO_LIMITE_IA
```

Não permitir chamadas externas indefinidamente.

---

# 29. Tentativas

Operações externas poderão possuir quantidade máxima de tentativas.

Exemplo:

```text
TENTATIVAS_INSTAGRAM
TENTATIVAS_IA
```

O comportamento definitivo será definido nos serviços correspondentes.

---

# 30. Limites

Configurações poderão controlar limites do sistema.

Exemplo:

```text
LIMITE_GERACOES_IA
LIMITE_DESCobertas
LIMITE_PUBLICACOES
```

Os nomes definitivos deverão seguir a convenção do projeto.

---

# 31. Não transformar tudo em variável

Nem toda constante precisa estar no `.env`.

Usar variável de ambiente para:

```text
segredo
credencial
endereço dependente do ambiente
configuração operacional
```

Manter no código valores realmente fixos e não sensíveis quando isso simplificar o sistema.

---

# 32. Configurações de negócio

Regras de negócio não deverão depender indiscriminadamente do `.env`.

Por exemplo:

```text
visualizações mínimas
```

deve ser um dado do produto, e não necessariamente:

```text
VIEWS_MINIMAS=1000000
```

se o usuário puder configurar esse valor.

---

# 33. Configuração do usuário

Quando uma configuração pertence ao usuário, ela deverá ser armazenada no banco.

Exemplo:

```text
visualizacoes_minimas
horario_preferido
tom_de_voz
objetivos
```

---

# 34. Configuração do sistema

Quando uma configuração pertence ao ambiente:

```text
URL
porta
credencial
chave
timeout
```

ela poderá ficar no ambiente.

---

# 35. Separação

```text
CONFIGURAÇÃO DO SISTEMA
        ↓
.env / ambiente

CONFIGURAÇÃO DO USUÁRIO
        ↓
MySQL

REGRA DE NEGÓCIO
        ↓
Código
```

---

# 36. Configuração de porta

Backend:

```text
PORTA_API=8000
```

Frontend:

```text
PORTA_FRONTEND=3000
```

Os valores podem variar conforme o ambiente.

---

# 37. Configuração do banco no Docker

Se o projeto utilizar Docker Compose, as configurações deverão ser passadas para os containers por ambiente.

Não colocar senha real diretamente no:

```text
docker-compose.yml
```

---

# 38. Desenvolvimento com Docker

A arquitetura poderá utilizar:

```text
frontend
backend
mysql
```

Cada serviço deverá receber somente as configurações necessárias.

---

# 39. Produção na VPS

Na VPS da Hostinger, as configurações deverão ser fornecidas de forma segura.

A estratégia definitiva poderá utilizar:

```text
arquivo de ambiente protegido
```

ou mecanismo equivalente.

Nunca colocar segredos diretamente no repositório.

---

# 40. Git

O `.gitignore` deverá ignorar pelo menos:

```text
.env
.env.*
!.env.example
__pycache__/
node_modules/
dist/
build/
logs/
arquivos temporários
```

A lista definitiva deverá ser adequada às ferramentas utilizadas.

---

# 41. Arquivo `.env.example`

Deverá conter:

```text
nomes
descrições
valores vazios
exemplos seguros
```

Nunca:

```text
credenciais reais
tokens reais
```

---

# 42. Exemplo de estrutura

```text
viralcode/
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yml
│
├── backend/
├── frontend/
├── banco/
├── scripts/
└── documentos/
```

---

# 43. Configuração carregada uma vez

O backend deverá carregar a configuração de forma centralizada.

Evitar que cada módulo leia diretamente:

```text
os.environ
```

espalhado pelo projeto.

Preferir:

```text
configuracao
   ↓
serviços
```

---

# 44. Tipagem da configuração

Quando possível, as configurações deverão possuir:

```text
tipo
valor padrão seguro
validação
```

Exemplo conceitual:

```text
PORTA_API → inteiro
MODO_DEBUG → booleano
URL_API → URL
```

---

# 45. Configuração inválida

Se uma configuração obrigatória estiver ausente:

```text
não iniciar silenciosamente
```

A aplicação deverá informar claramente que existe uma configuração obrigatória ausente.

Não revelar o segredo esperado.

---

# 46. Configuração de produção incompleta

Exemplo:

```text
INSTAGRAM_CLIENT_SECRET ausente
```

O sistema deverá impedir que a integração seja utilizada corretamente ou impedir a inicialização quando a configuração for essencial.

---

# 47. Verificação inicial

Ao iniciar o backend, poderá existir uma validação das configurações essenciais:

```text
banco
autenticação
integrações essenciais
```

---

# 48. Health check

O:

```text
GET /health
```

não deverá expor:

```text
senhas
tokens
chaves
URLs internas sensíveis
```

---

# 49. Configuração do ambiente de teste

Os testes deverão utilizar:

```text
banco de teste
credenciais de teste
tokens simulados
provedor de IA simulado quando possível
Instagram simulado
```

Evitar depender de serviços reais em todos os testes.

---

# 50. Mock de Instagram

O projeto deverá permitir substituir o conector real por um falso:

```text
ConectorInstagramFalso
```

Isso permitirá testar:

```text
descoberta
publicação
métricas
erros
```

sem depender da API real.

---

# 51. Mock de IA

Da mesma forma:

```text
ProvedorIAFalso
```

poderá retornar respostas controladas.

Isso permitirá testes rápidos e baratos.

---

# 52. Ambiente de desenvolvimento

Deverá priorizar:

```text
rapidez
facilidade
logs detalhados
dados de teste
```

---

# 53. Ambiente de teste

Deverá priorizar:

```text
isolamento
repetibilidade
dados controlados
```

---

# 54. Ambiente de produção

Deverá priorizar:

```text
segurança
estabilidade
backup
logs
disponibilidade
```

---

# 55. Não compartilhar segredos

Não reutilizar automaticamente:

```text
segredo desenvolvimento
```

em:

```text
produção
```

---

# 56. Rotação de segredos

A arquitetura deverá permitir trocar:

```text
senha
chave
token
client_secret
```

sem alterar o código.

---

# 57. Token Instagram expirado

O token da conta social deverá possuir informação de validade quando disponível.

Quando expirar:

```text
conta social
   ↓
REAUTENTICACAO_NECESSARIA
```

O sistema não deverá continuar tentando indefinidamente.

---

# 58. Configuração e documentação

Toda variável de ambiente importante deverá ser documentada no `.env.example` ou documentação associada.

Exemplo:

```text
INSTAGRAM_CLIENT_ID
→ identificador da aplicação Instagram/Meta
```

---

# 59. Regra para agentes de IA

Antes de criar uma nova variável de ambiente:

1. verificar se já existe configuração equivalente;
2. verificar se o valor realmente depende do ambiente;
3. evitar duplicidade;
4. adicionar ao `.env.example`;
5. documentar;
6. validar no startup quando necessário;
7. nunca adicionar segredo real ao código.

---

# 60. Regra contra configuração escondida

Não criar:

```text
variáveis mágicas
```

espalhadas em arquivos.

Toda configuração relevante deverá possuir localização conhecida.

---

# 61. Configuração e arquitetura

A separação deverá permanecer:

```text
FastAPI
   ↓
Configuração
   ↓
Serviços
   ↓
Repositórios / Conectores
```

---

# 62. Configuração futura

A arquitetura poderá posteriormente suportar:

```text
configuração por usuário
configuração por perfil
configuração por organização
configuração por plataforma
```

---

# 63. Não antecipar complexidade

No MVP não implementar:

```text
gerenciador empresarial de segredos
configuração distribuída
service discovery
configuração dinâmica complexa
```

A VPS deverá ser suficiente para a primeira fase.

---

# 64. Critério de sucesso

A configuração estará adequada quando for possível:

```text
clonar projeto
   ↓
copiar .env.example
   ↓
preencher ambiente
   ↓
iniciar backend
   ↓
iniciar frontend
   ↓
conectar banco
   ↓
executar aplicação
```

sem editar código-fonte para inserir segredos ou URLs específicas do ambiente.

---

# 65. Estrutura resumida

```text
viralcode/
│
├── .env                  # NÃO versionado
├── .env.example          # versionado
├── .gitignore
│
├── backend/
│   └── app/
│       └── configuracoes/
│           ├── ambiente.py
│           ├── banco.py
│           └── aplicacao.py
│
├── frontend/
├── banco/
├── scripts/
└── documentos/
```

---

# 66. Regra final

> **O código deve ser transportável entre ambientes sem carregar segredos ou configurações específicas dentro dele.**

A regra é:

```text
CÓDIGO
→ comportamento

AMBIENTE
→ configuração

BANCO
→ dados do produto

SEGREDOS
→ proteção externa ao código
```

Essa separação será fundamental quando o ViralCode sair do computador local e for hospedado na VPS da Hostinger.

**Versão:** 1.0  
**Status:** Documento oficial de Configuração e Ambiente
