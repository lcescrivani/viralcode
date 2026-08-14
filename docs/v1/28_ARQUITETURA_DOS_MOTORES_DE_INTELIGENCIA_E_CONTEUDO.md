# 28 — ARQUITETURA DOS MOTORES DE INTELIGÊNCIA E CONTEÚDO

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define a arquitetura dos motores responsáveis por transformar dados coletados e analisados em conteúdo útil para o usuário.

O ViralCode deverá evoluir de:

```text
DADOS
   ↓
ANÁLISE
   ↓
PADRÕES
   ↓
INSIGHTS
   ↓
IDEIAS
   ↓
CONTEÚDO
   ↓
PUBLICAÇÃO
   ↓
RESULTADO
   ↓
APRENDIZADO
```

O objetivo é criar um ciclo contínuo de melhoria.

---

# 2. Princípio fundamental

A IA não deverá ser o produto inteiro.

Ela será um componente dentro de um sistema maior.

```text
ViralCode
├── dados
├── regras
├── contexto
├── análise
├── inteligência
├── criação
├── publicação
└── aprendizado
```

A IA deverá utilizar o contexto produzido pelo sistema.

---

# 3. Motores do ViralCode

A arquitetura alvo deverá possuir os seguintes motores:

```text
MOTOR DE DESCOBERTA
MOTOR DE ANÁLISE
MOTOR DE INSIGHTS
MOTOR DE CRIAÇÃO
MOTOR DE PLANEJAMENTO
MOTOR DE PUBLICAÇÃO
MOTOR DE DESEMPENHO
MOTOR DE APRENDIZADO
```

No MVP, alguns poderão ser implementados como módulos dentro do mesmo backend.

---

# 4. Motor de Descoberta

Responsabilidade:

```text
encontrar conteúdos relevantes
```

Entrada:

```text
nicho
perfil
tema
palavras-chave
critérios
```

Saída:

```text
conteúdos descobertos
```

---

# 5. Motor de Análise

Responsabilidade:

```text
entender o conteúdo descoberto
```

Poderá identificar:

```text
tema
subtema
hook
estrutura
formato
emoção
CTA
ângulo
linguagem
```

---

# 6. Motor de Insights

Responsabilidade:

transformar análises individuais em padrões.

Exemplo:

```text
Conteúdo A
Conteúdo B
Conteúdo C
Conteúdo D
        ↓
PADRÃO
```

---

# 7. Motor de Criação

Responsabilidade:

transformar:

```text
perfil
+
nicho
+
padrões
+
insights
+
aprendizados
```

em:

```text
ideias
hooks
roteiros
legendas
CTAs
```

---

# 8. Motor de Planejamento

Responsabilidade:

organizar conteúdos no tempo.

Entrada:

```text
conteúdos aprovados
objetivos
frequência
datas
```

Saída:

```text
calendário
```

---

# 9. Motor de Publicação

Responsabilidade:

```text
enviar conteúdo para a rede social
```

No MVP:

```text
Instagram
```

---

# 10. Motor de Desempenho

Responsabilidade:

coletar e organizar resultados.

Exemplo:

```text
visualizações
curtidas
comentários
compartilhamentos
salvamentos
```

Somente métricas efetivamente disponíveis deverão ser armazenadas.

---

# 11. Motor de Aprendizado

Responsabilidade:

transformar desempenho em conhecimento reutilizável.

Exemplo:

```text
conteúdos
   ↓
métricas
   ↓
comparação
   ↓
padrão
   ↓
aprendizado
```

---

# 12. Relação entre os motores

Fluxo principal:

```text
DESCUBERTA
    ↓
ANÁLISE
    ↓
INSIGHTS
    ↓
CRIAÇÃO
    ↓
PLANEJAMENTO
    ↓
PUBLICAÇÃO
    ↓
DESEMPENHO
    ↓
APRENDIZADO
    └───────────────┐
                    ↓
                 CRIAÇÃO
```

Isso cria o ciclo de aprendizado do ViralCode.

---

# 13. Motor não significa microserviço

Esta é uma decisão importante.

No MVP:

```text
1 Backend
```

contendo:

```text
módulos
```

e não:

```text
8 servidores independentes
```

---

# 14. Arquitetura interna

Exemplo:

```text
backend/app/servicos/

servico_descoberta.py
servico_analise.py
servico_insight.py
servico_criacao.py
servico_planejamento.py
servico_publicacao.py
servico_desempenho.py
servico_aprendizado.py
```

---

# 15. Motor de análise e IA

A análise poderá utilizar IA.

Mas o serviço deverá controlar:

```text
entrada
contexto
prompt
modelo
saída
validação
persistência
```

---

# 16. Fluxo de análise

```text
Conteúdo
   ↓
normalização
   ↓
montagem do contexto
   ↓
prompt
   ↓
provedor IA
   ↓
resposta
   ↓
validação
   ↓
análise estruturada
   ↓
MySQL
```

---

# 17. Não confiar cegamente na resposta da IA

A saída da IA deverá ser validada.

Exemplo:

```text
IA retorna JSON
   ↓
validar estrutura
   ↓
validar campos
   ↓
validar valores
   ↓
persistir
```

Se a resposta for inválida:

```text
erro controlado
```

---

# 18. Estrutura de saída

A IA deverá preferencialmente retornar dados estruturados.

Exemplo conceitual:

```json
{
  "tema": "relacionamento",
  "hook": "Você conversa com seu parceiro?",
  "emocao": "identificação",
  "estrutura": [
    "hook",
    "problema",
    "explicação",
    "solução",
    "cta"
  ]
}
```

A estrutura definitiva será definida pelos esquemas da aplicação.

---

# 19. Prompts

Prompts deverão ser tratados como ativos do sistema.

Não espalhar prompts grandes dentro de funções.

Preferir uma estrutura organizada.

Exemplo:

```text
prompts/
├── analise/
├── insights/
├── criacao/
└── aprendizado/
```

---

# 20. Versionamento de prompts

Um prompt importante deverá possuir versão.

Exemplo:

```text
analise_conteudo_v1
analise_conteudo_v2
```

Isso permitirá descobrir qual prompt produziu determinado resultado.

---

# 21. Registro de execução

Quando apropriado, o sistema deverá registrar:

```text
prompt
versão
modelo
entrada
saída
status
tempo
tokens
custo estimado
```

A política de retenção deverá considerar privacidade e custo.

---

# 22. Contexto

O motor de criação não deverá receber somente:

```text
"crie um reel"
```

Deverá receber contexto.

Exemplo:

```text
perfil
+
nicho
+
público
+
tom
+
padrões
+
insights
+
aprendizados
+
objetivo
```

---

# 23. Contexto mínimo do MVP

No MVP, o contexto poderá conter:

```text
nicho
tema
perfil
conteúdos analisados
padrões
tom de voz
objetivo
```

---

# 24. Motor de criação

O motor deverá separar etapas quando isso melhorar o resultado.

Exemplo:

```text
IDEIA
 ↓
HOOK
 ↓
ROTEIRO
 ↓
LEGENDA
 ↓
CTA
```

Não necessariamente uma única chamada de IA deverá fazer tudo.

---

# 25. Pipeline de criação

Arquitetura recomendada:

```text
Briefing
   ↓
Gerador de ideia
   ↓
Gerador de hook
   ↓
Gerador de roteiro
   ↓
Gerador de legenda
   ↓
Validação
   ↓
Conteúdo
```

No MVP, etapas poderão ser combinadas para reduzir custo e complexidade.

---

# 26. Regra de simplicidade

Não criar cinco chamadas de IA quando uma chamada estruturada produzir resultado suficientemente bom.

A arquitetura deverá permitir separar depois.

---

# 27. Criação baseada em padrões

Exemplo:

```text
PADRÃO ENCONTRADO:
pergunta provocativa
+
contraste
+
exemplo cotidiano
+
CTA
```

O motor deverá transformar o padrão em nova criação.

---

# 28. Não copiar

O sistema deverá evitar copiar literalmente conteúdos externos.

O objetivo é extrair:

```text
estrutura
ângulo
mecanismo
emoção
padrão
```

e produzir uma nova peça.

---

# 29. Originalidade

Originalidade não deverá significar:

```text
criar algo completamente desconectado do que funciona
```

Deverá significar:

```text
usar padrões comprovados
+
novo contexto
+
nova abordagem
+
novo conteúdo
```

---

# 30. Perfil como contexto

Cada perfil poderá possuir:

```text
nome
nicho
subnicho
público
posicionamento
tom de voz
objetivos
restrições
```

O motor deverá respeitar esse contexto.

---

# 31. Múltiplos perfis

A arquitetura deverá permitir:

```text
Usuário
 ├── Perfil A
 ├── Perfil B
 └── Perfil C
```

Cada perfil poderá possuir:

```text
nicho diferente
tom diferente
conta social diferente
```

---

# 32. Nichos

O sistema não deverá ser construído especificamente para:

```text
casamento
```

Casamento poderá ser o primeiro nicho utilizado na validação.

A arquitetura deverá trabalhar com:

```text
nicho
```

como dado.

---

# 33. Redes sociais

O motor de criação deverá produzir conteúdo em um modelo interno.

Depois o conteúdo poderá ser adaptado para:

```text
Instagram
TikTok
YouTube
outras redes
```

---

# 34. Modelo interno

Exemplo:

```text
Conteúdo ViralCode
├── ideia
├── hook
├── roteiro
├── legenda
├── CTA
└── mídia
```

Depois:

```text
Adaptador Instagram
Adaptador TikTok
Adaptador YouTube
```

---

# 35. Não criar múltiplas redes no MVP

O MVP utilizará:

```text
Instagram
```

A arquitetura deverá apenas evitar que o Instagram contamine todo o domínio.

---

# 36. Adaptação por rede

Futuramente:

```text
Conteúdo interno
      ↓
Adaptador da rede
      ↓
formato específico
```

---

# 37. Regras de conteúdo

Além da IA, o sistema poderá possuir regras determinísticas.

Exemplos:

```text
tamanho máximo
campos obrigatórios
CTA obrigatório
estrutura mínima
```

---

# 38. IA + regras

Arquitetura:

```text
IA
 ↓
resultado
 ↓
regras
 ↓
validação
 ↓
conteúdo final
```

A IA não deverá ter autoridade absoluta sobre o estado do sistema.

---

# 39. Segurança da IA

Não enviar para o provedor informações que não sejam necessárias.

Especialmente:

```text
senha
tokens
segredos
dados internos
```

---

# 40. Instruções do sistema

Os prompts deverão distinguir:

```text
instruções do sistema
contexto do usuário
dados do conteúdo
tarefa
```

---

# 41. Conteúdo externo como dado

Conteúdo coletado da rede social deverá ser tratado como:

```text
DADO
```

e não como instrução confiável para a IA.

Isso reduz o risco de instruções maliciosas presentes no conteúdo analisado.

---

# 42. Prompt injection

Conteúdos externos poderão conter textos como:

```text
"ignore todas as instruções"
```

O sistema deverá tratar esse texto como conteúdo a ser analisado, não como comando para o agente.

---

# 43. Separação de contexto

Preferir:

```text
INSTRUÇÕES
+
DADOS
+
TAREFA
```

em vez de misturar tudo em uma única instrução sem estrutura.

---

# 44. Validação de saída

A saída da IA deverá ser validada por:

```text
Pydantic / esquema equivalente
```

antes de entrar no domínio.

---

# 45. Falha de validação

Se a IA retornar:

```text
JSON inválido
campo ausente
tipo errado
valor inválido
```

o sistema deverá:

```text
registrar
rejeitar
tentar novamente quando apropriado
```

---

# 46. Tentativa de correção

Quando apropriado, poderá existir uma segunda chamada para corrigir formato.

Exemplo:

```text
IA
 ↓
JSON inválido
 ↓
solicitação de correção
 ↓
validação
```

Não criar tentativas infinitas.

---

# 47. Limite de tentativas

O número de tentativas deverá ser limitado.

Exemplo conceitual:

```text
máximo de 2 ou 3
```

O valor definitivo será definido na implementação.

---

# 48. Custo

Cada chamada de IA deverá ser tratada como recurso com custo.

O sistema deverá evitar:

```text
chamadas desnecessárias
contextos gigantes
reprocessamento infinito
```

---

# 49. Contexto excessivo

Não enviar todo o banco para a IA.

Selecionar somente o contexto relevante.

---

# 50. Seleção de evidências

Para criação, selecionar:

```text
melhores padrões
melhores exemplos
aprendizados relevantes
```

em vez de enviar centenas de conteúdos indiscriminadamente.

---

# 51. Ranking

O sistema poderá possuir um mecanismo de ranking para selecionar os conteúdos mais relevantes.

Exemplo:

```text
relevância
+
desempenho
+
similaridade
+
recência
```

---

# 52. Não confundir viralidade com relevância

Um conteúdo com muitas visualizações não necessariamente será relevante para qualquer perfil.

A seleção deverá considerar:

```text
nicho
perfil
objetivo
formato
tema
```

---

# 53. Insight

Um insight deverá ser uma conclusão derivada de dados.

Exemplo:

```text
"Perguntas diretas apresentam maior taxa de comentários neste perfil."
```

Não registrar como insight sem evidência suficiente.

---

# 54. Aprendizado

Um aprendizado deverá ser diferente de um insight momentâneo.

Exemplo:

```text
Insight:
3 conteúdos tiveram alto desempenho usando perguntas.

Aprendizado:
perguntas diretas são uma estratégia promissora para este perfil.
```

---

# 55. Confiança

Insights e aprendizados deverão possuir algum indicador de confiança quando possível.

Exemplo:

```text
baixa
média
alta
```

ou um valor quantitativo.

---

# 56. Evidências

Todo aprendizado relevante deverá apontar para as evidências que o sustentam.

Exemplo:

```text
aprendizado
   ↓
publicação 10
publicação 18
publicação 27
```

---

# 57. Feedback do usuário

O usuário poderá futuramente indicar:

```text
gostei
não gostei
aprovar
rejeitar
editar
```

Esses sinais poderão alimentar o aprendizado.

---

# 58. Feedback como dado

Não considerar apenas métricas da rede.

Também considerar:

```text
feedback humano
```

---

# 59. Human in the loop

No MVP:

```text
IA
 ↓
USUÁRIO
 ↓
aprovação
```

O usuário continua sendo o responsável pela decisão final.

---

# 60. Autonomia futura

Somente depois de dados suficientes poderão existir níveis maiores de automação:

```text
assistido
semi-automático
automático
```

---

# 61. Motor de aprendizado futuro

Poderá futuramente utilizar:

```text
estatística
modelos preditivos
machine learning
IA
```

No MVP:

```text
regras
+
estatística simples
+
IA
```

são suficientes.

---

# 62. Não construir ML prematuramente

Não criar modelos próprios antes de possuir:

```text
volume de dados
qualidade de dados
problema claramente definido
```

---

# 63. Arquitetura de alto nível

```text
                    DADOS
                      │
                      ▼
                DESCOBERTA
                      │
                      ▼
                    ANÁLISE
                      │
                      ▼
                   INSIGHTS
                      │
                      ▼
                   CRIAÇÃO
                      │
                      ▼
                 PLANEJAMENTO
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
                      └──────────► CRIAÇÃO
```

---

# 64. Camada de IA

```text
Serviço de negócio
       ↓
ProvedorIA
       ↓
Modelo de IA
```

O serviço de negócio não deverá conhecer detalhes específicos do fornecedor.

---

# 65. Estrutura de código

Exemplo:

```text
backend/app/
│
├── servicos/
│   ├── servico_analise.py
│   ├── servico_insight.py
│   ├── servico_criacao.py
│   └── servico_aprendizado.py
│
├── provedores_ia/
│   ├── base/
│   │   └── provedor_ia.py
│   └── fabrica.py
│
└── prompts/
    ├── analise/
    ├── insights/
    ├── criacao/
    └── aprendizado/
```

---

# 66. Responsabilidade do Serviço

O serviço deverá controlar:

```text
regra
contexto
orquestração
validação
persistência
```

---

# 67. Responsabilidade do Provedor

O provedor deverá controlar:

```text
autenticação com fornecedor
formato específico
requisição
resposta
erro técnico
```

---

# 68. Responsabilidade do Prompt

O prompt deverá controlar:

```text
instrução
formato esperado
papel
tarefa
restrições
```

---

# 69. Responsabilidade do Banco

O banco deverá armazenar:

```text
dados
resultados
histórico
evidências
execuções
```

---

# 70. Fluxo completo de criação

```text
Perfil
   ↓
Nicho
   ↓
Objetivo
   ↓
Padrões
   ↓
Insights
   ↓
Aprendizados
   ↓
Contexto
   ↓
Prompt
   ↓
IA
   ↓
Validação
   ↓
Conteúdo
   ↓
Aprovação
```

---

# 71. Fluxo de melhoria

```text
Conteúdo criado
      ↓
Publicação
      ↓
Métricas
      ↓
Análise de desempenho
      ↓
Insight
      ↓
Aprendizado
      ↓
Próxima criação
```

---

# 72. Regra de ciclo

O valor do ViralCode estará menos em:

```text
gerar uma postagem
```

e mais em:

```text
aprender com cada postagem
```

---

# 73. MVP

No MVP, priorizar:

```text
análise
+
criação
+
aprendizado básico
```

---

# 74. P0

Obrigatório:

```text
Motor de análise
Motor de criação
Provedor de IA
Validação da saída
Contexto por perfil
```

---

# 75. P1

Depois:

```text
Motor de insights
Motor de aprendizado
ranking
feedback do usuário
```

---

# 76. P2

Futuramente:

```text
predição
machine learning
automação autônoma
otimização automática
adaptação multi-rede
```

---

# 77. Critério de sucesso

O motor de inteligência será considerado útil quando:

```text
conteúdos reais
   ↓
gerarem dados
   ↓
dados produzirem insights
   ↓
insights melhorarem novas criações
```

---

# 78. Regra para agentes de IA

Antes de modificar um motor:

1. identificar qual motor está sendo alterado;
2. preservar suas responsabilidades;
3. não mover lógica para outro módulo sem justificativa;
4. validar entrada e saída da IA;
5. proteger dados sensíveis;
6. testar falhas;
7. registrar execução quando necessário;
8. atualizar documentação.

---

# 79. Regra final

> **O ViralCode não deverá apenas gerar conteúdo. Deverá aprender quais padrões funcionam para cada perfil e utilizar esse aprendizado para melhorar a próxima criação.**

O ciclo estratégico é:

```text
OBSERVAR
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
MELHORAR
```

Esse ciclo será um dos principais diferenciais arquiteturais do ViralCode.

**Versão:** 1.0  
**Status:** Documento oficial da Arquitetura dos Motores de Inteligência e Conteúdo
