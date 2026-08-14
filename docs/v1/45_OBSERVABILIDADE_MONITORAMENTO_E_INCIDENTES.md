# 45 — OBSERVABILIDADE, MONITORAMENTO E TRATAMENTO DE INCIDENTES

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define como o ViralCode deverá identificar, diagnosticar e acompanhar problemas em:

```text
Frontend
Backend
Banco de dados
Instagram
Provedor de IA
Infraestrutura
Publicações
Processamentos
```

O objetivo do MVP é possuir observabilidade suficiente para responder:

```text
O sistema está funcionando?
O que falhou?
Onde falhou?
Quando falhou?
Quem foi afetado?
O problema ainda está acontecendo?
```

---

# 2. Princípio fundamental

Não basta detectar que houve erro.

O sistema deverá permitir:

```text
detectar
 ↓
identificar
 ↓
diagnosticar
 ↓
corrigir
 ↓
validar
```

---

# 3. Observabilidade no MVP

O MVP deverá priorizar:

```text
logs estruturados
+
health check
+
correlation_id
+
status das integrações
+
erros de aplicação
+
monitoramento básico da VPS
```

---

# 4. Não criar stack excessiva

No MVP não é necessário implantar automaticamente:

```text
Prometheus
Grafana
ELK
OpenTelemetry completo
Jaeger
Datadog
```

sem uma necessidade real.

A arquitetura deverá permitir evolução futura.

---

# 5. Três pilares

A observabilidade poderá evoluir para:

```text
LOGS
MÉTRICAS
RASTREAMENTO
```

No MVP:

```text
LOGS + MÉTRICAS BÁSICAS + CORRELATION_ID
```

são suficientes.

---

# 6. Logs

Logs deverão registrar eventos relevantes da aplicação.

Exemplo:

```text
usuário autenticado
conteúdo criado
análise iniciada
IA executada
publicação solicitada
publicação concluída
erro externo
```

---

# 7. Logs estruturados

Preferir formato estruturado quando possível.

Exemplo conceitual:

```json
{
  "nivel": "INFO",
  "evento": "PUBLICACAO_CONCLUIDA",
  "usuario_id": 123,
  "publicacao_id": 456,
  "correlation_id": "abc"
}
```

---

# 8. Níveis de log

Utilizar pelo menos:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

---

# 9. DEBUG

Utilizado principalmente durante desenvolvimento.

Não deverá gerar exposição de segredos.

---

# 10. INFO

Eventos normais importantes.

Exemplo:

```text
CONTEUDO_CRIADO
ANALISE_CONCLUIDA
PUBLICACAO_CONCLUIDA
```

---

# 11. WARNING

Situação anormal que não necessariamente interrompe a operação.

Exemplo:

```text
retry executado
credencial próxima de expirar
resposta externa incompleta
```

---

# 12. ERROR

Erro que impediu uma operação.

Exemplo:

```text
falha na geração
falha na publicação
falha de banco
```

---

# 13. CRITICAL

Falha grave que pode comprometer o funcionamento do sistema.

Exemplo:

```text
banco indisponível
serviço principal fora do ar
falha de inicialização
```

---

# 14. Não registrar segredos

Nunca registrar:

```text
senha
token
client_secret
chave de IA
cookie de autenticação
```

---

# 15. Dados pessoais nos logs

Evitar registrar:

```text
e-mail
telefone
nome completo
```

quando não forem necessários.

---

# 16. Identificação técnica

Preferir:

```text
usuario_id
conteudo_id
publicacao_id
execucao_id
correlation_id
```

para diagnóstico.

---

# 17. Correlation ID

Toda requisição relevante deverá possuir um:

```text
correlation_id
```

quando possível.

---

# 18. Objetivo do correlation_id

Permitir acompanhar:

```text
Frontend
 ↓
FastAPI
 ↓
Serviço
 ↓
Banco/Conector
```

---

# 19. Exemplo

```text
correlation_id = 8f2...
```

O mesmo identificador deverá aparecer nos logs relacionados àquela requisição.

---

# 20. Execução de IA

Além do correlation_id, operações de IA deverão possuir:

```text
execucao_id
```

quando representarem uma execução registrada.

---

# 21. Publicação

Operações de publicação deverão possuir:

```text
publicacao_id
```

e, quando necessário:

```text
correlation_id
```

---

# 22. Logs do Instagram

Registrar:

```text
operação
conta interna
status
tempo
erro
correlation_id
```

Não registrar tokens.

---

# 23. Logs da IA

Registrar:

```text
execucao_id
provedor
modelo
operação
status
tempo
erro
```

Quando disponível, também:

```text
tokens
custo estimado
```

---

# 24. Logs do banco

O MySQL deverá possuir logs suficientes para diagnóstico operacional.

Não habilitar logs excessivamente detalhados em produção sem necessidade.

---

# 25. NGINX

O NGINX deverá registrar:

```text
requisição
status HTTP
tempo
origem quando necessária
```

---

# 26. Health Check

A API deverá possuir:

```http
GET /health
```

---

# 27. Health básico

O health básico deverá responder se:

```text
aplicação está executando
```

---

# 28. Health detalhado

Quando existir:

```http
GET /health/detalhado
```

poderá verificar dependências.

Exemplo:

```text
API
Banco
```

Não expor detalhes sensíveis.

---

# 29. Health não é monitoramento completo

O endpoint:

```text
/health
```

não substitui monitoramento.

Ele apenas fornece um sinal operacional.

---

# 30. Status do banco

Monitorar:

```text
conectividade
tempo de resposta
erros
```

---

# 31. Status Instagram

A Área Administrativa deverá conseguir identificar:

```text
conta conectada
reautenticação necessária
erro
desconectada
```

---

# 32. Status IA

Monitorar:

```text
execuções
sucessos
erros
tempo
```

---

# 33. Status de publicação

Monitorar estados como:

```text
PENDENTE
PROCESSANDO
PUBLICADA
ERRO
CANCELADA
```

conforme o modelo definido para publicação.

---

# 34. Processamentos pendentes

O sistema deverá conseguir identificar operações que ficaram presas em:

```text
PROCESSANDO
```

por tempo anormal.

---

# 35. Timeout operacional

Toda operação externa deverá possuir limite de tempo.

---

# 36. Operação presa

Quando uma operação exceder o tempo esperado:

```text
identificar
 ↓
registrar warning/error
 ↓
executar recuperação apropriada
```

---

# 37. Retry

Retries deverão ser registrados.

Exemplo:

```text
RETRY_PUBLICACAO
```

---

# 38. Retry infinito

Nunca permitir retry infinito.

---

# 39. Backoff

Retries poderão utilizar:

```text
espera crescente
```

quando apropriado.

---

# 40. Falhas permanentes

Erros como:

```text
permissão negada
credencial inválida
conteúdo inválido
```

não deverão gerar retry automático infinito.

---

# 41. Métricas básicas

O sistema deverá acompanhar, quando possível:

```text
requisições
erros
tempo de resposta
execuções IA
publicações
falhas
```

---

# 42. Métricas da API

Exemplos:

```text
requisições por minuto
erros por minuto
latência
```

---

# 43. Métricas da IA

Exemplos:

```text
quantidade de execuções
tempo médio
taxa de erro
tokens
custo estimado
```

---

# 44. Métricas do Instagram

Exemplos:

```text
publicações solicitadas
publicações concluídas
falhas
reauthenticações
```

---

# 45. Métricas do banco

Acompanhar:

```text
conexões
tempo de consultas
erros
tamanho
```

---

# 46. Métricas da VPS

Acompanhar:

```text
CPU
RAM
disco
rede
```

---

# 47. CPU

Alertar somente quando houver utilização anormal sustentada.

Evitar alertas por picos curtos sem impacto.

---

# 48. Memória

Acompanhar:

```text
RAM
swap
```

quando aplicável.

---

# 49. Disco

O sistema deverá detectar:

```text
disco próximo da capacidade
```

antes de chegar a:

```text
100%
```

---

# 50. Banco cheio

O crescimento do banco deverá ser acompanhado.

---

# 51. Logs cheios

A rotação de logs deverá impedir que logs ocupem todo o disco.

---

# 52. Disponibilidade

O MVP poderá possuir um monitoramento externo simples que verifique:

```text
HTTPS
health
```

em intervalos regulares.

---

# 53. Não monitorar excessivamente

No MVP não é necessário monitorar centenas de indicadores.

Monitorar o que permite tomar decisão.

---

# 54. Alertas

Alertas deverão ser acionados somente quando houver ação necessária.

Exemplos:

```text
API fora do ar
banco indisponível
disco crítico
erro de publicação persistente
```

---

# 55. Evitar alertas inúteis

Não criar alerta para:

```text
qualquer warning
qualquer retry
qualquer pico de CPU
```

sem impacto real.

---

# 56. Severidade

Os alertas poderão utilizar:

```text
INFO
WARNING
ERROR
CRITICAL
```

---

# 57. Incidente

Um incidente ocorre quando uma falha impacta:

```text
disponibilidade
funcionalidade
dados
segurança
publicação
```

---

# 58. Fluxo de incidente

```text
DETECTAR
   ↓
CLASSIFICAR
   ↓
CONTER
   ↓
DIAGNOSTICAR
   ↓
CORRIGIR
   ↓
VALIDAR
   ↓
REGISTRAR
```

---

# 59. Classificação

### P0 — crítico

Sistema indisponível ou risco grave de dados/segurança.

### P1 — alto

Funcionalidade crítica indisponível.

### P2 — médio

Problema relevante com alternativa operacional.

### P3 — baixo

Problema sem impacto significativo.

---

# 60. P0

Exemplos:

```text
API completamente fora do ar
banco perdido
vazamento de credenciais
acesso indevido generalizado
```

---

# 61. P1

Exemplos:

```text
publicação indisponível
login indisponível
IA indisponível para todos
```

---

# 62. P2

Exemplos:

```text
métricas atrasadas
determinada integração instável
funcionalidade secundária indisponível
```

---

# 63. P3

Exemplos:

```text
erro visual
mensagem inadequada
problema não crítico
```

---

# 64. Contenção

A primeira prioridade de um incidente grave é:

```text
impedir que o problema aumente
```

---

# 65. Exemplo

Se uma chave de IA estiver comprometida:

```text
revogar chave
```

antes de investigar detalhes secundários.

---

# 66. Evidências

Durante incidente, preservar:

```text
logs
correlation_id
horários
status
erros
versão
```

---

# 67. Não apagar logs

Não apagar evidências para:

```text
"limpar o erro"
```

antes da investigação.

---

# 68. Causa raiz

Após correção, identificar:

```text
causa
```

quando possível.

---

# 69. Causa raiz não é culpado

O objetivo é corrigir:

```text
processo
código
configuração
infraestrutura
```

e não procurar culpados.

---

# 70. Pós-incidente

Para incidentes relevantes:

```text
o que aconteceu?
por que aconteceu?
como foi detectado?
como foi corrigido?
como evitar repetição?
```

---

# 71. Registro de incidente

Poderá conter:

```text
incidente_id
data
hora
severidade
impacto
causa
ação
resultado
```

---

# 72. Tempo de detecção

Futuramente acompanhar:

```text
MTTD
```

---

# 73. Tempo de recuperação

Futuramente acompanhar:

```text
MTTR
```

---

# 74. MVP

Não é necessário montar uma operação formal de SRE no início.

Basta possuir:

```text
logs
health
backup
monitoramento básico
procedimento de recuperação
```

---

# 75. Backup

Incidentes envolvendo banco deverão considerar:

```text
backup
restauração
```

conforme:

```text
40_INFRAESTRUTURA_LOCAL_E_VPS.md
```

---

# 76. Segurança

Incidentes de segurança deverão seguir:

```text
44_PRIVACIDADE_LGPD_E_PROTECAO_DE_DADOS.md
```

---

# 77. Desenvolvimento

Alterações deverão seguir:

```text
42_PADRAO_DE_DESENVOLVIMENTO_E_QUALIDADE_DE_CODIGO.md
```

---

# 78. Deploy

Falhas após publicação deverão seguir:

```text
43_FLUXO_DE_DESENVOLVIMENTO_GIT_E_DEPLOY.md
```

---

# 79. Testes

Correções de incidentes deverão criar testes quando possível.

Fluxo:

```text
incidente
 ↓
correção
 ↓
teste que reproduz o problema
 ↓
teste passa
```

---

# 80. Regra contra regressão

Uma falha importante corrigida deverá, sempre que possível, ganhar um teste de regressão.

---

# 81. Monitoramento da IA

Se a taxa de erro aumentar:

```text
detectar
 ↓
identificar modelo/provedor
 ↓
verificar custo
 ↓
verificar latência
 ↓
avaliar fallback
```

---

# 82. Monitoramento Instagram

Se falhas aumentarem:

```text
verificar credencial
verificar permissão
verificar API
verificar rate limit
verificar indisponibilidade externa
```

---

# 83. Monitoramento de publicação

Uma publicação não deverá permanecer indefinidamente sem estado conhecido.

---

# 84. Reconciliação

Quando houver dúvida sobre o estado externo:

```text
ESTADO DESCONHECIDO
```

poderá ser utilizado até que uma consulta/reconciliação determine o resultado.

---

# 85. Dados inconsistentes

Se houver:

```text
banco = PUBLICADA
Instagram = não publicada
```

ou o contrário:

```text
registrar incidente
```

e investigar a origem.

---

# 86. Alertas de publicação

Poderão ser considerados:

```text
muitas falhas consecutivas
muitas publicações presas
taxa de erro acima do limite
```

---

# 87. Alertas de IA

Poderão ser considerados:

```text
taxa de erro elevada
latência elevada
custo anormal
```

---

# 88. Alertas de infraestrutura

Poderão ser considerados:

```text
CPU sustentada
RAM crítica
disco crítico
API indisponível
```

---

# 89. Limites

Os limites dos alertas deverão ser definidos com base em comportamento real.

Não escolher dezenas de números arbitrários no início.

---

# 90. Dashboard administrativo

A Área Administrativa deverá futuramente exibir sinais básicos:

```text
saúde da API
saúde do banco
integrações
publicações
IA
erros recentes
```

---

# 91. Dashboard não substitui logs

O dashboard mostra:

```text
o que está acontecendo
```

Os logs ajudam a descobrir:

```text
por que aconteceu
```

---

# 92. Diagnóstico

Uma falha deverá ser rastreável por:

```text
data/hora
correlation_id
usuário quando necessário
recurso
operação
serviço
```

---

# 93. Exemplo de investigação

```text
Usuário informa:
"não consegui publicar"

        ↓

localizar publicacao_id

        ↓

localizar correlation_id

        ↓

consultar logs

        ↓

identificar conector Instagram

        ↓

identificar erro

        ↓

corrigir
```

---

# 94. Logs e privacidade

O diagnóstico não deverá justificar coleta indiscriminada de dados pessoais.

---

# 95. Retenção de logs

Logs deverão possuir política de retenção.

---

# 96. Rotação

Utilizar rotação para evitar:

```text
crescimento infinito
```

---

# 97. Acesso aos logs

Acesso deverá ser restrito a pessoas autorizadas.

---

# 98. Produção

Logs de produção não deverão ser tratados como:

```text
dados públicos
```

---

# 99. Ambiente local

No ambiente local poderá existir maior detalhamento, desde que não haja exposição de segredos.

---

# 100. Ambiente de produção

Produção deverá priorizar:

```text
segurança
sinal
diagnóstico
baixo ruído
```

---

# 101. Regra para agentes de IA

Ao investigar um erro:

1. localizar correlation_id;
2. localizar entidade relacionada;
3. verificar logs;
4. verificar estado no banco;
5. verificar integração externa;
6. verificar versão implantada;
7. reproduzir em ambiente seguro;
8. corrigir;
9. criar teste;
10. validar produção.

---

# 102. Regra contra apagar sintomas

Não resolver um incidente simplesmente escondendo:

```text
erro
warning
log
```

sem corrigir a causa.

---

# 103. Regra contra alertas falsos

Não criar alertas que gerem:

```text
fadiga de alerta
```

---

# 104. Regra contra observabilidade excessiva

Não registrar tudo.

Registrar o necessário para:

```text
operar
diagnosticar
proteger
```

---

# 105. Critério de sucesso

A observabilidade estará adequada quando:

```text
sabemos se a aplicação está no ar
+
sabemos se o banco está acessível
+
sabemos se integrações críticas estão funcionando
+
conseguimos localizar uma falha
+
conseguimos identificar a operação afetada
+
temos logs seguros
+
temos procedimento de incidente
+
temos backup
```

---

# 106. Arquitetura resumida

```text
                    VIRALCODE
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       FRONTEND       FASTAPI       MYSQL
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                      LOGS
                        │
                ┌───────┴───────┐
                ▼               ▼
           MONITORAMENTO     ALERTAS
                │
                ▼
           ADMINISTRAÇÃO
```

---

# 107. Evolução futura

Quando houver escala:

```text
APLICAÇÃO
   ↓
LOGS
   ↓
COLETA CENTRAL
   ↓
MÉTRICAS
   ↓
TRACING
   ↓
DASHBOARD
   ↓
ALERTAS
```

---

# 108. Regra final

> **Se o ViralCode não consegue explicar onde uma operação falhou, ele ainda não está pronto para crescer.**

A observabilidade deverá evoluir junto com o produto, mas sem transformar o MVP em uma plataforma de infraestrutura complexa antes da necessidade existir.

**Versão:** 1.0  
**Status:** Documento oficial de Observabilidade, Monitoramento e Tratamento de Incidentes
