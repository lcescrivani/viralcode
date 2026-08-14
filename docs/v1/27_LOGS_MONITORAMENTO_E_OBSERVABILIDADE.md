# 27 — LOGS, MONITORAMENTO E OBSERVABILIDADE

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define como o ViralCode deverá registrar, acompanhar e diagnosticar o comportamento da aplicação.

O objetivo do MVP é possuir observabilidade suficiente para responder rapidamente:

```text
O sistema está funcionando?
O que aconteceu?
Onde aconteceu?
Para qual usuário?
Qual operação falhou?
Uma integração externa está indisponível?
```

Não criar uma plataforma de observabilidade complexa antes de existir necessidade.

---

# 2. Princípio fundamental

Todo problema importante deverá deixar evidência suficiente para diagnóstico.

Fluxo:

```text
REQUISIÇÃO
   ↓
CORRELATION ID
   ↓
LOGS
   ↓
ERRO / RESULTADO
   ↓
DIAGNÓSTICO
```

---

# 3. O que é observabilidade

No ViralCode, observabilidade será tratada em três dimensões:

```text
LOGS
MÉTRICAS
SAÚDE DO SISTEMA
```

Posteriormente poderão ser adicionados:

```text
TRACES
ALERTAS AVANÇADOS
APM
```

---

# 4. Logs

Logs registrarão acontecimentos relevantes da aplicação.

Exemplos:

```text
usuário autenticado
conteúdo criado
descoberta executada
análise iniciada
IA respondeu
publicação enviada
métrica coletada
erro Instagram
erro banco
```

---

# 5. Não registrar tudo

Não transformar cada linha de código em log.

Um log deverá existir quando ajudar a:

```text
diagnosticar
auditar
entender fluxo
medir operação
```

---

# 6. Formato

Preferir logs estruturados.

Conceitualmente:

```json
{
  "nivel": "INFO",
  "evento": "conteudo_criado",
  "correlation_id": "abc123",
  "usuario_id": 10,
  "conteudo_id": 45
}
```

O formato definitivo poderá ser ajustado pela implementação.

---

# 7. Níveis

Utilizar níveis apropriados:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

---

# 8. DEBUG

Utilizado principalmente em desenvolvimento.

Exemplo:

```text
detalhes de processamento
```

Não depender de DEBUG em produção para informações essenciais.

---

# 9. INFO

Para acontecimentos normais relevantes.

Exemplos:

```text
login realizado
conta social conectada
conteúdo criado
publicação iniciada
```

---

# 10. WARNING

Para situações anormais que não interromperam necessariamente o sistema.

Exemplos:

```text
métrica indisponível
tentativa de operação repetida
resposta incompleta de integração
```

---

# 11. ERROR

Para falhas de uma operação.

Exemplos:

```text
falha ao publicar
falha ao consultar Instagram
falha ao gerar conteúdo
falha de banco
```

---

# 12. CRITICAL

Somente para situações que comprometam seriamente a aplicação.

Exemplos:

```text
aplicação não consegue iniciar
banco essencial indisponível
configuração crítica ausente
```

---

# 13. Correlation ID

Cada requisição relevante deverá possuir um identificador de correlação.

Exemplo:

```text
correlation_id = 7f2a...
```

Esse identificador deverá acompanhar:

```text
requisição
↓
rota
↓
serviço
↓
conector
↓
erro
```

---

# 14. Objetivo do Correlation ID

Permitir responder:

> "O que aconteceu com esta requisição?"

sem precisar procurar manualmente centenas de logs.

---

# 15. Retorno do Correlation ID

Quando apropriado, o backend poderá retornar o identificador no cabeçalho:

```text
X-Correlation-ID
```

Isso ajudará o suporte e o diagnóstico.

---

# 16. Usuário nos logs

Quando tecnicamente apropriado, registrar:

```text
usuario_id
perfil_id
```

para facilitar investigação.

Nunca registrar:

```text
senha
senha_hash
token completo
client_secret
chave privada
```

---

# 17. Dados sensíveis

Não registrar conteúdo sensível desnecessariamente.

Exemplo:

```text
token Instagram
```

deverá aparecer no máximo como informação mascarada, ou não aparecer.

---

# 18. Logs de autenticação

Registrar eventos como:

```text
login_sucesso
login_falhou
usuario_bloqueado
token_invalido
```

Sem registrar a senha.

---

# 19. Logs do Instagram

Registrar eventos relevantes:

```text
instagram_conexao_iniciada
instagram_conexao_concluida
instagram_token_atualizado
instagram_token_expirado
instagram_consulta_realizada
instagram_publicacao_iniciada
instagram_publicacao_concluida
instagram_erro
```

---

# 20. Logs da IA

Registrar:

```text
geracao_iniciada
geracao_concluida
geracao_falhou
modelo_utilizado
tempo_de_execucao
```

Quando disponível:

```text
tokens
custo_estimado
```

---

# 21. Não registrar prompt completo indiscriminadamente

Prompts podem conter:

```text
dados do usuário
estratégias internas
conteúdo privado
```

O projeto deverá avaliar o que pode ser armazenado.

O histórico de execução da IA poderá ser persistido no banco de acordo com o modelo de dados, sem necessariamente duplicar tudo nos logs.

---

# 22. Logs de publicação

Uma publicação deverá permitir reconstruir o fluxo:

```text
publicacao_solicitada
      ↓
validacao
      ↓
envio_instagram
      ↓
resposta
      ↓
publicacao_confirmada
```

ou:

```text
publicacao_solicitada
      ↓
erro
```

---

# 23. Logs de métricas

Registrar:

```text
coleta_iniciada
coleta_concluida
coleta_falhou
```

Não registrar cada métrica como log se ela já estiver sendo armazenada corretamente no banco.

---

# 24. Health Check

Endpoint:

```http
GET /health
```

deverá responder rapidamente.

Exemplo:

```json
{
  "status": "ok"
}
```

---

# 25. Health detalhado

Posteriormente poderá existir:

```http
GET /health/detalhado
```

com informações como:

```text
API
Banco
dependências essenciais
```

Não retornar segredos.

---

# 26. Liveness

O health básico deverá responder à pergunta:

```text
A aplicação está viva?
```

Não deve executar verificações pesadas.

---

# 27. Readiness

Posteriormente poderá existir uma verificação de:

```text
A aplicação está pronta para receber tráfego?
```

Exemplo:

```text
API funcionando
+
banco disponível
```

---

# 28. Métricas da aplicação

No MVP, acompanhar pelo menos:

```text
requisições
erros
tempo de resposta
```

---

# 29. Métricas de produto

Também deverão ser acompanhados:

```text
usuários cadastrados
perfis criados
contas conectadas
descobertas
análises
conteúdos gerados
aprovações
publicações
```

---

# 30. Métricas de IA

Quando possível:

```text
quantidade de chamadas
tempo médio
tokens
custo estimado
falhas
```

---

# 31. Métricas do Instagram

Quando disponíveis:

```text
consultas
publicações
falhas
tempo de resposta
limitações
```

---

# 32. Métricas da VPS

No mínimo:

```text
CPU
RAM
disco
rede
processos
```

---

# 33. Disco

O disco deverá ser monitorado porque:

```text
logs
backups
mídias
banco
```

podem consumir espaço.

---

# 34. Logs antigos

Não permitir crescimento infinito dos arquivos de log.

Deverá existir:

```text
rotação
retenção
limpeza
```

conforme a infraestrutura adotada.

---

# 35. Backup

O backup deverá gerar evidência de execução.

Exemplo:

```text
backup iniciado
backup concluído
backup falhou
```

O conteúdo do backup não deverá ser exposto nos logs.

---

# 36. Monitoramento externo

No MVP poderá ser suficiente utilizar ferramentas simples da própria VPS ou um serviço externo básico.

Não é obrigatório implantar uma stack completa de observabilidade.

---

# 37. Alertas

Inicialmente priorizar alertas para:

```text
aplicação indisponível
banco indisponível
disco quase cheio
falha recorrente
```

---

# 38. Alertas de integração

Futuramente poderão existir alertas quando:

```text
Instagram falhar repetidamente
provedor de IA falhar repetidamente
```

Não enviar alerta para cada erro isolado.

---

# 39. Evitar ruído

Um sistema que envia centenas de alertas deixa de ser útil.

Preferir:

```text
agregação
limite
janela de tempo
```

quando necessário.

---

# 40. Tempo de resposta

A aplicação deverá acompanhar:

```text
p50
p95
p99
```

quando houver volume suficiente para isso.

No começo, o tempo médio poderá ser utilizado como indicador simples.

---

# 41. Operações lentas

Priorizar monitoramento de:

```text
descoberta
análise
geração IA
publicação
coleta de métricas
```

---

# 42. Tempo de IA

Registrar o tempo gasto na chamada externa.

Exemplo:

```text
geracao_ia
tempo_ms = 4200
```

Isso permitirá identificar gargalos.

---

# 43. Tempo do Instagram

Da mesma forma:

```text
consulta_instagram
tempo_ms = 900
```

---

# 44. Erros externos

Diferenciar:

```text
erro interno
```

de:

```text
erro externo
```

Exemplo:

```text
ERRO_INTERNO
ERRO_INSTAGRAM
ERRO_PROVEDOR_IA
ERRO_BANCO
```

---

# 45. Códigos de erro

Os erros da aplicação deverão utilizar códigos consistentes.

Exemplos:

```text
INSTAGRAM_NAO_CONECTADO
INSTAGRAM_TOKEN_EXPIRADO
INSTAGRAM_INDISPONIVEL
IA_INDISPONIVEL
CONTEUDO_NAO_ENCONTRADO
ACESSO_NEGADO
```

---

# 46. Não expor detalhes internos

A resposta da API para o usuário não deverá mostrar:

```text
stack trace
SQL
senha
token
caminho interno
```

---

# 47. Stack trace

Stack traces poderão ser registrados internamente quando necessários para diagnóstico.

Nunca retornar diretamente ao usuário em produção.

---

# 48. Banco

Erros do banco deverão ser registrados com contexto suficiente.

Evitar registrar consultas contendo dados sensíveis.

---

# 49. Performance do banco

Quando houver necessidade, monitorar:

```text
tempo de consulta
consultas lentas
conexões
uso de CPU
```

---

# 50. Monitoramento de filas futuro

Se o projeto adotar filas:

```text
tamanho da fila
tempo de espera
falhas
reprocessamentos
```

deverão ser monitorados.

Isso não é obrigatório no MVP.

---

# 51. Rastreamento de publicação

O estado da publicação deverá estar no banco.

Logs complementam o estado.

Não usar logs como única fonte de verdade.

---

# 52. Regra importante

```text
BANCO
→ estado do negócio

LOG
→ histórico técnico

MÉTRICA
→ comportamento quantitativo
```

Não misturar as três responsabilidades.

---

# 53. Auditoria

Algumas ações importantes poderão futuramente possuir registro de auditoria:

```text
conectar Instagram
desconectar Instagram
publicar
aprovar
alterar configurações
```

A auditoria de negócio deverá ser separada dos logs técnicos quando necessário.

---

# 54. Dashboard futuro

Posteriormente poderá existir um painel técnico mostrando:

```text
saúde da API
erros
tempo de resposta
Instagram
IA
banco
VPS
```

Não é requisito do MVP.

---

# 55. Dashboard de produto

O dashboard do usuário será diferente.

Ele deverá mostrar:

```text
conteúdos
desempenho
aprendizados
planejamento
```

Não confundir com monitoramento técnico.

---

# 56. Privacidade

Logs deverão seguir o princípio:

```text
registrar somente o necessário
```

---

# 57. Retenção

A retenção dos logs deverá considerar:

```text
necessidade de diagnóstico
custo
privacidade
```

No MVP poderá ser definida uma retenção simples e revisada posteriormente.

---

# 58. Correlação frontend/backend

O frontend poderá enviar ou receber:

```text
X-Correlation-ID
```

para facilitar diagnóstico de uma operação iniciada na interface.

---

# 59. Erro exibido ao usuário

Exemplo:

```text
Não foi possível conectar ao Instagram.
Tente novamente.
Código: INSTAGRAM_INDISPONIVEL
```

O detalhe técnico ficará no log.

---

# 60. Erro interno

Ao usuário:

```text
Não foi possível concluir a operação.
```

Nos logs:

```text
erro
stack trace
correlation_id
contexto
```

---

# 61. Regra de suporte

Quando um usuário relatar:

```text
"deu erro"
```

o suporte deverá conseguir solicitar:

```text
correlation_id
```

e localizar a operação correspondente.

---

# 62. Logs e desenvolvimento

Em desenvolvimento, os logs poderão ser mais detalhados.

Em produção:

```text
menos ruído
mais estrutura
```

---

# 63. Não utilizar print

O mecanismo oficial de observabilidade não deverá ser:

```python
print("deu erro")
```

Preferir o sistema de logging da aplicação.

---

# 64. Estrutura de código

Poderá existir:

```text
backend/app/
└── utilitarios/
    └── logging.py
```

ou uma estrutura equivalente.

O importante é centralizar a configuração de logging.

---

# 65. Biblioteca

Utilizar mecanismos de logging apropriados ao ecossistema Python.

Não criar um sistema de logs próprio desnecessariamente.

---

# 66. Correlação em serviços

O `correlation_id` deverá ser preservado quando uma operação atravessar:

```text
rota
 ↓
serviço
 ↓
repositório
```

e principalmente:

```text
rota
 ↓
serviço
 ↓
conector externo
```

---

# 67. Correlação em chamadas externas

Quando apropriado, o identificador poderá acompanhar metadados técnicos da operação externa, sem violar as regras da plataforma.

---

# 68. Diagnóstico de IA

Uma execução de IA deverá permitir identificar:

```text
qual operação
qual usuário
qual conteúdo
qual modelo
quando iniciou
quando terminou
status
```

Quando apropriado.

---

# 69. Diagnóstico de Instagram

Uma operação Instagram deverá permitir identificar:

```text
qual conta social
qual operação
quando ocorreu
status
erro
```

Sem expor o token.

---

# 70. Diagnóstico de publicação

A publicação deverá permitir reconstruir:

```text
conteúdo
conta
usuário
início
resultado
erro
```

---

# 71. Falhas recorrentes

Se uma mesma falha ocorrer repetidamente, o sistema deverá permitir identificar:

```text
quantidade
período
componente
tipo de erro
```

---

# 72. Regra de agrupamento

Futuramente poderá agrupar:

```text
100 erros Instagram
```

como:

```text
Instagram indisponível
```

em vez de criar 100 alertas separados.

---

# 73. SLO futuro

Quando houver escala, poderão ser definidos objetivos como:

```text
99% das requisições < X ms
99,9% disponibilidade
```

Não é necessário definir metas rígidas antes de existir dados.

---

# 74. Monitoramento de custo

O sistema deverá permitir acompanhar custos variáveis relevantes:

```text
IA
armazenamento
infraestrutura
```

---

# 75. Custo por conteúdo

Futuramente poderá ser calculado:

```text
custo de IA
+
infraestrutura estimada
```

por conteúdo gerado.

Isso poderá ajudar na definição de preço do produto.

---

# 76. Regra para agentes de IA

Antes de alterar observabilidade:

1. verificar logs existentes;
2. preservar `correlation_id`;
3. não adicionar logs excessivos;
4. não registrar segredos;
5. diferenciar erro técnico de estado de negócio;
6. atualizar códigos de erro quando necessário;
7. testar o fluxo.

---

# 77. Critério de sucesso

A observabilidade estará adequada quando for possível responder rapidamente:

```text
O usuário fez o quê?
Quando?
Qual operação?
Qual componente?
Funcionou?
Se falhou, por quê?
```

usando:

```text
correlation_id
+
logs
+
estado do banco
+
métricas
```

---

# 78. Estrutura resumida

```text
                    APLICAÇÃO
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
        LOGS         MÉTRICAS      HEALTH
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                   DIAGNÓSTICO
```

---

# 79. Evolução futura

Quando o ViralCode crescer, poderá incorporar:

```text
monitoramento externo
APM
tracing distribuído
dashboards
alertas avançados
métricas históricas
filas monitoradas
```

Somente conforme necessidade.

---

# 80. Regra final

> **Se uma operação importante falhar, o sistema deve deixar pistas suficientes para descobrir o motivo sem precisar reproduzir o problema às cegas.**

A observabilidade do MVP deverá ser:

```text
simples
estruturada
segura
útil
```

e deverá crescer junto com o produto.

**Versão:** 1.0  
**Status:** Documento oficial de Logs, Monitoramento e Observabilidade
