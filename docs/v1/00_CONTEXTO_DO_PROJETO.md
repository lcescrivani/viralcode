# 00 — CONTEXTO DO PROJETO VIRALCODE

**Versão:** 0.1  
**Status:** Documento inicial  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo deste documento

Este documento apresenta o contexto oficial do projeto ViralCode.

Ele existe para que desenvolvedores, agentes de inteligência artificial e demais colaboradores entendam:

- o que é o ViralCode;
- qual problema estamos tentando resolver;
- qual é a visão do produto;
- qual é o estágio atual do projeto;
- quais decisões já foram tomadas;
- qual é o escopo do MVP;
- para onde o produto poderá evoluir;
- quais princípios devem ser preservados durante o desenvolvimento.

**Regra para agentes de IA:** este documento deve ser lido antes de realizar alterações relevantes no projeto.

---

## 2. O que é o ViralCode

O ViralCode será uma plataforma de inteligência de conteúdo.

A ideia inicial é permitir que o usuário informe um nicho, tema ou palavra-chave e encontre conteúdos de alto desempenho nas redes sociais, inicialmente com foco em vídeos curtos.

O sistema deverá coletar, organizar e armazenar informações sobre esses conteúdos para posteriormente analisá-los e identificar padrões associados ao desempenho.

A visão de longo prazo é transformar esses dados em inteligência para:

1. descobrir conteúdos relevantes;
2. identificar conteúdos virais;
3. analisar por que determinados conteúdos performam;
4. identificar padrões por nicho, perfil, público e plataforma;
5. gerar novos conteúdos baseados nesses padrões;
6. organizar conteúdos para publicação;
7. publicar conteúdos nas redes sociais;
8. coletar os resultados das publicações;
9. aprender com os próprios resultados.

O ViralCode, portanto, não deve ser tratado apenas como um buscador de vídeos.

A visão é construir uma plataforma de **inteligência, criação e distribuição de conteúdo**.

---

## 3. Problema que queremos resolver

Hoje, encontrar conteúdos que realmente performaram bem em determinado nicho é trabalhoso.

Uma pessoa que deseja criar conteúdo precisa pesquisar manualmente diferentes redes sociais, identificar vídeos relevantes, verificar visualizações, analisar formatos, observar ganchos, estudar comentários e tentar descobrir o que tornou determinado conteúdo bem-sucedido.

Esse processo é:

- demorado;
- repetitivo;
- difícil de comparar;
- dependente de pesquisa manual;
- pouco estruturado;
- difícil de transformar em conhecimento histórico.

O ViralCode pretende transformar esse processo em uma operação estruturada e automatizada.

---

## 4. Hipótese inicial do negócio

A hipótese que será validada pelo MVP é:

> Existe valor em uma ferramenta que permita descobrir rapidamente conteúdos de alto desempenho por nicho e organizar esses dados em um ranking pesquisável.

A primeira validação não depende de criar todo o produto final.

Precisamos primeiro descobrir se usuários realmente consideram valioso:

- pesquisar um nicho;
- encontrar conteúdos relevantes;
- filtrar por número de visualizações;
- visualizar os principais resultados;
- acessar os conteúdos originais;
- ter esses dados organizados em um único lugar.

Se essa hipótese for validada, o produto poderá evoluir para análise, geração e publicação.

---

## 5. Visão do produto

A evolução planejada do ViralCode é:

```text
DESCOBRIR
    ↓
ARMAZENAR
    ↓
ANALISAR
    ↓
ENTENDER
    ↓
CRIAR
    ↓
PUBLICAR
    ↓
MEDIR
    ↓
APRENDER
    ↓
MELHORAR A CRIAÇÃO
```

Essa visão representa o ciclo de inteligência do produto.

### 5.1 Descobrir

Encontrar conteúdos em diferentes redes sociais.

### 5.2 Armazenar

Criar uma base histórica própria com conteúdos, autores e métricas.

### 5.3 Analisar

Extrair características dos conteúdos.

### 5.4 Entender

Identificar padrões de desempenho, temas, ganchos, emoções, estruturas e chamadas para ação.

### 5.5 Criar

Gerar novos conteúdos utilizando a inteligência acumulada.

### 5.6 Publicar

Distribuir os conteúdos para diferentes redes sociais.

### 5.7 Medir

Coletar o desempenho dos conteúdos publicados.

### 5.8 Aprender

Comparar resultados e alimentar novamente o motor de inteligência.

---

## 6. Estado atual do projeto

Neste momento, o ViralCode está na fase de definição da arquitetura e preparação do MVP.

Ainda não estamos implementando todos os motores previstos para a visão futura.

O primeiro objetivo é construir uma versão mínima, funcional e simples o suficiente para validar o negócio.

---

## 7. MVP inicial

O MVP será propositalmente pequeno.

### Objetivo

Validar se existe valor em:

> pesquisar um nicho e encontrar conteúdos de alto desempenho organizados em um ranking.

### Fluxo do MVP

```text
USUÁRIO
   ↓
INFORMA NICHO / TERMO
   ↓
REACT
   ↓
FASTAPI
   ↓
SERVIÇO DE BUSCA
   ↓
PROVEDOR DE DADOS
   ↓
NORMALIZAÇÃO
   ↓
DEDUPLICAÇÃO
   ↓
REPOSITÓRIO
   ↓
SQLALCHEMY
   ↓
MYSQL
   ↓
REACT
   ↓
RESULTADOS
```

---

## 8. O que o MVP deverá fazer

A primeira versão deverá permitir:

- informar um termo ou nicho;
- selecionar uma plataforma inicialmente suportada;
- definir um número mínimo de visualizações;
- definir um período de pesquisa;
- executar a pesquisa;
- receber os resultados;
- eliminar resultados duplicados;
- armazenar os resultados no banco;
- exibir os conteúdos encontrados;
- ordenar os resultados por desempenho;
- acessar o conteúdo original.

Inicialmente, o foco será **Instagram e conteúdos em formato de Reel**, utilizando um provedor externo de dados para validar a hipótese.

O primeiro provedor considerado é a SocialKit.

A integração deverá ser isolada em uma camada própria para permitir sua substituição no futuro.

---

## 9. O que NÃO faz parte do MVP

É fundamental não antecipar funcionalidades futuras.

O MVP inicial NÃO deverá implementar, salvo solicitação explícita:

- geração automática de Reels;
- geração automática de posts;
- geração automática de carrosséis;
- publicação automática;
- calendário editorial;
- gerenciamento de múltiplos perfis;
- gerenciamento completo de múltiplas redes;
- análise avançada de comentários;
- sistema completo de Viral DNA;
- sistema completo de padrões virais;
- aprendizado automático baseado em desempenho;
- geração automática de vídeos;
- editor de vídeo;
- sistema completo de assinaturas;
- sistema de cobrança;
- aplicativo mobile;
- arquitetura distribuída complexa;
- microsserviços;
- infraestrutura de nuvem complexa.

Esses itens pertencem à visão futura e não devem aumentar a complexidade do MVP.

---

## 10. Arquitetura tecnológica definida

A arquitetura base definida para o projeto é:

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

### Frontend

- React
- TypeScript

### Backend

- Python
- FastAPI
- Pydantic

### Persistência

- MySQL
- SQLAlchemy
- Alembic

### Ambiente

- desenvolvimento local;
- Docker e Docker Compose quando aplicável;
- futura hospedagem em VPS da Hostinger.

---

## 11. Princípio de arquitetura

O sistema deverá separar responsabilidades.

### Rotas

Responsáveis por receber requisições e devolver respostas.

### Serviços

Responsáveis pelas regras de negócio.

### Repositórios

Responsáveis pelo acesso aos dados.

### SQLAlchemy

Responsável pelo mapeamento objeto-relacional.

### MySQL

Responsável pela persistência.

### Provedores

Responsáveis por integrações externas.

Exemplo:

```text
Rota
  ↓
Serviço
  ↓
Provedor externo
  ↓
Normalização
  ↓
Repositório
  ↓
SQLAlchemy
  ↓
MySQL
```

Uma rota não deve acessar diretamente o banco.

---

## 12. Idioma oficial do projeto

O ViralCode será desenvolvido integralmente em **português do Brasil**.

Isso se aplica a:

- documentação;
- nomes de arquivos;
- nomes de pastas;
- classes;
- funções;
- métodos;
- variáveis;
- tabelas;
- colunas;
- endpoints;
- schemas;
- serviços;
- repositórios;
- testes;
- mensagens de erro;
- logs;
- comentários;
- textos da interface.

### Exceção

Nomes próprios de tecnologias, bibliotecas, frameworks, comandos e produtos não serão traduzidos.

Exemplos:

- React;
- Python;
- FastAPI;
- SQLAlchemy;
- MySQL;
- Docker;
- Docker Compose;
- Alembic.

Não devemos criar traduções artificiais desses nomes.

---

## 13. Visão de arquitetura futura

O MVP deverá ser simples, mas o código deve ser organizado para permitir evolução.

A arquitetura-alvo é:

```text
                 VIRALCODE
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
   DESCOBERTA   INTELIGÊNCIA   CRIAÇÃO
        │            │            │
        └────────────┼────────────┘
                     ↓
                 PUBLICAÇÃO
                     ↓
                 DESEMPENHO
                     ↓
                  APRENDIZADO
                     │
                     └────────→ INTELIGÊNCIA
```

O produto deverá futuramente suportar:

- diferentes nichos;
- diferentes perfis;
- diferentes marcas;
- diferentes públicos;
- diferentes redes sociais;
- diferentes formatos de conteúdo;
- diferentes provedores de dados;
- diferentes provedores de inteligência artificial.

---

## 14. Multi-nicho

O nicho não deve ser codificado diretamente na aplicação.

Exemplos futuros:

```text
Casamento
Fitness
Finanças
Educação
Imóveis
Marketing
Religião
Tecnologia
```

O mesmo sistema deverá funcionar para qualquer nicho.

---

## 15. Multi-perfil

O ViralCode deverá futuramente permitir diferentes perfis.

Exemplo:

```text
Organização
│
├── Perfil Leonardo Escrivani
├── Perfil Fabi
├── Perfil Destrava Matemática
└── Perfil Cliente
```

Cada perfil poderá possuir:

- nicho;
- público;
- tom de voz;
- identidade visual;
- regras de conteúdo;
- contas sociais;
- configurações próprias de inteligência artificial.

Essa capacidade pertence à arquitetura futura, não ao primeiro MVP.

---

## 16. Multi-plataforma

A arquitetura deverá permitir futuramente:

```text
Instagram
TikTok
YouTube
Facebook
LinkedIn
```

Cada plataforma deverá ser tratada por um adaptador ou provedor específico.

O restante do sistema não deve depender de detalhes internos de uma plataforma específica.

---

## 17. Motor de criação futuro

Depois da validação do MVP, será criado um motor capaz de transformar inteligência em conteúdo.

Fluxo planejado:

```text
Conteúdos analisados
        ↓
Padrões identificados
        ↓
Nicho
        ↓
Perfil
        ↓
Público
        ↓
Tom de voz
        ↓
Motor de criação
        ↓
Post / Reel / Carrossel / Story
```

O motor deverá gerar conteúdo original.

A inteligência coletada deverá servir como referência e não como mecanismo para copiar conteúdos existentes.

---

## 18. Motor de publicação futuro

Posteriormente será criado um motor de publicação independente do motor de criação.

```text
Conteúdo
    ↓
Motor de publicação
    ↓
Adaptador da plataforma
    ├── Instagram
    ├── Facebook
    ├── TikTok
    └── YouTube
```

Isso permitirá que um mesmo conteúdo seja adaptado e distribuído para diferentes redes.

---

## 19. Motor de desempenho futuro

Após a publicação, o ViralCode deverá coletar métricas.

Exemplos:

- visualizações;
- curtidas;
- comentários;
- compartilhamentos;
- salvamentos;
- alcance;
- retenção, quando disponível;
- crescimento ao longo do tempo.

O sistema deverá manter histórico para permitir análise de evolução.

---

## 20. Motor de aprendizado futuro

A visão final é criar um ciclo de aprendizado:

```text
Conteúdo externo
      ↓
Inteligência
      ↓
Conteúdo criado
      ↓
Publicação
      ↓
Resultado
      ↓
Análise
      ↓
Aprendizado
      ↓
Nova inteligência
```

Com isso, o ViralCode poderá descobrir quais padrões funcionam para:

- determinado nicho;
- determinado perfil;
- determinado público;
- determinada plataforma;
- determinado formato.

---

## 21. Princípio de simplicidade

O MVP deverá ser o mais simples possível.

A regra é:

> **Construir somente o necessário para validar a hipótese atual.**

Não devemos implementar arquitetura complexa apenas porque ela será necessária no futuro.

Devemos, entretanto, evitar decisões que tornem a evolução futura desnecessariamente difícil.

A diferença é:

```text
EVITAR
Complexidade antecipada

PERMITIR
Evolução organizada
```

---

## 22. Princípio de evolução

Sempre que uma funcionalidade futura for necessária, ela deverá ser adicionada como uma evolução do sistema existente.

Não devemos criar todos os motores futuros no MVP.

A evolução planejada é:

```text
MVP
 ↓
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
```

---

## 23. Desenvolvimento local

Durante o desenvolvimento inicial, o projeto funcionará localmente.

O ambiente deverá permitir executar:

```text
Frontend React
Backend FastAPI
MySQL
```

preferencialmente de forma reproduzível através de Docker/Docker Compose quando essa configuração for criada.

---

## 24. Hospedagem futura

Após a validação do MVP, o sistema será hospedado em uma VPS da Hostinger.

A aplicação deverá ser preparada para migração do ambiente local para a VPS sem alterações estruturais significativas.

O ambiente de produção deverá posteriormente considerar:

```text
Internet
   ↓
Nginx
   ↓
Frontend / Backend
   ↓
MySQL
```

Detalhes de implantação serão definidos no documento de implantação.

---

## 25. Critério de sucesso do MVP

O MVP não será considerado bem-sucedido apenas porque funciona tecnicamente.

Precisamos validar o negócio.

As perguntas principais são:

1. As pessoas querem pesquisar conteúdos virais por nicho?
2. Os resultados são úteis?
3. O ranking economiza tempo?
4. O usuário voltaria a utilizar a ferramenta?
5. Existe disposição para pagar?
6. Qual informação é mais valorizada?
7. Qual será o próximo recurso mais importante?

O resultado dessas respostas determinará a próxima etapa do produto.

---

## 26. Regra para agentes de inteligência artificial

Qualquer agente que trabalhar neste projeto deverá:

1. Ler este documento antes de alterações relevantes.
2. Consultar o escopo do MVP.
3. Respeitar a arquitetura definida.
4. Respeitar o idioma português.
5. Não implementar funcionalidades futuras sem solicitação.
6. Não inventar integrações ou contratos de APIs.
7. Não expor chaves ou segredos no código.
8. Não alterar decisões arquiteturais importantes silenciosamente.
9. Testar alterações relevantes.
10. Manter a documentação atualizada quando uma decisão importante for modificada.

---

## 27. Regra principal do projeto

> **O ViralCode deve nascer pequeno, funcionar de verdade e crescer somente depois que o negócio provar que merece crescer.**

A arquitetura futura orienta o caminho.

O MVP determina o que deve ser construído agora.

**Não confundir visão de longo prazo com escopo de desenvolvimento atual.**

---

## 28. Estado deste documento

Este documento representa o contexto inicial do ViralCode.

Alterações importantes na visão, arquitetura ou estratégia deverão ser registradas e, quando necessário, acompanhadas de uma decisão arquitetural em `docs/16_DECISOES.md`.

**Versão atual:** 0.1  
**Status:** Base inicial do projeto
