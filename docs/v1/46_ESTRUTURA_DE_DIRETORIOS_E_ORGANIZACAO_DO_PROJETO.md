# 46 — ESTRUTURA DE DIRETÓRIOS E ORGANIZAÇÃO DO PROJETO

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define a organização física do código-fonte, documentação, infraestrutura e testes do ViralCode.

A estrutura deverá facilitar:

```text
localização
manutenção
desenvolvimento por IA
testes
deploy
crescimento
```

---

# 2. Princípio fundamental

A estrutura de diretórios deverá refletir a arquitetura do sistema.

Não criar pastas somente porque:

```text
"todo projeto possui essa pasta"
```

Cada diretório deverá possuir uma responsabilidade clara.

---

# 3. Estrutura raiz

Estrutura inicial:

```text
viralcode/
│
├── backend/
├── frontend/
├── infraestrutura/
├── docs/
├── testes/
├── scripts/
├── .env.exemplo
├── .gitignore
├── README.md
└── arquivos de configuração do projeto
```

A estrutura poderá evoluir conforme o desenvolvimento.

---

# 4. Backend

O backend será responsável por:

```text
API
regras de negócio
persistência
integrações
IA
autenticação
```

Estrutura conceitual:

```text
backend/
│
├── aplicacao/
├── dominio/
├── servicos/
├── repositorios/
├── conectores/
├── modelos/
├── esquemas/
├── configuracao/
├── banco/
├── seguranca/
└── testes/
```

Os nomes poderão ser ajustados conforme a implementação, mas as responsabilidades deverão permanecer separadas.

---

# 5. Aplicação

A camada de aplicação poderá conter:

```text
rotas
dependências
inicialização
configuração da API
```

Exemplo:

```text
backend/aplicacao/
```

---

# 6. Domínio

O domínio deverá representar conceitos próprios do ViralCode.

Exemplos:

```text
Usuario
Perfil
ContaSocial
Conteudo
Analise
Insight
Aprendizado
Publicacao
ExecucaoIA
```

---

# 7. Serviços

Serviços deverão concentrar regras de negócio.

Exemplos:

```text
ServicoUsuario
ServicoPerfil
ServicoConteudo
ServicoAnalise
ServicoIA
ServicoPublicacao
```

---

# 8. Repositórios

Repositórios deverão concentrar persistência.

Exemplos:

```text
RepositorioUsuario
RepositorioPerfil
RepositorioConteudo
RepositorioPublicacao
```

---

# 9. Conectores

Conectores deverão encapsular serviços externos.

Estrutura:

```text
backend/conectores/
│
├── instagram/
└── provedor_ia/
```

---

# 10. Instagram

O conector do Instagram deverá conter somente detalhes relacionados à integração externa.

Exemplo:

```text
backend/conectores/instagram/
```

---

# 11. Provedor de IA

O conector do provedor de IA deverá ficar isolado.

Exemplo:

```text
backend/conectores/provedor_ia/
```

---

# 12. Regra de isolamento

O restante do sistema não deverá conhecer:

```text
URL HTTP específica
headers externos
formato bruto da resposta
tratamento específico de OAuth
```

do Instagram ou do provedor de IA.

Esses detalhes pertencem ao conector.

---

# 13. Modelos

Os modelos de persistência deverão ficar organizados de forma consistente.

Exemplo:

```text
backend/modelos/
```

---

# 14. Esquemas

Os esquemas de entrada e saída da API poderão ficar em:

```text
backend/esquemas/
```

Eles representam:

```text
contrato externo
```

e não devem ser confundidos automaticamente com:

```text
modelo do banco
```

---

# 15. Configuração

Configuração central:

```text
backend/configuracao/
```

Responsável por carregar:

```text
variáveis de ambiente
configurações
validações
```

---

# 16. Banco

A camada de banco poderá conter:

```text
conexão
sessão
migrações
configuração SQLAlchemy
```

---

# 17. Alembic

As migrações poderão ficar em:

```text
backend/alembic/
```

ou estrutura equivalente definida pela ferramenta.

---

# 18. Segurança

Componentes de segurança poderão ficar em:

```text
backend/seguranca/
```

Exemplos:

```text
autenticação
hash de senha
tokens
autorização
```

---

# 19. Frontend

O frontend será React.

Estrutura conceitual:

```text
frontend/
│
├── src/
│   ├── componentes/
│   ├── paginas/
│   ├── servicos/
│   ├── contextos/
│   ├── rotas/
│   ├── tipos/
│   ├── utilitarios/
│   └── estilos/
│
└── arquivos de configuração
```

---

# 20. Componentes

Componentes reutilizáveis:

```text
frontend/src/componentes/
```

Exemplos:

```text
Botao
Modal
Tabela
CartaoConteudo
IndicadorStatus
```

---

# 21. Páginas

Páginas completas:

```text
frontend/src/paginas/
```

Exemplos:

```text
Login
Dashboard
Perfil
Conteudos
Publicacoes
Administracao
```

---

# 22. Serviços frontend

Chamadas para a API:

```text
frontend/src/servicos/
```

---

# 23. Regra frontend

Componentes não deverão espalhar chamadas HTTP diretamente por toda a aplicação.

Preferir:

```text
Componente
 ↓
Serviço
 ↓
API
```

---

# 24. Contextos

Estado global ou compartilhado poderá utilizar:

```text
frontend/src/contextos/
```

Somente quando realmente necessário.

---

# 25. Rotas

Rotas do React deverão ficar organizadas em:

```text
frontend/src/rotas/
```

ou estrutura equivalente.

---

# 26. Tipos

Tipos/interfaces do frontend deverão ficar organizados.

Exemplo:

```text
frontend/src/tipos/
```

---

# 27. Utilitários

Funções auxiliares genéricas:

```text
frontend/src/utilitarios/
```

Não colocar regras de negócio complexas nessa pasta.

---

# 28. Estilos

Estilos compartilhados deverão possuir organização consistente.

---

# 29. Administração

A Área Administrativa deverá possuir estrutura própria dentro do frontend.

Exemplo:

```text
frontend/src/paginas/administracao/
```

ou uma estrutura equivalente.

---

# 30. Regra de Admin

Não duplicar toda a aplicação para criar o Admin.

Compartilhar:

```text
componentes
serviços
tipos
autenticação
```

quando fizer sentido.

---

# 31. Documentação

Todos os documentos oficiais deverão ficar em:

```text
docs/
```

---

# 32. Numeração

Os documentos oficiais utilizarão numeração:

```text
00_
01_
02_
...
```

A numeração representa a organização do projeto e não necessariamente ordem de execução.

---

# 33. Documentação em português

A documentação do ViralCode deverá ser escrita em:

```text
Português do Brasil
```

---

# 34. Código em português

Conforme decisão do projeto, nomes internos de:

```text
classes
funções
variáveis
serviços
repositórios
rotas
entidades
```

deverão utilizar português, salvo nomes técnicos ou externos que precisem permanecer no idioma original.

---

# 35. Exceções de nomenclatura

Poderão permanecer em inglês nomes como:

```text
React
FastAPI
SQLAlchemy
MySQL
JSON
OAuth
HTTP
API
Git
Docker
```

---

# 36. Scripts

Scripts operacionais deverão ficar em:

```text
scripts/
```

Exemplos:

```text
subir_ambiente
backup
restauracao
deploy
verificar_saude
```

---

# 37. Infraestrutura

Arquivos de infraestrutura deverão ficar em:

```text
infraestrutura/
```

Estrutura possível:

```text
infraestrutura/
│
├── docker/
├── nginx/
├── scripts/
└── producao/
```

---

# 38. Docker

Arquivos relacionados ao Docker deverão ficar agrupados.

Evitar espalhar configurações Docker por toda a raiz.

---

# 39. NGINX

Configurações do NGINX deverão ficar em:

```text
infraestrutura/nginx/
```

---

# 40. Produção

Arquivos específicos de produção poderão ficar em:

```text
infraestrutura/producao/
```

sem conter segredos reais.

---

# 41. Testes

Os testes poderão ser organizados próximos ao código ou em diretório específico.

A escolha deverá ser consistente.

---

# 42. Testes backend

Estrutura possível:

```text
backend/testes/
│
├── unitarios/
├── integracao/
└── api/
```

---

# 43. Testes frontend

Estrutura possível:

```text
frontend/testes/
```

ou testes próximos aos componentes, conforme a ferramenta adotada.

---

# 44. Testes E2E

Testes ponta a ponta poderão ficar em:

```text
testes/e2e/
```

---

# 45. Fixtures

Dados reutilizáveis de testes deverão ficar organizados em:

```text
testes/fixtures/
```

ou estrutura equivalente.

---

# 46. Arquivos temporários

Não armazenar arquivos temporários no Git.

---

# 47. Uploads locais

Uploads temporários de desenvolvimento deverão ficar fora da estrutura versionada quando possível.

---

# 48. Mídias

Mídias reais de usuários não deverão ser armazenadas no repositório.

---

# 49. Arquivos gerados

Evitar versionar:

```text
build
dist
cache
logs
temporários
```

quando não forem artefatos intencionais do projeto.

---

# 50. `.gitignore`

O `.gitignore` deverá proteger:

```text
.env
cache
logs
arquivos temporários
builds
ambientes virtuais
dependências locais
```

conforme as ferramentas utilizadas.

---

# 51. README

A raiz deverá possuir:

```text
README.md
```

com pelo menos:

```text
objetivo
como executar
estrutura
requisitos
links para documentação
```

---

# 52. Documentação de execução

O README deverá explicar como subir o ambiente local.

---

# 53. Documentação de deploy

O procedimento de produção deverá permanecer documentado em:

```text
docs/
```

e/ou scripts versionados.

---

# 54. Não duplicar documentação

Evitar ter:

```text
README dizendo uma coisa
docs dizendo outra
```

A informação deverá possuir uma fonte principal.

---

# 55. Fonte da verdade

Para arquitetura:

```text
docs/
```

Para código:

```text
Git
```

Para configuração de ambiente:

```text
ambiente + documentação
```

---

# 56. Arquivos de configuração

Arquivos de configuração da aplicação deverão ficar próximos ao componente que os utiliza, sem duplicação.

---

# 57. Arquivos raiz

Manter a raiz limpa.

Não acumular:

```text
teste.py
teste2.py
novo.py
final.py
final2.py
```

---

# 58. Arquivo temporário

Arquivos experimentais deverão ficar fora do código oficial ou ser removidos após o experimento.

---

# 59. Experimentos

Se for necessário experimentar uma tecnologia:

```text
experimentos/
```

poderá ser criado temporariamente, mas não deverá virar dependência oculta do produto.

---

# 60. Dependências backend

Dependências deverão ser declaradas em arquivos próprios do Python/projeto.

---

# 61. Dependências frontend

Dependências deverão ser declaradas pelo gerenciador do projeto React.

---

# 62. Lockfiles

Lockfiles deverão ser versionados quando a ferramenta utilizada recomendar.

---

# 63. Configuração de ferramentas

Configurações de:

```text
lint
formatador
testes
TypeScript
React
Python
```

deverão possuir local previsível.

---

# 64. Formatação

O projeto deverá utilizar ferramentas automáticas de formatação quando adotadas.

---

# 65. Lint

O lint deverá ajudar a detectar:

```text
erros
imports não utilizados
padrões inconsistentes
problemas conhecidos
```

---

# 66. Não usar lint como arquitetura

Lint não substitui:

```text
revisão arquitetural
testes
segurança
```

---

# 67. Estrutura final conceitual

```text
viralcode/
│
├── backend/
│   ├── aplicacao/
│   ├── dominio/
│   ├── servicos/
│   ├── repositorios/
│   ├── conectores/
│   │   ├── instagram/
│   │   └── provedor_ia/
│   ├── modelos/
│   ├── esquemas/
│   ├── configuracao/
│   ├── banco/
│   ├── seguranca/
│   └── testes/
│
├── frontend/
│   ├── src/
│   │   ├── componentes/
│   │   ├── paginas/
│   │   ├── servicos/
│   │   ├── contextos/
│   │   ├── rotas/
│   │   ├── tipos/
│   │   ├── utilitarios/
│   │   └── estilos/
│   └── testes/
│
├── infraestrutura/
│   ├── docker/
│   ├── nginx/
│   ├── scripts/
│   └── producao/
│
├── testes/
│   ├── e2e/
│   └── fixtures/
│
├── scripts/
│
├── docs/
│
├── .env.exemplo
├── .gitignore
└── README.md
```

---

# 68. Regra de evolução

A estrutura acima é uma referência inicial.

Não criar todas as pastas imediatamente.

Uma pasta deverá nascer quando existir código que realmente precise dela.

---

# 69. MVP

No início, a estrutura poderá ser menor:

```text
backend/
frontend/
infraestrutura/
docs/
scripts/
```

e crescer conforme as funcionalidades forem implementadas.

---

# 70. Não criar diretórios vazios

Não criar dezenas de pastas vazias "para deixar preparado".

---

# 71. Organização por responsabilidade

Cada arquivo deverá ter um lugar lógico.

Pergunta:

```text
"Se outro desenvolvedor procurar isso daqui a seis meses, ele saberá onde encontrar?"
```

Se não, a estrutura precisa ser revista.

---

# 72. Regra para agentes de IA

Antes de criar um arquivo:

1. verificar se já existe;
2. identificar a camada correta;
3. verificar nomenclatura;
4. verificar se a responsabilidade pertence àquela pasta;
5. evitar duplicação;
6. atualizar documentação se a estrutura mudar.

---

# 73. Regra contra arquivos genéricos

Evitar arquivos como:

```text
utils.py
helpers.py
common.py
misc.py
```

quando eles acumularem responsabilidades diferentes.

Preferir nomes específicos.

---

# 74. Regra contra arquivos gigantes

Quando um arquivo começar a concentrar responsabilidades diferentes:

```text
identificar responsabilidades
 ↓
separar somente quando houver benefício real
```

---

# 75. Regra contra fragmentação

Também não criar:

```text
um arquivo para cada função trivial
```

sem benefício.

---

# 76. Equilíbrio

A estrutura deverá buscar:

```text
coerência
+
simplicidade
+
localização fácil
```

---

# 77. Arquitetura e diretórios

Os diretórios não substituem a arquitetura.

Eles são uma representação física dela.

---

# 78. Critério de sucesso

A estrutura estará adequada quando:

```text
novo desenvolvedor encontra rapidamente o código
+
IA consegue localizar responsabilidades
+
frontend e backend estão separados
+
integrações externas estão isoladas
+
documentação está centralizada
+
infraestrutura está organizada
+
testes são localizáveis
```

---

# 79. Regra final

> **A estrutura de diretórios deve tornar a arquitetura visível no código.**

O objetivo não é criar muitas pastas.

O objetivo é fazer com que cada parte do ViralCode tenha:

```text
um lugar claro
+
uma responsabilidade clara
+
um limite claro
```

**Versão:** 1.0  
**Status:** Documento oficial da Estrutura de Diretórios e Organização do Projeto
