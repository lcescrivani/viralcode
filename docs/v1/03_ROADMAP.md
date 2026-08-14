# 03 — ROADMAP DO VIRALCODE

**Versão:** 0.1  
**Status:** Documento inicial  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo deste documento

Este documento apresenta o caminho de evolução planejado para o ViralCode.

O roadmap existe para:

- organizar a evolução do produto;
- separar presente de futuro;
- evitar aumento prematuro de escopo;
- orientar decisões técnicas;
- permitir que agentes de inteligência artificial entendam a direção do projeto;
- manter o foco na validação do negócio.

O roadmap é uma direção, não uma obrigação imutável.

As prioridades poderão mudar conforme os resultados do MVP e os aprendizados obtidos com usuários reais.

---

## 2. Princípio principal do roadmap

> **Cada nova fase deve ser justificada pelo aprendizado da fase anterior.**

Não devemos construir uma funcionalidade apenas porque ela está prevista neste documento.

A evolução deverá seguir:

```text
Construir
   ↓
Validar
   ↓
Medir
   ↓
Aprender
   ↓
Priorizar
   ↓
Construir novamente
```

---

# 3. Visão geral das fases

A evolução inicial prevista é:

```text
FASE 0
Fundação
   ↓
FASE 1
MVP — Descoberta
   ↓
FASE 2
Inteligência
   ↓
FASE 3
Criação
   ↓
FASE 4
Publicação
   ↓
FASE 5
Desempenho
   ↓
FASE 6
Aprendizado
   ↓
FASE 7
Plataforma SaaS
```

---

# 4. FASE 0 — Fundação

## Objetivo

Criar a base técnica e documental do projeto.

## Escopo

- documentação inicial;
- estrutura de diretórios;
- React;
- FastAPI;
- SQLAlchemy;
- MySQL;
- Alembic;
- configuração de ambiente;
- estrutura de testes;
- integração inicial entre frontend e backend;
- endpoint de saúde da aplicação.

## Resultado esperado

Ter um projeto executável localmente e organizado para receber o MVP.

## Não construir

- inteligência artificial;
- geração de conteúdo;
- publicação;
- múltiplas plataformas;
- sistema de usuários completo;
- cobrança.

---

# 5. FASE 1 — MVP DE DESCOBERTA

**Prioridade: máxima**

## Objetivo

Validar a hipótese principal do negócio.

## Hipótese

> Usuários valorizam uma ferramenta que encontre e organize conteúdos de alto desempenho por nicho.

## Funcionalidades

- pesquisa por termo;
- seleção de plataforma;
- filtro mínimo de visualizações;
- filtro por período;
- consulta ao provedor;
- normalização;
- deduplicação;
- armazenamento;
- ranking;
- exibição dos resultados;
- acesso ao conteúdo original.

## Plataforma inicial

Instagram.

## Formato inicial

Reels.

## Provedor inicial

SocialKit, desde que os testes confirmem viabilidade técnica e econômica.

## Nicho inicial de validação

Casamento.

O nicho é apenas um dado de teste.

O sistema deverá ser genérico.

## Resultado esperado

Uma pessoa consegue pesquisar:

```text
casamento
```

com:

```text
Instagram
1.000.000+ visualizações
últimos 90 dias
```

e receber uma lista organizada de conteúdos.

---

# 6. Validação do MVP

Antes de construir a Fase 2, precisamos observar:

### Utilidade

Os resultados são realmente úteis?

### Relevância

Os conteúdos encontrados correspondem ao que o usuário procurou?

### Economia de tempo

O produto economiza tempo em relação à pesquisa manual?

### Retorno

O usuário volta a pesquisar?

### Interesse

O usuário quer mais informações sobre os conteúdos?

### Disposição para pagar

Existe valor comercial percebido?

---

# 7. FASE 2 — INTELIGÊNCIA DE CONTEÚDO

**Prioridade: alta, somente após validação do MVP**

## Objetivo

Transformar dados coletados em inteligência.

## Funcionalidades previstas

### Transcrição

Extrair o conteúdo falado dos vídeos quando tecnicamente e legalmente viável.

### Análise textual

Analisar:

- legenda;
- título;
- texto;
- transcrição.

### Análise estrutural

Identificar:

- hook;
- desenvolvimento;
- conclusão;
- CTA;
- formato.

### Análise emocional

Identificar emoções e necessidades exploradas.

### Classificação

Classificar:

- tema;
- subtema;
- nicho;
- formato;
- público;
- objetivo.

---

# 8. VIRAL DNA

Ainda na Fase 2, poderá ser criado o Viral DNA.

Exemplo:

```text
Conteúdo
   ↓
Viral DNA
   │
   ├── Tema
   ├── Hook
   ├── Dor
   ├── Desejo
   ├── Emoção
   ├── Estrutura
   ├── CTA
   ├── Formato
   └── Público
```

## Objetivo

Permitir comparação estruturada entre conteúdos.

---

# 9. PADRÕES VIRAIS

Também poderá ser criado um mecanismo para analisar conjuntos de conteúdos.

Exemplo:

```text
100 conteúdos de casamento
          ↓
       análise
          ↓
   padrões encontrados
          ↓
"Hooks com perguntas..."
"Conteúdo de identificação..."
"CTA para compartilhar..."
```

O sistema deverá apresentar padrões como observações e análises, evitando tratar correlação como causalidade.

---

# 10. FASE 3 — MOTOR DE CRIAÇÃO

**Prioridade: alta, depois de validar a inteligência**

## Objetivo

Transformar inteligência em conteúdo original.

## Entradas

```text
Nicho
Perfil
Público
Tom de voz
Objetivo
Plataforma
Formato
Padrões encontrados
```

## Saídas previstas

- ideias;
- hooks;
- roteiros;
- posts;
- carrosséis;
- Reels;
- Stories;
- legendas;
- CTAs.

---

# 11. PERFIL E IDENTIDADE

Antes da criação avançada, o sistema deverá compreender o perfil para o qual está criando.

Cada perfil poderá possuir:

- nome;
- nicho;
- público;
- posicionamento;
- objetivos;
- tom de voz;
- identidade visual;
- regras editoriais;
- temas permitidos;
- temas proibidos;
- plataformas conectadas.

Exemplo:

```text
Perfil:
Leonardo Escrivani

Nicho:
Casamento

Público:
Casais

Tom:
Direto, humano e acolhedor

Objetivo:
Autoridade + relacionamento + conversão
```

---

# 12. FASE 4 — MOTOR DE PUBLICAÇÃO

**Prioridade: média/alta**

## Objetivo

Permitir que o conteúdo criado seja enviado às plataformas.

## Arquitetura

```text
Conteúdo
   ↓
Motor de Publicação
   ↓
Adaptador da plataforma
   ├── Instagram
   ├── Facebook
   ├── TikTok
   ├── YouTube
   └── outras
```

Cada plataforma deverá possuir uma integração isolada.

---

# 13. CALENDÁRIO EDITORIAL

Como parte da Fase 4, poderá ser criado:

- calendário;
- agendamento;
- status de conteúdo;
- aprovação;
- fila de publicação;
- histórico.

Fluxo:

```text
Ideia
 ↓
Roteiro
 ↓
Produção
 ↓
Aprovação
 ↓
Agendamento
 ↓
Publicação
```

---

# 14. FASE 5 — DESEMPENHO

**Prioridade: média**

## Objetivo

Medir o que aconteceu depois da publicação.

O ViralCode deverá futuramente coletar:

- visualizações;
- curtidas;
- comentários;
- compartilhamentos;
- salvamentos;
- alcance;
- retenção, quando disponível;
- crescimento;
- outras métricas disponíveis por plataforma.

---

# 15. HISTÓRICO DE MÉTRICAS

O sistema deverá guardar a evolução das métricas.

Exemplo:

```text
Conteúdo
   │
   └── Histórico
       │
       ├── 10:00 → 100.000 visualizações
       ├── 14:00 → 180.000
       ├── 18:00 → 310.000
       └── 24:00 → 520.000
```

Isso permitirá medir velocidade de crescimento.

---

# 16. VIRAL VELOCITY

Funcionalidade futura para identificar a velocidade de crescimento de um conteúdo.

Exemplo:

```text
Conteúdo A
10.000 visualizações/hora

Conteúdo B
250.000 visualizações/hora
```

O segundo pode ser mais relevante para detectar uma tendência emergente, mesmo que ainda tenha menos visualizações totais.

---

# 17. FASE 6 — MOTOR DE APRENDIZADO

**Prioridade: alta no produto maduro**

## Objetivo

Fazer o ViralCode aprender com os resultados.

Fluxo:

```text
Conteúdo externo
      ↓
Padrão
      ↓
Conteúdo criado
      ↓
Publicação
      ↓
Resultado
      ↓
Comparação
      ↓
Aprendizado
```

O sistema poderá descobrir:

- quais hooks funcionam para determinado perfil;
- quais temas funcionam;
- quais formatos funcionam;
- quais CTAs funcionam;
- quais padrões externos também funcionam internamente;
- quais padrões não funcionam para determinado público.

---

# 18. INTELIGÊNCIA ESPECÍFICA POR PERFIL

No produto maduro, cada perfil terá seu próprio histórico.

Exemplo:

```text
Mercado
   ↓
Padrões gerais

Perfil
   ↓
Padrões próprios

ViralCode
   ↓
Combinação das duas inteligências
```

Isso permitirá recomendações mais específicas.

---

# 19. FASE 7 — PLATAFORMA SAAS

**Prioridade: somente quando houver validação comercial**

## Objetivo

Transformar o ViralCode em um produto SaaS comercial.

## Funcionalidades previstas

- cadastro de organizações;
- usuários;
- equipes;
- perfis;
- múltiplos nichos;
- contas sociais;
- permissões;
- planos;
- créditos;
- assinaturas;
- cobrança;
- limites de utilização.

---

# 20. MULTI-NICHO

O produto deverá funcionar para qualquer nicho.

Exemplos:

```text
Casamento
Fitness
Finanças
Educação
Imóveis
Marketing
Tecnologia
Beleza
Gastronomia
Religião
```

Nenhum nicho deverá ser codificado como regra fixa do sistema.

---

# 21. MULTI-PERFIL

Uma organização poderá possuir diversos perfis.

Exemplo:

```text
Organização
│
├── Perfil A
├── Perfil B
├── Perfil C
└── Perfil D
```

Cada perfil terá suas próprias configurações.

---

# 22. MULTI-PLATAFORMA

A evolução prevista é:

```text
Instagram
   ↓
TikTok
   ↓
YouTube
   ↓
Facebook
   ↓
LinkedIn
   ↓
outras plataformas
```

A ordem real será determinada por demanda, viabilidade técnica, APIs disponíveis e oportunidade de negócio.

---

# 23. FASE DE ESCALA

Somente quando houver necessidade real, poderão ser adicionados:

- processamento assíncrono em maior escala;
- filas distribuídas;
- cache avançado;
- armazenamento de objetos;
- mecanismos de busca especializados;
- processamento paralelo;
- observabilidade avançada;
- arquitetura distribuída.

Não implementar esses recursos antecipadamente.

---

# 24. Roadmap técnico resumido

```text
FASE 0
Fundação
React + FastAPI + SQLAlchemy + MySQL
        ↓
FASE 1
Busca + ranking
        ↓
FASE 2
Análise + Viral DNA
        ↓
FASE 3
Geração de conteúdo
        ↓
FASE 4
Publicação
        ↓
FASE 5
Métricas
        ↓
FASE 6
Aprendizado
        ↓
FASE 7
SaaS
        ↓
ESCALA
```

---

# 25. Roadmap de produto resumido

```text
                   VIRALCODE

              ┌───────────────┐
              │  DESCOBRIR    │
              └───────┬───────┘
                      ↓
              ┌───────────────┐
              │    ANALISAR   │
              └───────┬───────┘
                      ↓
              ┌───────────────┐
              │    ENTENDER   │
              └───────┬───────┘
                      ↓
              ┌───────────────┐
              │     CRIAR     │
              └───────┬───────┘
                      ↓
              ┌───────────────┐
              │   PUBLICAR    │
              └───────┬───────┘
                      ↓
              ┌───────────────┐
              │    MEDIR      │
              └───────┬───────┘
                      ↓
              ┌───────────────┐
              │   APRENDER    │
              └───────┬───────┘
                      │
                      └──────→ novo ciclo
```

---

# 26. Critérios para avançar de fase

Uma fase não deverá avançar automaticamente apenas porque a anterior foi concluída tecnicamente.

Para avançar, devemos avaliar:

### Produto

A funcionalidade resolve um problema real?

### Uso

As pessoas utilizam?

### Retorno

As pessoas voltam?

### Valor

A funcionalidade aumenta o valor percebido?

### Negócio

Existe possibilidade de monetização?

### Custo

O custo operacional é sustentável?

---

# 27. Critérios de prioridade

Quando houver várias funcionalidades possíveis, priorizar nesta ordem:

1. impacto na validação do negócio;
2. valor para o usuário;
3. redução de incerteza;
4. facilidade de implementação;
5. custo operacional;
6. escalabilidade.

Não priorizar uma funcionalidade apenas porque ela parece tecnicamente interessante.

---

# 28. O que pode mudar neste roadmap

Este documento não deve ser tratado como contrato imutável.

O roadmap poderá mudar por causa de:

- feedback de usuários;
- limitações das APIs;
- custos de provedores;
- mudanças das plataformas;
- novas oportunidades;
- novas tecnologias;
- resultados do MVP;
- mudanças no modelo de negócio.

Quando uma mudança for importante, ela deverá ser registrada no documento de decisões do projeto.

---

# 29. Relação entre roadmap e MVP

O roadmap mostra o caminho.

O documento `02_ESCOPO_DO_MVP.md` determina o que está sendo construído agora.

Portanto:

```text
ROADMAP
   = visão de evolução

MVP
   = trabalho atual
```

Uma funcionalidade estar no roadmap **não significa que ela deve ser implementada agora**.

---

# 30. Regra para agentes de inteligência artificial

Antes de implementar uma nova funcionalidade, o agente deverá verificar:

1. Ela está no escopo do MVP?
2. Ela é necessária para validar o negócio?
3. Ela foi explicitamente solicitada?
4. Ela altera alguma decisão arquitetural?
5. Ela deve ser registrada para uma fase futura?

Se não fizer parte do MVP, não implementar automaticamente.

---

# 31. Regra final

> **O ViralCode não deve crescer por antecipação. Deve crescer por validação.**

A visão pode ser grande.

A implementação atual deve ser pequena.

Cada fase deve provar que vale a pena construir a próxima.

**Versão atual:** 0.1  
**Status:** Roadmap inicial do produto
