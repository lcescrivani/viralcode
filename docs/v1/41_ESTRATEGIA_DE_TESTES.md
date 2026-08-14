# 41 — ESTRATÉGIA DE TESTES

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define a estratégia de testes do ViralCode.

O objetivo não é testar tudo de forma indiscriminada.

O objetivo é garantir que:

```text
regras críticas
+
fluxos principais
+
integrações
+
segurança
```

funcionem de forma previsível.

---

# 2. Princípio fundamental

A estratégia será baseada em risco.

Quanto mais crítica uma funcionalidade:

```text
maior cobertura
+
maior isolamento
+
maior quantidade de cenários
```

---

# 3. Pirâmide de testes

A arquitetura deverá priorizar:

```text
             TESTES E2E
                ▲
               / \
              /   \
        TESTES INTEGRAÇÃO
            /       \
           /         \
      TESTES UNITÁRIOS
```

A maior quantidade deverá estar nos testes unitários.

---

# 4. Tipos de teste

O projeto deverá considerar:

```text
teste unitário
teste de integração
teste de contrato
teste de segurança
teste de API
teste frontend
teste E2E
teste de integração externa
```

---

# 5. Teste unitário

Testa uma unidade isoladamente.

Exemplos:

```text
regra de negócio
validador
normalizador
serviço
função
```

---

# 6. Teste de integração

Testa componentes trabalhando juntos.

Exemplo:

```text
FastAPI
+
Serviço
+
MySQL
```

---

# 7. Teste de contrato

Garante que:

```text
React
```

e:

```text
FastAPI
```

continuem obedecendo ao contrato definido.

---

# 8. Teste de API

Testa endpoints reais do backend.

Exemplos:

```text
POST /login
GET /conteudos
POST /conteudos
POST /publicacoes
```

---

# 9. Teste de segurança

Testa principalmente:

```text
autenticação
autorização
isolamento de dados
segredos
IDOR
```

---

# 10. Teste E2E

Simula o usuário real.

Exemplo:

```text
login
 ↓
perfil
 ↓
Instagram
 ↓
conteúdo
 ↓
análise
 ↓
criação
 ↓
aprovação
```

---

# 11. Integrações externas

Instagram e provedor de IA não deverão ser chamados em toda execução da suíte.

Preferir:

```text
mock
stub
sandbox
conta de teste
```

quando disponíveis.

---

# 12. Regra principal do MVP

O MVP deverá possuir testes suficientes para proteger:

```text
login
usuário
perfil
Instagram
conteúdo
análise
IA
publicação
admin
```

---

# 13. Backend

Os testes do backend deverão cobrir:

```text
rotas
serviços
regras
repositórios
integrações
erros
```

---

# 14. Frontend

Os testes do React deverão cobrir:

```text
componentes críticos
serviços de API
navegação
autenticação
fluxos principais
```

---

# 15. Banco de dados

Os testes de banco deverão verificar:

```text
criação
leitura
atualização
exclusão
relacionamentos
restrições
migrações
```

---

# 16. Testes unitários prioritários

### P0

```text
autenticação
autorização
propriedade de recurso
validação
normalização
regras de publicação
seleção de conteúdo
```

---

# 17. Testes de autenticação

Devem verificar:

```text
cadastro válido
cadastro inválido
login válido
senha incorreta
usuário inexistente
usuário bloqueado
sessão inválida
sessão expirada
```

---

# 18. Testes de autorização

Devem verificar:

```text
usuário acessa próprio recurso
usuário não acessa recurso de outro
admin acessa admin
usuário comum não acessa admin
```

---

# 19. Teste crítico de IDOR

Exemplo:

```text
Usuário A possui conteúdo 100.

Usuário B tenta:

GET /api/v1/conteudos/100
```

Resultado esperado:

```text
acesso negado
```

Esse teste é obrigatório.

---

# 20. Testes de perfil

Verificar:

```text
criar
editar
consultar
selecionar
```

e isolamento entre usuários.

---

# 21. Testes da conta Instagram

Verificar:

```text
conexão
callback
state
identificação
desconexão
credencial inválida
reautenticação
```

---

# 22. Não testar OAuth somente com lógica

O teste deverá verificar o comportamento do sistema.

Não basta testar uma função isolada que diga:

```text
state == state
```

Também testar o fluxo da API.

---

# 23. Testes de conteúdo

Verificar:

```text
criação
edição
listagem
filtros
status
propriedade
```

---

# 24. Testes de análise

Verificar:

```text
solicitação
contexto
execução
resultado
persistência
erro
```

---

# 25. Testes de geração

Verificar:

```text
perfil
nicho
objetivo
contexto
prompt
resposta
validação
persistência
```

---

# 26. Testes de saída da IA

A IA deverá ser tratada como uma dependência não determinística.

Os testes deverão validar principalmente:

```text
estrutura
campos obrigatórios
tipos
regras
```

e não exigir que o texto seja exatamente igual em todas as execuções.

---

# 27. Exemplo

Não exigir:

```text
hook == "Você está destruindo seu casamento..."
```

como única resposta válida.

Preferir:

```text
hook existe
+
não está vazio
+
possui tamanho permitido
```

---

# 28. Testes de prompt

Quando um prompt mudar:

```text
executar conjunto de casos representativos
```

para verificar regressão.

---

# 29. Testes de publicação

Devem verificar:

```text
conteúdo aprovado
conta conectada
credencial válida
publicação solicitada
sucesso
erro
retry
duplicidade
```

---

# 30. Idempotência

Teste obrigatório:

```text
mesma solicitação
+
mesma chave de idempotência
```

não deverá produzir duas publicações.

---

# 31. Timeout

Simular:

```text
Instagram demora
```

e verificar que o sistema:

```text
não trava indefinidamente
```

---

# 32. Retry

Verificar que:

```text
erro temporário
```

pode ser repetido quando apropriado.

E:

```text
erro permanente
```

não gera retry infinito.

---

# 33. Rate limit

Simular resposta equivalente a:

```text
429
```

e verificar comportamento.

---

# 34. Testes de métricas

Verificar:

```text
importação
normalização
atualização
histórico
duplicidade
```

quando a funcionalidade estiver implementada.

---

# 35. Testes de descoberta

Verificar:

```text
nicho
filtros
paginação
deduplicação
ranking
```

---

# 36. Teste de limite de visualizações

Se o motor receber:

```text
limite = 1.000.000
```

verificar:

```text
conteúdo >= 1.000.000 → elegível
conteúdo < 1.000.000 → não elegível
```

Somente quando a métrica estiver oficialmente disponível para aquela fonte.

---

# 37. Testes de normalização

Uma mesma estrutura externa deverá ser convertida corretamente para o modelo interno.

Exemplo:

```text
Instagram
 ↓
Normalizador
 ↓
Conteudo
```

---

# 38. Testes de deduplicação

Se o mesmo conteúdo externo aparecer duas vezes:

```text
não criar dois registros
```

---

# 39. Testes de API

Todos os endpoints críticos deverão possuir testes.

---

# 40. Status HTTP

Testar pelo menos:

```text
200
201
202
400
401
403
404
409
422
429
500
```

quando aplicável.

---

# 41. Erros padronizados

Verificar se a API respeita:

```text
formato de erro
código
mensagem
correlation_id
```

conforme o contrato da API.

---

# 42. Paginação

Testar:

```text
primeira página
página intermediária
última página
sem resultados
limite inválido
```

---

# 43. Filtros

Testar:

```text
filtro único
múltiplos filtros
filtro inexistente
filtro inválido
```

---

# 44. Ordenação

Testar:

```text
campo válido
direção válida
campo inválido
```

---

# 45. Testes de banco

Utilizar banco isolado para testes.

Não executar a suíte diretamente sobre:

```text
banco de produção
```

---

# 46. Dados de teste

Os dados de teste deverão ser controlados.

Evitar depender de:

```text
dados reais
```

quando não necessário.

---

# 47. Fixtures

Criar dados reutilizáveis para:

```text
usuário
perfil
conta Instagram
conteúdo
publicação
análise
```

---

# 48. Limpeza

Cada teste deverá evitar deixar lixo que interfira nos testes seguintes.

---

# 49. Testes de migração

As migrações deverão ser testadas em ambiente controlado.

---

# 50. Testes do frontend

Priorizar:

```text
Login
Dashboard
Perfil
Instagram
Conteúdos
Criação
Publicação
Admin
```

---

# 51. Teste de login frontend

Verificar:

```text
login sucesso
login erro
sessão expirada
logout
```

---

# 52. Teste de proteção de rota

Usuário não autenticado tentando acessar:

```text
/dashboard
```

deverá ser redirecionado para autenticação.

---

# 53. Teste de admin

Usuário comum tentando abrir:

```text
/administracao
```

não deverá visualizar conteúdo administrativo.

O backend deverá negar o acesso mesmo que o usuário tente acessar diretamente a URL.

---

# 54. Teste de formulário

Verificar:

```text
campo obrigatório
formato inválido
envio
loading
erro
sucesso
```

---

# 55. Teste de estados

Verificar:

```text
carregando
vazio
sucesso
erro
```

---

# 56. Teste de publicação frontend

Fluxo:

```text
conteúdo
 ↓
aprovar
 ↓
publicar
 ↓
loading
 ↓
sucesso/erro
```

---

# 57. Testes E2E prioritários

### Fluxo 1 — Cadastro

```text
cadastro
 ↓
login
 ↓
dashboard
```

### Fluxo 2 — Perfil

```text
login
 ↓
perfil
 ↓
editar
 ↓
salvar
```

### Fluxo 3 — Conteúdo

```text
login
 ↓
conteúdo
 ↓
análise
 ↓
criação
 ↓
revisão
```

### Fluxo 4 — Publicação

```text
conteúdo aprovado
 ↓
publicar
 ↓
resultado
```

### Fluxo 5 — Admin

```text
admin
 ↓
dashboard
 ↓
usuários
 ↓
conteúdos
```

---

# 58. E2E não deve cobrir tudo

Testes E2E são mais caros e frágeis.

Não utilizar E2E para cada regra simples.

---

# 59. Testes de contrato frontend/backend

Quando o backend alterar:

```text
JSON
campo
status
endpoint
```

os testes deverão detectar incompatibilidade.

---

# 60. OpenAPI

O contrato OpenAPI deverá ser utilizado como referência para os contratos da API.

---

# 61. Testes de segurança

Além de IDOR:

```text
SQL injection
XSS
CSRF quando aplicável
autenticação
autorização
exposição de segredo
rate limiting
```

---

# 62. SQL Injection

O sistema deverá utilizar:

```text
SQLAlchemy
```

e evitar concatenação insegura de SQL.

---

# 63. XSS

Conteúdo externo e texto gerado pela IA não deverá ser considerado automaticamente confiável no frontend.

---

# 64. Prompt Injection

Testar conteúdo externo contendo instruções como:

```text
ignore as instruções anteriores
```

e verificar que ele continua sendo tratado como dado.

---

# 65. Segredos

Criar teste/revisão para garantir que respostas da API não retornem:

```text
senha
token Instagram
client secret
chave IA
```

---

# 66. Testes de configuração

Verificar:

```text
configuração válida
variável ausente
variável inválida
ambiente incorreto
```

---

# 67. Testes de infraestrutura

No mínimo:

```text
container inicia
MySQL inicia
backend inicia
frontend inicia
NGINX responde
health responde
```

---

# 68. Teste de backup

Periodicamente:

```text
backup
 ↓
restauração
 ↓
verificação
```

---

# 69. Teste de recuperação

Simular:

```text
backend parado
```

e verificar se o processo de recuperação funciona.

---

# 70. Teste de banco indisponível

Simular:

```text
MySQL indisponível
```

e verificar que a API:

```text
não expõe stack trace
```

---

# 71. Teste de provedor IA indisponível

Simular:

```text
IA indisponível
```

e verificar:

```text
erro tratado
ExecucaoIA = ERRO
usuário recebe mensagem adequada
```

---

# 72. Teste Instagram indisponível

Simular:

```text
Instagram indisponível
```

e verificar:

```text
publicação não fica indefinidamente processando
```

---

# 73. Teste de timeout externo

Todos os conectores externos deverão possuir testes de timeout.

---

# 74. Dados sensíveis

Testes não deverão utilizar dados pessoais reais sem necessidade.

---

# 75. Dados de produção

Nunca rodar testes destrutivos contra produção.

---

# 76. Testes antes de deploy

Pipeline mínimo:

```text
lint
 ↓
testes unitários
 ↓
testes integração
 ↓
build
```

---

# 77. Deploy

Somente após:

```text
testes críticos aprovados
```

---

# 78. Smoke test

Após deploy:

```text
health
login
dashboard
```

e os fluxos diretamente afetados pela alteração.

---

# 79. Testes manuais

Nem tudo precisa ser automatizado no primeiro momento.

O MVP poderá utilizar testes manuais documentados para:

```text
OAuth Instagram
publicação real
comportamento visual
integrações externas
```

---

# 80. Checklist manual Instagram

```text
[ ] iniciar conexão
[ ] autorizar
[ ] retornar callback
[ ] identificar conta
[ ] salvar conexão
[ ] visualizar conta
[ ] desconectar
[ ] reconectar
```

---

# 81. Checklist manual publicação

```text
[ ] criar conteúdo
[ ] revisar
[ ] aprovar
[ ] publicar
[ ] verificar status
[ ] verificar Instagram
[ ] verificar histórico
```

---

# 82. Qualidade de IA

A avaliação da IA deverá considerar:

```text
estrutura
relevância
aderência ao perfil
clareza
utilidade
```

---

# 83. Avaliação humana

No MVP, parte importante da avaliação de qualidade deverá ser humana.

---

# 84. Casos de avaliação

Criar exemplos representativos para:

```text
nicho
tema
objetivo
formato
```

---

# 85. Regressão de IA

Quando trocar:

```text
modelo
prompt
temperatura/configuração
contexto
```

executar os casos de avaliação novamente.

---

# 86. Teste de custo

Monitorar se alterações provocam aumento inesperado de:

```text
tokens
tempo
custo
```

---

# 87. Teste de performance

O MVP não precisa de uma suíte de carga complexa.

Mas deverá medir:

```text
tempo de resposta API
tempo de consulta
tempo de geração
```

---

# 88. Teste de carga futuro

Quando houver usuários reais suficientes:

```text
carga
concorrência
fila
limites
```

poderão ser avaliados.

---

# 89. Teste de concorrência

Operações críticas deverão considerar:

```text
duas publicações simultâneas
duas atualizações
duas solicitações de geração
```

---

# 90. Estado consistente

Testar se concorrência não cria:

```text
duplicidade
estado impossível
```

---

# 91. Teste de idempotência geral

Operações que possam ser repetidas deverão possuir estratégia clara.

---

# 92. Teste de auditoria

Verificar se ações administrativas críticas geram registros.

---

# 93. Teste de logs

Verificar que erros possuem:

```text
correlation_id
```

quando aplicável.

---

# 94. Teste de observabilidade

Uma falha deverá poder ser rastreada de:

```text
frontend
 ↓
API
 ↓
serviço
 ↓
conector
```

por meio do identificador de correlação quando disponível.

---

# 95. Níveis de prioridade

Os testes serão classificados:

```text
P0 = crítico
P1 = importante
P2 = complementar
```

---

# 96. P0

Obrigatórios antes de produção:

```text
login
autorização
IDOR
admin
conteúdo
publicação
segredos
health
```

---

# 97. P1

```text
filtros
métricas
descoberta
retry
rate limit
integrações
```

---

# 98. P2

```text
detalhes visuais
otimizações
casos raros
```

---

# 99. Cobertura

Não estabelecer como objetivo único:

```text
100% de cobertura
```

Cobertura de código não significa cobertura de risco.

---

# 100. Objetivo real

O objetivo é:

```text
100% das regras críticas protegidas
```

quando isso for razoavelmente alcançável.

---

# 101. Testes obrigatórios para cada funcionalidade

Toda nova funcionalidade deverá responder:

```text
qual é o comportamento esperado?
qual é o erro?
quem pode acessar?
o que acontece se repetir?
o que acontece se depender de serviço externo?
```

---

# 102. Teste antes de código

Quando possível:

```text
regra
 ↓
teste
 ↓
implementação
```

---

# 103. Regra para agentes de IA

Antes de alterar código:

1. localizar testes existentes;
2. verificar comportamento esperado;
3. alterar código;
4. executar testes relevantes;
5. criar testes se não existirem;
6. verificar regressão;
7. documentar mudanças importantes.

---

# 104. Regra contra apagar testes

Uma IA não deverá remover teste simplesmente porque:

```text
está falhando
```

Primeiro deverá entender:

```text
o código está errado?
ou
o teste está desatualizado?
```

---

# 105. Regra contra mascarar falha

Não alterar teste para:

```text
fazer passar
```

sem confirmar que o comportamento esperado mudou.

---

# 106. Testes locais

O desenvolvedor deverá conseguir executar a suíte localmente.

---

# 107. Comando

O comando definitivo será documentado quando a stack de testes for instalada.

---

# 108. CI/CD futuro

Quando houver pipeline:

```text
commit
 ↓
testes
 ↓
build
 ↓
deploy
```

---

# 109. Falha no pipeline

Se teste P0 falhar:

```text
não promover para produção
```

---

# 110. Critério de aceite

Uma funcionalidade poderá ser considerada pronta quando:

```text
funciona
+
testes críticos existem
+
erros são tratados
+
segurança foi considerada
+
contrato da API está correto
+
não há regressão conhecida
```

---

# 111. Matriz inicial de testes

| Área | Unitário | Integração | E2E | Prioridade |
|---|---:|---:|---:|---|
| Autenticação | Sim | Sim | Sim | P0 |
| Autorização | Sim | Sim | Sim | P0 |
| Usuários | Sim | Sim | Sim | P0 |
| Perfis | Sim | Sim | Sim | P0 |
| Instagram | Sim | Sim | Manual/E2E | P0 |
| Conteúdos | Sim | Sim | Sim | P0 |
| Análises | Sim | Sim | Parcial | P0 |
| IA | Sim | Sim | Parcial | P0 |
| Publicações | Sim | Sim | Sim | P0 |
| Métricas | Sim | Sim | Parcial | P1 |
| Descoberta | Sim | Sim | Parcial | P1 |
| Admin | Sim | Sim | Sim | P0 |
| Infraestrutura | — | Sim | Smoke | P0 |

---

# 112. Arquitetura de testes

```text
                  E2E
                   ▲
                   │
              INTEGRAÇÃO
                   ▲
                   │
               UNITÁRIO
                   │
                   ▼
              CÓDIGO VIRALCODE
```

---

# 113. Regra final

> **Testar o ViralCode não significa testar cada linha. Significa proteger as regras e fluxos que fazem o negócio funcionar.**

No MVP, a prioridade será:

```text
SEGURANÇA
+
AUTENTICAÇÃO
+
DADOS
+
IA
+
INSTAGRAM
+
PUBLICAÇÃO
```

e não uma cobertura artificial de 100%.

**Versão:** 1.0  
**Status:** Documento oficial da Estratégia de Testes
