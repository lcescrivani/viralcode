# 07 — BANCO DE DADOS DO VIRALCODE

**Versão:** 0.1  
**Status:** Documento inicial  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode  
**Banco:** MySQL  
**ORM:** SQLAlchemy  
**Migrações:** Alembic

---

## 1. Objetivo deste documento

Este documento define as regras e a estrutura inicial do banco de dados do ViralCode.

O objetivo é:

- definir as tabelas do MVP;
- definir os relacionamentos;
- estabelecer padrões de nomenclatura;
- orientar a criação dos modelos SQLAlchemy;
- orientar as migrations Alembic;
- evitar duplicação de dados;
- preparar o banco para evolução futura;
- impedir que agentes de inteligência artificial criem estruturas desnecessárias.

A regra principal é:

> **O banco do MVP deve ser pequeno, mas não deve bloquear a evolução do produto.**

---

# 2. Banco oficial

O banco de dados oficial do ViralCode será:

> **MySQL**

A aplicação utilizará:

> **SQLAlchemy**

As alterações estruturais serão controladas por:

> **Alembic**

Fluxo:

```text
Código
   ↓
Modelo SQLAlchemy
   ↓
Alembic
   ↓
MySQL
```

---

# 3. Princípios do banco

O banco deverá seguir estes princípios:

1. nomes em português;
2. estrutura simples;
3. integridade referencial;
4. índices adequados;
5. evitar duplicação;
6. migrations versionadas;
7. chaves internas estáveis;
8. identificadores externos separados;
9. datas explícitas;
10. não criar tabelas futuras antecipadamente sem necessidade.

---

# 4. Modelo mínimo do MVP

O MVP deverá começar com quatro entidades principais:

```text
buscas
conteudos
autores
metricas_conteudo
```

Relacionamento:

```text
BUSCA
  │
  └── resultados
          │
          └── CONTEÚDO
                  │
                  ├── AUTOR
                  │
                  └── MÉTRICAS
```

---

# 5. Tabela `buscas`

## Objetivo

Registrar cada pesquisa realizada no ViralCode.

### Campos conceituais

```text
id
termo
plataforma
visualizacoes_minimas
periodo_dias
data_criacao
```

### Descrição

| Campo | Tipo conceitual | Obrigatório | Descrição |
|---|---|---:|---|
| id | inteiro | Sim | Identificador interno |
| termo | texto | Sim | Termo pesquisado |
| plataforma | texto | Sim | Plataforma pesquisada |
| visualizacoes_minimas | inteiro | Sim | Filtro mínimo |
| periodo_dias | inteiro | Não | Período da busca |
| data_criacao | data/hora | Sim | Momento da pesquisa |

Os tipos exatos serão definidos na implementação SQLAlchemy.

---

# 6. Tabela `autores`

## Objetivo

Representar o autor original do conteúdo encontrado.

Um autor não precisa ser usuário do ViralCode.

### Campos conceituais

```text
id
plataforma
identificador_externo
nome_usuario
nome
url_perfil
seguidores
data_criacao
data_atualizacao
```

### Regras

O identificador externo deverá ser utilizado quando estiver disponível.

A combinação:

```text
plataforma
+
identificador_externo
```

deverá ser considerada para unicidade.

---

# 7. Tabela `conteudos`

## Objetivo

Representar o conteúdo encontrado.

### Campos conceituais

```text
id
plataforma
identificador_externo
autor_id
tipo
url
legenda
data_publicacao
url_imagem
data_primeira_coleta
data_ultima_atualizacao
data_criacao
data_atualizacao
```

### Campos prioritários do MVP

- id;
- plataforma;
- identificador externo;
- autor;
- tipo;
- URL;
- legenda, quando disponível;
- data de publicação, quando disponível;
- imagem, quando disponível;
- data de coleta.

---

# 8. Identificador externo

O conteúdo deverá possuir um identificador externo quando a plataforma/provedor disponibilizar.

Exemplo:

```text
plataforma = instagram
identificador_externo = 123456789
```

A combinação deverá ser única:

```text
instagram + 123456789
```

Isso evita armazenar o mesmo conteúdo duas vezes.

---

# 9. URL

A URL original do conteúdo deverá ser armazenada quando disponível.

A URL poderá ser utilizada para:

- abrir o conteúdo;
- referência ao usuário;
- validação;
- recuperação futura.

A URL não deve necessariamente ser a chave primária.

---

# 10. Tipo de conteúdo

O campo `tipo` deverá permitir identificar formatos.

Exemplos:

```text
reel
video
post
carrossel
story
short
```

No MVP, o valor principal será:

```text
reel
```

---

# 11. Tabela `metricas_conteudo`

## Objetivo

Armazenar métricas observadas de um conteúdo.

### Campos conceituais

```text
id
conteudo_id
visualizacoes
curtidas
comentarios
compartilhamentos
salvamentos
data_coleta
```

Alguns campos podem não estar disponíveis dependendo do provedor.

---

# 12. Métricas opcionais

O sistema não deverá exigir que todas as métricas existam.

Exemplo:

```text
visualizacoes = 1.500.000
curtidas = 90.000
comentarios = NULL
```

A ausência de uma métrica não significa necessariamente erro.

---

# 13. Histórico de métricas

A tabela de métricas deverá permitir múltiplas observações do mesmo conteúdo.

Exemplo:

```text
conteudo_id = 10

10:00 → 100.000 visualizações
14:00 → 180.000 visualizações
18:00 → 310.000 visualizações
22:00 → 500.000 visualizações
```

Isso será fundamental para funcionalidades futuras de:

- velocidade de crescimento;
- tendência;
- desempenho;
- aprendizado.

---

# 14. Relação `conteudos` → `metricas_conteudo`

Um conteúdo poderá possuir muitas métricas.

```text
conteudos
    1
    │
    │
    └──────── N
        metricas_conteudo
```

Relacionamento:

> Um conteúdo possui muitas observações de métricas.

---

# 15. Relação `autores` → `conteudos`

Um autor poderá possuir muitos conteúdos.

```text
autores
   1
   │
   └──────── N
          conteudos
```

Um conteúdo poderá possuir um autor conhecido.

Se o provedor não retornar autor, o sistema deverá permitir ausência dessa relação quando apropriado.

---

# 16. Relação `buscas` → `conteudos`

Uma busca poderá retornar muitos conteúdos.

Mas um conteúdo poderá aparecer em muitas buscas.

Portanto, conceitualmente:

```text
buscas
  N
  │
  │
  N
conteudos
```

Esse é um relacionamento muitos-para-muitos.

---

# 17. Tabela intermediária de resultados

Para representar a relação entre busca e conteúdo, o banco deverá utilizar uma tabela intermediária.

Nome sugerido:

```text
resultados_busca
```

### Campos conceituais

```text
id
busca_id
conteudo_id
posicao
data_criacao
```

Opcionalmente poderá armazenar informações específicas daquela busca.

---

# 18. Tabela `resultados_busca`

## Objetivo

Registrar quais conteúdos apareceram em determinada busca.

Exemplo:

```text
Busca 1
│
├── Conteúdo 10
├── Conteúdo 15
├── Conteúdo 20
└── Conteúdo 25
```

A mesma busca não deverá relacionar o mesmo conteúdo duas vezes.

Regra:

```text
UNIQUE(busca_id, conteudo_id)
```

---

# 19. Posição no ranking

O campo `posicao` poderá registrar a posição do conteúdo no momento da busca.

Exemplo:

```text
Conteúdo A → posição 1
Conteúdo B → posição 2
Conteúdo C → posição 3
```

Isso permite preservar o resultado original mesmo se as métricas mudarem depois.

---

# 20. Modelo relacional do MVP

```text
┌──────────────┐
│    buscas    │
├──────────────┤
│ id           │
│ termo        │
│ plataforma   │
│ mínimo       │
│ período      │
│ data_criacao │
└──────┬───────┘
       │
       │ 1:N
       ▼
┌────────────────────┐
│ resultados_busca   │
├────────────────────┤
│ id                 │
│ busca_id           │
│ conteudo_id        │
│ posicao            │
└──────────┬─────────┘
           │
           │ N:1
           ▼
┌──────────────────────────┐
│        conteudos         │
├──────────────────────────┤
│ id                       │
│ plataforma               │
│ identificador_externo    │
│ autor_id                 │
│ tipo                     │
│ url                      │
│ legenda                  │
│ data_publicacao          │
│ url_imagem               │
│ data_primeira_coleta     │
│ data_ultima_atualizacao  │
└────────────┬─────────────┘
             │
             ├──────────────────────┐
             │                      │
             │ N:1                  │ 1:N
             ▼                      ▼
┌──────────────────────┐   ┌────────────────────────┐
│       autores        │   │   metricas_conteudo    │
├──────────────────────┤   ├────────────────────────┤
│ id                   │   │ id                     │
│ plataforma           │   │ conteudo_id            │
│ identificador_ext.   │   │ visualizacoes          │
│ nome_usuario         │   │ curtidas               │
│ nome                 │   │ comentarios            │
│ url_perfil           │   │ compartilhamentos     │
│ seguidores           │   │ salvamentos            │
└──────────────────────┘   │ data_coleta            │
                           └────────────────────────┘
```

---

# 21. Índices

Os índices deverão ser criados de acordo com os principais padrões de consulta.

Prioridades do MVP:

### `conteudos`

Índice em:

```text
plataforma
identificador_externo
```

Índice para:

```text
data_publicacao
```

### `metricas_conteudo`

Índice em:

```text
conteudo_id
data_coleta
```

### `resultados_busca`

Índice em:

```text
busca_id
conteudo_id
```

E uma restrição única:

```text
busca_id + conteudo_id
```

---

# 22. Índice de visualizações

Como o ranking inicial será baseado em visualizações, pode existir necessidade de otimização para consultas por essa métrica.

Entretanto, antes de criar índices adicionais, avaliar:

- quantidade de registros;
- plano de execução;
- frequência das consultas;
- custo do índice.

Não criar índices indiscriminadamente.

---

# 23. Integridade referencial

Relacionamentos deverão possuir chaves estrangeiras quando apropriado.

Exemplo:

```text
conteudos.autor_id
    ↓
autores.id
```

E:

```text
metricas_conteudo.conteudo_id
    ↓
conteudos.id
```

---

# 24. Exclusão de dados

Não excluir registros automaticamente sem uma regra clara.

Especialmente conteúdos e métricas históricas.

No futuro, poderá ser necessário utilizar:

- exclusão lógica;
- status;
- arquivamento.

A estratégia será definida conforme o produto evoluir.

---

# 25. Datas e horários

As datas deverão ser armazenadas de forma consistente.

Devemos diferenciar:

```text
data_publicacao
data_coleta
data_criacao
data_atualizacao
```

A aplicação deverá trabalhar com uma estratégia consistente de fuso horário.

---

# 26. Nomes das tabelas

Todas as tabelas serão nomeadas em português.

Exemplos:

```text
buscas
resultados_busca
conteudos
autores
metricas_conteudo
```

Evitar:

```text
searches
search_results
contents
authors
content_metrics
```

---

# 27. Nomes das colunas

Também deverão ser em português.

Exemplos:

```text
identificador_externo
data_publicacao
data_coleta
visualizacoes
curtidas
comentarios
```

Evitar:

```text
external_id
published_at
collected_at
views
likes
comments
```

---

# 28. Chaves primárias

As tabelas deverão possuir identificadores internos.

Exemplo:

```text
id
```

O identificador interno não deverá depender diretamente do identificador da rede social.

---

# 29. Identificadores externos

Identificadores de plataformas deverão ser armazenados separadamente.

Exemplo:

```text
id = 10

plataforma = instagram

identificador_externo = "ABC123"
```

Isso evita acoplamento do banco ao identificador externo.

---

# 30. Valores nulos

Campos que podem não existir na fonte deverão aceitar ausência quando fizer sentido.

Exemplo:

```text
compartilhamentos = NULL
```

não significa:

```text
compartilhamentos = 0
```

São situações diferentes.

---

# 31. Dados históricos

Métricas são observações históricas.

Não sobrescrever automaticamente todo o histórico.

Exemplo:

```text
10:00 → 100.000
12:00 → 150.000
14:00 → 220.000
```

Cada observação deverá permanecer quando o histórico for necessário.

---

# 32. Normalização

Os dados recebidos da SocialKit ou de outro provedor deverão ser convertidos para o modelo interno antes da persistência.

Fluxo:

```text
API externa
   ↓
Resposta externa
   ↓
Mapeador
   ↓
Modelo interno
   ↓
Validação
   ↓
Banco
```

O banco não deverá refletir simplesmente o formato de uma API externa.

---

# 33. Independência do provedor

O banco deverá representar o domínio do ViralCode.

Não criar dezenas de campos específicos de um único provedor sem necessidade.

Quando uma informação for específica de uma plataforma, avaliar se:

- pertence ao domínio comum;
- deve ser armazenada em estrutura específica;
- pode ser descartada;
- será necessária futuramente.

---

# 34. Evolução futura do banco

Depois do MVP, poderão ser adicionadas entidades como:

```text
organizacoes
usuarios
perfis
nichos
temas
subtemas
plataformas
contas_sociais
analises_conteudo
padroes
viral_dna
ideias
conteudos_gerados
publicacoes
desempenhos
campanhas
agendamentos
```

Essas tabelas não devem ser criadas apenas por antecipação.

---

# 35. Futuro relacionamento de perfis

Visão futura:

```text
organizacoes
      │
      └── perfis
            │
            ├── nichos
            └── contas_sociais
```

---

# 36. Futuro relacionamento de análises

Visão futura:

```text
conteudos
     │
     └── analises_conteudo
            │
            ├── temas
            ├── hooks
            ├── emocoes
            ├── estruturas
            └── chamadas_para_acao
```

A modelagem exata será definida quando essa funcionalidade entrar no produto.

---

# 37. Futuro relacionamento de publicação

```text
conteudo_gerado
      │
      └── publicacoes
             │
             ├── plataforma
             ├── conta_social
             ├── data_publicacao
             └── status
```

---

# 38. Futuro relacionamento de desempenho

```text
publicacao
     │
     └── desempenho
            │
            ├── visualizacoes
            ├── curtidas
            ├── comentarios
            ├── compartilhamentos
            └── salvamentos
```

---

# 39. Futuro multi-organização

Quando o SaaS for implementado:

```text
organizacao
    │
    ├── usuarios
    ├── perfis
    ├── contas_sociais
    ├── buscas
    ├── conteudos
    └── configuracoes
```

As regras de isolamento de dados deverão ser definidas antes dessa fase.

---

# 40. Migrations

Toda alteração de estrutura deverá gerar uma migration.

Fluxo:

```text
Alteração no modelo
        ↓
Alembic
        ↓
Migration
        ↓
Banco
```

Não editar diretamente a estrutura de produção sem migration correspondente.

---

# 41. Desenvolvimento das migrations

As migrations deverão:

- possuir descrição clara;
- ser versionadas;
- ser reproduzíveis;
- permitir criação do banco do zero;
- permitir atualização incremental.

Evitar migrations que dependam de estado manual não documentado.

---

# 42. Banco de desenvolvimento

O ambiente local poderá possuir um banco específico para desenvolvimento.

Os dados de teste não devem ser tratados como dados de produção.

---

# 43. Dados de teste

Poderão existir dados fictícios para testes.

Exemplo:

```text
@perfil_teste
conteudo_teste
busca_teste
```

Não utilizar dados reais de usuários como massa de teste sem necessidade e autorização apropriada.

---

# 44. Seed

Um mecanismo de seed poderá ser criado para popular dados mínimos de desenvolvimento.

Exemplo:

```text
1 nicho
3 autores
10 conteúdos
métricas fictícias
```

Não é obrigatório no primeiro momento.

---

# 45. Backup futuro

Na produção, o MySQL deverá possuir estratégia de backup.

A frequência e retenção serão definidas em `14_IMPLANTACAO.md`.

No desenvolvimento local, backup não é prioridade.

---

# 46. Performance

O banco deverá ser otimizado somente com base em necessidade real.

Ordem:

```text
Modelo correto
   ↓
Consultas corretas
   ↓
Índices
   ↓
Medição
   ↓
Otimização
```

Evitar otimizações prematuras.

---

# 47. Segurança

Nunca armazenar no banco:

- chaves de API sem necessidade;
- senhas em texto puro;
- segredos de provedores sem proteção.

Credenciais deverão ser tratadas pela camada de configuração e segurança apropriada.

---

# 48. Regra para agentes de inteligência artificial

Antes de criar uma tabela:

1. verificar se a entidade já existe;
2. verificar se é realmente uma entidade;
3. verificar se pode ser apenas uma coluna;
4. verificar se faz parte do MVP;
5. verificar se existe relação com outra tabela;
6. verificar impacto nas migrations;
7. atualizar este documento se a decisão for relevante.

---

# 49. Regra de simplicidade do banco

O banco inicial deve ser pequeno.

Não criar:

```text
20 tabelas
```

porque a visão futura possui 20 entidades.

Começar com:

```text
buscas
resultados_busca
conteudos
autores
metricas_conteudo
```

e adicionar novas tabelas conforme o produto precisar.

---

# 50. Modelo mínimo recomendado

A primeira versão do banco deverá seguir aproximadamente:

```text
buscas
   │
   ▼
resultados_busca
   │
   ▼
conteudos
   │
   ├──── autores
   │
   └──── metricas_conteudo
```

Essa estrutura é suficiente para validar o primeiro fluxo.

---

# 51. Regra final

> **O banco de dados deve armazenar o conhecimento necessário para o produto atual sem transformar a visão futura em complexidade prematura.**

O MVP precisa provar:

```text
Busca
  ↓
Conteúdo
  ↓
Métrica
  ↓
Ranking
  ↓
Valor
```

Depois, o banco poderá evoluir para armazenar:

```text
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

**Versão atual:** 0.1  
**Status:** Modelo inicial do banco de dados do ViralCode
