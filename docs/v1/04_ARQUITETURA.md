# 04 — ARQUITETURA DO VIRALCODE

**Versão:** 0.1  
**Status:** Documento inicial  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo deste documento

Este documento define a arquitetura técnica do ViralCode.

A arquitetura foi projetada com dois objetivos simultâneos:

1. manter o MVP simples;
2. permitir evolução para uma plataforma de inteligência, criação e publicação de conteúdo.

A arquitetura atual não deve antecipar a implementação de todos os componentes futuros.

A regra é:

> **Arquitetura preparada para crescer, implementação simples para validar.**

---

# 2. Princípio arquitetural principal

A arquitetura base do ViralCode será:

```text
React
   ↓
FastAPI
   ↓
Serviços
   ↓
Repositórios
   ↓
SQLAlchemy
   ↓
MySQL
```

Integrações externas ficarão isoladas em provedores.

```text
                         FastAPI
                            │
                     ┌──────┴──────┐
                     │             │
                     ▼             ▼
                  Serviços      Provedores
                     │             │
                     ▼             ▼
                Repositórios   APIs externas
                     │
                     ▼
                 SQLAlchemy
                     │
                     ▼
                   MySQL
```

---

# 3. Arquitetura em camadas

O ViralCode utilizará separação de responsabilidades.

## 3.1 Apresentação

Responsável pela interface.

Tecnologia:

> React

Responsabilidades:

- exibir telas;
- receber entradas;
- apresentar resultados;
- controlar estado da interface;
- chamar a API.

Não deverá conter regras de negócio críticas.

---

## 3.2 API

Responsável pela comunicação HTTP.

Tecnologia:

> FastAPI

Responsabilidades:

- receber requisições;
- validar entradas;
- autenticar futuramente;
- chamar serviços;
- retornar respostas;
- padronizar erros.

As rotas não devem implementar regras complexas de negócio.

---

## 3.3 Serviços

Responsáveis pelas regras de negócio.

Exemplos:

```text
Serviço de Busca
Serviço de Conteúdo
Serviço de Análise
Serviço de Publicação
Serviço de Desempenho
```

No MVP, apenas os serviços necessários deverão existir.

---

## 3.4 Repositórios

Responsáveis pelo acesso aos dados.

Exemplos:

```text
Repositório de Conteúdo
Repositório de Autor
Repositório de Busca
```

Um serviço não deverá escrever SQL diretamente.

---

## 3.5 ORM

Tecnologia:

> SQLAlchemy

Responsável pelo mapeamento entre objetos Python e banco de dados.

---

## 3.6 Banco de dados

Tecnologia:

> MySQL

Responsável pela persistência dos dados.

---

# 4. Integrações externas

Integrações externas deverão ser isoladas através de provedores.

Exemplo inicial:

```text
Serviço de Busca
       ↓
Provedor SocialKit
       ↓
API SocialKit
```

O restante do sistema não deverá depender diretamente do formato específico da SocialKit.

---

# 5. Padrão de provedor

A aplicação deverá possuir uma abstração conceitual para provedores.

Exemplo:

```text
Provedor de Conteúdo
│
├── SocialKit
├── Provedor Instagram futuro
├── Provedor TikTok futuro
└── Provedor YouTube futuro
```

Isso permitirá substituir ou adicionar fontes sem alterar as regras de negócio.

---

# 6. Fluxo de pesquisa do MVP

O fluxo principal será:

```text
Usuário
   ↓
React
   ↓
POST /api/v1/buscas
   ↓
FastAPI
   ↓
Serviço de Busca
   ↓
Provedor SocialKit
   ↓
Dados externos
   ↓
Normalização
   ↓
Deduplicação
   ↓
Repositório
   ↓
SQLAlchemy
   ↓
MySQL
   ↓
Serviço
   ↓
FastAPI
   ↓
React
   ↓
Ranking
```

---

# 7. Responsabilidade da rota

Exemplo conceitual:

```text
POST /api/v1/buscas
```

A rota deverá:

1. receber a requisição;
2. validar os dados;
3. chamar o serviço de busca;
4. devolver a resposta.

Não deverá:

- chamar diretamente a SocialKit;
- executar SQL;
- implementar deduplicação;
- calcular regras complexas;
- manipular diretamente o ORM.

---

# 8. Responsabilidade do serviço

O serviço de busca será responsável pelo fluxo de negócio.

Exemplo:

```text
Serviço de Busca
│
├── validar critérios
├── chamar provedor
├── normalizar resultados
├── eliminar duplicados
├── aplicar regras de negócio
├── persistir
└── retornar resultados
```

---

# 9. Responsabilidade do provedor

O provedor será responsável por conversar com a API externa.

Exemplo:

```text
Provedor SocialKit
│
├── autenticação
├── requisição HTTP
├── timeout
├── tratamento de erro externo
├── leitura da resposta
└── conversão para modelo interno
```

A lógica de negócio não deverá ficar no provedor.

---

# 10. Responsabilidade do repositório

O repositório será responsável pela persistência.

Exemplo:

```text
Repositório de Conteúdo
│
├── salvar
├── buscar por identificador
├── buscar por URL
├── listar
└── atualizar
```

O repositório não deverá decidir regras de negócio.

---

# 11. Fluxo de dependência

A direção das dependências deverá ser:

```text
Rotas
  ↓
Serviços
  ↓
Repositórios / Provedores
  ↓
Infraestrutura
```

Evitar dependências invertidas desnecessárias.

---

# 12. Regra fundamental

> **Router não acessa banco diretamente.**

Errado:

```text
Rota
  ↓
SQLAlchemy
```

Correto:

```text
Rota
  ↓
Serviço
  ↓
Repositório
  ↓
SQLAlchemy
```

---

# 13. Regra para integrações externas

Não fazer:

```text
Rota
  ↓
SocialKit
```

Nem:

```text
React
  ↓
SocialKit
```

O correto será:

```text
React
  ↓
FastAPI
  ↓
Serviço
  ↓
Provedor
  ↓
SocialKit
```

---

# 14. Estrutura lógica do backend

A estrutura inicial prevista:

```text
backend/
└── app/
    ├── principal.py
    │
    ├── api/
    │   ├── rotas/
    │   └── dependencias.py
    │
    ├── servicos/
    │
    ├── repositorios/
    │
    ├── modelos/
    │
    ├── esquemas/
    │
    ├── provedores/
    │
    ├── banco/
    │
    └── configuracao/
```

Os nomes devem permanecer em português.

---

# 15. Estrutura lógica do frontend

Estrutura conceitual:

```text
frontend/
└── src/
    ├── componentes/
    ├── paginas/
    ├── servicos/
    ├── ganchos/
    ├── tipos/
    ├── utilitarios/
    └── aplicativo/
```

O React deverá consumir exclusivamente a API do ViralCode para dados de negócio.

---

# 16. API REST

A API deverá utilizar versionamento.

Exemplo:

```text
/api/v1/
```

Primeiros recursos previstos:

```text
/api/v1/saude
/api/v1/buscas
/api/v1/conteudos
```

Os endpoints específicos serão detalhados em `08_API.md`.

---

# 17. Modelo de comunicação

Frontend e backend utilizarão:

```text
HTTP
+
JSON
```

A comunicação deverá ser documentada e padronizada.

---

# 18. Modelos e esquemas

O backend deverá separar:

### Modelos

Representam persistência e entidades do banco.

### Esquemas

Representam entrada e saída da API.

Não devemos expor automaticamente objetos do banco diretamente como resposta da API.

Fluxo:

```text
Requisição
   ↓
Esquema de entrada
   ↓
Serviço
   ↓
Modelo
   ↓
Repositório
   ↓
Modelo
   ↓
Esquema de saída
   ↓
JSON
```

---

# 19. Tratamento de erros

Erros deverão ser classificados.

### Erros de entrada

Exemplo:

```text
Termo de pesquisa vazio.
```

### Erros de negócio

Exemplo:

```text
Filtro de visualizações inválido.
```

### Erros externos

Exemplo:

```text
Provedor temporariamente indisponível.
```

### Erros internos

Exemplo:

```text
Falha inesperada ao processar a pesquisa.
```

A API deverá retornar mensagens controladas sem expor detalhes internos sensíveis.

---

# 20. Configuração

Configurações deverão utilizar variáveis de ambiente.

Exemplos:

```text
BANCO_DADOS_URL
CHAVE_SOCIALKIT
AMBIENTE
NIVEL_LOG
```

Os nomes reais serão definidos no documento de tecnologia/configuração.

Nunca armazenar chaves diretamente no código.

---

# 21. Banco de dados

O MVP utilizará:

> MySQL

A comunicação será feita através de:

> SQLAlchemy

As alterações de estrutura do banco deverão utilizar:

> Alembic

Não alterar tabelas manualmente em produção sem migration correspondente.

---

# 22. Transações

Operações que alterem múltiplos registros relacionados deverão considerar transações apropriadas.

Exemplo:

```text
Salvar busca
+
Salvar conteúdos
+
Salvar métricas
```

Se uma operação crítica falhar, o sistema deverá evitar deixar dados inconsistentes.

---

# 23. Deduplicação

A deduplicação será uma regra de negócio.

Um conteúdo encontrado em diferentes buscas não deverá gerar registros duplicados.

O identificador utilizado deverá ser definido por plataforma.

Exemplo conceitual:

```text
plataforma + identificador_externo
```

Quando esse identificador não existir, poderá ser utilizada uma combinação segura de dados disponíveis.

---

# 24. Histórico de métricas

O MVP poderá armazenar a data de coleta das métricas.

O histórico detalhado de crescimento será desenvolvido em fase posterior.

Visão futura:

```text
conteúdo
   ↓
métrica 10h
métrica 14h
métrica 18h
métrica 22h
```

Isso permitirá futuramente calcular velocidade de crescimento.

---

# 25. Processamento síncrono no MVP

O MVP deverá evitar complexidade desnecessária.

Inicialmente, a busca poderá ser executada de forma síncrona se o tempo de resposta for aceitável.

Se o volume ou tempo de processamento exigir, poderemos introduzir processamento assíncrono posteriormente.

Não implementar filas complexas antes da necessidade real.

---

# 26. Arquitetura futura de processamento

Quando necessário, poderá ser adicionada uma camada de tarefas em segundo plano:

```text
FastAPI
   ↓
Fila
   ↓
Trabalhadores
   ├── Descoberta
   ├── Análise
   ├── Geração
   ├── Publicação
   └── Desempenho
```

Essa arquitetura não faz parte obrigatoriamente do MVP.

---

# 27. Arquitetura futura de inteligência

O futuro Motor de Inteligência será separado do núcleo de descoberta.

```text
Conteúdo
   ↓
Motor de Inteligência
   ├── Transcrição
   ├── Análise textual
   ├── Análise visual
   ├── Classificação
   ├── Viral DNA
   └── Padrões
```

Isso permitirá evoluir a inteligência sem alterar o mecanismo básico de coleta.

---

# 28. Arquitetura futura de criação

O Motor de Criação deverá consumir a inteligência armazenada.

```text
Perfil
   +
Nicho
   +
Público
   +
Padrões
   +
Objetivo
   ↓
Motor de Criação
   ↓
Conteúdo original
```

O motor não deverá depender diretamente da API de uma rede social.

---

# 29. Arquitetura futura de publicação

O Motor de Publicação será independente da criação.

```text
Conteúdo
   ↓
Motor de Publicação
   ↓
Adaptador
   ├── Instagram
   ├── TikTok
   ├── YouTube
   ├── Facebook
   └── LinkedIn
```

Isso permitirá reutilização.

---

# 30. Arquitetura futura de desempenho

Após publicação:

```text
Conteúdo publicado
        ↓
Coleta de métricas
        ↓
Histórico
        ↓
Análise
        ↓
Inteligência
```

---

# 31. Arquitetura futura de aprendizado

O ciclo completo será:

```text
Descoberta
    ↓
Inteligência
    ↓
Criação
    ↓
Publicação
    ↓
Desempenho
    ↓
Aprendizado
    ↓
Nova Inteligência
```

---

# 32. Multi-nicho

O sistema deverá tratar nichos como dados.

Não criar:

```python
if nicho == "casamento":
    ...
```

como regra permanente do domínio.

O correto será:

```text
nicho
 ↓
dados
 ↓
configuração
 ↓
regras aplicáveis
```

O primeiro nicho de validação é casamento, mas o sistema deverá permanecer genérico.

---

# 33. Multi-perfil

Perfis deverão ser entidades independentes.

Um perfil poderá possuir:

- nicho;
- público;
- tom de voz;
- objetivos;
- identidade visual;
- contas sociais;
- regras de conteúdo.

A visão futura é:

```text
Organização
   ↓
Perfis
   ↓
Conteúdos
```

---

# 34. Multi-plataforma

Plataformas deverão ser tratadas como entidades/configurações.

A integração deverá ser isolada.

Exemplo:

```text
Plataforma
   ↓
Adaptador
   ↓
API externa
```

A lógica central do ViralCode não deverá depender de uma única plataforma.

---

# 35. Multi-organização futuro

O sistema poderá futuramente ser transformado em SaaS.

Estrutura:

```text
Organização
│
├── Usuários
├── Perfis
├── Nichos
├── Contas sociais
├── Conteúdos
├── Análises
└── Configurações
```

Esse isolamento deverá ser considerado nas decisões futuras de domínio e banco, mas não precisa ser implementado integralmente no primeiro MVP.

---

# 36. Escalabilidade

A arquitetura deverá permitir crescimento gradual.

Ordem recomendada:

```text
Aplicação simples
   ↓
Otimização
   ↓
Cache
   ↓
Processamento assíncrono
   ↓
Filas
   ↓
Trabalhadores
   ↓
Processamento paralelo
   ↓
Arquitetura distribuída
```

Não começar pelo último estágio.

---

# 37. Desempenho

No MVP, priorizar:

- simplicidade;
- respostas previsíveis;
- baixo consumo;
- poucas chamadas externas;
- deduplicação;
- índices adequados;
- consultas eficientes.

Não realizar otimizações prematuras sem evidência de problema.

---

# 38. Cache futuro

Poderemos utilizar cache para reduzir chamadas externas.

Exemplo:

```text
Pesquisa
   ↓
Existe resultado recente?
   │
   ├── Sim → usar cache
   │
   └── Não → consultar provedor
```

A estratégia será definida quando houver necessidade.

---

# 39. Observabilidade futura

Em uma fase posterior poderemos adicionar:

- logs estruturados;
- métricas;
- monitoramento;
- rastreamento;
- alertas;
- acompanhamento de erros.

No MVP, teremos apenas o necessário para diagnosticar problemas.

---

# 40. Deploy

O desenvolvimento será local.

A produção será futuramente hospedada em uma VPS da Hostinger.

Arquitetura conceitual:

```text
Internet
   ↓
Nginx
   ↓
Aplicação
├── React
└── FastAPI
   ↓
MySQL
```

Detalhes serão documentados em `14_IMPLANTACAO.md`.

---

# 41. Docker

Docker e Docker Compose poderão ser utilizados para padronizar o ambiente.

Objetivos:

- reduzir diferenças entre máquinas;
- facilitar instalação;
- facilitar testes;
- facilitar deploy futuro.

Não criar uma infraestrutura Docker excessivamente complexa.

---

# 42. Segurança arquitetural

Princípios:

- segredos fora do código;
- variáveis de ambiente;
- validação de entrada;
- separação de responsabilidades;
- tratamento seguro de erros;
- controle de acesso futuro;
- logs sem dados sensíveis.

Detalhes serão documentados em `10_SEGURANCA.md`.

---

# 43. Testabilidade

Cada camada deverá poder ser testada isoladamente.

Exemplo:

```text
Serviço
   ↓
Mock do provedor
   ↓
Teste da regra de negócio
```

O serviço não deverá depender necessariamente de uma API externa real para ser testado.

---

# 44. Princípio de baixo acoplamento

Componentes externos deverão ser substituíveis.

Especialmente:

- provedores de dados;
- provedores de inteligência artificial;
- plataformas sociais;
- serviços de armazenamento.

O núcleo do ViralCode não deve depender excessivamente de uma empresa específica.

---

# 45. Princípio de alta coesão

Cada componente deve possuir uma responsabilidade clara.

Exemplo:

```text
Serviço de Busca
→ regras de busca

Repositório de Conteúdo
→ persistência de conteúdo

Provedor SocialKit
→ comunicação com SocialKit
```

Evitar componentes que fazem tudo.

---

# 46. Princípio de simplicidade

A arquitetura futura não deve justificar código complexo no MVP.

A pergunta deve ser:

> **"Qual é a solução mais simples que mantém a evolução possível?"**

Essa será uma das regras centrais do projeto.

---

# 47. Regra para agentes de IA

Antes de criar ou alterar um componente, o agente deverá:

1. identificar a camada correta;
2. verificar se já existe componente equivalente;
3. reutilizar código existente quando apropriado;
4. evitar duplicação;
5. respeitar o idioma português;
6. verificar o escopo do MVP;
7. não implementar arquitetura futura sem necessidade;
8. criar testes;
9. atualizar documentação quando necessário.

---

# 48. Fluxo arquitetural do MVP

A primeira implementação deve ser simples:

```text
                  USUÁRIO
                     │
                     ▼
                  REACT
                     │
                     ▼
                  FASTAPI
                     │
                     ▼
             SERVIÇO DE BUSCA
                     │
                     ▼
             PROVEDOR SOCIALKIT
                     │
                     ▼
                NORMALIZAÇÃO
                     │
                     ▼
               DEDUPLICAÇÃO
                     │
                     ▼
                REPOSITÓRIO
                     │
                     ▼
                SQLALCHEMY
                     │
                     ▼
                   MYSQL
                     │
                     ▼
                  FASTAPI
                     │
                     ▼
                  REACT
```

---

# 49. Arquitetura-alvo

A evolução completa deverá chegar a:

```text
                              VIRALCODE
                                  │
          ┌───────────────────────┼───────────────────────┐
          │                       │                       │
          ▼                       ▼                       ▼
      DESCOBERTA             INTELIGÊNCIA             CRIAÇÃO
          │                       │                       │
          └───────────────────────┼───────────────────────┘
                                  │
                                  ▼
                              PUBLICAÇÃO
                                  │
                                  ▼
                              DESEMPENHO
                                  │
                                  ▼
                              APRENDIZADO
                                  │
                                  └──────────────→ INTELIGÊNCIA
```

A implementação deverá evoluir gradualmente até essa arquitetura.

---

# 50. Regra final

> **O ViralCode deve ter uma arquitetura capaz de crescer sem obrigar o MVP a ser complexo.**

A arquitetura deve proteger:

- simplicidade;
- separação de responsabilidades;
- baixo acoplamento;
- testabilidade;
- evolução;
- substituição de provedores;
- expansão para novos nichos;
- expansão para novos perfis;
- expansão para novas plataformas.

**Versão atual:** 0.1  
**Status:** Arquitetura inicial do ViralCode
