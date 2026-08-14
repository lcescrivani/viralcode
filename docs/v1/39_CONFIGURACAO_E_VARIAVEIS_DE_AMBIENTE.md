# 39 — CONFIGURAÇÃO E VARIÁVEIS DE AMBIENTE

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define como o ViralCode deverá organizar configurações e segredos em diferentes ambientes.

Ambientes previstos:

```text
DESENVOLVIMENTO
TESTE
PRODUÇÃO
```

O princípio central é:

```text
código
≠
configuração
≠
segredo
```

---

# 2. Princípio fundamental

Nenhum segredo deverá ser gravado diretamente no código-fonte.

Nunca:

```python
SENHA = "123456"
```

ou:

```python
CHAVE_API = "abc..."
```

---

# 3. Configuração

Configuração representa valores que podem mudar entre ambientes.

Exemplos:

```text
URL da API
porta
modo de execução
nome do ambiente
níveis de log
```

---

# 4. Segredo

Segredo representa informação que não deve ser exposta.

Exemplos:

```text
senha do MySQL
chave do provedor de IA
client secret do Instagram
chaves de autenticação
```

---

# 5. Ambientes

O projeto deverá possuir separação clara:

```text
LOCAL
 ↓
DESENVOLVIMENTO
 ↓
PRODUÇÃO
```

O ambiente de teste poderá existir separadamente quando necessário.

---

# 6. Arquivo `.env`

No desenvolvimento local, poderá ser utilizado:

```text
.env
```

O arquivo deverá estar no:

```text
.gitignore
```

---

# 7. Arquivo de exemplo

O projeto deverá possuir:

```text
.env.exemplo
```

contendo apenas:

```text
nomes das variáveis
valores fictícios
comentários
```

Nunca credenciais reais.

---

# 8. Exemplo

```env
AMBIENTE=desenvolvimento

BANCO_HOST=localhost
BANCO_PORTA=3306
BANCO_NOME=viralcode
BANCO_USUARIO=viralcode
BANCO_SENHA=

INSTAGRAM_CLIENT_ID=
INSTAGRAM_CLIENT_SECRET=
INSTAGRAM_REDIRECT_URI=

PROVEDOR_IA=
MODELO_IA=
CHAVE_PROVEDOR_IA=
```

---

# 9. Regra de nomenclatura

As variáveis de ambiente deverão utilizar:

```text
MAIUSCULAS_COM_UNDERSCORE
```

Exemplo:

```text
BANCO_HOST
BANCO_PORTA
```

---

# 10. Ambiente

Variável:

```text
AMBIENTE
```

Valores:

```text
desenvolvimento
teste
producao
```

---

# 11. Configuração do backend

O FastAPI deverá possuir uma camada central de configuração.

Conceitualmente:

```text
configuracao/
   ↓
variáveis de ambiente
   ↓
objeto de configuração
```

---

# 12. Não acessar `.env` em qualquer lugar

Evitar:

```text
os.getenv(...)
```

espalhado por dezenas de arquivos.

Preferir:

```text
configuração central
```

---

# 13. Banco de dados

Variáveis conceituais:

```text
BANCO_HOST
BANCO_PORTA
BANCO_NOME
BANCO_USUARIO
BANCO_SENHA
```

---

# 14. URL do banco

Opcionalmente poderá existir uma variável consolidada:

```text
BANCO_URL
```

A implementação deverá escolher uma estratégia consistente.

---

# 15. SQLAlchemy

A configuração do SQLAlchemy deverá ser construída a partir da configuração central.

Não gravar credenciais no código.

---

# 16. Alembic

As migrações deverão utilizar a mesma configuração segura do banco.

---

# 17. Instagram

Variáveis conceituais:

```text
INSTAGRAM_CLIENT_ID
INSTAGRAM_CLIENT_SECRET
INSTAGRAM_REDIRECT_URI
```

---

# 18. Regra Instagram

O:

```text
INSTAGRAM_CLIENT_SECRET
```

nunca poderá estar no frontend.

---

# 19. Provedor de IA

Variáveis conceituais:

```text
PROVEDOR_IA
MODELO_IA
CHAVE_PROVEDOR_IA
```

---

# 20. Modelo de IA

O modelo deverá ser configurável.

Não espalhar o nome do modelo em código.

---

# 21. URLs externas

Quando necessário:

```text
INSTAGRAM_API_URL
PROVEDOR_IA_URL
```

também poderão ser configuradas.

---

# 22. API pública

O backend poderá possuir:

```text
URL_PUBLICA_API
```

quando necessário para:

```text
OAuth
callbacks
integrações
```

---

# 23. Frontend

O frontend deverá possuir somente configurações públicas.

Exemplo:

```text
URL_PUBLICA_API
```

---

# 24. Segredos nunca no frontend

Nunca disponibilizar para React:

```text
BANCO_SENHA
INSTAGRAM_CLIENT_SECRET
CHAVE_PROVEDOR_IA
```

---

# 25. CORS

A origem permitida poderá ser configurada.

Exemplo:

```text
ORIGENS_PERMITIDAS
```

---

# 26. Desenvolvimento

Exemplo conceitual:

```env
AMBIENTE=desenvolvimento
URL_PUBLICA_API=http://localhost:8000
```

---

# 27. Produção

Exemplo conceitual:

```env
AMBIENTE=producao
URL_PUBLICA_API=https://api.seudominio.com
```

O domínio real será definido posteriormente.

---

# 28. DEBUG

Deverá existir configuração equivalente a:

```text
DEBUG
```

No ambiente de produção:

```text
DEBUG=false
```

---

# 29. Logs

Poderá existir:

```text
NIVEL_LOG
```

Exemplos:

```text
DEBUG
INFO
WARNING
ERROR
```

---

# 30. Segurança de logs

Mesmo em:

```text
DEBUG
```

não registrar:

```text
senha
token
client_secret
chave de IA
```

---

# 31. Correlation ID

Não precisa ser uma variável fixa.

Ele deverá ser gerado por requisição quando necessário.

---

# 32. Sessão/autenticação

Configurações relacionadas à autenticação poderão incluir:

```text
CHAVE_AUTENTICACAO
TEMPO_EXPIRACAO_SESSAO
```

Os nomes finais deverão acompanhar a implementação escolhida.

---

# 33. CORS de produção

Não utilizar:

```text
*
```

como configuração permanente em produção.

---

# 34. Host permitido

Quando aplicável, configurar os hosts permitidos.

---

# 35. Armazenamento

Quando o projeto utilizar armazenamento externo de mídia, suas configurações deverão ser externas ao código.

Exemplo futuro:

```text
ARMAZENAMENTO_TIPO
ARMAZENAMENTO_BUCKET
ARMAZENAMENTO_REGIAO
ARMAZENAMENTO_CHAVE
ARMAZENAMENTO_SEGREDO
```

---

# 36. Não criar agora

No MVP não criar configuração para serviços que ainda não existem.

Evitar:

```text
S3
Redis
Kafka
Elasticsearch
```

sem necessidade real.

---

# 37. Configuração mínima do MVP

Backend:

```text
AMBIENTE
DEBUG
BANCO_HOST
BANCO_PORTA
BANCO_NOME
BANCO_USUARIO
BANCO_SENHA
URL_PUBLICA_API
ORIGENS_PERMITIDAS
CHAVE_AUTENTICACAO
INSTAGRAM_CLIENT_ID
INSTAGRAM_CLIENT_SECRET
INSTAGRAM_REDIRECT_URI
PROVEDOR_IA
MODELO_IA
CHAVE_PROVEDOR_IA
NIVEL_LOG
```

A lista poderá ser ajustada quando as implementações concretas forem definidas.

---

# 38. Configuração obrigatória

O sistema deverá falhar de forma clara quando uma variável obrigatória não estiver configurada.

Não utilizar:

```text
valor padrão inseguro
```

para segredos obrigatórios.

---

# 39. Validação no startup

No início da aplicação, validar:

```text
configuração obrigatória
```

---

# 40. Exemplo

Se faltar:

```text
BANCO_SENHA
```

o backend deverá informar que a configuração obrigatória está ausente, sem exibir o valor de outros segredos.

---

# 41. Configuração tipada

A configuração deverá ser carregada para um objeto tipado.

Isso reduz erros como:

```text
porta = "abc"
```

---

# 42. Booleanos

Variáveis booleanas deverão ser interpretadas corretamente.

Exemplo:

```text
DEBUG=true
```

não deverá ser tratado como texto arbitrário.

---

# 43. Números

Portas e tempos deverão ser validados como números.

---

# 44. URLs

URLs deverão ser validadas quando possível.

---

# 45. Listas

Configurações como origens permitidas deverão possuir formato definido.

Exemplo conceitual:

```text
ORIGENS_PERMITIDAS=https://app.exemplo.com,https://admin.exemplo.com
```

---

# 46. Desenvolvimento local

O desenvolvedor deverá poder executar o projeto sem depender de credenciais de produção.

---

# 47. Credenciais locais

Utilizar:

```text
contas de desenvolvimento
```

e não:

```text
credenciais de produção
```

---

# 48. Produção na VPS

Na VPS da Hostinger, os segredos deverão ser configurados no ambiente do servidor.

Não colocar segredos no repositório.

---

# 49. Deploy

O processo de deploy deverá:

```text
atualizar código
 ↓
carregar configuração
 ↓
validar configuração
 ↓
executar migrações quando necessário
 ↓
iniciar/reiniciar aplicação
```

---

# 50. Backup

Credenciais de backup não deverão ser gravadas no código.

---

# 51. Rotação

Segredos importantes deverão poder ser substituídos sem alteração do código.

Exemplo:

```text
trocar chave da IA
```

sem editar arquivos Python.

---

# 52. Comprometimento de segredo

Se um segredo for exposto:

```text
revogar
+
gerar novo
+
atualizar ambiente
+
verificar logs/repositório
```

---

# 53. Git

O repositório deverá ignorar:

```text
.env
.env.*
```

com exceção explícita do arquivo de exemplo quando necessário.

---

# 54. Atenção ao `.env.exemplo`

O `.env.exemplo` não deverá conter:

```text
senha real
token real
client secret real
```

---

# 55. Docker

Se Docker for utilizado, as variáveis deverão ser injetadas no container.

Não copiar segredos para a imagem.

---

# 56. Imagem Docker

Nunca fazer:

```dockerfile
COPY .env /app/.env
```

em uma imagem de produção.

---

# 57. Logs de startup

O startup poderá informar:

```text
ambiente
modo
serviços configurados
```

mas nunca valores secretos.

---

# 58. Diagnóstico

Em caso de configuração inválida, informar:

```text
qual variável está ausente ou inválida
```

sem revelar segredos.

---

# 59. Testes

Testar:

```text
configuração válida
variável ausente
tipo inválido
URL inválida
ambiente inválido
```

---

# 60. Teste de segurança

Garantir que:

```text
segredos não aparecem em logs
segredos não aparecem em exceções
segredos não aparecem em respostas HTTP
```

---

# 61. Ambiente de testes

Testes automatizados deverão preferir:

```text
credenciais simuladas
```

ou:

```text
ambiente isolado
```

em vez de credenciais reais.

---

# 62. Integração Instagram em testes

Não executar chamadas reais ao Instagram em todos os testes.

Usar mocks/simulações quando apropriado.

---

# 63. IA em testes

Não executar chamadas pagas do provedor de IA em toda a suíte automatizada.

Usar respostas simuladas para testes unitários.

---

# 64. Custos

O ambiente de desenvolvimento deverá evitar chamadas externas desnecessárias.

---

# 65. Configuração por operação

Se no futuro diferentes operações utilizarem modelos diferentes, a configuração poderá evoluir para:

```text
MODELO_IA_ANALISE
MODELO_IA_CRIACAO
```

mas isso não é obrigatório no MVP.

---

# 66. Configuração de limites

Poderão existir futuramente:

```text
LIMITE_REQUISICOES
LIMITE_GERACOES_IA
LIMITE_POR_PAGINA
```

Somente criar quando realmente utilizados.

---

# 67. Princípio de menor configuração

Toda variável de ambiente deve ter uma finalidade clara.

Não criar variáveis "por precaução".

---

# 68. Documentação

Toda variável de ambiente utilizada pelo sistema deverá estar documentada.

---

# 69. Tabela de referência

| Variável | Tipo | Obrigatória | Segredo |
|---|---|---:|---:|
| `AMBIENTE` | texto | Sim | Não |
| `DEBUG` | booleano | Sim | Não |
| `BANCO_HOST` | texto | Sim | Não |
| `BANCO_PORTA` | número | Sim | Não |
| `BANCO_NOME` | texto | Sim | Não |
| `BANCO_USUARIO` | texto | Sim | Não |
| `BANCO_SENHA` | texto | Sim | Sim |
| `URL_PUBLICA_API` | URL | Sim | Não |
| `ORIGENS_PERMITIDAS` | lista | Sim | Não |
| `CHAVE_AUTENTICACAO` | texto | Sim | Sim |
| `INSTAGRAM_CLIENT_ID` | texto | Sim | Não* |
| `INSTAGRAM_CLIENT_SECRET` | texto | Sim | Sim |
| `INSTAGRAM_REDIRECT_URI` | URL | Sim | Não |
| `PROVEDOR_IA` | texto | Sim | Não |
| `MODELO_IA` | texto | Sim | Não |
| `CHAVE_PROVEDOR_IA` | texto | Sim | Sim |
| `NIVEL_LOG` | texto | Sim | Não |

`*` O client ID poderá ser considerado público em alguns contextos, mas deverá continuar sendo tratado como configuração de backend.

---

# 70. Regra de nomes

Mesmo que bibliotecas externas utilizem nomenclatura em inglês, as variáveis internas do projeto deverão seguir o padrão oficial do ViralCode em português sempre que não houver motivo técnico para preservar o nome externo.

---

# 71. Frontend e variáveis públicas

Variáveis realmente expostas ao navegador deverão possuir prefixo definido pela tecnologia escolhida.

A nomenclatura final será registrada quando o projeto React for configurado.

---

# 72. Não duplicar configuração

Evitar:

```text
URL_API_A
URL_API_B
URL_API_C
```

quando apenas uma URL é necessária.

---

# 73. Configuração central

Fluxo:

```text
Ambiente
 ↓
Configuração
 ↓
Serviços
```

---

# 74. Arquitetura

```text
                   AMBIENTE
                       │
                       ▼
               VARIÁVEIS DE AMBIENTE
                       │
                       ▼
                  CONFIGURAÇÃO
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
        BANCO       INSTAGRAM       IA
          │            │            │
          ▼            ▼            ▼
      SQLAlchemy     Conector     Provedor
```

---

# 75. Regra para agentes de IA

Antes de criar uma nova variável:

1. verificar se já existe configuração equivalente;
2. verificar se o valor é realmente variável por ambiente;
3. classificar como configuração ou segredo;
4. documentar;
5. adicionar ao `.env.exemplo`;
6. validar no startup quando obrigatório;
7. atualizar documentação.

---

# 76. Regra contra segredo no código

Nenhuma IA deverá:

```text
inserir chave real
inserir senha real
copiar segredo para código
copiar segredo para frontend
```

---

# 77. Regra contra configuração escondida

Não criar valores críticos diretamente dentro de serviços sem documentar.

---

# 78. Critério de sucesso

A configuração estará adequada quando:

```text
local funciona
+
produção funciona
+
credenciais não estão no Git
+
segredos não chegam ao frontend
+
ambientes são independentes
+
configuração é validada
+
troca de segredo não exige alteração de código
```

---

# 79. Regra final

> **O mesmo código deve poder rodar em desenvolvimento e produção mudando configuração, e não sendo reescrito para cada ambiente.**

A separação oficial será:

```text
CÓDIGO
+
CONFIGURAÇÃO
+
SEGREDOS
```

com os segredos permanecendo fora do código-fonte e fora do frontend.

**Versão:** 1.0  
**Status:** Documento oficial de Configuração e Variáveis de Ambiente
