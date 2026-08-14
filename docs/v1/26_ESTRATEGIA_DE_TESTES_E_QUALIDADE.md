# 26 — ESTRATÉGIA DE TESTES E QUALIDADE

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define como a qualidade do ViralCode será validada durante o desenvolvimento.

O objetivo não é criar uma estrutura de testes complexa para o MVP.

O objetivo é garantir que cada parte importante do sistema:

```text
funcione
+
não quebre o que já funciona
+
possa ser alterada com segurança
```

---

# 2. Princípio fundamental

O teste deverá acompanhar o desenvolvimento.

Não fazer:

```text
desenvolver tudo
   ↓
testar no final
```

Preferir:

```text
desenvolver
   ↓
testar
   ↓
corrigir
   ↓
integrar
```

---

# 3. Pirâmide de testes

A estratégia deverá priorizar:

```text
          TESTES E2E
             ▲
            / \
           /   \
      TESTES DE API
         ▲
        / \
       /   \
 TESTES DE INTEGRAÇÃO
       ▲
      / \
     /   \
TESTES UNITÁRIOS
```

A maior quantidade deverá estar nos testes unitários e de integração.

---

# 4. Tipos de teste

O projeto deverá utilizar:

```text
testes unitários
testes de integração
testes de API
testes de frontend
testes de ponta a ponta
testes de integração externa
```

Nem todos terão a mesma prioridade no MVP.

---

# 5. Testes unitários

Objetivo:

validar uma unidade pequena de código de maneira isolada.

Exemplos:

```text
Serviço de criação
Serviço de descoberta
validador
regra de publicação
cálculo de métricas
```

---

# 6. O que testar unitariamente

Prioridade para:

```text
regras de negócio
validações
transformações
normalização
filtros
ranking
deduplicação
cálculos
```

---

# 7. O que não testar excessivamente

Não criar testes para cada linha trivial.

Exemplo:

```text
getter simples
setter simples
função sem lógica
```

O objetivo é proteger comportamento, não quantidade de testes.

---

# 8. Testes de integração

Validam a interação entre componentes.

Exemplo:

```text
Serviço
   ↓
Repositório
   ↓
MySQL
```

---

# 9. Banco de teste

Os testes de integração deverão utilizar banco separado.

Nunca utilizar:

```text
produção
```

---

# 10. Testes de API

Validam o contrato:

```text
HTTP
 ↓
FastAPI
 ↓
Serviço
```

Deverão verificar:

```text
status HTTP
resposta
validação
autenticação
autorização
erros
```

---

# 11. Testes de autenticação

Obrigatórios:

```text
cadastro correto
cadastro duplicado
login correto
senha incorreta
usuário inexistente
token ausente
token inválido
token expirado
usuário bloqueado
```

---

# 12. Teste de isolamento

Obrigatório no MVP.

Cenário:

```text
Usuário A
   ↓
Perfil A

Usuário B
   ↓
Perfil B
```

Usuário A tentando acessar Perfil B:

```text
ACESSO NEGADO
```

Esse teste deverá existir para os principais recursos.

---

# 13. Recursos que devem possuir teste de isolamento

No mínimo:

```text
perfil
conta social
conteúdo
planejamento
publicação
métricas
aprendizado
```

---

# 14. Testes de descoberta

Testar:

```text
critérios válidos
critérios inválidos
nenhum resultado
resultados duplicados
métrica ausente
filtro de visualizações
paginação
erro do Instagram
conta desconectada
```

---

# 15. Teste de descoberta com métrica ausente

Regra:

```text
visualizacoes = NULL
```

deverá permanecer diferente de:

```text
visualizacoes = 0
```

---

# 16. Teste de deduplicação

Exemplo:

```text
resultado hashtag
+
resultado conta
```

contendo o mesmo conteúdo.

Resultado esperado:

```text
1 conteúdo
```

---

# 17. Testes de análise

Testar:

```text
conteúdo válido
conteúdo inexistente
IA disponível
IA indisponível
resposta inválida da IA
timeout
erro do provedor
```

---

# 18. Testes de criação

Testar:

```text
perfil válido
nicho válido
aprendizados disponíveis
sem aprendizados
IA funcionando
IA falhando
resposta incompleta
```

---

# 19. Teste de originalidade

O teste não deverá tentar provar criatividade de forma automática.

Deverá garantir que o fluxo de criação utilize:

```text
padrões
insights
aprendizados
```

como contexto, em vez de simplesmente copiar um conteúdo externo.

---

# 20. Testes de aprovação

Testar:

```text
conteúdo pendente
aprovação
rejeição
aprovação duplicada
conteúdo inexistente
usuário sem acesso
```

---

# 21. Testes de publicação

São críticos.

Testar:

```text
conteúdo aprovado
conteúdo não aprovado
conta conectada
conta desconectada
erro Instagram
timeout
duplicidade
tentativa repetida
```

---

# 22. Regra de publicação

Deverá existir teste garantindo:

```text
conteúdo NÃO aprovado
        ↓
tentativa de publicação
        ↓
BLOQUEADA
```

---

# 23. Teste de idempotência

Cenário:

```text
usuário solicita publicação
        ↓
requisição enviada duas vezes
```

Resultado esperado:

```text
não criar duas publicações indevidas
```

---

# 24. Testes de métricas

Testar:

```text
coleta correta
métrica inexistente
métrica igual a zero
métrica desconhecida
histórico
duplicidade
erro Instagram
```

---

# 25. Teste de histórico

Exemplo:

```text
10:00 → 10.000
14:00 → 20.000
18:00 → 40.000
```

O sistema deverá preservar os três registros quando forem medições distintas.

---

# 26. Testes de aprendizado

Testar:

```text
dados insuficientes
dados suficientes
evidências
confiança
atualização
duplicação
```

---

# 27. Regra de evidência

Um aprendizado deverá conseguir apontar para suas evidências.

Teste:

```text
aprendizado
   ↓
evidência
   ↓
conteúdo/publicação/métrica
```

---

# 28. Testes de IA

A IA real não deverá ser necessária em todos os testes.

Utilizar:

```text
ProvedorIAFalso
```

para testes determinísticos.

---

# 29. Exemplo de provedor falso

```text
ServicoCriacao
      ↓
ProvedorIAFalso
      ↓
resposta conhecida
```

Isso permite testar o serviço sem custo e sem depender da internet.

---

# 30. Testes do Instagram

O conector real deverá possuir testes específicos.

Mas a maior parte do sistema deverá utilizar:

```text
ConectorInstagramFalso
```

ou mocks.

---

# 31. Teste real do Instagram

Além dos testes automatizados, deverá existir uma rotina de validação real.

Exemplo:

```text
conta de desenvolvimento
      ↓
login
      ↓
consulta
      ↓
publicação de teste
      ↓
métrica
```

A frequência dessa validação deverá ser definida conforme mudanças da plataforma.

---

# 32. Testes de contrato

Os contratos definidos em:

```text
20_CONTRATOS_DA_API.md
```

deverão ser protegidos por testes.

Se a API mudar:

```text
teste quebra
      ↓
mudança analisada
      ↓
contrato atualizado conscientemente
```

---

# 33. Testes do frontend

Priorizar os fluxos críticos:

```text
login
dashboard
conectar Instagram
descoberta
análise
criação
aprovação
publicação
desempenho
```

---

# 34. Testes de componentes

Componentes reutilizáveis importantes deverão ser testados.

Exemplos:

```text
Botao
CampoTexto
Modal
Tabela
CartaoConteudo
CartaoMetrica
```

Não é necessário testar visualmente cada componente simples no primeiro momento.

---

# 35. Testes de ponta a ponta

O MVP deverá possuir pelo menos um fluxo completo:

```text
login
 ↓
perfil
 ↓
conta social
 ↓
conteúdo
 ↓
análise
 ↓
criação
 ↓
aprovação
```

A publicação real poderá ser incluída quando a integração estiver validada.

---

# 36. Ambiente E2E

Os testes de ponta a ponta deverão utilizar ambiente controlado.

Evitar depender de:

```text
Instagram real
IA real
dados de produção
```

para todos os testes E2E.

---

# 37. Dados de teste

Criar dados controlados para:

```text
usuários
perfis
conteúdos
publicações
métricas
aprendizados
```

---

# 38. Fixtures

Poderão existir dados reutilizáveis para:

```text
usuário válido
perfil válido
conteúdo válido
conta Instagram simulada
publicação simulada
```

---

# 39. Testes negativos

Não testar somente o caminho feliz.

Para cada funcionalidade importante, considerar:

```text
entrada inválida
recurso inexistente
sem permissão
dependência indisponível
duplicidade
timeout
```

---

# 40. Testes de segurança

No MVP, validar principalmente:

```text
autenticação
autorização
isolamento
segredos
entrada inválida
```

---

# 41. Injeção

As consultas ao banco deverão utilizar mecanismos seguros do SQLAlchemy.

Não construir SQL com concatenação insegura de entrada do usuário.

---

# 42. Entrada do usuário

Validar:

```text
tipo
tamanho
formato
valores permitidos
```

---

# 43. Testes de configuração

Testar:

```text
configuração válida
variável obrigatória ausente
URL inválida
porta inválida
credencial ausente
```

---

# 44. Testes de migração

Cada alteração importante do modelo deverá ser validada.

Fluxo:

```text
banco anterior
 ↓
migração
 ↓
banco novo
```

---

# 45. Teste de migração limpa

Também deverá ser possível:

```text
banco vazio
 ↓
todas as migrações
 ↓
estrutura final
```

---

# 46. Teste de migração incremental

Deverá ser possível evoluir:

```text
versão N
 ↓
versão N+1
```

sem perder dados quando a migração não for destrutiva.

---

# 47. Qualidade do código

Além dos testes, utilizar ferramentas de qualidade para:

```text
formatação
lint
tipagem quando aplicável
detecção de problemas
```

---

# 48. Backend

A rotina de qualidade deverá considerar:

```text
formatador Python
lint Python
verificação de tipos quando adotada
testes
```

As ferramentas definitivas serão escolhidas durante a implementação.

---

# 49. Frontend

Considerar:

```text
formatador
lint
TypeScript
testes
build
```

---

# 50. Build

O projeto deverá validar que:

```text
backend inicia
frontend compila
```

antes de considerar uma alteração pronta.

---

# 51. Definition of Done

Uma funcionalidade será considerada pronta quando:

```text
[ ] código implementado
[ ] regra de negócio validada
[ ] testes criados
[ ] testes passando
[ ] lint/formatação
[ ] tratamento de erro
[ ] contrato atualizado
[ ] documentação atualizada quando necessário
```

---

# 52. Pull Request

Quando houver colaboração por Git, o PR deverá informar:

```text
objetivo
alterações
testes executados
impacto
```

---

# 53. Testes antes do commit

Sempre que possível:

```text
formatar
 ↓
lint
 ↓
testes
```

---

# 54. Testes antes do deploy

Obrigatório:

```text
testes automatizados
 ↓
build
 ↓
deploy
```

---

# 55. Teste pós-deploy

Depois do deploy:

```text
health check
 ↓
login
 ↓
endpoint crítico
```

deverão ser validados.

---

# 56. Smoke test

O smoke test mínimo deverá verificar:

```text
API responde
Banco conecta
Frontend abre
Login funciona
```

---

# 57. Teste de regressão

Quando um bug for corrigido, criar um teste que reproduza o problema sempre que possível.

Fluxo:

```text
bug
 ↓
teste reproduz
 ↓
correção
 ↓
teste passa
```

---

# 58. Regra contra regressão

Nenhuma correção crítica deverá depender somente de:

```text
"testei manualmente"
```

quando for possível automatizar.

---

# 59. Testes de performance

No MVP, não é necessário criar uma suíte completa de carga.

Porém, acompanhar:

```text
tempo de resposta
tempo de geração
tempo de descoberta
tempo de publicação
```

---

# 60. Performance futura

Quando houver usuários suficientes:

```text
teste de carga
teste de estresse
teste de concorrência
```

poderão ser adicionados.

---

# 61. Testes de disponibilidade

Não é necessário criar alta disponibilidade no MVP.

A infraestrutura deverá possuir:

```text
health check
reinício
backup
```

---

# 62. Testes de backup

Periodicamente:

```text
criar backup
 ↓
restaurar
 ↓
validar banco
```

---

# 63. Testes de recuperação

Quando houver ambiente de produção, testar:

```text
falha do backend
falha do MySQL
falha da integração
restauração do backup
```

---

# 64. Falha do Instagram

O sistema deverá permanecer utilizável quando o Instagram estiver indisponível.

Exemplo:

```text
Instagram fora do ar
       ↓
criação de conteúdo
       ↓
continua funcionando
```

Quando uma operação depender do Instagram:

```text
erro controlado
```

---

# 65. Falha da IA

Da mesma forma:

```text
IA indisponível
       ↓
erro controlado
       ↓
conteúdo existente preservado
```

---

# 66. Falha do banco

Se o banco estiver indisponível:

```text
erro controlado
```

Não mascarar a falha como sucesso.

---

# 67. Observabilidade durante testes

Erros de teste deverão possuir contexto suficiente para diagnóstico.

Utilizar:

```text
correlation_id
logs
mensagem de erro
```

sem expor segredos.

---

# 68. Cobertura

Não definir inicialmente uma meta artificial como:

```text
100% de cobertura
```

Priorizar cobertura das regras críticas.

---

# 69. Prioridade de cobertura

### P0

```text
autenticação
autorização
isolamento
publicação
descoberta
criação
```

### P1

```text
análise
métricas
aprendizado
planejamento
```

### P2

```text
funcionalidades administrativas
recursos secundários
```

---

# 70. Regra de qualidade

Um teste que não protege comportamento relevante não deve existir apenas para aumentar cobertura.

---

# 71. Organização dos testes

Backend:

```text
backend/testes/
├── unitarios/
├── integracao/
└── api/
```

Frontend:

```text
frontend/testes/
```

---

# 72. Nomenclatura

Os nomes dos testes deverão explicar o comportamento.

Exemplo:

```text
test_usuario_nao_pode_acessar_perfil_de_outro_usuario
```

Preferir nomes descritivos.

---

# 73. Testes e documentação

Quando uma regra importante for criada:

```text
documentação
+
teste
+
código
```

deverão representar a mesma decisão.

---

# 74. Regra para agentes de IA

Antes de alterar código:

1. localizar testes existentes;
2. entender a regra protegida;
3. modificar o menor conjunto possível;
4. adicionar teste para comportamento novo;
5. executar testes relacionados;
6. executar suíte completa quando necessário;
7. atualizar documentação se houver mudança arquitetural.

---

# 75. Regra contra apagar testes

Uma IA não deverá apagar um teste somente porque ele está falhando.

Primeiro deverá determinar:

```text
o código está errado?
ou
o teste está desatualizado?
```

Somente depois decidir.

---

# 76. Testes como documentação

Os testes deverão ajudar a responder:

```text
Como este módulo deve funcionar?
```

Por isso, deverão ser claros e pequenos.

---

# 77. Critério de sucesso

A estratégia de testes estará funcionando quando for possível alterar o sistema e receber rapidamente sinais de:

```text
erro de regra
erro de contrato
erro de integração
erro de segurança
regressão
```

---

# 78. Pipeline mínimo

Mesmo sem CI/CD completo, o fluxo deverá ser:

```text
ALTERAÇÃO
   ↓
FORMATAR
   ↓
LINT
   ↓
TESTES
   ↓
BUILD
   ↓
REVISÃO
   ↓
DEPLOY
```

---

# 79. Evolução

Futuramente poderão ser adicionados:

```text
CI/CD
cobertura automatizada
testes de carga
testes de segurança automatizados
testes E2E completos
monitoramento contínuo
```

---

# 80. Não antecipar complexidade

No MVP não criar:

```text
infraestrutura de testes distribuída
laboratório de performance
pipeline extremamente complexo
testes de carga contínuos
```

sem necessidade.

---

# 81. Regra final

> **Qualidade no ViralCode significa proteger o comportamento que gera valor para o usuário, sem transformar o MVP em um projeto de testes maior que o próprio produto.**

A prioridade será:

```text
SEGURANÇA
   ↓
CORREÇÃO
   ↓
INTEGRAÇÃO
   ↓
REGRESSÃO
   ↓
PERFORMANCE
```

E não:

```text
quantidade de testes
```

**Versão:** 1.0  
**Status:** Documento oficial da Estratégia de Testes e Qualidade
