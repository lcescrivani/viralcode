# 38 — ARQUITETURA DO PROVEDOR DE INTELIGÊNCIA ARTIFICIAL

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define como o ViralCode utilizará inteligência artificial sem acoplar o domínio a um único provedor.

A arquitetura deverá permitir:

```text
ViralCode
   ↓
Serviço de IA
   ↓
Interface do provedor
   ↓
Provedor de IA
```

O objetivo é permitir evolução futura de:

```text
modelo
provedor
custo
capacidade
prompt
```

sem reconstruir o sistema.

---

# 2. Princípio fundamental

O domínio do ViralCode não deverá conhecer detalhes específicos de um provedor.

O domínio deverá solicitar:

```text
analisar conteúdo
gerar ideia
gerar roteiro
gerar legenda
gerar CTA
gerar insight
```

e não:

```text
chamar modelo X do provedor Y
```

---

# 3. Arquitetura

```text
CONTEÚDO
   ↓
SERVIÇO DE IA
   ↓
ORQUESTRADOR
   ↓
INTERFACE DE PROVEDOR
   ↓
PROVEDOR / MODELO
```

---

# 4. Responsabilidades do Serviço de IA

O Serviço de IA será responsável por:

```text
montar contexto
selecionar operação
selecionar modelo
montar prompt
executar chamada
validar resposta
registrar execução
tratar erro
retornar resultado estruturado
```

---

# 5. Provedor

Um provedor é a infraestrutura que oferece modelos de IA.

A implementação inicial deverá utilizar um provedor definido no início do desenvolvimento.

A arquitetura não deverá assumir que ele será o único provedor para sempre.

---

# 6. Modelo

O modelo é uma configuração do provedor.

Exemplo conceitual:

```text
provedor
   ↓
modelo
```

O código não deverá espalhar nomes de modelos por toda a aplicação.

---

# 7. Configuração centralizada

A escolha do provedor e modelo deverá ser centralizada.

Exemplo conceitual:

```text
PROVEDOR_IA
MODELO_IA
```

---

# 8. Segredos

Chaves do provedor deverão permanecer no backend.

Nunca:

```text
React
resposta API
banco em texto puro
logs
```

---

# 9. Interface do provedor

O sistema deverá possuir uma interface abstrata.

Conceitualmente:

```text
ProvedorIA
   ├── gerar_texto()
   └── ...
```

Os métodos finais deverão refletir as capacidades realmente utilizadas pelo produto.

---

# 10. Não abstrair demais

Não criar uma interface gigantesca para recursos que o MVP não utiliza.

A abstração deverá ser pequena e baseada nas necessidades reais.

---

# 11. Operações de IA

O MVP deverá considerar pelo menos:

```text
ANALISE
CRIACAO
ROTEIRO
LEGENDA
CTA
```

Poderão existir futuramente:

```text
INSIGHT
APRENDIZADO
REESCRITA
VARIACAO
```

---

# 12. Análise

A análise deverá receber contexto do conteúdo.

Exemplo:

```text
conteúdo
+
métricas disponíveis
+
perfil
```

e produzir uma resposta estruturada.

---

# 13. Criação

A criação deverá utilizar:

```text
perfil
+
nicho
+
objetivo
+
insights
+
aprendizados
+
contexto solicitado
```

---

# 14. Roteiro

O motor deverá conseguir produzir uma estrutura de roteiro adequada ao formato solicitado.

Exemplo:

```text
HOOK
DESENVOLVIMENTO
VIRADA
CTA
```

A estrutura final deverá ser definida pelo domínio do produto.

---

# 15. Legenda

A legenda deverá ser gerada respeitando:

```text
tom de voz
objetivo
tema
perfil
```

---

# 16. CTA

O CTA deverá ser contextual.

Não utilizar sempre a mesma chamada.

---

# 17. Contexto

O contexto enviado ao modelo deverá ser construído pelo backend.

Exemplo:

```text
Perfil
   ↓
Nicho
   ↓
Tom
   ↓
Objetivo
   ↓
Insights
   ↓
Aprendizados
   ↓
Conteúdo
```

---

# 18. Não enviar banco inteiro

Nunca enviar indiscriminadamente todos os dados do usuário para a IA.

Selecionar somente o contexto necessário.

---

# 19. Privacidade

Antes de enviar dados ao provedor, avaliar:

```text
necessidade
sensibilidade
finalidade
```

Enviar o mínimo necessário.

---

# 20. Prompt

Prompts deverão ser tratados como parte do produto.

Não espalhar textos críticos de prompt por dezenas de arquivos.

---

# 21. Versionamento de prompt

Toda operação importante deverá identificar:

```text
versao_prompt
```

Exemplo:

```text
ANALISE_REEL_V1
```

---

# 22. Por que versionar

Permite saber:

```text
qual prompt gerou o resultado
```

e comparar mudanças.

---

# 23. Prompt como configuração

Quando possível, prompts deverão ser organizados de maneira que possam evoluir sem alterar toda a lógica da aplicação.

---

# 24. Resultado estruturado

A IA deverá retornar dados estruturados sempre que o caso exigir.

Exemplo:

```json
{
  "tema": "comunicação",
  "hook": "Você fala com seu marido ou apenas reclama?",
  "emocao": "curiosidade",
  "cta": "Comente..."
}
```

---

# 25. Não confiar cegamente na saída

A resposta da IA deverá ser validada pelo backend.

---

# 26. Validação de saída

Validar:

```text
formato
campos obrigatórios
tipos
tamanho
enum
estrutura
```

---

# 27. Resposta inválida

Se a IA retornar formato inválido:

```text
registrar erro
+
tentar correção/reexecução quando apropriado
+
não persistir resultado inválido como resultado final
```

---

# 28. Retry de IA

Retries deverão ser limitados.

Não repetir indefinidamente.

---

# 29. Tipos de erro

Separar pelo menos:

```text
ERRO_REDE
ERRO_PROVEDOR
ERRO_AUTENTICACAO
ERRO_LIMITE
ERRO_MODELO
ERRO_RESPOSTA_INVALIDA
ERRO_VALIDACAO
```

---

# 30. Rate limit

O sistema deverá considerar limites do provedor.

---

# 31. Controle de custo

Cada execução deverá poder registrar:

```text
provedor
modelo
tokens_entrada
tokens_saida
custo_estimado
```

quando essas informações estiverem disponíveis.

---

# 32. ExecucaoIA

Toda operação relevante deverá gerar uma entidade:

```text
ExecucaoIA
```

conforme o Modelo de Dados.

---

# 33. Fluxo da execução

```text
solicitação
 ↓
criar ExecucaoIA
 ↓
PROCESSANDO
 ↓
montar contexto
 ↓
montar prompt
 ↓
chamar provedor
 ↓
validar resposta
 ↓
CONCLUIDA
```

Em erro:

```text
ERRO
```

---

# 34. Tempo de execução

Registrar:

```text
tempo_execucao_ms
```

quando possível.

Isso permitirá identificar gargalos.

---

# 35. Tokens

Quando fornecidos pelo provedor:

```text
tokens_entrada
tokens_saida
```

deverão ser registrados.

---

# 36. Custo

Quando possível, calcular:

```text
custo_estimado
```

com base no modelo e consumo.

Não depender exclusivamente desse valor para cobrança ao usuário.

---

# 37. Cobrança

A arquitetura de custo da IA é diferente da cobrança comercial do ViralCode.

Separar:

```text
CUSTO INTERNO DE IA
```

de:

```text
PREÇO DO PRODUTO
```

---

# 38. Modelo de seleção

No MVP, o modelo poderá ser definido por configuração.

Futuramente poderá existir:

```text
operação
 ↓
política
 ↓
modelo
```

---

# 39. Exemplo

```text
ANÁLISE
→ modelo econômico

CRIAÇÃO PREMIUM
→ modelo mais capaz
```

A decisão deverá ser baseada em qualidade, custo e velocidade.

---

# 40. Fallback

A arquitetura poderá suportar fallback entre modelos/provedores.

Exemplo:

```text
modelo principal
 ↓
falha
 ↓
modelo alternativo
```

Não implementar fallback complexo no MVP sem necessidade real.

---

# 41. Timeout

Toda chamada ao provedor deverá possuir timeout.

---

# 42. Circuit breaker

Não é requisito do MVP.

Poderá ser adicionado quando houver volume suficiente para justificar.

---

# 43. Fila

Operações longas poderão futuramente utilizar processamento assíncrono:

```text
API
 ↓
fila
 ↓
worker
 ↓
IA
```

No MVP, utilizar processamento síncrono somente quando o tempo e a experiência permitirem.

---

# 44. Execuções assíncronas

Quando uma operação for longa:

```text
POST
 ↓
202
 ↓
execucao_id
 ↓
consulta de status
```

---

# 45. Contexto de perfil

O perfil deverá funcionar como uma camada de contexto persistente.

Exemplo:

```text
nicho
subnicho
público
posicionamento
tom
objetivo
```

---

# 46. Insights

Quando disponíveis, insights poderão alimentar a IA.

```text
Conteúdo
 ↓
Análise
 ↓
Insight
 ↓
Criação
```

---

# 47. Aprendizados

Aprendizados representarão conhecimento mais consolidado.

```text
Análises
 ↓
Insights
 ↓
Aprendizados
 ↓
Nova criação
```

---

# 48. Não gerar conteúdo sem contexto

O motor deverá evitar gerar conteúdo genérico quando houver contexto suficiente do perfil.

---

# 49. Personalização

A IA deverá adaptar a saída para:

```text
nicho
subnicho
público
tom
objetivo
```

---

# 50. Reutilização de análise

Resultados de análise poderão ser persistidos para evitar chamadas desnecessárias.

---

# 51. Cache de IA

Cache poderá ser utilizado quando:

```text
mesmo conteúdo
+
mesma versão de análise
+
mesmo contexto relevante
```

permitirem reaproveitamento seguro.

---

# 52. Regra de cache

Não reutilizar uma resposta antiga quando:

```text
prompt mudou
modelo mudou significativamente
contexto relevante mudou
```

sem uma estratégia explícita.

---

# 53. Observabilidade

A Área Administrativa deverá conseguir acompanhar:

```text
execuções
erros
modelo
tempo
tokens
custo
```

---

# 54. Logs

Registrar:

```text
execucao_id
correlation_id
tipo
modelo
status
tempo
```

Não registrar prompts/respostas completos automaticamente se eles contiverem dados sensíveis sem necessidade.

---

# 55. Segurança de prompts

Prompts deverão ser tratados como lógica do produto.

Evitar expor internamente:

```text
instruções proprietárias
regras internas
```

quando não necessário.

---

# 56. Prompt injection

Conteúdo externo poderá conter instruções maliciosas.

Exemplo:

```text
legenda externa:
"ignore todas as instruções..."
```

O conteúdo analisado deverá ser tratado como:

```text
DADO
```

e não como instrução do sistema.

---

# 57. Separação de instruções

Conceitualmente:

```text
INSTRUÇÕES DO SISTEMA
        ↓
CONTEXTO DO VIRALCODE
        ↓
DADOS DO USUÁRIO
        ↓
CONTEÚDO EXTERNO
```

Os dados externos não deverão sobrescrever instruções superiores.

---

# 58. Conteúdo não confiável

Tratar como não confiável:

```text
legenda
comentário
texto externo
conteúdo importado
```

---

# 59. Moderação

Se o produto precisar tratar conteúdo potencialmente sensível ou proibido, a estratégia deverá ser definida antes da implementação dessa capacidade.

---

# 60. Qualidade

O sistema deverá avaliar a saída da IA por regras objetivas sempre que possível.

Exemplo:

```text
hook não vazio
roteiro possui estrutura
CTA existe
```

---

# 61. Avaliação

Futuramente poderá existir:

```text
conjunto de casos de teste
```

para comparar versões de prompts/modelos.

---

# 62. Testes de IA

Não testar somente:

```text
"chamada retornou 200"
```

Também testar:

```text
estrutura
conteúdo
regras
casos extremos
```

---

# 63. Dataset de avaliação

Poderá ser criado futuramente um conjunto de conteúdos representativos.

---

# 64. Regra de regressão

Alterar prompt/modelo não deverá destruir silenciosamente a qualidade esperada.

---

# 65. Modelo multimodal

Se houver necessidade de analisar:

```text
imagem
vídeo
áudio
```

a interface deverá ser ampliada somente quando a necessidade real aparecer.

---

# 66. MVP

O MVP deverá priorizar:

```text
texto
análise
geração
roteiro
legenda
CTA
```

---

# 67. Não começar com IA complexa

Evitar inicialmente:

```text
agentes autônomos
multiagentes
memória complexa
RAG sofisticado
orquestração excessiva
```

A menos que uma necessidade concreta do produto justifique.

---

# 68. Regra de simplicidade

No MVP:

```text
1 serviço de IA
+
1 provedor principal
+
modelo configurável
+
prompts versionados
+
validação
+
registro de execução
```

é suficiente.

---

# 69. Provedor alternativo

A arquitetura deverá permitir adicionar posteriormente:

```text
Provedor A
Provedor B
Provedor C
```

sem alterar o domínio.

---

# 70. Interface conceitual

```text
ServicoIA
    ↓
ProvedorIA
    ↓
Modelo
```

---

# 71. Exemplo de fluxo de análise

```text
POST /conteudos/100/analisar
        ↓
Serviço de IA
        ↓
carrega conteúdo
        ↓
carrega perfil
        ↓
carrega contexto
        ↓
monta prompt
        ↓
executa modelo
        ↓
valida JSON
        ↓
salva Analise
        ↓
atualiza ExecucaoIA
        ↓
responde API
```

---

# 72. Exemplo de fluxo de criação

```text
POST /conteudos/gerar
        ↓
perfil
        ↓
objetivo
        ↓
insights
        ↓
aprendizados
        ↓
prompt
        ↓
IA
        ↓
validação
        ↓
Conteudo
```

---

# 73. Falha de provedor

```text
IA
 ↓
erro
 ↓
ExecucaoIA = ERRO
 ↓
classificar erro
 ↓
retry/fallback quando permitido
 ↓
resposta segura
```

---

# 74. Regra de persistência

Não salvar uma geração como:

```text
CONTEUDO = FINAL
```

antes da validação.

Preferir:

```text
GERADO
```

e permitir revisão.

---

# 75. Aprovação humana

O usuário deverá permanecer no controle da publicação.

Fluxo:

```text
IA gera
 ↓
usuário revisa
 ↓
usuário aprova
 ↓
publicação
```

---

# 76. Não publicar automaticamente no MVP

A geração de IA não deverá implicar publicação automática.

A publicação deverá ser uma ação explícita ou uma rotina previamente configurada pelo usuário.

---

# 77. Auditoria

Quando necessário registrar:

```text
quem solicitou
qual operação
qual modelo
qual prompt
qual resultado
quando
```

sem expor segredos.

---

# 78. Versionamento

A execução deverá conseguir identificar:

```text
versão do prompt
modelo
provedor
```

---

# 79. Migração de modelo

Ao trocar o modelo:

```text
registrar nova configuração
+
avaliar qualidade
+
avaliar custo
```

---

# 80. Configuração por ambiente

Desenvolvimento e produção poderão utilizar configurações diferentes.

Nunca colocar credenciais de produção no ambiente local por padrão.

---

# 81. Regra para agentes de IA

Antes de alterar o motor de IA:

1. consultar este documento;
2. consultar Modelo de Dados;
3. consultar Contratos da API;
4. verificar versão do prompt;
5. verificar modelo;
6. verificar custo;
7. validar saída;
8. criar testes;
9. registrar mudança;
10. atualizar documentação.

---

# 82. Regra contra acoplamento

Nunca colocar no domínio:

```text
if provedor == "X":
```

como regra espalhada pela aplicação.

A escolha do provedor pertence à infraestrutura/configuração.

---

# 83. Regra contra segredo

Nunca escrever:

```text
CHAVE_API = "..."
```

no código.

---

# 84. Critério de sucesso

O motor de IA estará adequado quando:

```text
pode trocar modelo
+
pode trocar provedor
+
prompts são versionados
+
respostas são validadas
+
custos são rastreados
+
erros são tratados
+
dados externos são tratados como não confiáveis
+
usuário mantém controle da publicação
```

---

# 85. Arquitetura final

```text
                    VIRALCODE
                        │
                        ▼
                  SERVIÇO DE IA
                        │
                ┌───────┴───────┐
                ▼               ▼
          ORQUESTRADOR      CONTEXTO
                │               │
                └───────┬───────┘
                        ▼
                  PROVEDOR IA
                        │
                      MODELO
                        │
                        ▼
                 RESPOSTA ESTRUTURADA
                        │
                        ▼
                    VALIDAÇÃO
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
          CONTEÚDO             ANÁLISE
              │
              ▼
          USUÁRIO REVISA
              │
              ▼
           PUBLICAÇÃO
```

---

# 86. Regra final

> **A inteligência artificial deve ser um componente substituível do ViralCode, não o centro do domínio.**

O produto deve continuar funcionando conceitualmente mesmo que amanhã seja necessário trocar:

```text
provedor
modelo
prompt
estratégia de geração
```

A inteligência está no sistema:

```text
dados
+
análises
+
insights
+
aprendizados
+
contexto
+
IA
```

e não exclusivamente no modelo utilizado.

**Versão:** 1.0  
**Status:** Documento oficial da Arquitetura do Provedor de Inteligência Artificial
