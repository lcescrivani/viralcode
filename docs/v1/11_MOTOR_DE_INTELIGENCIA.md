# 11 — MOTOR DE INTELIGÊNCIA

**Versão:** 0.1  
**Status:** Documento inicial  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

O Motor de Inteligência será o componente responsável por transformar dados brutos de conteúdos sociais em conhecimento estruturado.

A função do motor não é simplesmente "descrever um Reel".

A função é descobrir:

> **Por que determinados conteúdos funcionam e quais padrões podem ser reutilizados pelo ViralCode.**

Fluxo conceitual:

```text
CONTEÚDOS
   ↓
COLETA DE DADOS
   ↓
ANÁLISE
   ↓
CLASSIFICAÇÃO
   ↓
PADRÕES
   ↓
VIRAL DNA
   ↓
INSIGHTS
```

---

# 2. O problema que o motor resolve

O ViralCode não deverá se limitar a mostrar:

```text
Reel A → 2 milhões de visualizações
Reel B → 1,5 milhão
Reel C → 1,2 milhão
```

Isso é apenas descoberta.

O valor estratégico começa quando conseguimos identificar:

```text
O que esses conteúdos têm em comum?
```

Exemplo:

```text
Hook forte
+
Dor específica
+
Identificação emocional
+
História curta
+
Quebra de expectativa
+
CTA
```

---

# 3. Objetivo do MVP

O MVP do Motor de Inteligência deverá ser simples.

Primeiro objetivo:

> **Conseguir analisar conteúdos que já foram coletados e transformar suas características em dados estruturados.**

Não precisamos começar com uma inteligência sofisticada.

---

# 4. Princípio fundamental

> **Primeiro coletar dados confiáveis. Depois inferir padrões.**

O motor não deve inventar conclusões com base em poucos conteúdos.

---

# 5. Hierarquia da inteligência

A arquitetura conceitual será:

```text
DADO
 ↓
INFORMAÇÃO
 ↓
ANÁLISE
 ↓
PADRÃO
 ↓
INSIGHT
 ↓
RECOMENDAÇÃO
```

### Dado

Exemplo:

```text
1.800.000 visualizações
```

### Informação

```text
Conteúdo sobre conflito no casamento.
```

### Análise

```text
Começa com uma pergunta provocativa.
```

### Padrão

```text
Perguntas provocativas aparecem em grande parte dos conteúdos de alto desempenho.
```

### Insight

```text
Perguntas podem aumentar identificação inicial.
```

### Recomendação

```text
Testar hooks em formato de pergunta para o perfil.
```

---

# 6. Evidência versus inferência

O motor deverá diferenciar:

## Evidência

Algo observado diretamente.

Exemplo:

```text
O vídeo começa com uma pergunta.
```

## Inferência

Conclusão derivada de dados.

Exemplo:

```text
Perguntas parecem ser frequentes entre conteúdos de alto desempenho.
```

## Hipótese

Explicação ainda não comprovada.

Exemplo:

```text
A pergunta pode ter contribuído para a retenção.
```

Essa separação é obrigatória.

---

# 7. Não confundir correlação com causalidade

Se conteúdos com perguntas possuem muitas visualizações, isso não prova que:

> "Perguntas causam viralização."

Pode haver outros fatores:

- autor;
- audiência;
- assunto;
- distribuição;
- timing;
- qualidade;
- contexto;
- histórico do perfil.

O motor deverá utilizar linguagem cuidadosa.

---

# 8. Entrada do motor

O motor poderá receber:

```text
Conteúdo
Autor
Legenda
Métricas
Data
Plataforma
Tipo
Mídia
Transcrição futura
```

Nem todos os dados estarão disponíveis no MVP.

---

# 9. Dados mínimos

Para uma primeira análise:

```text
conteúdo
+
legenda quando disponível
+
métricas
+
autor
+
data
+
plataforma
```

---

# 10. Análise multimodal futura

O motor poderá evoluir para analisar:

```text
Texto
Áudio
Vídeo
Imagem
Transcrição
Métricas
Comentários
```

Arquitetura:

```text
Conteúdo
   │
   ├── Texto
   ├── Áudio
   ├── Vídeo
   └── Métricas
        ↓
   Motor de Inteligência
```

---

# 11. Camadas de análise

O motor deverá ser dividido conceitualmente.

```text
Análise de Conteúdo
│
├── Classificação
├── Estrutura
├── Linguagem
├── Emoção
├── Hook
├── CTA
├── Tema
├── Público
└── Métricas
```

---

# 12. Classificação

O conteúdo poderá ser classificado por:

- nicho;
- tema;
- subtema;
- formato;
- objetivo;
- emoção;
- estágio do funil;
- tipo de hook.

Exemplo:

```text
Nicho:
Casamento

Tema:
Conflitos

Subtema:
Falta de diálogo

Formato:
Reel

Objetivo:
Identificação
```

---

# 13. Hook

O hook representa o elemento inicial responsável por chamar atenção.

Exemplos de categorias:

```text
Pergunta
Afirmação
Contradição
Promessa
Alerta
Curiosidade
História
Número
Provocação
Confissão
```

O motor deverá classificar o hook.

---

# 14. Hook textual

Quando houver transcrição ou legenda suficiente, o motor poderá identificar o hook textual.

Exemplo:

```text
"Se vocês brigam sempre pela mesma coisa, presta atenção."
```

Classificação:

```text
tipo_hook = alerta + identificação
```

---

# 15. Hook visual

Futuramente, o motor poderá analisar:

- enquadramento;
- movimento;
- texto na tela;
- expressão;
- mudança de cena;
- elemento visual inicial.

Essa análise dependerá da disponibilidade de vídeo/imagem.

---

# 16. Estrutura do conteúdo

O motor deverá identificar estruturas recorrentes.

Exemplo:

```text
Hook
 ↓
Dor
 ↓
História
 ↓
Explicação
 ↓
Esperança
 ↓
CTA
```

Outro:

```text
Pergunta
 ↓
Resposta
 ↓
Exemplo
 ↓
CTA
```

---

# 17. Dor

Identificar qual problema o conteúdo aborda.

Exemplo:

```text
"Meu marido não conversa comigo."
```

Classificação:

```text
dor = falta de diálogo
```

---

# 18. Desejo

Identificar o resultado desejado.

Exemplo:

```text
"Quero voltar a sentir conexão com meu marido."
```

Classificação:

```text
desejo = reconexão emocional
```

---

# 19. Emoção

O motor poderá classificar emoções predominantes.

Exemplos:

```text
medo
raiva
tristeza
esperança
curiosidade
identificação
surpresa
amor
desejo
alívio
```

A classificação deverá ser interpretativa e marcada como análise.

---

# 20. Linguagem

O motor poderá identificar características linguísticas:

```text
frases curtas
perguntas
imperativos
histórias
metáforas
números
listas
contrastes
afirmações fortes
```

---

# 21. CTA

Identificar chamada para ação.

Exemplos:

```text
Comente
Compartilhe
Salve
Siga
Envie para alguém
Veja a parte 2
Acesse o link
```

---

# 22. Tema

O motor poderá classificar o tema principal.

Exemplo:

```text
Nicho:
Casamento

Tema:
Diálogo

Subtema:
Silêncio emocional
```

---

# 23. Público

O motor poderá inferir o público-alvo.

Exemplo:

```text
Casais
Mulheres casadas
Homens casados
Casais em crise
```

A classificação deverá ser tratada como inferência, não como fato absoluto.

---

# 24. Objetivo do conteúdo

Possíveis classificações:

```text
Alcance
Identificação
Educação
Autoridade
Engajamento
Relacionamento
Conversão
```

---

# 25. Formato

Exemplos:

```text
Reel falando para a câmera
Storytelling
Lista
Tutorial
Entrevista
Corte
Cena dramatizada
Texto na tela
Antes/depois
Resposta a comentário
```

---

# 26. Métricas de desempenho

O motor deverá considerar as métricas disponíveis.

Exemplo:

```text
visualizações
curtidas
comentários
compartilhamentos
salvamentos
```

No futuro poderá calcular indicadores derivados.

---

# 27. Indicadores derivados

Exemplo:

```text
taxa_curtidas =
curtidas / visualizações
```

Outros:

```text
taxa_comentarios
taxa_compartilhamentos
taxa_salvamentos
```

Esses valores são cálculos, não dados originais da plataforma.

---

# 28. Velocidade de crescimento

Quando houver histórico:

```text
visualizações no tempo
```

poderemos calcular:

```text
visualizações por hora
```

Exemplo:

```text
10h → 100 mil
14h → 300 mil

crescimento = 200 mil em 4 horas
```

---

# 29. Aceleração

Futuramente:

```text
velocidade 1
        ↓
velocidade 2
        ↓
aceleração
```

Isso poderá ajudar a identificar conteúdos que estão ganhando tração rapidamente.

Não faz parte da primeira versão.

---

# 30. Conteúdos de referência

O motor poderá trabalhar com conjuntos de conteúdos.

Exemplo:

```text
100 Reels
```

em vez de analisar apenas um.

Isso permite encontrar padrões.

---

# 31. Comparação entre grupos

Exemplo:

```text
Grupo A
Conteúdos > 1 milhão de visualizações

versus

Grupo B
Conteúdos < 100 mil visualizações
```

O motor poderá procurar diferenças.

Essa será uma das funcionalidades mais importantes para o futuro.

---

# 32. Padrões

Um padrão deverá representar uma característica recorrente.

Exemplo:

```text
Padrão:
Hook em pergunta.

Ocorrência:
62% dos conteúdos analisados.
```

---

# 33. Padrão forte

Um padrão poderá ser considerado mais relevante quando:

- aparecer muitas vezes;
- aparecer em conteúdos de alto desempenho;
- tiver baixa ocorrência em conteúdos de baixo desempenho;
- existir quantidade suficiente de dados.

---

# 34. Padrão fraco

Se aparecer poucas vezes:

```text
2 de 10 conteúdos
```

não devemos afirmar:

> "Esse é um padrão viral."

Devemos tratar como:

```text
observação preliminar
```

---

# 35. Confiança

As análises poderão possuir nível de confiança.

Exemplo:

```text
confianca = alta
confianca = media
confianca = baixa
```

Ou um valor numérico futuramente.

---

# 36. Evidências do padrão

Um padrão deverá apontar para os conteúdos que o sustentam.

Exemplo:

```text
Padrão:
Pergunta nos primeiros segundos

Evidências:
Conteúdo 12
Conteúdo 17
Conteúdo 28
Conteúdo 43
```

Isso melhora a auditabilidade.

---

# 37. Viral DNA

O Viral DNA será uma representação estruturada das características de um conteúdo.

Exemplo:

```text
VIRAL DNA
│
├── Hook
├── Dor
├── Desejo
├── Emoção
├── Estrutura
├── Tema
├── Formato
├── CTA
└── Público
```

---

# 38. Viral DNA não é fórmula mágica

O sistema não deverá afirmar:

> "Faça exatamente isso e viralize."

O objetivo é:

> identificar características recorrentes que podem inspirar novos testes.

---

# 39. Insight

Um insight combina:

```text
dados
+
análise
+
padrão
```

Exemplo:

```text
Dos 50 conteúdos de maior desempenho,
34 começam com uma pergunta diretamente relacionada
a uma dor do público.
```

Insight:

```text
Hooks que começam com uma pergunta sobre uma dor específica
são frequentes entre os conteúdos analisados.
```

---

# 40. Recomendação

Uma recomendação deverá nascer de evidências.

Exemplo:

```text
Insight:
Perguntas sobre dores específicas aparecem com frequência.

Recomendação:
Testar hooks em formato de pergunta
em novos conteúdos do perfil.
```

---

# 41. Motor de inteligência não cria conteúdo

Essa separação é importante.

O Motor de Inteligência:

```text
ANALISA
```

O Motor de Criação:

```text
CRIA
```

Arquitetura:

```text
Conteúdos
   ↓
Motor de Inteligência
   ↓
Conhecimento
   ↓
Motor de Criação
```

---

# 42. Saída do motor

Uma análise poderá produzir algo conceitualmente semelhante a:

```json
{
  "conteudo_id": 123,
  "tema": "casamento",
  "subtema": "falta de dialogo",
  "hook": {
    "tipo": "pergunta",
    "texto": "Vocês brigam sempre pela mesma coisa?"
  },
  "emocao": "identificacao",
  "estrutura": [
    "hook",
    "dor",
    "explicacao",
    "esperanca",
    "cta"
  ],
  "cta": "compartilhe",
  "confianca": "media"
}
```

Esse formato é conceitual e poderá evoluir.

---

# 43. Armazenamento da análise

A análise deverá ser persistida quando houver benefício.

Possível entidade futura:

```text
analises_conteudo
```

Ela poderá guardar:

```text
conteudo_id
versao_modelo
resultado
confianca
data_analise
```

---

# 44. Versionamento da inteligência

Modelos e prompts poderão evoluir.

Por isso, uma análise deverá futuramente registrar:

```text
versao_modelo
```

Exemplo:

```text
modelo = "analise_conteudo"
versao = "1.2"
```

Isso permite comparar resultados de versões diferentes.

---

# 45. Reprocessamento

Se o modelo de análise melhorar:

```text
Análise v1
   ↓
Modelo melhor
   ↓
Análise v2
```

O sistema deverá poder reprocessar conteúdos.

Não sobrescrever histórico sem controle.

---

# 46. IA como componente substituível

O motor não deverá depender de um único fornecedor de IA.

Arquitetura:

```text
Motor de Inteligência
        ↓
Provedor de IA
        ↓
Modelo
```

Futuramente poderá haver:

```text
Provedor A
Provedor B
Provedor C
```

---

# 47. Prompt como componente versionado

Prompts importantes deverão ser tratados como artefatos versionados.

Exemplo:

```text
prompts/
├── analise_hook_v1
├── analise_hook_v2
├── analise_estrutura_v1
└── classificacao_tema_v1
```

A estrutura definitiva será definida posteriormente.

---

# 48. Não colocar prompts críticos espalhados

Evitar prompts importantes diretamente dentro de rotas.

Errado:

```text
FastAPI
  ↓
string gigante de prompt
```

Correto:

```text
Serviço de Inteligência
  ↓
Prompt versionado
  ↓
Provedor de IA
```

---

# 49. Custo de IA

Cada análise poderá gerar custo.

O sistema deverá futuramente permitir medir:

```text
conteúdos analisados
tokens utilizados
tempo
custo estimado
```

Não é obrigatório no primeiro MVP.

---

# 50. Estratégia de custo

No início:

> **Analisar somente conteúdos selecionados.**

Não enviar milhares de conteúdos para IA sem necessidade.

Exemplo:

```text
1000 conteúdos encontrados
        ↓
Filtro
        ↓
100 melhores
        ↓
Análise
```

Isso reduz custo e ruído.

---

# 51. Lote de análise

Futuramente, análises poderão ser realizadas em lote.

```text
100 conteúdos
   ↓
Fila
   ↓
Análise
   ↓
Resultados
```

Não implementar fila obrigatoriamente no MVP.

---

# 52. Análise incremental

Se um conteúdo já foi analisado e não mudou, não necessariamente precisa ser analisado novamente.

Poderemos utilizar:

```text
hash do conteúdo
+
versão da análise
```

para identificar necessidade de reprocessamento.

---

# 53. Comentários

No futuro, comentários poderão ser uma fonte extremamente valiosa.

Exemplo:

```text
Conteúdo viral
   ↓
Comentários
   ↓
Dores reais
   ↓
Linguagem do público
   ↓
Novas ideias
```

Essa funcionalidade será posterior.

---

# 54. Comentários como evidência

Comentários poderão ajudar a identificar:

- perguntas;
- objeções;
- desejos;
- linguagem;
- dores;
- temas emergentes.

Mas deverão ser tratados conforme disponibilidade, permissões e políticas da plataforma.

---

# 55. Aprendizado com conteúdo próprio

Quando o Motor de Publicação estiver funcionando:

```text
Conteúdo criado
   ↓
Publicado
   ↓
Desempenho
   ↓
Análise
   ↓
Aprendizado
```

O Motor de Inteligência poderá comparar:

```text
o que funcionou nos outros
```

com:

```text
o que funcionou no próprio perfil.
```

---

# 56. Inteligência por perfil

No futuro, cada perfil poderá possuir um conjunto próprio de aprendizados.

Exemplo:

```text
Perfil Leonardo
│
├── Hooks
├── Temas
├── Formatos
├── Emoções
└── CTAs
```

---

# 57. Inteligência por nicho

Também poderemos ter:

```text
Nicho: Casamento
```

com padrões gerais.

Depois:

```text
Perfil: Leonardo
```

com padrões específicos.

Isso permite separar:

```text
Padrão geral do mercado
```

de:

```text
Padrão específico do perfil.
```

---

# 58. Hierarquia futura de conhecimento

```text
PLATAFORMA
    ↓
NICHO
    ↓
SUBNICHO
    ↓
PERFIL
    ↓
CONTEÚDO
    ↓
DESEMPENHO
```

Isso poderá permitir recomendações cada vez mais específicas.

---

# 59. Motor de inteligência e nichos

O motor deverá ser genérico.

Não criar um motor:

```text
MotorCasamento
```

e outro:

```text
MotorFitness
```

O correto será:

```text
MotorInteligencia
```

alimentado por:

```text
nicho
tema
perfil
plataforma
dados
```

---

# 60. Configuração por nicho

No futuro, regras específicas poderão ser configuráveis.

Exemplo:

```text
Nicho:
Casamento

Categorias relevantes:
- diálogo
- intimidade
- confiança
- conflitos
```

Outro:

```text
Nicho:
Fitness

Categorias relevantes:
- treino
- alimentação
- composição corporal
```

O motor continua sendo o mesmo.

---

# 61. Dados insuficientes

Se não houver dados suficientes, o motor deverá dizer:

```text
dados insuficientes
```

e não fabricar um padrão.

---

# 62. Resultado inconclusivo

Exemplo:

```text
Foram analisados 8 conteúdos.

Conclusão:
não há evidência suficiente para identificar um padrão confiável.
```

Isso é um resultado válido.

---

# 63. Qualidade da análise

A qualidade deverá considerar:

```text
quantidade de dados
+
qualidade dos dados
+
consistência
+
confiança da classificação
```

---

# 64. Auditoria

Cada insight importante deverá poder responder:

```text
De onde veio essa conclusão?
```

Exemplo:

```text
Insight
 ↓
Padrão
 ↓
Conteúdos utilizados
 ↓
Métricas
 ↓
Dados originais
```

---

# 65. Evitar "IA diz"

O sistema não deverá apresentar conclusões como autoridade absoluta.

Evitar:

> "A IA descobriu a fórmula viral."

Preferir:

> "Entre os conteúdos analisados, observamos este padrão."

---

# 66. Saída para o usuário

A interface futura poderá mostrar:

```text
🔥 PADRÃO ENCONTRADO

73% dos Reels analisados começam
com uma afirmação forte ou pergunta.

Exemplos:
• Conteúdo A
• Conteúdo B
• Conteúdo C
```

---

# 67. Saída para o Motor de Criação

O Motor de Criação poderá receber algo como:

```json
{
  "nicho": "casamento",
  "tema": "dialogo",
  "padroes": [
    "pergunta sobre dor",
    "historia curta",
    "cta para compartilhar"
  ],
  "emocao": "identificacao"
}
```

O Motor de Criação então produzirá conteúdo original.

---

# 68. Regra contra cópia

O Motor de Inteligência deverá identificar padrões.

O Motor de Criação deverá produzir conteúdo original.

Não devemos transformar:

```text
conteúdo viral
```

em:

```text
cópia do conteúdo viral
```

A finalidade é:

> **aprender a estrutura, não copiar a peça.**

---

# 69. Conteúdo protegido

A análise deverá respeitar as regras aplicáveis à utilização dos conteúdos externos.

O sistema não deverá transformar a coleta em mecanismo de reprodução indevida de material de terceiros.

---

# 70. MVP do Motor de Inteligência

A primeira versão poderá fazer:

```text
Receber conteúdo
     ↓
Classificar tema
     ↓
Classificar hook
     ↓
Classificar emoção
     ↓
Identificar estrutura
     ↓
Identificar CTA
     ↓
Salvar análise
```

---

# 71. O que NÃO fazer no MVP

Não implementar inicialmente:

```text
análise visual avançada
análise de áudio avançada
análise de comentários em massa
machine learning próprio
embeddings
banco vetorial
agentes autônomos
aprendizado automático complexo
```

Tudo isso poderá vir depois.

---

# 72. Primeira versão prática

O primeiro objetivo pode ser:

```text
Top 100 Reels
     ↓
IA analisa
     ↓
estrutura padronizada
     ↓
dashboard
```

O usuário deverá conseguir responder:

> "O que esses Reels têm em comum?"

---

# 73. Métrica de sucesso do motor

O primeiro sucesso não será:

```text
IA sofisticada
```

Será:

> **O usuário olhar para os resultados e descobrir algo que não conseguiria perceber facilmente sozinho.**

---

# 74. Evolução

### Fase 1

```text
Classificação
```

### Fase 2

```text
Padrões
```

### Fase 3

```text
Viral DNA
```

### Fase 4

```text
Comparação entre grupos
```

### Fase 5

```text
Recomendações
```

### Fase 6

```text
Aprendizado com conteúdo próprio
```

---

# 75. Arquitetura do motor

```text
                    CONTEÚDOS
                        │
                        ▼
                 PRÉ-PROCESSAMENTO
                        │
                        ▼
                 MOTOR DE ANÁLISE
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       TEXTO         MÉTRICAS       MÍDIA
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                  CLASSIFICAÇÃO
                        │
                        ▼
                     PADRÕES
                        │
                        ▼
                   VIRAL DNA
                        │
                        ▼
                    INSIGHTS
                        │
                        ▼
                 MOTOR DE CRIAÇÃO
```

---

# 76. Regra para agentes de inteligência artificial

Antes de implementar uma nova análise:

1. verificar se ela já existe;
2. definir o que é dado e o que é inferência;
3. evitar conclusões sem evidência;
4. registrar confiança;
5. versionar prompts/modelos quando necessário;
6. não acoplar o motor a um fornecedor de IA;
7. manter o motor independente do nicho;
8. criar testes;
9. evitar custo desnecessário;
10. atualizar a documentação.

---

# 77. Regra de simplicidade

O Motor de Inteligência não precisa nascer "inteligente".

Ele precisa nascer:

```text
CONSISTENTE
AUDITÁVEL
TESTÁVEL
ÚTIL
```

A inteligência poderá evoluir com os dados.

---

# 78. Regra final

> **O Motor de Inteligência transforma conteúdos em conhecimento estruturado para que o ViralCode possa aprender o que funciona antes de tentar criar o que funciona.**

O ciclo futuro será:

```text
DESCOBRIR
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
CRIAR MELHOR
```

**Versão atual:** 0.1  
**Status:** Motor de Inteligência inicial do ViralCode
