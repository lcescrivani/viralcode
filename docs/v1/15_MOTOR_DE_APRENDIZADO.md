# 15 — MOTOR DE APRENDIZADO

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

O Motor de Aprendizado será responsável por transformar os resultados observados nos conteúdos publicados em conhecimento reutilizável pelo ViralCode.

Ele representa a etapa que fecha o ciclo:

```text
DESCOBRIR
   ↓
ANALISAR
   ↓
CRIAR
   ↓
PUBLICAR
   ↓
MEDIR
   ↓
APRENDER
   ↓
CRIAR NOVAMENTE
```

O objetivo não é criar um modelo de inteligência artificial próprio no MVP.

O objetivo inicial é:

> **registrar o que funcionou, o que não funcionou e em quais contextos, para melhorar as próximas decisões do ViralCode.**

---

# 2. Princípio fundamental

O Motor de Aprendizado não deverá transformar automaticamente qualquer resultado em uma regra.

Exemplo:

```text
Um Reel teve 2 milhões de visualizações.
```

Isso não significa automaticamente:

```text
"O formato desse Reel sempre funciona."
```

O aprendizado deverá considerar:

```text
dados
+
contexto
+
quantidade de exemplos
+
comparações
+
consistência
```

---

# 3. Relação com os outros motores

O Motor de Aprendizado recebe informações principalmente do Motor de Desempenho e do Motor de Inteligência.

```text
Motor de Desempenho
        ↓
Resultados reais
        ↓
Motor de Inteligência
        ↓
Análises
        ↓
Motor de Aprendizado
        ↓
Conhecimento
        ↓
Motor de Criação
```

---

# 4. Aprendizado não é machine learning

No MVP, aprendizado significa:

```text
registrar
comparar
classificar
acumular evidências
atualizar conhecimento
```

Não significa necessariamente:

```text
treinar rede neural
```

ou:

```text
criar algoritmo próprio de machine learning
```

Essas possibilidades poderão ser consideradas no futuro.

---

# 5. O que o motor aprende

O sistema poderá aprender relações entre:

```text
nicho
tema
subtema
formato
hook
estrutura
emoção
CTA
público
perfil
plataforma
horário
data
desempenho
```

Exemplo:

```text
Perfil X
+
Tema Y
+
Hook Z
+
Reel
=
desempenho acima da média
```

Isso é uma observação de contexto, não uma garantia.

---

# 6. Níveis de conhecimento

O ViralCode poderá trabalhar com diferentes níveis.

```text
OBSERVAÇÃO
   ↓
PADRÃO
   ↓
INSIGHT
   ↓
HIPÓTESE
   ↓
APRENDIZADO
   ↓
RECOMENDAÇÃO
```

---

# 7. Observação

É um fato registrado.

Exemplo:

```text
O conteúdo recebeu 800 mil visualizações.
```

---

# 8. Padrão

É uma característica recorrente.

Exemplo:

```text
7 de 10 conteúdos de alto desempenho
utilizaram perguntas no hook.
```

---

# 9. Insight

É uma interpretação baseada em dados.

Exemplo:

```text
Perguntas aparecem com frequência
nos conteúdos de alto desempenho analisados.
```

---

# 10. Hipótese

É uma explicação que ainda precisa ser testada.

Exemplo:

```text
Perguntas podem aumentar a identificação inicial.
```

---

# 11. Aprendizado

Um aprendizado deverá surgir quando existir evidência suficiente para orientar uma decisão futura.

Exemplo:

```text
Para este perfil, Reels com storytelling
sobre conflitos de relacionamento apresentaram
desempenho acima da mediana em múltiplas publicações.
```

---

# 12. Recomendação

A recomendação transforma aprendizado em ação.

Exemplo:

```text
Priorizar testes de storytelling
sobre conflitos de relacionamento.
```

---

# 13. Evidência

Todo aprendizado importante deverá possuir evidências.

Exemplo:

```text
Aprendizado:
Storytelling performa acima da mediana.

Evidências:
Conteúdo A
Conteúdo B
Conteúdo C
Conteúdo D
```

Isso permite auditoria.

---

# 14. Confiança

Cada aprendizado poderá possuir:

```text
BAIXA
MEDIA
ALTA
```

A confiança deverá depender de fatores como:

```text
quantidade de conteúdos
consistência dos resultados
qualidade dos dados
comparação com grupos
tempo
```

---

# 15. Amostra

Um aprendizado deverá registrar o tamanho da amostra.

Exemplo:

```text
amostra = 4
```

Uma amostra pequena deverá reduzir a confiança.

---

# 16. Regra contra conclusões precipitadas

Não transformar:

```text
1 conteúdo
```

em:

```text
regra editorial
```

Exemplo incorreto:

> "Esse hook viraliza."

Exemplo correto:

> "Esse hook apresentou bom desempenho neste conteúdo."

---

# 17. Comparação

Sempre que possível, comparar:

```text
grupo que utilizou o padrão
```

com:

```text
grupo de referência
```

Exemplo:

```text
Com pergunta:
mediana = 600k

Sem pergunta:
mediana = 280k
```

Isso fornece uma evidência melhor do que observar um único conteúdo.

---

# 18. Controle de contexto

O mesmo padrão pode funcionar em um contexto e não funcionar em outro.

Exemplo:

```text
Nicho:
Casamento

Perfil A:
bom desempenho

Perfil B:
baixo desempenho
```

Por isso, o aprendizado deverá registrar o contexto.

---

# 19. Aprendizado por nicho

Exemplo:

```text
Nicho:
Casamento

Aprendizado:
conteúdos sobre conflitos apresentam alto interesse.
```

---

# 20. Aprendizado por perfil

Exemplo:

```text
Perfil:
Perfil A

Aprendizado:
conteúdos com histórias pessoais
performam acima da média.
```

---

# 21. Aprendizado por plataforma

Um padrão poderá funcionar no:

```text
Instagram
```

e apresentar comportamento diferente em:

```text
TikTok
```

Portanto, a plataforma deverá fazer parte do contexto quando relevante.

---

# 22. Aprendizado temporal

O desempenho poderá mudar com o tempo.

Exemplo:

```text
2026:
formato A performa bem

futuro:
formato A perde desempenho
```

O sistema deverá permitir que aprendizados sejam atualizados.

---

# 23. Aprendizado não é permanente

Um aprendizado poderá possuir:

```text
ATIVO
EM_VALIDACAO
SUPERADO
ARQUIVADO
```

Isso evita tratar uma conclusão antiga como verdade permanente.

---

# 24. Validade

Um aprendizado poderá possuir:

```text
criado_em
atualizado_em
ultima_evidencia_em
```

Futuramente poderá existir:

```text
validade
```

ou mecanismo de revisão.

---

# 25. Conhecimento geral versus específico

O sistema deverá separar:

```text
Conhecimento do nicho
```

de:

```text
Conhecimento do perfil
```

Exemplo:

```text
Nicho:
perguntas são frequentes em conteúdos de alto desempenho.

Perfil:
storytelling apresenta desempenho superior neste perfil.
```

---

# 26. Hierarquia do conhecimento

```text
PLATAFORMA
    ↓
NICHO
    ↓
SUBNICHO
    ↓
PERFIL
    ↓
TEMA
    ↓
CONTEÚDO
```

Quanto mais específico o conhecimento, maior a necessidade de evidência própria.

---

# 27. Conhecimento global

Futuramente poderá existir conhecimento agregado de vários perfis.

Exemplo:

```text
Instagram
   ↓
Casamento
   ↓
Padrões gerais
```

Esse conhecimento deverá ser separado do conhecimento privado de cada perfil.

---

# 28. Privacidade

O aprendizado de um perfil não deverá ser compartilhado automaticamente com outro perfil.

Exemplo:

```text
Perfil A
   ↓
aprendizado privado
```

não deverá automaticamente virar:

```text
Perfil B
   ↓
regra
```

---

# 29. Conhecimento reutilizável

Quando houver base suficiente, alguns aprendizados poderão ser generalizados.

Exemplo:

```text
Perfil A
+
Perfil B
+
Perfil C
        ↓
Padrão recorrente do nicho
```

A generalização deverá ocorrer somente quando houver evidência suficiente.

---

# 30. Estrutura de um aprendizado

Modelo conceitual:

```text
Aprendizado
├── id
├── tipo
├── escopo
├── plataforma
├── nicho
├── perfil_id
├── tema
├── afirmação
├── evidências
├── amostra
├── confiança
├── status
├── criado_em
├── atualizado_em
└── ultima_evidencia_em
```

---

# 31. Tipos de aprendizado

Exemplos:

```text
HOOK
FORMATO
TEMA
EMOCAO
ESTRUTURA
CTA
HORARIO
FREQUENCIA
PUBLICO
ANGULO
```

Novos tipos poderão ser adicionados.

---

# 32. Exemplo de aprendizado

```json
{
  "tipo": "HOOK",
  "escopo": "PERFIL",
  "afirmacao": "Hooks em formato de pergunta apresentam desempenho acima da mediana.",
  "amostra": 18,
  "confianca": "MEDIA",
  "status": "ATIVO"
}
```

Esse registro é uma representação de conhecimento, não uma promessa de resultado.

---

# 33. Evidências do aprendizado

Cada aprendizado deverá conseguir apontar para seus dados de origem.

Exemplo:

```text
Aprendizado
    ↓
Publicação A
Publicação B
Publicação C
Publicação D
```

---

# 34. Atualização do aprendizado

Quando uma nova publicação for analisada:

```text
Novo resultado
      ↓
Evidência existente?
      ↓
SIM
      ↓
Atualizar aprendizado
```

Ou:

```text
Novo resultado
      ↓
Contradiz aprendizado?
      ↓
Reavaliar confiança
```

---

# 35. Aprendizado contraditório

Exemplo:

```text
Aprendizado:
perguntas performam melhor.

Novos dados:
perguntas performam pior.
```

O sistema não deverá apagar silenciosamente o aprendizado anterior.

Deverá registrar a mudança.

---

# 36. Revisão

Um aprendizado poderá passar por:

```text
ATIVO
   ↓
EM_REVISAO
   ↓
ATUALIZADO
```

ou:

```text
ATIVO
   ↓
SUPERADO
```

---

# 37. Recomendações

O Motor de Aprendizado poderá produzir recomendações para o Motor de Criação.

Exemplo:

```text
Aprendizado:
storytelling performa acima da mediana.

Recomendação:
gerar novas variações de storytelling.
```

---

# 38. Recomendação não é ordem

O Motor de Criação poderá considerar a recomendação, mas não deverá ser obrigado a utilizá-la em todas as situações.

Exemplo:

```text
Recomendação:
priorizar storytelling.

Nova estratégia:
testar também formato de pergunta.
```

Isso permite experimentação.

---

# 39. Hipóteses de teste

O sistema poderá registrar hipóteses.

Exemplo:

```text
Hipótese:
perguntas específicas aumentam o engajamento inicial.
```

Depois:

```text
Criar conteúdo
   ↓
Publicar
   ↓
Medir
   ↓
Avaliar hipótese
```

---

# 40. Experimentos futuros

Futuramente poderá existir:

```text
Experimento
├── hipótese
├── grupo
├── variação
├── métrica
├── período
└── resultado
```

Não é necessário implementar um sistema completo de experimentação no MVP.

---

# 41. Ciclo de hipótese

```text
HIPÓTESE
   ↓
CRIAÇÃO
   ↓
PUBLICAÇÃO
   ↓
MEDIÇÃO
   ↓
ANÁLISE
   ↓
APRENDIZADO
```

---

# 42. Feedback para o Motor de Criação

O Motor de Criação poderá receber:

```text
aprendizados ativos
+
recomendações
+
padrões
+
restrições
```

Exemplo:

```text
Criar Reel sobre diálogo.

Conhecimento disponível:
- perguntas funcionam bem;
- storytelling funciona melhor neste perfil;
- CTA de compartilhamento apresenta bom resultado.
```

---

# 43. Feedback para o Motor de Inteligência

O Motor de Inteligência poderá utilizar os aprendizados para priorizar análises.

Exemplo:

```text
Aprendizado:
conteúdos sobre conflitos têm alto desempenho.

Nova coleta:
dar atenção a novos conteúdos sobre conflitos.
```

---

# 44. Feedback para o Planejamento

Futuramente, o aprendizado poderá influenciar um Motor de Planejamento.

Exemplo:

```text
Tema com bom desempenho
       ↓
Maior prioridade editorial
```

O planejamento continuará sendo um componente separado.

---

# 45. Motor de Aprendizado não publica

O Motor de Aprendizado jamais deverá publicar diretamente.

Fluxo:

```text
Aprendizado
   ↓
Recomendação
   ↓
Motor de Criação
   ↓
Aprovação
   ↓
Motor de Publicação
```

---

# 46. Motor de Aprendizado não coleta diretamente

A coleta deverá permanecer no:

```text
Conector
```

e:

```text
Motor de Desempenho
```

O Motor de Aprendizado recebe dados já estruturados.

---

# 47. Motor de Aprendizado não cria conteúdo

Ele pode recomendar:

```text
"teste mais conteúdos desse tipo"
```

mas não deverá gerar o conteúdo.

---

# 48. Arquitetura de serviços

Fluxo:

```text
Motor de Desempenho
        ↓
ServicoAprendizado
        ↓
RepositorioAprendizado
        ↓
MySQL
```

Para utilização:

```text
ServicoAprendizado
        ↓
Motor de Criação
```

---

# 49. Serviço

Exemplo conceitual:

```python
class ServicoAprendizado:
    def atualizar_aprendizados(self, dados_desempenho):
        ...
```

---

# 50. Repositório

Exemplo:

```python
class RepositorioAprendizado:
    def salvar(self, aprendizado):
        ...

    def listar_ativos(self, contexto):
        ...
```

O serviço não deverá conhecer detalhes de SQL.

---

# 51. API futura

Endpoints conceituais:

```text
GET /aprendizados
GET /aprendizados/{id}
GET /perfis/{id}/aprendizados
GET /nichos/{id}/aprendizados
```

A criação automática de aprendizados poderá permanecer interna no MVP.

---

# 52. Dashboard futuro

O usuário poderá visualizar:

```text
MEUS APRENDIZADOS

🔥 O que está funcionando
⚠️ O que perdeu desempenho
🧪 O que está sendo testado
💡 O que testar agora
```

---

# 53. Transparência

O usuário deverá conseguir entender:

```text
Por que o ViralCode recomenda isso?
```

Resposta:

```text
Porque X conteúdos apresentaram
Y comportamento em determinado contexto.
```

---

# 54. Evitar caixa-preta

Não apresentar:

> "Nossa IA sabe que isso funciona."

Preferir:

> "Nos últimos 20 conteúdos semelhantes, a mediana foi X e este padrão apresentou desempenho Y."

---

# 55. Dados insuficientes

Quando não houver evidência suficiente:

```text
SEM EVIDÊNCIA SUFICIENTE
```

O sistema não deverá fabricar aprendizado.

---

# 56. Contradição

Quando os dados forem conflitantes:

```text
EVIDÊNCIA INCONCLUSIVA
```

Isso é preferível a uma recomendação falsa.

---

# 57. Confiança baixa

Uma recomendação baseada em poucos dados deverá possuir:

```text
confiança = baixa
```

E poderá ser apresentada como hipótese de teste.

---

# 58. Confiança média

Quando houver repetição suficiente, mas ainda houver incerteza:

```text
confiança = média
```

---

# 59. Confiança alta

Somente quando houver evidência consistente e contexto adequado:

```text
confiança = alta
```

Mesmo assim, não tratar como garantia de resultado futuro.

---

# 60. Aprendizado temporal

O sistema deverá permitir observar:

```text
Antes
   ↓
Depois
```

Isso ajudará a identificar mudanças de comportamento.

---

# 61. Decaimento de conhecimento

Futuramente poderá existir um mecanismo para reduzir a confiança de aprendizados antigos quando novos dados contradisserem o histórico.

Exemplo:

```text
Aprendizado antigo:
confiança alta

Novos resultados:
contrários

↓
confiança reduzida
```

Não implementar automaticamente no MVP.

---

# 62. Versionamento

Mudanças relevantes em um aprendizado deverão ser rastreáveis.

Exemplo:

```text
Aprendizado v1
Aprendizado v2
Aprendizado v3
```

Isso permite saber como o conhecimento evoluiu.

---

# 63. Auditoria

Para cada aprendizado importante deverá ser possível responder:

```text
De onde veio?
Quantos conteúdos sustentam?
Qual período?
Qual perfil?
Qual nicho?
Qual plataforma?
Qual foi a métrica?
```

---

# 64. MVP

O MVP deverá ser simples.

Implementar:

```text
Desempenho
   ↓
Identificar padrões simples
   ↓
Registrar aprendizados
   ↓
Associar evidências
   ↓
Disponibilizar para criação
```

---

# 65. O que NÃO fazer no MVP

Não implementar inicialmente:

```text
machine learning próprio
redes neurais
modelos preditivos complexos
agentes autônomos
aprendizado automático irreversível
otimização automática de estratégia
decisões automáticas de publicação
```

---

# 66. Primeiro caso de uso

Exemplo:

```text
20 Reels publicados
        ↓
Métricas coletadas
        ↓
Análise
        ↓
Padrões identificados
        ↓
Aprendizados registrados
        ↓
Nova criação
```

---

# 67. Critério de sucesso

O Motor de Aprendizado será considerado funcional quando conseguir:

> **transformar resultados reais de conteúdos publicados em aprendizados rastreáveis que possam ser utilizados na próxima rodada de criação.**

---

# 68. Regra para agentes de IA

Antes de modificar o Motor de Aprendizado:

1. ler este documento;
2. ler o Motor de Desempenho;
3. ler o Motor de Inteligência;
4. não transformar uma observação isolada em regra;
5. registrar evidências;
6. registrar contexto;
7. registrar confiança;
8. preservar histórico;
9. não apagar aprendizados silenciosamente;
10. atualizar a documentação quando a arquitetura mudar.

---

# 69. Arquitetura do Motor de Aprendizado

```text
                    MOTOR DE DESEMPENHO
                            │
                            ▼
                     DADOS REAIS
                            │
                            ▼
                 MOTOR DE INTELIGÊNCIA
                            │
                            ▼
                  PADRÕES / INSIGHTS
                            │
                            ▼
                  MOTOR DE APRENDIZADO
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
        APRENDIZADOS    HIPÓTESES    RECOMENDAÇÕES
              │             │             │
              └─────────────┼─────────────┘
                            ▼
                     MOTOR DE CRIAÇÃO
                            │
                            ▼
                         CONTEÚDO
```

---

# 70. Arquitetura-alvo completa

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
                       PADRÕES / INSIGHTS
                              │
                              ▼
                       MOTOR DE CRIAÇÃO
                              │
                              ▼
                           CONTEÚDO
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
                              │
                              ▼
                    NOVOS APRENDIZADOS
                              │
                              └──────────────→ MOTOR DE CRIAÇÃO
```

---

# 71. Regra final

> **O Motor de Aprendizado transforma resultados em conhecimento reutilizável, mas nunca deve confundir evidência com certeza.**

O ViralCode deverá evoluir por ciclos:

```text
TESTAR
   ↓
MEDIR
   ↓
COMPARAR
   ↓
APRENDER
   ↓
TESTAR NOVAMENTE
```

Essa abordagem permitirá que a inteligência do ViralCode cresça junto com os dados reais dos perfis, sem depender de uma "fórmula viral" fixa.

**Versão:** 1.0  
**Status:** Documento oficial do Motor de Aprendizado
