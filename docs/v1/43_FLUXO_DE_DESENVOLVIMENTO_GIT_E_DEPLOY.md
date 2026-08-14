# 43 — FLUXO DE DESENVOLVIMENTO, GIT E DEPLOY

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define o fluxo operacional para transformar uma alteração de código em uma versão executável do ViralCode.

O fluxo oficial será:

```text
DOCUMENTAÇÃO
     ↓
TAREFA
     ↓
DESENVOLVIMENTO LOCAL
     ↓
TESTES
     ↓
GIT
     ↓
BUILD
     ↓
DEPLOY
     ↓
VALIDAÇÃO
```

---

# 2. Princípio fundamental

Nenhuma alteração deverá ir diretamente para produção sem passar por:

```text
desenvolvimento
+
validação
+
testes
```

---

# 3. Fonte oficial do código

O código deverá permanecer versionado em:

```text
Git
```

O repositório será a fonte oficial do código-fonte.

---

# 4. Documentação

Antes de implementar uma funcionalidade, consultar os documentos relevantes em:

```text
docs/
```

---

# 5. Tarefa

Toda alteração deverá possuir uma finalidade clara.

Exemplo:

```text
Implementar conexão com Instagram
```

ou:

```text
Corrigir duplicidade de publicação
```

---

# 6. Antes de codificar

O desenvolvedor ou agente de IA deverá:

```text
entender o objetivo
 ↓
consultar arquitetura
 ↓
localizar código existente
 ↓
identificar impactos
 ↓
implementar
```

---

# 7. Ambiente local

O desenvolvimento deverá ocorrer inicialmente em ambiente local.

Arquitetura:

```text
React
+
FastAPI
+
MySQL
```

---

# 8. Banco local

O banco local deverá ser independente da produção.

Nunca utilizar o banco de produção como banco de desenvolvimento.

---

# 9. Dados de desenvolvimento

Preferir dados:

```text
fictícios
controlados
reprodutíveis
```

---

# 10. Alteração de banco

Sempre que houver alteração estrutural:

```text
modelo
 ↓
migração
 ↓
teste
```

---

# 11. Migrações

Utilizar:

```text
Alembic
```

para controlar alterações do banco.

---

# 12. Não alterar produção manualmente

Evitar comandos SQL manuais em produção sem registro e sem necessidade excepcional.

---

# 13. Desenvolvimento incremental

Preferir alterações pequenas:

```text
uma funcionalidade
 ↓
testar
 ↓
próxima funcionalidade
```

---

# 14. Testes durante desenvolvimento

Executar testes relevantes antes de finalizar a tarefa.

---

# 15. Lint e qualidade

Antes de commit:

```text
lint
+
testes
```

deverão ser executados conforme as ferramentas adotadas pelo projeto.

---

# 16. Commit

O commit deverá representar uma mudança coerente.

Exemplos:

```text
feat: adicionar conexão com Instagram
fix: corrigir duplicidade de publicação
test: adicionar teste de autorização
refactor: separar serviço de conteúdo
docs: atualizar integração Instagram
```

---

# 17. Commits pequenos

Evitar commits gigantes que misturem:

```text
frontend
backend
infraestrutura
documentação
```

sem relação entre si.

---

# 18. Mensagem de commit

A mensagem deverá explicar a mudança de forma curta e objetiva.

---

# 19. Branch

A estratégia de branches deverá permanecer simples no MVP.

Modelo sugerido:

```text
main
  ↓
desenvolvimento
```

ou branches curtas de funcionalidade quando necessário.

---

# 20. Branch principal

A branch principal deverá representar uma versão estável do projeto.

---

# 21. Branch de funcionalidade

Quando necessário:

```text
feature/nome-da-funcionalidade
```

---

# 22. Correção

Para correções:

```text
fix/nome-da-correcao
```

---

# 23. Documentação

Para alterações somente documentais:

```text
docs/nome-da-alteracao
```

---

# 24. Pull Request

Se houver trabalho colaborativo, utilizar Pull Request para revisar alterações.

---

# 25. Revisão

A revisão deverá verificar:

```text
arquitetura
regra de negócio
segurança
testes
legibilidade
```

---

# 26. IA no desenvolvimento

Agentes de IA poderão criar e alterar código.

Porém:

```text
IA gera
 ↓
testes validam
 ↓
humano/revisão valida
```

---

# 27. Regra para IA

A IA não deverá:

```text
inventar endpoint
ignorar contrato
remover teste
desabilitar segurança
colocar segredo no código
```

---

# 28. Documentação como contrato

Quando uma implementação contrariar a documentação, primeiro avaliar se:

```text
código está errado
```

ou:

```text
arquitetura realmente mudou
```

---

# 29. Mudança arquitetural

Se a arquitetura mudar:

```text
documentação
 ↓
código
 ↓
testes
```

deverão permanecer alinhados.

---

# 30. Build

Antes do deploy, gerar os artefatos de produção.

Frontend:

```text
build React
```

Backend:

```text
dependências
+
configuração
```

---

# 31. Validação do build

O build deverá ser executado localmente ou em ambiente automatizado antes da promoção.

---

# 32. Deploy

Fluxo inicial:

```text
Git
 ↓
VPS
 ↓
atualizar código
 ↓
instalar dependências/build
 ↓
migrações
 ↓
reiniciar serviços
```

---

# 33. Backup antes de migração

Quando uma migração alterar dados ou estrutura relevante:

```text
backup
 ↓
migração
```

---

# 34. Ordem do deploy

Ordem conceitual:

```text
1. verificar versão
2. verificar configuração
3. backup quando necessário
4. atualizar código
5. instalar dependências
6. executar migrações
7. gerar build
8. reiniciar serviços
9. verificar health
10. executar smoke test
```

---

# 35. Health Check

Após o deploy:

```http
GET /health
```

deverá responder corretamente.

---

# 36. Smoke Test

Verificar pelo menos:

```text
API
login
dashboard
banco
```

e a funcionalidade diretamente alterada.

---

# 37. Deploy de alteração do frontend

Após alterar React:

```text
build
 ↓
publicação dos arquivos
 ↓
NGINX
 ↓
teste
```

---

# 38. Deploy do backend

Após alterar FastAPI:

```text
atualizar código
 ↓
dependências
 ↓
migração quando necessária
 ↓
reiniciar aplicação
 ↓
health
```

---

# 39. Deploy de banco

Após alteração de banco:

```text
backup
 ↓
migração
 ↓
teste
```

---

# 40. Deploy de integração externa

Alterações no Instagram ou IA deverão possuir validação específica.

---

# 41. Credenciais de produção

As credenciais deverão existir somente no ambiente de produção.

Nunca copiar:

```text
.env de produção
```

para o repositório.

---

# 42. Variáveis

Consultar:

```text
39_CONFIGURACAO_E_VARIAVEIS_DE_AMBIENTE.md
```

---

# 43. Infraestrutura

Consultar:

```text
40_INFRAESTRUTURA_LOCAL_E_VPS.md
```

---

# 44. Testes

Consultar:

```text
41_ESTRATEGIA_DE_TESTES.md
```

---

# 45. Qualidade

Consultar:

```text
42_PADRAO_DE_DESENVOLVIMENTO_E_QUALIDADE_DE_CODIGO.md
```

---

# 46. Falha no deploy

Se o deploy falhar:

```text
não improvisar diretamente em produção
```

Primeiro:

```text
identificar erro
 ↓
avaliar impacto
 ↓
corrigir
```

---

# 47. Rollback

Quando necessário:

```text
versão anterior
 ↓
deploy
 ↓
health
 ↓
smoke test
```

---

# 48. Rollback de banco

Rollback do código e rollback do banco são operações diferentes.

Não executar rollback de banco automaticamente sem entender o impacto.

---

# 49. Deploy parcial

Evitar deixar:

```text
frontend novo
+
backend antigo incompatível
```

quando houver mudança de contrato.

---

# 50. Compatibilidade

Mudanças na API deverão ser feitas considerando a versão atualmente utilizada pelo frontend.

---

# 51. Mudança incompatível

Se necessário:

```text
nova versão da API
```

deverá ser considerada.

---

# 52. Produção

A produção deverá possuir:

```text
HTTPS
NGINX
React
FastAPI
MySQL
backup
logs
health
```

---

# 53. VPS

A infraestrutura alvo é:

```text
Hostinger VPS
```

As características específicas da VPS deverão ser registradas quando definidas.

---

# 54. Acesso SSH

A administração da VPS deverá utilizar acesso seguro.

---

# 55. Firewall

Somente portas necessárias deverão estar expostas.

---

# 56. Logs

Após deploy, verificar logs de:

```text
NGINX
FastAPI
MySQL
worker, quando existir
```

---

# 57. Correlation ID

Se houver erro funcional, utilizar:

```text
correlation_id
```

para rastrear a requisição.

---

# 58. Monitoramento

Após publicação, acompanhar:

```text
CPU
RAM
disco
API
MySQL
erros
```

---

# 59. Deploy sem downtime

Não é requisito do MVP.

Uma pequena indisponibilidade durante deploy é aceitável inicialmente, desde que seja controlada.

---

# 60. Alta disponibilidade

Não é requisito do MVP.

---

# 61. Pipeline futuro

Quando o projeto crescer:

```text
Git push
 ↓
CI
 ↓
testes
 ↓
build
 ↓
deploy
 ↓
smoke test
```

---

# 62. CI/CD

O pipeline deverá impedir promoção quando testes críticos falharem.

---

# 63. Segredos no CI

Segredos deverão ser armazenados como:

```text
secrets
```

da plataforma de CI/CD, quando disponível.

---

# 64. Não imprimir segredos

Scripts de deploy não deverão imprimir valores sensíveis.

---

# 65. Versionamento de release

Quando houver versões formais:

```text
v0.1.0
v0.2.0
v1.0.0
```

ou padrão equivalente.

---

# 66. MVP

O MVP poderá utilizar:

```text
versões simples
```

sem processo complexo de release.

---

# 67. Changelog

Alterações importantes deverão ser registradas.

---

# 68. Auditoria

Alterações administrativas do sistema deverão ser auditáveis quando aplicável.

---

# 69. Deploy de correção crítica

Para correções críticas:

```text
identificar
 ↓
corrigir
 ↓
testar
 ↓
deploy
 ↓
validar
```

---

# 70. Incidente

Quando houver incidente:

```text
detectar
 ↓
conter
 ↓
corrigir
 ↓
validar
 ↓
registrar causa
```

---

# 71. Não apagar evidências

Em caso de erro, não apagar imediatamente:

```text
logs
registros
ExecucaoIA
status de publicação
```

sem entender o incidente.

---

# 72. Dados de publicação

Falhas de publicação deverão preservar informações suficientes para investigação.

---

# 73. Dados de IA

Falhas de IA deverão manter:

```text
execucao_id
modelo
status
tempo
erro
```

quando aplicável.

---

# 74. Alteração de configuração

Alterações em produção deverão ser registradas.

---

# 75. Alteração de segredo

Quando um segredo for rotacionado:

```text
revogar antigo
 ↓
gerar novo
 ↓
atualizar ambiente
 ↓
testar
```

---

# 76. Banco de produção

Acesso administrativo ao banco deverá ser restrito.

---

# 77. Backup

Antes de operações de risco:

```text
backup
```

---

# 78. Restauração

O procedimento de restauração deverá estar documentado.

---

# 79. Checklist de desenvolvimento

```text
[ ] li documentação relevante
[ ] entendi a tarefa
[ ] localizei código existente
[ ] implementei
[ ] criei/ajustei testes
[ ] executei testes
[ ] revisei segurança
[ ] revisei contrato
```

---

# 80. Checklist de commit

```text
[ ] somente arquivos relacionados
[ ] sem segredos
[ ] sem código de debug
[ ] testes passando
[ ] mensagem clara
```

---

# 81. Checklist de deploy

```text
[ ] versão correta
[ ] testes aprovados
[ ] backup quando necessário
[ ] configuração validada
[ ] migração revisada
[ ] build aprovado
[ ] deploy executado
[ ] health aprovado
[ ] smoke test aprovado
[ ] logs verificados
```

---

# 82. Checklist de rollback

```text
[ ] identificar versão estável
[ ] avaliar banco
[ ] restaurar aplicação
[ ] verificar health
[ ] executar smoke test
[ ] analisar causa
```

---

# 83. Critério de sucesso

O fluxo estará adequado quando:

```text
qualquer desenvolvedor/IA consegue entender como alterar
+
testes protegem a alteração
+
Git registra a mudança
+
deploy é reproduzível
+
produção pode ser validada
+
rollback é possível
```

---

# 84. Regra para agentes de IA

Antes de executar uma alteração:

1. ler a documentação relevante;
2. localizar arquivos existentes;
3. não criar estrutura duplicada;
4. implementar a menor mudança correta;
5. executar testes;
6. verificar o impacto;
7. gerar commit somente quando solicitado;
8. nunca fazer alteração destrutiva em produção sem autorização explícita.

---

# 85. Regra contra deploy automático

O agente não deverá assumir autorização para publicar em produção.

Deploy de produção deverá ser uma ação explícita do responsável pelo projeto.

---

# 86. Regra contra mudanças destrutivas

Não executar automaticamente:

```text
DROP DATABASE
DROP TABLE
DELETE massivo
reset de produção
```

---

# 87. Regra final

> **O código entra no ViralCode por um caminho controlado: entender → implementar → testar → versionar → publicar → validar.**

O objetivo é permitir que o projeto cresça sem transformar a manutenção em uma sequência de operações manuais e imprevisíveis.

**Versão:** 1.0  
**Status:** Documento oficial do Fluxo de Desenvolvimento, Git e Deploy
