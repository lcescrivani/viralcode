# 21 — ESTRUTURA DO PROJETO

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define a estrutura física e lógica do código-fonte do ViralCode.

O objetivo é garantir que:

- novas IAs consigam entender o projeto;
- cada responsabilidade tenha um local definido;
- frontend e backend permaneçam separados;
- regras de negócio não fiquem espalhadas;
- integrações externas sejam isoladas;
- o projeto possa crescer sem precisar ser reescrito;
- o desenvolvimento local e o futuro deploy na VPS sejam previsíveis.

---

# 2. Princípio fundamental

A estrutura deverá refletir a arquitetura definida pelo projeto:

```text
React
  ↓
FastAPI
  ↓
Serviços
  ↓
Repositórios / Conectores
  ↓
SQLAlchemy
  ↓
MySQL
```

A organização física deverá respeitar essa separação.

---

# 3. Estrutura raiz

A estrutura inicial será:

```text
viralcode/
│
├── backend/
├── frontend/
├── banco/
├── scripts/
├── testes/
├── documentos/
├── .env.example
├── .gitignore
├── README.md
└── docker-compose.yml
```

Os nomes poderão ser ajustados caso a implementação adote uma convenção técnica diferente, mas a separação conceitual deverá permanecer.

---

# 4. Backend

Estrutura:

```text
backend/
│
├── app/
│   ├── principal.py
│   ├── configuracoes/
│   ├── rotas/
│   ├── modelos/
│   ├── esquemas/
│   ├── servicos/
│   ├── repositorios/
│   ├── conectores/
│   ├── provedores_ia/
│   ├── seguranca/
│   └── utilitarios/
│
├── testes/
├── migracoes/
├── requisitos.txt
└── README.md
```

---

# 5. Aplicação principal

Arquivo:

```text
backend/app/principal.py
```

Responsabilidade:

- criar a aplicação FastAPI;
- registrar rotas;
- configurar middleware;
- configurar tratamento de erros;
- iniciar componentes necessários.

Não deverá conter regras de negócio.

---

# 6. Configurações

Diretório:

```text
backend/app/configuracoes/
```

Responsabilidade:

```text
variáveis de ambiente
configuração da aplicação
configuração do banco
configuração de integrações
```

Exemplo:

```text
configuracoes/
├── ambiente.py
├── banco.py
└── aplicacao.py
```

---

# 7. Rotas

Diretório:

```text
backend/app/rotas/
```

Responsabilidade:

```text
receber requisição
validar entrada
chamar serviço
retornar resposta
```

Exemplo:

```text
rotas/
├── autenticacao.py
├── perfis.py
├── contas_sociais.py
├── descobertas.py
├── conteudos.py
├── planejamento.py
├── publicacoes.py
├── desempenho.py
└── aprendizados.py
```

As rotas não deverão acessar o banco diretamente.

---

# 8. Modelos

Diretório:

```text
backend/app/modelos/
```

Responsabilidade:

representar entidades persistidas no banco.

Exemplo:

```text
modelos/
├── usuario.py
├── perfil.py
├── nicho.py
├── conta_social.py
├── conteudo.py
├── conteudo_externo.py
├── analise_conteudo.py
├── padrao.py
├── insight.py
├── planejamento.py
├── item_planejamento.py
├── publicacao.py
├── metrica_publicacao.py
├── aprendizado.py
├── evidencia_aprendizado.py
├── prompt.py
└── execucao_ia.py
```

---

# 9. Esquemas

Diretório:

```text
backend/app/esquemas/
```

Responsabilidade:

definir estruturas de entrada e saída da API.

Exemplo:

```text
esquemas/
├── usuario.py
├── autenticacao.py
├── perfil.py
├── conta_social.py
├── descoberta.py
├── conteudo.py
├── planejamento.py
├── publicacao.py
├── desempenho.py
└── aprendizado.py
```

---

# 10. Diferença entre modelo e esquema

Modelo:

```text
representa banco
```

Esquema:

```text
representa contrato da API
```

Exemplo:

```text
SQLAlchemy
   ↓
ModeloPerfil

FastAPI
   ↓
EsquemaPerfil
```

Não misturar os dois conceitos.

---

# 11. Serviços

Diretório:

```text
backend/app/servicos/
```

Aqui ficará a regra de negócio.

Exemplo:

```text
servicos/
├── servico_autenticacao.py
├── servico_perfil.py
├── servico_conta_social.py
├── servico_descoberta.py
├── servico_inteligencia.py
├── servico_criacao.py
├── servico_planejamento.py
├── servico_publicacao.py
├── servico_desempenho.py
└── servico_aprendizado.py
```

---

# 12. Regra dos serviços

O serviço deverá:

```text
receber dados
↓
validar regras
↓
executar lógica
↓
chamar repositório/conector
↓
retornar resultado
```

---

# 13. Repositórios

Diretório:

```text
backend/app/repositorios/
```

Responsabilidade:

```text
acesso ao banco
```

Exemplo:

```text
repositorios/
├── repositorio_usuario.py
├── repositorio_perfil.py
├── repositorio_conteudo.py
├── repositorio_publicacao.py
├── repositorio_metrica.py
├── repositorio_aprendizado.py
└── repositorio_planejamento.py
```

---

# 14. Regra dos repositórios

O repositório não deverá decidir regra de negócio.

Exemplo correto:

```text
Serviço:
"publicação precisa estar aprovada"

Repositório:
"buscar publicação"
```

---

# 15. Conectores

Diretório:

```text
backend/app/conectores/
```

Responsabilidade:

comunicação com serviços externos.

Estrutura inicial:

```text
conectores/
├── base/
│   └── conector_rede_social.py
└── instagram/
    ├── conector_instagram.py
    ├── autenticacao.py
    ├── publicacao.py
    ├── descoberta.py
    └── metricas.py
```

---

# 16. Regra do conector

O conector deverá esconder detalhes específicos da plataforma.

O restante do sistema deverá trabalhar com conceitos internos.

Evitar:

```text
ServicoPublicacao
   ↓
chamada direta ao Instagram
```

Preferir:

```text
ServicoPublicacao
   ↓
ConectorInstagram
   ↓
Instagram
```

---

# 17. Provedores de IA

Diretório:

```text
backend/app/provedores_ia/
```

Responsabilidade:

abstrair o fornecedor de inteligência artificial.

Estrutura:

```text
provedores_ia/
├── base/
│   └── provedor_ia.py
├── provedor_principal.py
└── fabrica.py
```

O nome do fornecedor específico não deverá contaminar os serviços de negócio.

---

# 18. Regra do provedor de IA

Preferir:

```text
ServicoCriacao
      ↓
ProvedorIA
      ↓
Modelo
```

e não:

```text
ServicoCriacao
      ↓
API específica do fornecedor
```

---

# 19. Segurança

Diretório:

```text
backend/app/seguranca/
```

Responsabilidade:

```text
autenticação
autorização
hash de senha
tokens
sessão
```

Exemplo:

```text
seguranca/
├── autenticacao.py
├── autorizacao.py
├── senhas.py
└── tokens.py
```

---

# 20. Utilitários

Diretório:

```text
backend/app/utilitarios/
```

Somente funções realmente compartilhadas deverão ficar aqui.

Evitar transformar `utilitarios` em uma pasta genérica para código sem lugar definido.

---

# 21. Frontend

Estrutura:

```text
frontend/
│
├── src/
│   ├── componentes/
│   ├── paginas/
│   ├── servicos/
│   ├── tipos/
│   ├── hooks/
│   ├── contexto/
│   ├── rotas/
│   ├── utilitarios/
│   └── estilos/
│
├── publico/
├── testes/
├── package.json
└── README.md
```

---

# 22. Componentes

Diretório:

```text
frontend/src/componentes/
```

Responsabilidade:

componentes visuais reutilizáveis.

Exemplo:

```text
componentes/
├── Botao/
├── CampoTexto/
├── Modal/
├── Tabela/
├── CartaoConteudo/
├── CartaoMetrica/
└── Calendario/
```

---

# 23. Páginas

Diretório:

```text
frontend/src/paginas/
```

Exemplo:

```text
paginas/
├── Login/
├── Dashboard/
├── Perfil/
├── Descoberta/
├── Conteudos/
├── Criacao/
├── Planejamento/
├── Publicacoes/
└── Desempenho/
```

---

# 24. Serviços do frontend

Diretório:

```text
frontend/src/servicos/
```

Responsabilidade:

comunicação com a API.

Exemplo:

```text
servicos/
├── api.ts
├── autenticacao.ts
├── perfis.ts
├── contasSociais.ts
├── descobertas.ts
├── conteudos.ts
├── planejamento.ts
├── publicacoes.ts
├── desempenho.ts
└── aprendizados.ts
```

Mesmo mantendo o domínio em português, nomes técnicos exigidos pela linguagem poderão seguir a convenção do TypeScript/JavaScript.

---

# 25. Regra do frontend

O frontend não deverá acessar:

```text
MySQL
Instagram
provedor de IA
```

Diretamente.

Sempre:

```text
React
 ↓
API
```

---

# 26. Tipos

Diretório:

```text
frontend/src/tipos/
```

Deverá conter os contratos usados pelo frontend.

Exemplo:

```text
Perfil
Conteudo
Publicacao
Metrica
Aprendizado
```

Idealmente esses tipos deverão acompanhar os contratos da API.

---

# 27. Banco

Diretório:

```text
banco/
```

Responsabilidade:

arquivos relacionados à persistência e desenvolvimento do banco.

Estrutura:

```text
banco/
├── scripts/
├── dados_iniciais/
└── README.md
```

As migrações ficarão no backend, junto ao código de persistência.

---

# 28. Scripts

Diretório:

```text
scripts/
```

Utilizado para tarefas auxiliares.

Exemplos:

```text
iniciar_ambiente
parar_ambiente
popular_banco
executar_testes
backup
```

Scripts deverão ser pequenos e documentados.

---

# 29. Documentação

Diretório:

```text
documentos/
```

Deverá conter a documentação oficial do projeto.

Exemplo:

```text
documentos/
├── 00_...
├── 01_...
├── ...
├── 17_DEFINICAO_OFICIAL_DO_MVP.md
├── 18_ESTRATEGIA_DE_DESCOBERTA_DO_INSTAGRAM.md
├── 19_MODELO_DE_DADOS.md
├── 20_CONTRATOS_DA_API.md
└── 21_ESTRUTURA_DO_PROJETO.md
```

---

# 30. Documentação como fonte de verdade

As IAs que trabalharem no projeto deverão ler os documentos antes de modificar arquitetura.

Regra:

```text
Código
   +
Documentação
```

devem permanecer coerentes.

---

# 31. Testes do backend

Estrutura:

```text
backend/testes/
│
├── unitarios/
├── integracao/
└── api/
```

---

# 32. Testes unitários

Testar:

```text
serviços
regras
funções
validadores
```

Sem depender de Instagram real.

---

# 33. Testes de integração

Testar:

```text
serviço
+
repositório
+
banco de teste
```

---

# 34. Testes de API

Testar:

```text
endpoint
autenticação
validação
resposta
erros
```

---

# 35. Testes do frontend

Estrutura:

```text
frontend/testes/
```

Priorizar inicialmente:

```text
componentes críticos
fluxo de login
descoberta
criação
aprovação
publicação
```

---

# 36. Ambiente local

O desenvolvimento deverá funcionar localmente.

Arquitetura:

```text
Computador do desenvolvedor
       │
       ├── React
       ├── FastAPI
       └── MySQL
```

---

# 37. Docker

O projeto poderá utilizar Docker para padronizar o ambiente.

Estrutura:

```text
docker-compose.yml
```

Serviços iniciais:

```text
frontend
backend
mysql
```

Não criar containers separados para cada serviço de negócio.

---

# 38. Regra de simplicidade

No MVP:

```text
1 frontend
1 backend
1 banco
```

Os motores são módulos dentro do backend.

Não transformar cada motor em um microserviço.

---

# 39. Arquitetura modular

Apesar de existir um único backend, os módulos deverão permanecer separados.

Exemplo:

```text
servicos/
├── servico_inteligencia.py
├── servico_criacao.py
├── servico_publicacao.py
└── servico_desempenho.py
```

---

# 40. Quando separar em serviços independentes

Somente considerar microserviços quando houver necessidade real de:

```text
escala independente
isolamento
processamento assíncrono
volume elevado
equipes independentes
```

---

# 41. Variáveis de ambiente

Arquivo:

```text
.env
```

Não deverá ser versionado.

Arquivo:

```text
.env.example
```

deverá ser versionado.

---

# 42. Git

O repositório deverá conter:

```text
.gitignore
README.md
```

Nunca versionar:

```text
.env
tokens
segredos
senhas
dados sensíveis
```

---

# 43. README principal

O arquivo:

```text
README.md
```

deverá explicar:

```text
o que é o ViralCode
como executar
tecnologias
estrutura
como configurar
como testar
onde está a documentação
```

---

# 44. Arquivo de regras para IA

Deverá existir futuramente um arquivo de orientação para agentes de IA.

Exemplo:

```text
INSTRUCOES_PARA_IA.md
```

Ele deverá indicar:

```text
documentos que devem ser lidos
regras de arquitetura
regras de idioma
regras de nomenclatura
o que não alterar
como testar
```

---

# 45. Regra de leitura da IA

Antes de alterar código, a IA deverá consultar pelo menos:

```text
17_DEFINICAO_OFICIAL_DO_MVP.md
18_ESTRATEGIA_DE_DESCOBERTA_DO_INSTAGRAM.md
19_MODELO_DE_DADOS.md
20_CONTRATOS_DA_API.md
21_ESTRUTURA_DO_PROJETO.md
```

e os documentos específicos do módulo que será alterado.

---

# 46. Dependências

Backend:

```text
FastAPI
SQLAlchemy
driver MySQL
biblioteca de migração
bibliotecas de autenticação
bibliotecas HTTP
```

Frontend:

```text
React
TypeScript
biblioteca HTTP
biblioteca de roteamento
```

As versões serão fixadas em arquivos de dependência.

---

# 47. Nomenclatura do backend

Classes:

```python
ServicoCriacao
RepositorioConteudo
ConectorInstagram
```

Funções:

```python
criar_conteudo()
obter_metricas()
publicar_conteudo()
```

Variáveis:

```python
conteudo_id
perfil_id
conta_social
```

---

# 48. Nomenclatura do banco

Preferir:

```text
snake_case
```

Exemplo:

```text
metricas_publicacao
conteudos_externos
evidencias_aprendizado
```

---

# 49. Nomenclatura do frontend

Componentes React poderão seguir a convenção da tecnologia:

```text
CartaoConteudo
TabelaConteudos
PaginaDashboard
```

Arquivos poderão seguir a convenção escolhida pelo projeto, desde que seja consistente.

---

# 50. Regra contra arquivos gigantes

Não criar um único arquivo contendo:

```text
todas as rotas
todos os serviços
todos os modelos
```

Separar por responsabilidade.

---

# 51. Regra contra abstração excessiva

Também não criar dezenas de camadas sem necessidade.

No MVP:

```text
Rota
 ↓
Serviço
 ↓
Repositório / Conector
```

é suficiente na maioria dos casos.

---

# 52. Dependências entre módulos

Preferir:

```text
Serviço A
 ↓
interface necessária
 ↓
Serviço B
```

Evitar dependências circulares.

---

# 53. Conectores independentes

O código específico do Instagram deverá ficar isolado.

Exemplo:

```text
conectores/instagram/
```

Quando surgir outra rede:

```text
conectores/tiktok/
```

sem alterar o núcleo do domínio mais do que o necessário.

---

# 54. Provedores de IA independentes

Da mesma forma:

```text
provedores_ia/
```

deverá permitir substituir o fornecedor.

---

# 55. Fluxo de execução

Exemplo de publicação:

```text
rota publicacoes.py
        ↓
ServicoPublicacao
        ↓
RepositorioConteudo
        ↓
ConectorInstagram
        ↓
Instagram
        ↓
RepositorioPublicacao
        ↓
Resposta
```

---

# 56. Fluxo de descoberta

```text
rota descobertas.py
        ↓
ServicoDescoberta
        ↓
EstrategiaDescoberta
        ↓
ConectorInstagram
        ↓
Instagram
        ↓
RepositorioConteudo
        ↓
Resposta
```

---

# 57. Fluxo de criação

```text
rota conteudos.py
        ↓
ServicoCriacao
        ↓
RepositorioAprendizado
        ↓
RepositorioPrompt
        ↓
ProvedorIA
        ↓
Conteúdo
        ↓
RepositorioConteudo
```

---

# 58. Fluxo de desempenho

```text
rota desempenho.py
        ↓
ServicoDesempenho
        ↓
ConectorInstagram
        ↓
RepositorioMetricas
        ↓
MySQL
```

---

# 59. Fluxo de aprendizado

```text
ServicoDesempenho
        ↓
ServicoAprendizado
        ↓
RepositorioAprendizado
        ↓
Evidências
```

---

# 60. Configuração de produção

A estrutura deverá permitir:

```text
desenvolvimento
teste
produção
```

sem modificar código de negócio.

As diferenças deverão estar principalmente em:

```text
variáveis de ambiente
infraestrutura
configuração
```

---

# 61. VPS

A aplicação será posteriormente hospedada em uma VPS da Hostinger.

Arquitetura inicial esperada:

```text
Internet
   ↓
Nginx
   ↓
Frontend / Backend
   ↓
MySQL
```

A configuração definitiva será detalhada no documento de infraestrutura.

---

# 62. Deploy

O código deverá poder ser instalado em ambiente limpo seguindo documentação.

O objetivo é evitar:

```text
"funciona somente no computador do desenvolvedor"
```

---

# 63. Logs

Logs deverão estar centralizados no backend.

Não espalhar:

```text
print()
```

como mecanismo oficial de observabilidade.

---

# 64. Arquivos temporários

Arquivos temporários deverão ficar em diretório próprio e não deverão ser versionados.

---

# 65. Uploads

Se o ViralCode precisar armazenar arquivos:

```text
mídias
vídeos
imagens
```

essa estratégia deverá ser definida separadamente.

No MVP, não assumir armazenamento permanente de mídia sem necessidade.

---

# 66. Banco de produção

Não utilizar:

```text
MySQL local
```

como banco de produção.

A produção deverá possuir banco separado.

---

# 67. Backup

O código não substitui backup.

O banco deverá possuir estratégia própria de backup, definida no documento de infraestrutura.

---

# 68. Segurança

A estrutura deverá permitir separar:

```text
código
configuração
segredos
dados
```

---

# 69. Regra para agentes de IA

Uma IA trabalhando no projeto não deverá:

```text
mudar arquitetura sem necessidade
criar microserviços
trocar React
trocar FastAPI
trocar MySQL
misturar domínio com integração
duplicar regras
criar endpoints sem documentação
```

---

# 70. Regra de mudança

Antes de alterar estrutura:

```text
1. identificar motivo
2. verificar documentação
3. avaliar impacto
4. alterar
5. testar
6. atualizar documentação
```

---

# 71. Critério de sucesso

A estrutura será considerada adequada quando um desenvolvedor novo ou uma IA conseguir:

```text
clonar
 ↓
ler README
 ↓
ler documentos
 ↓
instalar dependências
 ↓
configurar ambiente
 ↓
iniciar projeto
 ↓
executar testes
```

sem depender de conhecimento oculto.

---

# 72. Estrutura resumida

```text
viralcode/
│
├── backend/
│   ├── app/
│   │   ├── configuracoes/
│   │   ├── rotas/
│   │   ├── modelos/
│   │   ├── esquemas/
│   │   ├── servicos/
│   │   ├── repositorios/
│   │   ├── conectores/
│   │   ├── provedores_ia/
│   │   ├── seguranca/
│   │   └── utilitarios/
│   │
│   ├── testes/
│   └── migracoes/
│
├── frontend/
│   ├── src/
│   │   ├── componentes/
│   │   ├── paginas/
│   │   ├── servicos/
│   │   ├── tipos/
│   │   ├── hooks/
│   │   ├── contexto/
│   │   ├── rotas/
│   │   └── estilos/
│   └── testes/
│
├── banco/
├── scripts/
├── documentos/
├── .env.example
├── .gitignore
├── README.md
└── docker-compose.yml
```

---

# 73. Regra final

> **A estrutura do projeto deve tornar evidente onde cada responsabilidade vive.**

A regra básica é:

```text
React
→ interface

FastAPI
→ entrada da aplicação

Serviços
→ regras de negócio

Repositórios
→ banco

Conectores
→ sistemas externos

Provedores de IA
→ inteligência artificial

Modelos
→ persistência

Esquemas
→ contratos

Testes
→ validação

Documentação
→ conhecimento do projeto
```

Essa estrutura deverá permitir que o ViralCode comece como um MVP simples e evolua sem transformar o código em um monólito desorganizado.

**Versão:** 1.0  
**Status:** Documento oficial da Estrutura do Projeto
