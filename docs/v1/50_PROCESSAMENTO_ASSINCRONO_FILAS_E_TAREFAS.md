# 50 — PROCESSAMENTO ASSÍNCRONO, FILAS E TAREFAS EM SEGUNDO PLANO

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define como o ViralCode deverá tratar operações que não precisam ou não devem ser executadas diretamente durante uma requisição HTTP.

O objetivo é permitir que o sistema evolua de:

```text
processamento simples e síncrono
```

para:

```text
processamento assíncrono
+
filas
+
workers
```

sem transformar o MVP em uma arquitetura desnecessariamente complexa.

---

# 2. Princípio fundamental

O MVP deverá utilizar processamento síncrono sempre que isso for suficiente.

Somente utilizar processamento assíncrono quando existir uma necessidade concreta.

---

# 3. Quando utilizar processamento síncrono

Preferir processamento síncrono para operações:

```text
rápidas
simples
determinísticas
```

Exemplos:

```text
criar usuário
consultar perfil
editar conteúdo
listar publicações
```

---

# 4. Quando utilizar processamento assíncrono

Considerar processamento assíncrono para operações:

```text
demoradas
pesadas
em lote
externas
repetitivas
agendadas
```

Exemplos:

```text
analisar muitos conteúdos
gerar muitos conteúdos
publicar vários conteúdos
coletar dados
processar vídeos
```

---

# 5. Problema do processamento longo

Não manter uma requisição HTTP aberta durante uma operação que pode durar muito tempo.

Evitar:

```text
POST /analises
        ↓
espera vários minutos
        ↓
resposta
```

---

# 6. Modelo assíncrono

Preferir:

```text
POST /analises
        ↓
cria tarefa
        ↓
retorna
        ↓
worker processa
```

---

# 7. Fluxo

```text
USUÁRIO
   ↓
FRONTEND
   ↓
API
   ↓
CRIAR TAREFA
   ↓
FILA
   ↓
WORKER
   ↓
PROCESSAMENTO
   ↓
BANCO
   ↓
RESULTADO
```

---

# 8. Tarefa

Uma tarefa representa uma unidade de trabalho que será executada.

Exemplos:

```text
ANALISAR_CONTEUDO
GERAR_CONTEUDO
PUBLICAR_CONTEUDO
COLETAR_DADOS
```

---

# 9. Status da tarefa

Estados conceituais:

```text
PENDENTE
PROCESSANDO
CONCLUIDA
ERRO
CANCELADA
```

---

# 10. Tarefa pendente

A tarefa foi criada, mas ainda não começou.

---

# 11. Tarefa processando

Um worker está executando a tarefa.

---

# 12. Tarefa concluída

A operação terminou com sucesso.

---

# 13. Tarefa com erro

A operação terminou sem sucesso.

O erro deverá ser registrado sem expor segredos.

---

# 14. Tarefa cancelada

A operação foi interrompida intencionalmente.

---

# 15. Identificação

Uma tarefa deverá possuir um identificador próprio.

Exemplo:

```text
tarefa_id
```

---

# 16. Correlation ID

Quando uma tarefa nascer de uma requisição:

```text
correlation_id
```

deverá ser preservado quando possível.

---

# 17. Execução

Uma tarefa poderá possuir informações como:

```text
tarefa_id
tipo
status
data_criacao
data_inicio
data_fim
tentativas
erro
```

---

# 18. Relação com entidades

Quando necessário, uma tarefa poderá apontar para:

```text
conteudo_id
analise_id
publicacao_id
execucao_ia_id
perfil_id
```

---

# 19. Não duplicar contexto

Não copiar grandes quantidades de dados dentro da tarefa quando for possível armazenar apenas:

```text
identificador
```

e buscar os dados necessários durante o processamento.

---

# 20. Exemplo

Em vez de:

```text
tarefa = {
    conteúdo_completo: "texto enorme..."
}
```

preferir:

```text
tarefa = {
    conteudo_id: 123
}
```

quando isso for suficiente.

---

# 21. Fila

A fila representa tarefas aguardando processamento.

No início, o projeto poderá utilizar uma implementação simples.

---

# 22. Fila no MVP

Não é obrigatório introduzir um sistema externo de filas no primeiro MVP.

A necessidade deverá ser avaliada pelo volume real.

---

# 23. Evolução

Quando necessário, a arquitetura poderá evoluir para:

```text
API
 ↓
FILA
 ↓
WORKER
```

---

# 24. Redis

Redis não é dependência obrigatória do MVP.

Poderá ser introduzido posteriormente se houver necessidade concreta de:

```text
fila
cache
coordenação
```

---

# 25. RabbitMQ

RabbitMQ não é dependência obrigatória do MVP.

Somente adicionar se o volume ou a complexidade justificar.

---

# 26. Kafka

Kafka não faz parte da arquitetura inicial.

Não introduzir no MVP.

---

# 27. Regra contra complexidade prematura

Não adicionar:

```text
Redis
RabbitMQ
Kafka
```

somente para "preparar para escala".

---

# 28. Worker

Worker é o processo responsável por executar tarefas fora do ciclo da requisição HTTP.

---

# 29. Responsabilidade do worker

O worker deverá:

```text
buscar tarefa
 ↓
marcar como processando
 ↓
executar
 ↓
registrar resultado
```

---

# 30. Concorrência

O sistema deverá controlar quantos workers podem processar simultaneamente.

---

# 31. MVP

Um único worker poderá ser suficiente.

---

# 32. Evolução

Futuramente:

```text
Worker 1
Worker 2
Worker 3
...
```

poderão processar tarefas em paralelo.

---

# 33. Idempotência

Tarefas que possam ser executadas novamente deverão possuir proteção contra efeitos duplicados.

---

# 34. Publicação

Esse cuidado é especialmente importante para:

```text
publicação no Instagram
```

---

# 35. Exemplo de duplicidade

Sem idempotência:

```text
worker executa
 ↓
Instagram publica
 ↓
worker perde conexão
 ↓
worker tenta novamente
 ↓
segunda publicação
```

---

# 36. Proteção

Utilizar:

```text
chave de idempotência
+
estado interno
+
reconciliação
```

quando aplicável.

---

# 37. Retry

Uma tarefa poderá ser repetida quando a falha for temporária.

---

# 38. Falhas temporárias

Exemplos:

```text
timeout
erro temporário de rede
indisponibilidade momentânea
```

---

# 39. Falhas permanentes

Exemplos:

```text
credencial inválida
conteúdo inválido
permissão negada
```

Não devem gerar retries infinitos.

---

# 40. Número de tentativas

Toda tarefa com retry deverá possuir limite.

Exemplo conceitual:

```text
tentativa 1
tentativa 2
tentativa 3
```

Depois disso:

```text
ERRO
```

ou outro estado definido.

---

# 41. Backoff

Quando apropriado, utilizar espera crescente:

```text
tentativa 1 → espera curta
tentativa 2 → espera maior
tentativa 3 → espera maior
```

---

# 42. Dead Letter

Uma fila futura poderá possuir uma área para tarefas que falharam repetidamente.

Exemplo:

```text
FILA PRINCIPAL
      ↓
tentativas
      ↓
DEAD LETTER
```

No MVP isso não é obrigatório.

---

# 43. Tarefa presa

Uma tarefa poderá ficar:

```text
PROCESSANDO
```

mesmo depois que o worker morrer.

---

# 44. Recuperação de tarefa presa

O sistema deverá possuir mecanismo futuro para detectar:

```text
PROCESSANDO por tempo anormal
```

e permitir recuperação.

---

# 45. Lease

Quando houver múltiplos workers, poderá ser utilizado um mecanismo de posse temporária da tarefa.

Conceitualmente:

```text
worker assume
 ↓
processa
 ↓
renova posse
 ↓
conclui
```

---

# 46. Não implementar cedo demais

No MVP, não criar um sistema complexo de lease se um worker único tornar isso desnecessário.

---

# 47. Tarefas agendadas

Operações futuras poderão ser executadas em horários definidos.

Exemplos:

```text
publicar às 18:00
coletar dados diariamente
atualizar métricas
```

---

# 48. Agendamento

O agendamento deverá gerar uma tarefa executável.

Exemplo:

```text
agendamento
 ↓
chega o horário
 ↓
cria tarefa
 ↓
worker processa
```

---

# 49. Não publicar diretamente pelo agendador

O agendador não deverá conter toda a lógica de publicação.

Preferir:

```text
Agendador
 ↓
Tarefa
 ↓
Motor de Publicação
 ↓
Conector Instagram
```

---

# 50. Fuso horário

Agendamentos deverão considerar o fuso horário do perfil/usuário conforme regra do produto.

---

# 51. Armazenamento de horário

A estratégia de datas deverá seguir o padrão definido para o projeto.

Preferência:

```text
armazenamento → UTC
apresentação → timezone do usuário
```

---

# 52. Tarefas de IA

O Motor de Geração poderá criar tarefas para:

```text
geração individual
geração em lote
análise
reprocessamento
```

---

# 53. Execução de IA

A tarefa deverá apontar para:

```text
execucao_ia_id
```

quando houver registro correspondente.

---

# 54. Status da IA

A tarefa e a execução de IA são conceitos diferentes.

```text
Tarefa
→ trabalho a ser executado

ExecucaoIA
→ registro da execução do provedor/modelo
```

---

# 55. Falha da IA

Se a IA falhar:

```text
registrar erro
 ↓
avaliar retry
 ↓
atualizar tarefa
```

---

# 56. Timeout da IA

Chamadas ao provedor deverão possuir timeout.

---

# 57. Custo da IA

Tarefas de IA poderão registrar:

```text
tokens
custo_estimado
```

quando disponíveis.

---

# 58. Tarefas de análise

Uma análise grande poderá ser dividida em tarefas menores.

Exemplo:

```text
ANALISE_LOTE
    ↓
conteúdo 1
conteúdo 2
conteúdo 3
...
```

---

# 59. MVP

Não dividir uma operação em dezenas de tarefas se uma única execução for suficiente.

---

# 60. Lote

Quando houver processamento em lote:

```text
definir tamanho de lote
```

para evitar consumo excessivo de:

```text
RAM
CPU
IA
API externa
```

---

# 61. Rate Limit externo

Workers deverão respeitar limites das plataformas externas.

---

# 62. Instagram

O Motor de Publicação deverá respeitar os limites e regras oficiais da plataforma.

---

# 63. IA

O Serviço de IA deverá respeitar limites do provedor.

---

# 64. Concorrência externa

Não aumentar a quantidade de workers indiscriminadamente sem avaliar o impacto nos serviços externos.

---

# 65. Prioridade

Tarefas poderão possuir prioridade no futuro.

Exemplo:

```text
ALTA
NORMAL
BAIXA
```

No MVP:

```text
NORMAL
```

pode ser suficiente.

---

# 66. Ordem

Quando não houver prioridade, processar pela ordem de criação.

---

# 67. Cancelamento

Uma tarefa pendente poderá ser cancelada.

---

# 68. Cancelamento em processamento

Cancelar uma tarefa já em processamento pode ser mais complexo.

A implementação deverá definir se o cancelamento será:

```text
imediato
cooperativo
somente antes do início
```

---

# 69. Não interromper operação externa indevidamente

Não assumir que cancelar internamente cancela uma operação já enviada ao Instagram ou à IA.

---

# 70. Estado desconhecido

Se o worker perder conexão após executar uma operação externa:

```text
ESTADO_DESCONHECIDO
```

poderá ser necessário.

---

# 71. Reconciliação

Após estado desconhecido:

```text
consultar externo
 ↓
comparar
 ↓
atualizar estado interno
```

---

# 72. Publicação crítica

Fluxo recomendado:

```text
PENDENTE
   ↓
PROCESSANDO
   ↓
ENVIANDO
   ↓
CONFIRMANDO
   ↓
PUBLICADA
```

Os estados exatos poderão ser simplificados no MVP.

---

# 73. Não inventar sucesso

O sistema não deverá marcar:

```text
PUBLICADA
```

somente porque a requisição foi enviada.

Deverá possuir confirmação adequada para a operação.

---

# 74. Erro conhecido

Erros conhecidos deverão ser classificados quando possível.

Exemplo:

```text
CREDENCIAL_INVALIDA
PERMISSAO_NEGADA
TIMEOUT
LIMITE_EXCEDIDO
CONTEUDO_INVALIDO
ERRO_INTERNO
```

---

# 75. Mensagem técnica

Mensagens internas de erro poderão possuir detalhes técnicos.

---

# 76. Mensagem para usuário

O frontend deverá receber mensagem adequada ao usuário.

Não expor:

```text
stack trace
SQL
token
segredo
```

---

# 77. Logs

Toda falha relevante de tarefa deverá ser registrada.

Utilizar:

```text
tarefa_id
correlation_id
```

quando disponíveis.

---

# 78. Métricas

Futuramente acompanhar:

```text
tarefas criadas
tarefas concluídas
tarefas com erro
tempo médio
retries
```

---

# 79. Fila acumulada

Uma métrica importante será:

```text
quantidade de tarefas pendentes
```

---

# 80. Atraso

Futuramente medir:

```text
tempo entre criação e início
```

---

# 81. Tempo de execução

Também medir:

```text
tempo entre início e conclusão
```

---

# 82. Capacidade

Essas métricas permitirão avaliar quando será necessário:

```text
mais workers
fila externa
processamento paralelo
```

---

# 83. MVP

Não escalar antes de existir evidência de necessidade.

---

# 84. Banco como fila

No MVP, se o volume for baixo, uma tabela de tarefas no MySQL poderá ser suficiente.

Conceitualmente:

```text
tarefas
```

com:

```text
id
tipo
status
tentativas
data_criacao
data_inicio
data_fim
erro
```

---

# 85. Limitação

Usar MySQL como fila poderá se tornar inadequado em escala maior.

---

# 86. Evolução

Quando necessário:

```text
MySQL
 ↓
fila dedicada
```

poderá ser adotado.

---

# 87. Não esconder a evolução

A implementação deverá manter o processamento assíncrono desacoplado o suficiente para permitir substituição do mecanismo de fila.

---

# 88. Interface de fila

Quando existir uma necessidade real de múltiplos mecanismos, poderá ser criada uma abstração como:

```text
FilaTarefas
```

---

# 89. Não abstrair prematuramente

No MVP, uma implementação simples poderá ser suficiente.

---

# 90. Worker e banco

O worker deverá utilizar os serviços/repositórios existentes.

Evitar duplicar regra de negócio no worker.

---

# 91. Fluxo correto

```text
Worker
 ↓
Servico
 ↓
Repositorio/Conector
```

---

# 92. Fluxo incorreto

Evitar:

```text
Worker
 ↓
SQL direto
 ↓
API Instagram diretamente
```

se isso duplicar regras já existentes.

---

# 93. Regra de responsabilidade

```text
Fila
→ organiza tarefas

Worker
→ executa tarefas

Serviço
→ aplica regra de negócio

Conector
→ comunica com externo
```

---

# 94. Testes

Tarefas deverão possuir testes para:

```text
sucesso
erro
retry
limite de tentativas
cancelamento
estado inválido
```

quando aplicável.

---

# 95. Teste de idempotência

Publicações deverão possuir teste que demonstre que uma mesma operação não gera duplicidade indevida.

---

# 96. Teste de recuperação

Quando houver mecanismo de recuperação de tarefa presa, deverá existir teste correspondente.

---

# 97. Desenvolvimento

No ambiente local poderá existir comando para executar o worker.

Exemplo conceitual:

```text
executar_worker
```

---

# 98. Produção

O worker deverá possuir processo controlado de execução e reinício.

---

# 99. Reinício

Se o worker morrer:

```text
serviço de processo
 ↓
detecta
 ↓
reinicia
```

conforme infraestrutura adotada.

---

# 100. Monitoramento

O sistema deverá permitir identificar:

```text
worker ativo
worker parado
fila acumulada
tarefas com erro
```

---

# 101. Worker único no MVP

A arquitetura inicial poderá ser:

```text
API
Worker
MySQL
```

na mesma VPS.

---

# 102. Evolução futura

Poderá evoluir para:

```text
              ┌── Worker 1
API → FILA ───┼── Worker 2
              ├── Worker 3
              └── Worker N
```

---

# 103. Não separar servidores cedo demais

No MVP, API e Worker podem compartilhar a mesma VPS, desde que os recursos sejam suficientes.

---

# 104. CPU

Processamentos de IA, vídeo ou lote podem consumir CPU.

O impacto deverá ser monitorado.

---

# 105. Memória

Workers deverão limitar processamento simultâneo para não consumir toda a RAM.

---

# 106. Falha do worker

A falha de um worker não deverá corromper os dados da tarefa.

---

# 107. Transação

Atualizações de estado da tarefa deverão utilizar transações apropriadas.

---

# 108. Concorrência

Dois workers não deverão processar a mesma tarefa simultaneamente sem mecanismo de proteção.

---

# 109. Bloqueio

Quando necessário, utilizar mecanismos de bloqueio/seleção adequados ao MySQL para aquisição segura de tarefas.

---

# 110. Estado da tarefa

A mudança de:

```text
PENDENTE
```

para:

```text
PROCESSANDO
```

deverá ocorrer de maneira controlada.

---

# 111. Regra contra corrida

Evitar:

```text
Worker A lê tarefa
Worker B lê tarefa
Worker A processa
Worker B processa
```

---

# 112. Lock

Quando houver múltiplos workers, o mecanismo de aquisição deverá impedir processamento duplicado.

---

# 113. Agendamento futuro

A arquitetura poderá evoluir para um componente:

```text
Agendador
```

responsável por criar tarefas no momento adequado.

---

# 114. Agendador não é worker

São responsabilidades diferentes:

```text
Agendador
→ decide quando criar/executar

Worker
→ executa
```

---

# 115. Publicações programadas

Fluxo futuro:

```text
Usuário agenda
 ↓
Publicacao criada
 ↓
Agendamento registrado
 ↓
Agendador identifica horário
 ↓
Tarefa criada
 ↓
Worker
 ↓
Motor de Publicação
 ↓
Instagram
```

---

# 116. Falha no agendamento

Se o agendador falhar, deverá existir mecanismo para identificar tarefas que deveriam ter sido criadas.

---

# 117. Precisão

O MVP não precisa garantir precisão de segundos para publicações agendadas, salvo se isso virar requisito explícito.

---

# 118. Regra de negócio

O horário exato de publicação deverá ser definido pelo produto.

---

# 119. IA em lote

Quando o usuário solicitar:

```text
gerar 30 conteúdos
```

o sistema poderá criar:

```text
1 tarefa de lote
```

que gera:

```text
tarefas individuais
```

quando isso for necessário.

---

# 120. Não gerar tudo em uma única chamada

Não assumir que uma única chamada à IA é sempre melhor.

O tamanho do lote deverá considerar:

```text
qualidade
tokens
tempo
custo
risco de falha
```

---

# 121. Reprocessamento

O sistema deverá permitir reprocessar tarefas que falharam quando fizer sentido.

---

# 122. Reprocessamento manual

A Área Administrativa poderá futuramente permitir:

```text
reprocessar tarefa
```

com autorização adequada.

---

# 123. Reprocessamento automático

Somente utilizar quando:

```text
erro temporário
+
operação idempotente
```

ou mecanismo equivalente.

---

# 124. Auditoria

Operações administrativas de reprocessamento deverão ser registradas quando relevantes.

---

# 125. Regra para agentes de IA

Antes de transformar uma operação em tarefa assíncrona:

1. medir ou estimar duração;
2. verificar se HTTP síncrono é suficiente;
3. avaliar necessidade de retry;
4. avaliar idempotência;
5. definir estados;
6. definir tratamento de erro;
7. definir logs;
8. definir recuperação;
9. criar testes.

---

# 126. Regra contra fila desnecessária

Não criar tarefa assíncrona para:

```text
consulta simples
alteração simples
operação instantânea
```

sem benefício.

---

# 127. Regra contra worker inteligente demais

O worker não deverá concentrar toda a lógica do sistema.

---

# 128. Regra contra dependência de infraestrutura

A regra de negócio não deverá depender diretamente de:

```text
Redis
RabbitMQ
Kafka
```

se uma abstração simples puder ser utilizada quando necessário.

---

# 129. Regra de simplicidade

A primeira implementação poderá ser:

```text
FastAPI
+
MySQL
+
tabela de tarefas
+
worker simples
```

somente quando o MVP realmente precisar de processamento assíncrono.

---

# 130. Critério de sucesso

O processamento assíncrono estará adequado quando:

```text
operações longas não bloqueiam a API
+
tarefas possuem estado
+
erros são rastreáveis
+
retries são controlados
+
duplicidades são evitadas
+
worker pode ser reiniciado
+
a arquitetura pode evoluir
```

---

# 131. Arquitetura resumida

```text
                 FRONTEND
                     │
                     ▼
                  FASTAPI
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
      OPERAÇÃO              CRIAR TAREFA
      SÍNCRONA                    │
          │                       ▼
          │                     FILA
          │                       │
          │                       ▼
          │                    WORKER
          │                       │
          │              ┌────────┼────────┐
          │              ▼        ▼        ▼
          │          SERVIÇO   SERVIÇO   SERVIÇO
          │             │         │        │
          └─────────────┴─────────┴────────┘
                              │
                 ┌────────────┼────────────┐
                 ▼            ▼            ▼
              MYSQL      INSTAGRAM        IA
```

---

# 132. Regra final

> **O ViralCode deve começar simples e introduzir filas e workers somente quando o processamento real justificar.**

A evolução desejada é:

```text
MVP
 ↓
tarefas simples
 ↓
worker
 ↓
fila dedicada
 ↓
múltiplos workers
 ↓
escala
```

sem antecipar infraestrutura que o negócio ainda não precisa.

**Versão:** 1.0  
**Status:** Documento oficial de Processamento Assíncrono, Filas e Tarefas em Segundo Plano
