# 16 — MOTOR DE PLANEJAMENTO

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

O Motor de Planejamento será responsável por transformar estratégia, aprendizados e objetivos em um plano editorial executável.

Ele responderá:

> **O que devemos criar, para qual perfil, em qual formato, com qual objetivo e quando devemos publicar?**

O fluxo será:

```text
INTELIGÊNCIA
   ↓
APRENDIZADOS
   ↓
ESTRATÉGIA
   ↓
PLANEJAMENTO
   ↓
MOTOR DE CRIAÇÃO
   ↓
CONTEÚDO
   ↓
PUBLICAÇÃO
```

---

# 2. Princípio fundamental

O Motor de Planejamento não deverá criar o conteúdo.

Ele deverá definir a necessidade de conteúdo.

```text
Planejamento
→ decide o que precisa ser criado

Criação
→ cria

Publicação
→ publica
```

---

# 3. Responsabilidades

O Motor de Planejamento será responsável por:

- organizar o calendário editorial;
- definir prioridades;
- distribuir temas;
- definir formatos;
- definir objetivos;
- utilizar aprendizados;
- evitar repetição excessiva;
- criar oportunidades de teste;
- preparar demandas para o Motor de Criação;
- controlar o estado do planejamento.

---

# 4. O que não pertence ao Motor de Planejamento

Não deverá ser responsabilidade dele:

```text
gerar roteiro
gerar legenda
editar vídeo
publicar
coletar métricas
interpretar dados
```

Essas funções pertencem a outros componentes.

---

# 5. Relação com o Motor de Aprendizado

O planejamento deverá utilizar os aprendizados disponíveis.

```text
Motor de Aprendizado
        ↓
Aprendizados
        ↓
Motor de Planejamento
        ↓
Plano editorial
```

Exemplo:

```text
Aprendizado:
storytelling apresenta bom desempenho neste perfil.

Planejamento:
incluir novos testes de storytelling.
```

---

# 6. Relação com o Motor de Inteligência

O Motor de Inteligência identifica:

```text
padrões
insights
oportunidades
```

O Motor de Planejamento transforma essas informações em ações editoriais.

```text
Inteligência
   ↓
"O tema X apresenta oportunidade."
   ↓
Planejamento
   ↓
"Adicionar 3 conteúdos sobre X."
```

---

# 7. Perfil

Todo planejamento deverá estar associado a um perfil.

Exemplo:

```text
Perfil
├── nome
├── nicho
├── público
├── posicionamento
├── objetivos
├── frequência
└── regras editoriais
```

---

# 8. Nicho

O planejamento deverá considerar o nicho do perfil.

Exemplo:

```text
Nicho:
Casamento

Temas:
- diálogo
- intimidade
- conflitos
- confiança
- reconexão
```

O sistema deverá permitir outros nichos sem alteração estrutural do motor.

---

# 9. Objetivos

Cada item planejado deverá possuir um objetivo.

Exemplos:

```text
ALCANCE
IDENTIFICACAO
EDUCACAO
AUTORIDADE
ENGAJAMENTO
RELACIONAMENTO
CONVERSAO
```

---

# 10. Distribuição de objetivos

Um calendário não deverá ser formado somente por um tipo de conteúdo.

Exemplo:

```text
40% alcance
25% identificação
20% educação
10% autoridade
5% conversão
```

Os percentuais são exemplos conceituais.

No MVP, a distribuição poderá ser definida manualmente pelo usuário.

---

# 11. Temas

O planejamento deverá trabalhar com:

```text
tema
subtema
ângulo
```

Exemplo:

```text
Tema:
Diálogo

Subtema:
Silêncio emocional

Ângulo:
"Quando o casal para de conversar"
```

---

# 12. Pilares editoriais

O perfil poderá possuir pilares.

Exemplo:

```text
Pilar 1:
Relacionamento

Pilar 2:
Comunicação

Pilar 3:
Intimidade

Pilar 4:
Espiritualidade
```

Os pilares ajudam a organizar o conteúdo.

---

# 13. Equilíbrio editorial

O planejamento deverá evitar concentração excessiva em um único tema.

Exemplo:

```text
Segunda → diálogo
Terça → intimidade
Quarta → conflitos
Quinta → história
Sexta → esperança
```

O objetivo é manter variedade sem perder posicionamento.

---

# 14. Frequência

O perfil poderá possuir uma frequência desejada.

Exemplo:

```text
3 conteúdos por semana
```

ou:

```text
1 conteúdo por dia
```

A frequência deverá ser uma configuração do perfil.

---

# 15. Calendário

O calendário poderá representar:

```text
data
horário
perfil
plataforma
tema
formato
objetivo
status
```

Modelo conceitual:

```text
ItemCalendario
├── id
├── perfil_id
├── plataforma
├── data
├── horario
├── tema
├── formato
├── objetivo
├── prioridade
└── status
```

---

# 16. Status do planejamento

Exemplo:

```text
IDEIA
PLANEJADO
EM_CRIACAO
CRIADO
APROVADO
AGENDADO
PUBLICADO
CANCELADO
```

---

# 17. Prioridade

Cada item poderá possuir:

```text
ALTA
MEDIA
BAIXA
```

Exemplo:

```text
Tema estratégico:
ALTA

Teste experimental:
MEDIA

Conteúdo complementar:
BAIXA
```

---

# 18. Prioridade baseada em aprendizado

Futuramente o sistema poderá calcular prioridade com base em:

```text
relevância
desempenho histórico
objetivo
oportunidade
necessidade editorial
```

No MVP, prioridade manual é suficiente.

---

# 19. Conteúdo planejado

Um item de planejamento não é necessariamente um conteúdo pronto.

Exemplo:

```text
Planejamento:

Tema:
Falta de diálogo

Formato:
Reel

Objetivo:
Identificação
```

Depois:

```text
Motor de Criação
        ↓
Roteiro
        ↓
Conteúdo
```

---

# 20. Briefing de criação

O planejamento poderá gerar um briefing.

Exemplo:

```text
BRIEFING

Nicho:
Casamento

Tema:
Falta de diálogo

Objetivo:
Identificação

Formato:
Reel

Tom:
Direto e acolhedor

Padrão recomendado:
Pergunta no hook

CTA:
Compartilhamento
```

Esse briefing será uma entrada para o Motor de Criação.

---

# 21. Planejamento e padrões

O planejamento poderá utilizar padrões identificados pelo Motor de Inteligência.

Exemplo:

```text
Padrão:
hook em pergunta

Planejamento:
criar 3 conteúdos utilizando esse padrão
em temas diferentes.
```

---

# 22. Planejamento e testes

O calendário deverá reservar espaço para experimentação.

Exemplo:

```text
70% formatos já conhecidos
30% testes
```

Os percentuais são apenas exemplos.

O usuário poderá definir a estratégia.

---

# 23. Hipóteses

O planejamento poderá transformar uma hipótese em teste.

Exemplo:

```text
Hipótese:
perguntas específicas geram maior identificação.

Planejamento:
criar 3 Reels com perguntas específicas.
```

Depois:

```text
Publicação
   ↓
Desempenho
   ↓
Aprendizado
```

---

# 24. Não repetir automaticamente o que funcionou

Se um conteúdo performar bem, o sistema não deverá simplesmente duplicá-lo.

Preferir:

```text
conteúdo que funcionou
        ↓
padrão
        ↓
novos ângulos
        ↓
novos conteúdos
```

---

# 25. Conteúdo evergreen

O planejamento poderá identificar conteúdos que não dependem de uma data específica.

Exemplo:

```text
Como melhorar o diálogo no casamento.
```

Esses conteúdos poderão ser reutilizados ou atualizados futuramente.

---

# 26. Conteúdo temporal

Alguns conteúdos dependem de:

```text
data
evento
tendência
momento
```

O planejamento deverá registrar essa característica.

Exemplo:

```text
Tema:
Dia dos Namorados

Data:
12/06
```

---

# 27. Tendências

O Motor de Planejamento poderá futuramente receber oportunidades identificadas pelo Motor de Inteligência.

```text
Tendência detectada
       ↓
Avaliação
       ↓
Planejamento
       ↓
Criação
```

Não implementar monitoramento automático de tendências no MVP.

---

# 28. Calendário por plataforma

O mesmo perfil poderá possuir calendários diferentes.

Exemplo:

```text
Instagram
→ Reel

TikTok
→ vídeo adaptado

YouTube
→ Shorts
```

---

# 29. Conteúdo multiplataforma

Um planejamento poderá representar:

```text
Ideia central
      ↓
Adaptação Instagram
      ↓
Adaptação TikTok
      ↓
Adaptação YouTube
```

Cada publicação continuará sendo controlada pelo Motor de Publicação.

---

# 30. Horário

O planejamento poderá possuir horário sugerido.

Exemplo:

```text
19:00
```

No MVP, o horário poderá ser definido manualmente.

O sistema não deverá assumir que existe um "horário mágico" universal.

---

# 31. Horário baseado em dados

Futuramente o sistema poderá analisar:

```text
horários de publicação
+
desempenho
```

e sugerir horários.

Exemplo:

```text
Para este perfil:
terça-feira às 19h
apresentou desempenho acima da mediana.
```

Isso deverá ser tratado como recomendação, não garantia.

---

# 32. Calendário mensal

Futuramente o usuário poderá visualizar:

```text
AGOSTO

01 — Reel
03 — Carrossel
05 — Reel
07 — Post
...
```

---

# 33. Calendário semanal

Também poderá existir:

```text
SEG
TER
QUA
QUI
SEX
SAB
DOM
```

com os conteúdos planejados.

---

# 34. Planejamento por campanha

Futuramente:

```text
Campanha
├── objetivo
├── período
├── público
├── temas
├── conteúdos
└── métricas
```

Uma campanha poderá possuir vários itens do calendário.

---

# 35. Planejamento por série

Também poderá existir:

```text
Série:
"21 dias de reconexão"

Dia 1
Dia 2
Dia 3
...
Dia 21
```

Isso permite criar sequências editoriais.

---

# 36. Dependências

Alguns conteúdos poderão depender de outros.

Exemplo:

```text
Parte 1
   ↓
Parte 2
   ↓
Parte 3
```

O planejamento deverá futuramente permitir relações entre itens.

---

# 37. Conteúdo urgente

Um item poderá possuir:

```text
URGENTE
```

para oportunidades temporais.

Exemplo:

```text
assunto em alta
evento
notícia
tendência
```

---

# 38. Conteúdo atrasado

Se um item não for produzido no prazo:

```text
PLANEJADO
   ↓
ATRASADO
```

O usuário poderá:

```text
reagendar
cancelar
priorizar
```

---

# 39. Replanejamento

O calendário deverá ser editável.

Exemplo:

```text
Conteúdo A
20/08
   ↓
reagendar
   ↓
22/08
```

O histórico da alteração poderá ser registrado futuramente.

---

# 40. Planejamento versus execução

O planejamento representa intenção.

A publicação representa execução.

Exemplo:

```text
Planejado:
20/08 às 19h

Real:
20/08 às 19h07
```

Os dois dados são diferentes.

---

# 41. Relação com publicação

Fluxo:

```text
Planejamento
   ↓
Criação
   ↓
Aprovação
   ↓
Publicação
```

O Motor de Planejamento não deverá publicar diretamente.

---

# 42. Relação com desempenho

Depois da publicação:

```text
Planejamento
   ↓
Publicação
   ↓
Desempenho
```

Isso permitirá avaliar:

```text
planejado
versus
executado
versus
resultado
```

---

# 43. Planejado versus realizado

Exemplo:

```text
Planejado:
5 Reels

Realizado:
4 Reels

Publicados:
4

Cancelados:
1
```

Esses indicadores poderão ser usados para medir execução editorial.

---

# 44. Planejamento e aprendizado

O Motor de Aprendizado poderá informar:

```text
Tema X:
bom desempenho

Tema Y:
baixo desempenho
```

O planejamento poderá ajustar a distribuição futura.

---

# 45. Não automatizar toda a estratégia no MVP

No MVP:

```text
Usuário
   ↓
define estratégia
   ↓
Motor de Planejamento
   ↓
organiza calendário
```

A automação estratégica completa poderá vir depois.

---

# 46. Banco de ideias

O Motor de Planejamento poderá utilizar uma fila de ideias.

Estados:

```text
NOVA
AVALIADA
PLANEJADA
CRIADA
DESCARTADA
```

---

# 47. Origem da ideia

Uma ideia poderá vir de:

```text
Usuário
Motor de Inteligência
Motor de Aprendizado
Análise de conteúdos
Planejamento manual
```

A origem deverá ser registrada.

---

# 48. Score de oportunidade futuro

Uma ideia poderá futuramente receber:

```text
score_oportunidade
```

considerando:

```text
relevância
demanda
desempenho histórico
timing
aderência ao perfil
```

Não implementar no MVP.

---

# 49. Geração automática de calendário futura

Futuramente:

```text
Perfil
+
Objetivo
+
Frequência
+
Aprendizados
+
Pilares
        ↓
Motor de Planejamento
        ↓
Calendário sugerido
```

No MVP, o calendário poderá ser criado pelo usuário.

---

# 50. MVP

O MVP deverá implementar:

```text
Perfil
   ↓
Temas
   ↓
Itens de calendário
   ↓
Data
   ↓
Formato
   ↓
Objetivo
   ↓
Status
```

Opcionalmente:

```text
briefing
prioridade
```

---

# 51. O que NÃO fazer no MVP

Não implementar inicialmente:

```text
planejamento totalmente automático
otimização automática de calendário
previsão de melhor horário
campanhas complexas
séries complexas
dependências avançadas
tendências automáticas
multiplataforma completa
```

---

# 52. Primeiro caso de uso

Exemplo:

```text
Usuário cria perfil
        ↓
Define frequência
        ↓
Define pilares
        ↓
Adiciona temas
        ↓
Cria calendário
        ↓
Gera briefing
        ↓
Motor de Criação
```

---

# 53. Critério de sucesso

O Motor de Planejamento será considerado funcional quando o usuário conseguir:

> **transformar sua estratégia editorial em uma lista organizada de conteúdos que precisam ser criados, com tema, formato, objetivo, prioridade e data.**

---

# 54. API futura

Endpoints conceituais:

```text
GET /planejamento
POST /planejamento
GET /planejamento/{id}
PUT /planejamento/{id}
DELETE /planejamento/{id}

GET /calendario
POST /calendario
PUT /calendario/{id}
```

Os nomes definitivos deverão seguir o padrão oficial da API do projeto.

---

# 55. Serviço

Exemplo:

```python
class ServicoPlanejamento:
    def criar_item(self, dados):
        ...
```

---

# 56. Repositório

Exemplo:

```python
class RepositorioPlanejamento:
    def salvar(self, item):
        ...

    def listar_por_periodo(self, inicio, fim):
        ...
```

---

# 57. Separação de responsabilidades

```text
FastAPI
   ↓
ServicoPlanejamento
   ↓
RepositorioPlanejamento
   ↓
SQLAlchemy
   ↓
MySQL
```

Para criação:

```text
Planejamento
   ↓
Motor de Criação
```

---

# 58. Testes

Devem existir testes para:

```text
criar item
editar item
cancelar item
reagendar
alterar status
listar calendário
filtrar por perfil
filtrar por período
duplicidade
```

---

# 59. Segurança

O planejamento deverá respeitar a separação por:

```text
usuário
organização
perfil
```

Um usuário não deverá acessar o planejamento de outro perfil sem autorização.

---

# 60. Auditoria futura

Poderá registrar:

```text
quem criou
quem alterou
quando alterou
o que mudou
```

---

# 61. Arquitetura do Motor de Planejamento

```text
             MOTOR DE INTELIGÊNCIA
                      │
                      ▼
               MOTOR DE APRENDIZADO
                      │
                      ▼
                 PLANEJAMENTO
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
        TEMAS      OBJETIVOS    FORMATOS
          │           │           │
          └───────────┼───────────┘
                      ▼
                 CALENDÁRIO
                      │
                      ▼
              BRIEFING DE CRIAÇÃO
                      │
                      ▼
              MOTOR DE CRIAÇÃO
```

---

# 62. Arquitetura-alvo completa

```text
                         REDE SOCIAL
                              │
                              ▼
                           CONECTOR
                              │
                              ▼
                         DESCOBERTA
                              │
                              ▼
                         BANCO DE DADOS
                              │
                              ▼
                    MOTOR DE INTELIGÊNCIA
                              │
                              ▼
                       MOTOR DE APRENDIZADO
                              │
                              ▼
                      MOTOR DE PLANEJAMENTO
                              │
                              ▼
                       MOTOR DE CRIAÇÃO
                              │
                              ▼
                           APROVAÇÃO
                              │
                              ▼
                    MOTOR DE PUBLICAÇÃO
                              │
                              ▼
                         REDE SOCIAL
                              │
                              ▼
                    MOTOR DE DESEMPENHO
                              │
                              ▼
                    MOTOR DE APRENDIZADO
```

---

# 63. Regra final

> **O Motor de Planejamento transforma estratégia e conhecimento em uma agenda editorial organizada, sem assumir para si as responsabilidades de criação, publicação ou análise.**

A separação deverá permanecer:

```text
INTELIGÊNCIA
→ entende oportunidades

APRENDIZADO
→ registra o que foi aprendido

PLANEJAMENTO
→ decide o que precisa ser feito

CRIAÇÃO
→ produz

APROVAÇÃO
→ valida

PUBLICAÇÃO
→ executa

DESEMPENHO
→ mede
```

Esse desenho permite começar manualmente no MVP e automatizar gradualmente o planejamento conforme o ViralCode acumular dados suficientes.

**Versão:** 1.0  
**Status:** Documento oficial do Motor de Planejamento
