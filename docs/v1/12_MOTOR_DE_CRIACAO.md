# 12 — MOTOR DE CRIAÇÃO

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

O Motor de Criação será responsável por transformar o conhecimento produzido pelo Motor de Inteligência em novos conteúdos originais.

O fluxo principal será:

```text
DADOS
  ↓
MOTOR DE INTELIGÊNCIA
  ↓
PADRÕES
  ↓
INSIGHTS
  ↓
MOTOR DE CRIAÇÃO
  ↓
CONTEÚDO
```

O Motor de Criação não deverá simplesmente copiar conteúdos analisados.

Seu objetivo será:

> **Utilizar padrões de desempenho como referência para criar conteúdos originais, adequados ao nicho, perfil, público e objetivo definidos pelo usuário.**

---

# 2. Princípio fundamental

O ViralCode deverá separar:

```text
APRENDER
```

de:

```text
COPIAR
```

O Motor de Inteligência identifica padrões.

O Motor de Criação utiliza esses padrões para gerar novas possibilidades.

Exemplo:

```text
Conteúdo viral
      ↓
Identificação do padrão:
"pergunta sobre uma dor específica"
      ↓
Motor de Criação
      ↓
Novo conteúdo original
```

---

# 3. Relação com o Motor de Inteligência

O Motor de Criação dependerá dos resultados estruturados do Motor de Inteligência.

```text
Motor de Inteligência
        ↓
Viral DNA
        ↓
Padrões
        ↓
Insights
        ↓
Motor de Criação
```

O Motor de Criação não deverá precisar acessar diretamente os conteúdos externos para descobrir os padrões.

---

# 4. Entrada do Motor de Criação

Uma solicitação de criação poderá possuir:

```text
nicho
subnicho
perfil
plataforma
objetivo
público
tema
subtema
tom
formato
duração
padrões
insights
restrições
CTA
```

Exemplo conceitual:

```json
{
  "nicho": "casamento",
  "tema": "dialogo",
  "objetivo": "alcance",
  "formato": "reel",
  "duracao_segundos": 30,
  "tom": "direto",
  "cta": "compartilhar"
}
```

---

# 5. Perfil

O conteúdo deverá ser criado para um perfil específico.

Exemplo:

```text
Perfil
├── nome
├── nicho
├── público
├── posicionamento
├── tom_de_voz
├── objetivos
└── regras_editoriais
```

O mesmo padrão poderá gerar conteúdos diferentes para perfis diferentes.

---

# 6. Nicho

O Motor de Criação deverá ser independente de nicho.

Não criar:

```text
MotorCriacaoCasamento
```

ou:

```text
MotorCriacaoFitness
```

O correto será:

```text
MotorCriacao
```

alimentado por:

```text
nicho
tema
público
perfil
objetivo
padrões
```

---

# 7. Tema

Todo conteúdo deverá possuir um tema.

Exemplo:

```text
Nicho:
Casamento

Tema:
Diálogo

Subtema:
Silêncio emocional
```

O tema poderá vir:

- do usuário;
- de uma estratégia editorial;
- do Motor de Inteligência;
- de uma oportunidade identificada no banco.

---

# 8. Objetivo do conteúdo

O Motor de Criação deverá saber por que aquele conteúdo está sendo criado.

Objetivos possíveis:

```text
Alcance
Identificação
Educação
Autoridade
Engajamento
Relacionamento
Conversão
```

Um mesmo tema poderá gerar conteúdos diferentes dependendo do objetivo.

---

# 9. Formatos

O MVP deverá priorizar formatos simples.

Exemplos:

```text
Reel
Post
Carrossel
```

A arquitetura deverá permitir novos formatos posteriormente.

---

# 10. Reel

O Reel deverá possuir uma estrutura própria.

Exemplo:

```text
Hook
 ↓
Desenvolvimento
 ↓
Conclusão
 ↓
CTA
```

Uma estrutura mais elaborada poderá ser:

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

A estrutura deverá ser configurável.

---

# 11. Hook

O Motor de Criação deverá gerar hooks coerentes com o padrão identificado.

Exemplo:

```text
Padrão identificado:
pergunta relacionada a uma dor específica
```

Possível criação:

```text
"Você sente que seu marido está perto,
mas emocionalmente está cada vez mais longe?"
```

O resultado deve ser original.

---

# 12. Desenvolvimento

Depois do hook, o conteúdo deverá desenvolver a ideia.

O desenvolvimento deverá:

- manter coerência;
- aprofundar a promessa;
- evitar repetição;
- respeitar o tempo do formato;
- utilizar linguagem do perfil;
- conduzir naturalmente à conclusão.

---

# 13. Conclusão

A conclusão deverá entregar algum tipo de valor.

Pode ser:

```text
explicação
insight
orientação
mudança de perspectiva
passo prático
```

Não criar conteúdo que apenas provoque curiosidade sem entregar valor.

---

# 14. CTA

O CTA deverá estar relacionado ao objetivo.

Exemplo:

```text
Objetivo:
Engajamento

CTA:
"Você já viveu isso? Comente."
```

Outro:

```text
Objetivo:
Compartilhamento

CTA:
"Envie para alguém que precisa ouvir isso."
```

---

# 15. Tom de voz

Cada perfil poderá possuir seu próprio tom.

Exemplo:

```text
direto
acolhedor
provocativo
educacional
inspirador
bem-humorado
bíblico
técnico
```

O Motor de Criação deverá respeitar a configuração do perfil.

---

# 16. Identidade editorial

O conteúdo deverá respeitar:

```text
posicionamento
valores
linguagem
vocabulário
promessas
restrições
```

Isso será importante para que o ViralCode não produza conteúdos genéricos.

---

# 17. Regras editoriais

Um perfil poderá possuir regras.

Exemplo:

```text
Evitar:
- linguagem agressiva
- promessas absolutas
- determinados termos

Preferir:
- linguagem simples
- frases curtas
- exemplos cotidianos
```

As regras deverão ser consideradas pelo Motor de Criação.

---

# 18. Conteúdo original

A saída deverá ser uma nova criação.

O sistema poderá utilizar:

```text
tema
estrutura
emoção
padrão
ângulo
formato
CTA
```

Mas não deverá simplesmente reproduzir:

```text
texto
roteiro
legenda
frases
sequência
```

de um conteúdo externo.

---

# 19. Referências

O conteúdo poderá registrar quais padrões e insights influenciaram sua criação.

Exemplo:

```text
Conteúdo criado
      ↓
Padrão utilizado
      ↓
Insight utilizado
```

Isso permitirá medir posteriormente quais aprendizados geraram melhores resultados.

---

# 20. Rastreabilidade

Cada conteúdo gerado deverá futuramente possuir referência para:

```text
perfil
estratégia
tema
padrões
insights
modelo de IA
versão do prompt
data de criação
```

---

# 21. Estrutura do conteúdo

O modelo interno poderá possuir:

```text
ConteudoGerado
├── id
├── perfil_id
├── plataforma
├── formato
├── tema
├── subtema
├── objetivo
├── hook
├── roteiro
├── legenda
├── cta
├── hashtags
├── status
├── data_criacao
└── referencia_analise
```

---

# 22. Status do conteúdo

Exemplo:

```text
RASCUNHO
GERADO
EM_REVISAO
APROVADO
REJEITADO
AGENDADO
PUBLICADO
ARQUIVADO
```

No MVP, poderá ser suficiente:

```text
RASCUNHO
APROVADO
PUBLICADO
```

---

# 23. Geração de múltiplas opções

O Motor poderá gerar mais de uma alternativa.

Exemplo:

```text
Tema:
falta de diálogo

Opção A:
Hook provocativo

Opção B:
Hook em pergunta

Opção C:
Storytelling

Opção D:
Contraste
```

O usuário poderá escolher a melhor.

---

# 24. Variações

Uma mesma ideia poderá gerar variações.

Exemplo:

```text
Ideia central
   ├── Reel A
   ├── Reel B
   └── Reel C
```

As variações poderão alterar:

```text
hook
ângulo
emoção
estrutura
CTA
```

sem alterar necessariamente o tema principal.

---

# 25. Testes A/B futuros

A arquitetura deverá permitir futuramente:

```text
Conteúdo A
versus
Conteúdo B
```

com variação controlada de:

```text
hook
CTA
estrutura
ângulo
```

O desempenho poderá alimentar o Motor de Inteligência.

---

# 26. IA

O Motor de Criação poderá utilizar modelos de IA.

Arquitetura:

```text
Motor de Criação
       ↓
Abstração de IA
       ↓
Provedor de IA
       ↓
Modelo
```

O Motor de Criação não deverá ficar acoplado a um único fornecedor.

---

# 27. Provedor de IA

Deverá existir uma abstração.

Exemplo:

```python
class ProvedorInteligenciaArtificial:
    def gerar_conteudo(self, contexto):
        ...
```

Implementação futura:

```python
class ProvedorOpenAI(ProvedorInteligenciaArtificial):
    ...
```

Outros provedores poderão ser adicionados posteriormente.

---

# 28. Prompts

Prompts importantes deverão ser tratados como componentes versionados.

Exemplo:

```text
prompts/
├── gerar_reel_v1
├── gerar_post_v1
├── gerar_carrossel_v1
└── revisar_conteudo_v1
```

Não espalhar prompts críticos dentro das rotas da API.

---

# 29. Prompt e contexto

O prompt deverá receber contexto estruturado.

Exemplo:

```text
Perfil
+
Nicho
+
Tema
+
Objetivo
+
Tom
+
Padrões
+
Restrições
+
Formato
```

Isso é preferível a enviar apenas:

```text
"Crie um Reel sobre casamento."
```

---

# 30. Revisão automática

Futuramente o Motor poderá possuir uma etapa de revisão.

```text
Geração
   ↓
Revisão
   ↓
Aprovação
```

A revisão poderá verificar:

```text
clareza
coerência
estrutura
tom
CTA
duplicidade
regras editoriais
```

---

# 31. Segurança da geração

Conteúdo gerado por IA deverá ser considerado não confiável até passar pelas validações necessárias.

A IA não deverá possuir automaticamente autorização para:

```text
publicar
excluir
alterar configurações
```

---

# 32. Conteúdo sensível

O sistema deverá possuir mecanismos futuros para identificar conteúdos que possam exigir revisão humana.

Exemplos:

```text
afirmações médicas
questões jurídicas
promessas financeiras
alegações sensíveis
conteúdo potencialmente enganoso
```

O objetivo é evitar publicação automática de conteúdos inadequados.

---

# 33. Human in the loop

No MVP, a aprovação humana deverá ser priorizada.

Fluxo:

```text
Motor de Criação
      ↓
Conteúdo
      ↓
Usuário revisa
      ↓
Aprova
      ↓
Publicação futura
```

---

# 34. Custo

Cada geração poderá consumir recursos de IA.

O sistema deverá futuramente registrar:

```text
modelo
tokens
tempo
custo_estimado
```

No MVP, a prioridade é manter a implementação simples.

---

# 35. Limite de geração

O sistema deverá evitar geração ilimitada.

Poderá existir futuramente:

```text
limite por usuário
limite por perfil
limite por organização
limite por plano
```

---

# 36. Conteúdo baseado em padrões

O Motor de Criação poderá receber:

```json
{
  "padroes": [
    "hook em pergunta",
    "dor específica",
    "história curta"
  ],
  "emocao": "identificacao",
  "estrutura": [
    "hook",
    "dor",
    "historia",
    "esperanca",
    "cta"
  ]
}
```

O resultado deverá ser uma nova composição.

---

# 37. Não prometer viralização

O ViralCode não deverá afirmar:

```text
"Este conteúdo vai viralizar."
```

O correto será:

```text
"Este conteúdo utiliza padrões
observados em conteúdos de alto desempenho."
```

Padrões aumentam a capacidade de testar hipóteses.

Não garantem resultado.

---

# 38. Conteúdo e desempenho

Depois da publicação:

```text
Conteúdo criado
      ↓
Publicação
      ↓
Métricas
      ↓
Motor de Inteligência
```

O desempenho deverá voltar para o ciclo de aprendizado.

---

# 39. Ciclo completo

A arquitetura-alvo será:

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

---

# 40. Inteligência por perfil

O Motor de Criação deverá futuramente considerar o que funciona especificamente para cada perfil.

Exemplo:

```text
Nicho:
Casamento

Padrão geral:
pergunta provocativa

Perfil:
Leonardo

Aprendizado próprio:
storytelling performa melhor
```

Nesse caso, a criação poderá priorizar o aprendizado específico do perfil.

---

# 41. Inteligência por nicho

A criação poderá combinar:

```text
Padrões gerais do nicho
+
Padrões específicos do perfil
```

Isso permitirá personalização progressiva.

---

# 42. Calendário de conteúdo futuro

O Motor de Criação poderá futuramente receber uma programação:

```text
Segunda
→ Reel educativo

Terça
→ Post de identificação

Quarta
→ Reel provocativo
```

O calendário será responsabilidade de uma camada própria.

---

# 43. Motor de Criação não é calendário

Separar:

```text
Motor de Criação
→ cria

Motor de Planejamento
→ decide quando criar/publicar
```

Isso evita acoplamento.

---

# 44. Motor de Criação não publica

O Motor de Criação produz o conteúdo.

O Motor de Publicação será responsável por:

```text
agendamento
autorização
envio
publicação
confirmação
```

---

# 45. Integração com o Motor de Publicação

Fluxo:

```text
Motor de Criação
      ↓
Conteúdo aprovado
      ↓
Motor de Publicação
      ↓
Conector da Rede Social
      ↓
Instagram
```

---

# 46. Integração com múltiplas redes

O mesmo conteúdo conceitual poderá possuir adaptações.

Exemplo:

```text
Ideia central
     │
     ├── Instagram Reel
     ├── TikTok
     └── YouTube Shorts
```

Cada adaptação poderá possuir:

```text
formato
duração
CTA
legenda
estrutura
```

específicos.

---

# 47. Conteúdo multiplataforma

Não assumir que um conteúdo deve ser publicado exatamente igual em todas as redes.

O Motor de Criação poderá gerar:

```text
Conteúdo base
      ↓
Adaptação por plataforma
```

---

# 48. Banco de ideias

Futuramente poderá existir:

```text
Ideia
├── tema
├── origem
├── padrão
├── status
├── prioridade
└── oportunidades
```

Uma ideia poderá gerar vários conteúdos.

---

# 49. Reaproveitamento

Uma ideia poderá ser transformada em:

```text
Reel
Post
Carrossel
Story
```

Isso deverá ser feito sem simplesmente duplicar o mesmo conteúdo.

---

# 50. Geração por lote

Futuramente:

```text
Tema
   ↓
10 ideias
   ↓
10 roteiros
   ↓
10 legendas
```

No MVP, a geração individual é suficiente.

---

# 51. Qualidade

Uma criação deverá ser avaliada em critérios como:

```text
clareza
relevância
originalidade
aderência ao perfil
aderência ao tema
estrutura
CTA
```

---

# 52. Score futuro

Futuramente poderá existir:

```text
score_conteudo
```

calculado antes da publicação.

Exemplo conceitual:

```text
Hook              90
Relevância        95
Clareza           88
Aderência         92
CTA               85
```

Esse score não deverá ser tratado como previsão garantida de desempenho.

---

# 53. Detecção de duplicidade

Antes de salvar uma nova criação, o sistema poderá verificar conteúdos muito semelhantes já existentes.

Objetivo:

```text
evitar repetição
```

Essa funcionalidade poderá evoluir posteriormente para comparação semântica.

---

# 54. Banco vetorial futuro

Embeddings e banco vetorial poderão ser considerados no futuro para:

- encontrar ideias semelhantes;
- evitar duplicidade;
- recuperar conteúdos relacionados;
- recuperar aprendizados;
- gerar conteúdo baseado em contexto.

Não são necessários no MVP.

---

# 55. MVP

O MVP do Motor de Criação deverá fazer somente:

```text
Receber contexto
      ↓
Receber padrões
      ↓
Gerar conteúdo
      ↓
Salvar rascunho
      ↓
Mostrar ao usuário
```

---

# 56. O que NÃO fazer no MVP

Não implementar inicialmente:

```text
geração multimodal avançada
voz sintética
avatar
edição automática de vídeo
machine learning próprio
embeddings
banco vetorial
agentes autônomos
publicação automática
A/B automático
```

Essas capacidades poderão ser adicionadas depois da validação do negócio.

---

# 57. Primeiro caso de uso

O primeiro caso de uso recomendado:

```text
Usuário escolhe:
Nicho
Tema
Objetivo
Formato
```

O sistema:

```text
busca padrões existentes
       ↓
monta contexto
       ↓
gera 3 opções
       ↓
usuário escolhe
       ↓
salva como rascunho
```

---

# 58. Critério de sucesso

O Motor de Criação será considerado útil quando conseguir:

> **reduzir significativamente o tempo necessário para transformar uma oportunidade identificada pelo Motor de Inteligência em um conteúdo pronto para revisão.**

---

# 59. Regra para agentes de IA

Antes de modificar o Motor de Criação:

1. ler este documento;
2. ler o documento do Motor de Inteligência;
3. verificar os modelos existentes;
4. respeitar o perfil e o nicho;
5. não copiar conteúdos externos;
6. versionar prompts importantes;
7. não acoplar a um único provedor de IA;
8. validar a saída;
9. manter aprovação humana no MVP;
10. atualizar a documentação quando a arquitetura mudar.

---

# 60. Arquitetura do Motor de Criação

```text
                  MOTOR DE INTELIGÊNCIA
                           │
                           ▼
                    PADRÕES / INSIGHTS
                           │
                           ▼
                    MOTOR DE CRIAÇÃO
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
       CONTEXTO          PROMPT           REGRAS
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                    PROVEDOR DE IA
                           │
                           ▼
                       CONTEÚDO
                           │
                           ▼
                       VALIDAÇÃO
                           │
                           ▼
                       RASCUNHO
                           │
                           ▼
                 APROVAÇÃO DO USUÁRIO
                           │
                           ▼
                  MOTOR DE PUBLICAÇÃO
```

---

# 61. Arquitetura-alvo do ViralCode

```text
REDE SOCIAL
     ↓
CONECTOR
     ↓
DESCOBERTA
     ↓
BANCO DE DADOS
     ↓
MOTOR DE INTELIGÊNCIA
     ↓
PADRÕES / INSIGHTS
     ↓
MOTOR DE CRIAÇÃO
     ↓
CONTEÚDO
     ↓
APROVAÇÃO
     ↓
MOTOR DE PUBLICAÇÃO
     ↓
REDE SOCIAL
     ↓
MÉTRICAS
     ↓
MOTOR DE INTELIGÊNCIA
```

Esse ciclo cria a base para o aprendizado contínuo do ViralCode.

---

# 62. Regra final

> **O Motor de Criação não existe para copiar o que viralizou. Ele existe para transformar inteligência em novas hipóteses de conteúdo original.**

A arquitetura deve preservar o ciclo:

```text
DESCOBRIR
   ↓
ANALISAR
   ↓
APRENDER
   ↓
CRIAR
   ↓
PUBLICAR
   ↓
MEDIR
   ↓
APRENDER NOVAMENTE
```

**Versão:** 1.0  
**Status:** Documento oficial do Motor de Criação do ViralCode
