# 35 — ARQUITETURA DO FRONTEND

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define a arquitetura do frontend do ViralCode.

Tecnologia principal:

```text
React
```

O frontend será responsável por:

```text
interface
navegação
interação do usuário
estado visual
validação de entrada
consumo da API
apresentação de dados
```

Não será responsável por regras críticas de negócio.

---

# 2. Arquitetura geral

```text
                    USUÁRIO
                       │
                       ▼
                    REACT
                       │
              ┌────────┴────────┐
              ▼                 ▼
       ÁREA DO USUÁRIO      ÁREA ADMIN
              │                 │
              └────────┬────────┘
                       ▼
                    API REST
                       │
                    FASTAPI
```

---

# 3. Princípio fundamental

O frontend deverá ser:

```text
simples
modular
reutilizável
responsivo
seguro
orientado à API
```

---

# 4. React

O frontend será desenvolvido com:

```text
React
```

A versão específica deverá ser definida no início da implementação e registrada no ambiente do projeto.

---

# 5. Responsabilidades do React

O React deverá cuidar de:

```text
renderização
interação
navegação
formulários
estado da interface
requisições HTTP
tratamento visual de carregamento
tratamento visual de erro
```

---

# 6. O que NÃO pertence ao React

Não colocar no frontend:

```text
senha de banco
token secreto do Instagram
client secret
chave do provedor de IA
regra crítica de autorização
regra de negócio que precise de proteção
```

---

# 7. Regra principal

```text
Frontend
→ apresenta e solicita

Backend
→ decide e executa
```

---

# 8. Estrutura conceitual

A estrutura deverá separar:

```text
páginas
componentes
serviços
estado
rotas
tipos
utilitários
```

---

# 9. Estrutura sugerida

```text
frontend/
├── src/
│   ├── paginas/
│   │   ├── autenticacao/
│   │   ├── usuario/
│   │   └── administrativo/
│   │
│   ├── componentes/
│   │   ├── comuns/
│   │   ├── usuario/
│   │   └── administrativo/
│   │
│   ├── servicos/
│   │   ├── api/
│   │   ├── autenticacao/
│   │   ├── conteudos/
│   │   ├── instagram/
│   │   ├── publicacoes/
│   │   └── administrativo/
│   │
│   ├── estado/
│   ├── rotas/
│   ├── tipos/
│   ├── utilitarios/
│   └── estilos/
│
└── ...
```

A estrutura poderá ser refinada durante a implementação sem alterar os princípios arquiteturais.

---

# 10. Páginas

Uma página representa uma tela ou rota relevante do produto.

Exemplos:

```text
Login
Cadastro
Dashboard
Perfil
Instagram
Descoberta
Conteúdos
Análises
Criação
Publicações
Métricas
Admin
```

---

# 11. Componentes

Componentes deverão ser reutilizáveis quando houver repetição real.

Exemplos:

```text
Botao
CampoTexto
Seletor
Modal
Tabela
Cartao
Indicador
Carregando
MensagemErro
```

---

# 12. Não criar abstração prematura

Não transformar qualquer trecho de HTML em componente somente porque é possível.

Criar componentes quando houver:

```text
reutilização
complexidade
isolamento
clareza
```

---

# 13. Componentes comuns

Componentes comuns não deverão possuir regra específica de Instagram ou Admin.

Exemplo:

```text
Botao
Tabela
Modal
```

podem ser utilizados em várias áreas.

---

# 14. Componentes de domínio

Componentes específicos poderão existir.

Exemplo:

```text
CartaoConteudo
StatusPublicacao
ContaInstagram
EditorRoteiro
```

---

# 15. Navegação

A aplicação deverá possuir rotas claras.

Conceitualmente:

```text
/login
/cadastro
/dashboard
/perfis
/conteudos
/conteudos/:id
/analises
/criacao
/publicacoes
/metricas
/administracao
```

---

# 16. Rotas administrativas

A área administrativa deverá possuir rotas próprias.

Exemplo:

```text
/administracao
/administracao/usuarios
/administracao/perfis
/administracao/contas-sociais
/administracao/conteudos
/administracao/publicacoes
/administracao/ia
/administracao/erros
/administracao/auditoria
```

---

# 17. Proteção de rotas

O frontend poderá impedir visualmente o acesso a páginas protegidas.

Porém:

> **A proteção real sempre será feita pelo backend.**

---

# 18. Autenticação no frontend

O frontend deverá saber:

```text
usuário autenticado?
```

e utilizar o mecanismo de autenticação definido pelo backend.

---

# 19. Token

Se o projeto utilizar token:

```text
Authorization: Bearer <token>
```

O armazenamento do token deverá seguir a estratégia de segurança definida para o projeto.

Não escolher armazenamento inseguro simplesmente por facilidade.

---

# 20. Expiração

Quando a autenticação expirar:

```text
API
 ↓
401
 ↓
frontend identifica sessão inválida
 ↓
usuário retorna ao login
```

---

# 21. Estado global

Não colocar todo o estado da aplicação em um único estado global.

Separar:

```text
estado de autenticação
estado da interface
estado de dados
estado local
```

---

# 22. Estado local

Usar estado local para situações como:

```text
campo de formulário
modal aberto
aba selecionada
filtro temporário
```

---

# 23. Estado compartilhado

Usar estado compartilhado quando múltiplas partes realmente precisarem da mesma informação.

Exemplo:

```text
usuário autenticado
perfil selecionado
```

---

# 24. Dados da API

Dados provenientes do backend deverão possuir estratégia clara de:

```text
carregamento
cache
atualização
erro
invalidação
```

A biblioteca específica poderá ser escolhida na implementação.

---

# 25. Serviços de API

Não espalhar chamadas HTTP diretamente por dezenas de componentes.

Preferir:

```text
componente
 ↓
serviço
 ↓
API
```

---

# 26. Exemplo

Em vez de:

```text
Componente
→ fetch()
→ regra
→ tratamento
```

preferir:

```text
Componente
→ servicoConteudos.listar()
→ API
```

---

# 27. Cliente HTTP

Deverá existir uma camada central para comunicação com o backend.

Responsabilidades:

```text
URL base
headers
autenticação
tratamento de resposta
tratamento de erro
correlation_id
```

---

# 28. Contrato com backend

O frontend deverá seguir o documento:

```text
34_CONTRATOS_DA_API_REST.md
```

Não criar respostas próprias incompatíveis com o contrato.

---

# 29. Tipos

As estruturas de dados utilizadas pelo frontend deverão possuir tipos claros.

Exemplos:

```text
Usuario
Perfil
ContaSocial
Conteudo
Analise
Publicacao
Metrica
```

---

# 30. Sincronização com API

Quando uma ação alterar dados:

```text
usuário
 ↓
ação
 ↓
API
 ↓
sucesso
 ↓
atualizar estado
```

Não assumir sucesso antes da confirmação do backend.

---

# 31. Loading

Toda operação que possa demorar deverá possuir estado visual apropriado.

Exemplos:

```text
CARREGANDO
PROCESSANDO
PUBLICANDO
ANALISANDO
```

---

# 32. Erros

Erros da API deverão ser transformados em mensagens compreensíveis para o usuário.

Não mostrar diretamente:

```text
stack trace
SQL
erro interno
```

---

# 33. Correlation ID

Quando houver erro relevante, o frontend poderá apresentar:

```text
Código de atendimento: ABC123
```

permitindo que o suporte encontre o evento.

---

# 34. Formulários

Formulários deverão possuir:

```text
validação
mensagem de erro
estado de envio
sucesso
```

---

# 35. Validação frontend x backend

O frontend poderá validar para melhorar a experiência.

Mas:

```text
frontend
→ validação de experiência

backend
→ validação definitiva
```

---

# 36. Dashboard do usuário

O MVP deverá possuir uma dashboard simples.

Possíveis blocos:

```text
Conteúdos
Publicações
Desempenho
Insights
```

---

# 37. Dashboard não deve ser complexo

No MVP, evitar:

```text
dezenas de gráficos
```

A dashboard deverá responder:

```text
O que aconteceu?
O que está acontecendo?
O que devo fazer agora?
```

---

# 38. Tela de Perfil

Deverá permitir visualizar/editar:

```text
nome
nicho
subnicho
público
posicionamento
tom de voz
objetivo
```

---

# 39. Tela Instagram

Deverá permitir:

```text
conectar
visualizar status
reautenticar quando necessário
desconectar
```

---

# 40. Nunca exibir credenciais

A interface não deverá mostrar:

```text
token
client secret
senha
```

---

# 41. Tela Descoberta

Deverá permitir ao usuário informar critérios para encontrar conteúdos relevantes.

Exemplo:

```text
nicho
tema
palavras-chave
filtros
```

---

# 42. Resultado da descoberta

Apresentar:

```text
conteúdo
autor
métricas disponíveis
data
link
```

quando esses dados estiverem disponíveis.

---

# 43. Tela de Conteúdos

Deverá permitir:

```text
listar
filtrar
abrir
editar
analisar
aprovar
arquivar
```

conforme o estado do conteúdo.

---

# 44. Tela de Análise

Deverá apresentar os resultados de forma visual.

Exemplo:

```text
Tema
Hook
Estrutura
Emoção
CTA
Padrões
```

---

# 45. Tela de Criação

Deverá permitir gerar conteúdo a partir do contexto do perfil.

Exemplo:

```text
tema
objetivo
formato
```

O sistema deverá utilizar automaticamente o contexto disponível:

```text
perfil
insights
aprendizados
```

quando aplicável.

---

# 46. Editor

O usuário deverá poder revisar o conteúdo gerado.

Exemplo:

```text
Hook
Roteiro
Legenda
CTA
```

---

# 47. Aprovação

O fluxo visual deverá deixar claro:

```text
RASCUNHO
 ↓
EM REVISÃO
 ↓
APROVADO
```

---

# 48. Publicação

O usuário deverá conseguir:

```text
publicar agora
```

ou:

```text
agendar
```

quando a funcionalidade estiver disponível.

---

# 49. Status da publicação

Exibir claramente:

```text
PENDENTE
ENVIANDO
PUBLICADA
ERRO
CANCELADA
```

---

# 50. Tela de Métricas

Deverá apresentar evolução das publicações.

Exemplos:

```text
visualizações
curtidas
comentários
compartilhamentos
salvamentos
```

Somente métricas disponíveis deverão ser mostradas.

---

# 51. Área Administrativa

A arquitetura do frontend deverá possuir uma área separada:

```text
/administracao
```

---

# 52. Dashboard Admin

Mostrar:

```text
usuários
perfis
contas sociais
conteúdos
publicações
erros
execuções IA
```

---

# 53. Usuários Admin

Tabela com:

```text
nome
e-mail
status
cadastro
último acesso
```

---

# 54. Conteúdos Admin

Filtros:

```text
usuário
perfil
tipo
status
origem
data
```

---

# 55. Publicações Admin

Mostrar:

```text
usuário
conteúdo
conta
status
data
erro
```

---

# 56. IA Admin

Mostrar:

```text
tipo
modelo
status
tempo
tokens
custo
data
```

---

# 57. Erros Admin

Permitir:

```text
buscar
filtrar
abrir
consultar correlation_id
```

---

# 58. Auditoria Admin

Mostrar:

```text
administrador
ação
recurso
data
resultado
```

---

# 59. Responsividade

O frontend deverá funcionar adequadamente em:

```text
desktop
tablet
celular
```

A prioridade do MVP poderá ser:

```text
desktop
+
mobile funcional
```

---

# 60. Acessibilidade

Considerar:

```text
contraste
teclado
labels
foco
tamanho de texto
mensagens de erro
```

Não precisa criar um sistema de acessibilidade complexo no primeiro dia, mas não deverá criar barreiras desnecessárias.

---

# 61. Feedback visual

Toda ação relevante deverá possuir retorno.

Exemplos:

```text
salvo
erro
publicado
conectado
desconectado
gerado
```

---

# 62. Confirmações

Operações destrutivas ou relevantes deverão pedir confirmação quando apropriado.

Exemplo:

```text
Desconectar Instagram?
```

---

# 63. Estados vazios

Toda lista deverá possuir estado vazio.

Exemplo:

```text
Você ainda não possui conteúdos.
```

Evitar telas simplesmente em branco.

---

# 64. Skeleton

Skeleton/loading poderá ser utilizado para melhorar percepção de desempenho.

Não é obrigatório em todas as telas do MVP.

---

# 65. Erro de rede

Quando a API estiver indisponível:

```text
mostrar mensagem
+
permitir tentar novamente
```

---

# 66. Offline

Offline completo não é requisito do MVP.

---

# 67. Upload de mídia

Se o MVP exigir upload:

```text
validar
mostrar progresso
tratar erro
```

A estratégia de armazenamento deverá seguir o documento de infraestrutura.

---

# 68. Mídia

Não assumir que o frontend deve armazenar mídia permanentemente.

Preferir:

```text
backend
+
armazenamento apropriado
```

---

# 69. Segurança do frontend

Nunca armazenar no bundle:

```text
segredos
chaves privadas
senhas
tokens administrativos
```

---

# 70. Variáveis públicas

Somente configurações realmente públicas poderão ficar no frontend.

Exemplo:

```text
URL pública da API
```

---

# 71. Ambiente

O frontend deverá suportar:

```text
desenvolvimento
teste
produção
```

sem alterar código manualmente para cada ambiente.

---

# 72. URL da API

Deverá ser configurável por ambiente.

Exemplo conceitual:

```text
DESENVOLVIMENTO → API local
PRODUÇÃO → API VPS
```

---

# 73. Logs frontend

Logs de desenvolvimento poderão existir.

Produção deverá evitar:

```text
dados pessoais
tokens
informações sensíveis
```

---

# 74. Performance

Evitar:

```text
componentes gigantes
requisições duplicadas
imagens desnecessariamente grandes
renderizações desnecessárias
```

---

# 75. Code splitting

Poderá ser utilizado para separar áreas:

```text
usuário
admin
```

quando houver benefício.

Não é obrigatório no MVP.

---

# 76. Lazy loading

Páginas administrativas ou funcionalidades pesadas poderão ser carregadas sob demanda.

---

# 77. SEO

SEO não é prioridade principal para a aplicação autenticada.

Caso o ViralCode tenha páginas públicas de marketing, elas poderão possuir estratégia própria.

---

# 78. Design System

O frontend deverá possuir componentes visuais consistentes.

Exemplos:

```text
cores
tipografia
espaçamento
botões
inputs
cards
tabelas
status
```

A definição visual detalhada será tratada em documento específico quando necessário.

---

# 79. Não acoplar domínio ao visual

Exemplo:

```text
Publicacao
```

não deverá depender de:

```text
ComponenteTabelaPublicacao
```

O domínio pertence aos dados e serviços.

---

# 80. Testes

O frontend deverá possuir testes para:

```text
componentes importantes
fluxos críticos
serviços de API
autenticação
permissões visuais
```

---

# 81. Testes prioritários do MVP

```text
login
cadastro
criação de perfil
conexão Instagram
listagem conteúdo
geração
aprovação
publicação
dashboard admin
```

---

# 82. Tratamento de sessão

O frontend deverá reagir adequadamente a:

```text
sessão expirada
usuário bloqueado
acesso negado
```

---

# 83. Permissão administrativa

O frontend poderá esconder menus administrativos para usuários comuns.

Mas:

```text
backend = autoridade
```

---

# 84. Arquitetura de comunicação

```text
COMPONENTE
   ↓
SERVIÇO FRONTEND
   ↓
CLIENTE HTTP
   ↓
FASTAPI
   ↓
SERVIÇO
```

---

# 85. Regra contra lógica duplicada

Não repetir no frontend regras que precisam ser idênticas ao backend.

Exemplo:

```text
"pode publicar?"
```

deve ser decidido definitivamente pelo backend.

O frontend apenas representa o estado.

---

# 86. Regra de estados

O frontend deverá refletir o estado retornado pela API.

Exemplo:

```text
API → PUBLICADA
frontend → PUBLICADA
```

Não inventar estado local incompatível.

---

# 87. Internacionalização

O idioma inicial será:

```text
Português do Brasil
```

A arquitetura poderá permitir internacionalização futura.

Não é requisito do MVP implementar múltiplos idiomas.

---

# 88. Nomenclatura

Variáveis, componentes e arquivos deverão seguir o padrão definido para o projeto.

Como o projeto será em português, preferir nomes de domínio em português.

Exemplo:

```text
ListaConteudos
CartaoPublicacao
ServicoInstagram
```

---

# 89. Exceções técnicas

Bibliotecas, protocolos e APIs externas poderão manter nomenclatura oficial.

Exemplo:

```text
React
FastAPI
SQLAlchemy
Instagram
OAuth
JSON
HTTP
```

---

# 90. Estrutura final conceitual

```text
src/
│
├── paginas/
│   ├── autenticacao/
│   ├── usuario/
│   └── administrativo/
│
├── componentes/
│   ├── comuns/
│   ├── usuario/
│   └── administrativo/
│
├── servicos/
│   ├── api/
│   ├── autenticacao/
│   ├── perfis/
│   ├── instagram/
│   ├── conteudos/
│   ├── analises/
│   ├── publicacoes/
│   ├── metricas/
│   └── administrativo/
│
├── estado/
├── rotas/
├── tipos/
├── utilitarios/
└── estilos/
```

---

# 91. Regra para agentes de IA

Antes de alterar o frontend:

1. consultar este documento;
2. consultar os contratos da API;
3. identificar a página;
4. reutilizar componentes existentes;
5. não duplicar chamadas HTTP;
6. respeitar autenticação;
7. respeitar permissões;
8. criar testes quando necessário;
9. atualizar documentação quando a arquitetura mudar.

---

# 92. Regra contra código improvisado

Não criar diretamente dentro de uma página:

```text
fetch
regra de negócio
tratamento complexo
```

quando já existir uma camada adequada para isso.

---

# 93. Critério de sucesso

O frontend estará adequado quando:

```text
usuário entende o que fazer
+
API é consumida de forma organizada
+
estados são claros
+
erros são compreensíveis
+
admin é separado
+
segredos não são expostos
+
componentes são reutilizados quando necessário
```

---

# 94. MVP — telas prioritárias

### P0

```text
Login
Cadastro
Dashboard
Perfil
Instagram
Conteúdos
Análise
Criação
Publicação
```

### P1

```text
Métricas
Insights
Aprendizados
```

### Admin P0

```text
Dashboard
Usuários
Contas Instagram
Conteúdos
Publicações
Erros
```

### Admin P1

```text
Execuções IA
Custos
Auditoria
```

---

# 95. Fluxo principal do frontend

```text
LOGIN
 ↓
DASHBOARD
 ↓
PERFIL
 ↓
CONECTAR INSTAGRAM
 ↓
DESCOBRIR
 ↓
ANALISAR
 ↓
CRIAR
 ↓
REVISAR
 ↓
APROVAR
 ↓
PUBLICAR
 ↓
ACOMPANHAR
```

---

# 96. Regra final

> **O frontend do ViralCode deve tornar a inteligência do sistema simples de usar, sem carregar para o navegador responsabilidades que pertencem ao backend.**

A arquitetura deverá permanecer:

```text
REACT
   ↓
SERVIÇOS FRONTEND
   ↓
API REST
   ↓
FASTAPI
   ↓
SERVIÇOS
   ↓
REPOSITÓRIOS / CONECTORES
   ↓
MYSQL / INSTAGRAM / IA
```

**Versão:** 1.0  
**Status:** Documento oficial da Arquitetura do Frontend
