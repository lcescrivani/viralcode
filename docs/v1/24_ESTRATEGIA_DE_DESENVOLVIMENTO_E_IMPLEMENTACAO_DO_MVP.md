# 24 — ESTRATÉGIA DE DESENVOLVIMENTO E IMPLEMENTAÇÃO DO MVP

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define a ordem de implementação do ViralCode.

O objetivo é impedir que o projeto tente construir toda a arquitetura-alvo de uma vez.

O MVP deverá ser desenvolvido de forma incremental:

```text
INFRAESTRUTURA
   ↓
AUTENTICAÇÃO
   ↓
PERFIL
   ↓
INSTAGRAM
   ↓
DESCOBERTA
   ↓
ANÁLISE
   ↓
CRIAÇÃO
   ↓
APROVAÇÃO
   ↓
PUBLICAÇÃO
   ↓
MÉTRICAS
   ↓
APRENDIZADO
```

---

# 2. Princípio principal

O MVP deve validar o negócio antes de validar a arquitetura completa.

A pergunta central é:

> **As pessoas realmente conseguem utilizar o ViralCode para descobrir padrões de conteúdo, criar conteúdos melhores e melhorar seus resultados?**

Não:

```text
Temos uma arquitetura sofisticada?
```

---

# 3. Ordem de implementação

A implementação deverá seguir aproximadamente:

```text
FASE 01 — Fundação
FASE 02 — Usuários
FASE 03 — Perfil
FASE 04 — Instagram
FASE 05 — Descoberta
FASE 06 — Análise
FASE 07 — Criação
FASE 08 — Planejamento
FASE 09 — Publicação
FASE 10 — Desempenho
FASE 11 — Aprendizado
FASE 12 — Validação do MVP
```

---

# 4. Fase 01 — Fundação

Objetivo:

```text
projeto executável
```

Implementar:

```text
estrutura de pastas
FastAPI
React
MySQL
SQLAlchemy
migrações
configuração
Docker
README
```

Resultado:

```text
Frontend funcionando
Backend funcionando
Banco funcionando
```

---

# 5. Fase 02 — Usuários

Implementar:

```text
cadastro
login
token
usuário autenticado
autorização
isolamento
```

Testar:

```text
Usuário A ≠ Usuário B
```

Resultado:

```text
usuário consegue entrar no sistema
```

---

# 6. Fase 03 — Perfil

Implementar:

```text
criar perfil
listar perfil
editar perfil
selecionar nicho
```

Exemplo:

```text
Perfil:
Casamento

Nicho:
Relacionamentos

Público:
Casais

Tom:
Direto e acolhedor
```

---

# 7. Fase 04 — Instagram

Esta é uma fase crítica.

Implementar primeiro:

```text
aplicação
OAuth
callback
token
conta social
status da conexão
```

Depois testar:

```text
conta profissional
mídias
métricas
recursos de descoberta disponíveis
```

---

# 8. Regra da POC do Instagram

Não avançar para uma implementação grande antes de confirmar tecnicamente:

```text
login
permissões
conta
consulta
métricas
descoberta
```

A integração real deverá ser validada com a documentação atual da plataforma e uma conta de desenvolvimento.

---

# 9. Resultado esperado da Fase 04

Ao final:

```text
Usuário
   ↓
Perfil
   ↓
Conecta Instagram
   ↓
Conta aparece no ViralCode
```

---

# 10. Fase 05 — Descoberta

Implementar o menor mecanismo de descoberta que a integração oficial permitir.

Exemplo:

```text
hashtag
```

ou:

```text
conta
```

ou:

```text
mídias da conta
```

dependendo da capacidade efetivamente confirmada.

---

# 11. Não bloquear o projeto pela busca ideal

O produto ideal pode desejar:

```text
"casamento"
+
"> 1.000.000 visualizações"
```

e:

```text
ordenar do maior para o menor
```

Mas isso somente deverá ser implementado se os dados estiverem realmente disponíveis.

---

# 12. Fallback de descoberta

Caso a descoberta ampla não seja possível:

```text
reduzir escopo
```

e validar o restante do produto com:

```text
conteúdos disponíveis
+
contas selecionadas
+
dados armazenados
```

---

# 13. Fase 06 — Análise

Implementar:

```text
analisar conteúdo
```

A IA deverá identificar, conforme os dados disponíveis:

```text
hook
tema
subtema
formato
estrutura
emoção
CTA
ângulo
```

---

# 14. Primeira análise

Não tentar construir uma inteligência artificial proprietária.

No MVP:

```text
dados
+
prompt
+
modelo de IA
=
análise
```

---

# 15. Resultado da análise

Exemplo:

```text
Conteúdo
   ↓
Hook: pergunta provocativa
Tema: diálogo
Emoção: identificação
CTA: comentário
Estrutura: problema → tensão → solução
```

---

# 16. Fase 07 — Criação

Implementar:

```text
gerar ideia
gerar hook
gerar roteiro
gerar legenda
gerar CTA
```

A criação deverá considerar:

```text
perfil
nicho
tom de voz
padrões
insights
aprendizados
```

---

# 17. Regra de originalidade

O ViralCode não deverá simplesmente copiar o conteúdo analisado.

O objetivo é:

```text
PADRÃO
   ↓
INSIGHT
   ↓
NOVA IDEIA
```

Não:

```text
CONTEÚDO
   ↓
CÓPIA
```

---

# 18. Fase 08 — Planejamento

Implementar um calendário simples.

O usuário deverá conseguir:

```text
visualizar
criar
editar
aprovar
organizar
```

conteúdos planejados.

---

# 19. Calendário mínimo

Exemplo:

```text
SEG
REEL — diálogo

TER
REEL — intimidade

QUA
POST — reflexão

QUI
REEL — conflito

SEX
REEL — relacionamento
```

A quantidade e frequência deverão ser configuráveis.

---

# 20. Fase 09 — Publicação

Somente depois de:

```text
conteúdo criado
+
conteúdo aprovado
+
conta conectada
```

implementar publicação.

---

# 21. Regra de aprovação

No MVP:

```text
IA cria
   ↓
USUÁRIO REVISA
   ↓
USUÁRIO APROVA
   ↓
PUBLICAR
```

Não iniciar com publicação autônoma.

---

# 22. Publicação manual assistida

Se a integração oficial permitir publicação:

```text
ViralCode
   ↓
Instagram
```

poderá ser implementada.

Se não permitir algum recurso necessário:

```text
ViralCode
   ↓
gera conteúdo
   ↓
usuário publica
```

O produto deverá continuar funcionando.

---

# 23. Fase 10 — Desempenho

Depois da publicação, coletar métricas disponíveis.

Exemplos:

```text
visualizações
curtidas
comentários
compartilhamentos
salvamentos
alcance
impressões
```

Somente quando a plataforma fornecer a métrica.

---

# 24. Histórico

Não guardar somente o resultado atual.

Sempre que possível:

```text
10h → 10.000
14h → 18.000
18h → 32.000
22h → 50.000
```

Isso permitirá calcular crescimento.

---

# 25. Fase 11 — Aprendizado

Depois de possuir conteúdo + desempenho:

```text
Conteúdo
   ↓
Métricas
   ↓
Comparação
   ↓
Padrões
   ↓
Aprendizado
```

---

# 26. Aprendizado inicial

Não construir machine learning próprio.

No MVP, utilizar:

```text
regras
+
estatística simples
+
IA
```

---

# 27. Exemplo de aprendizado

Depois de vários conteúdos:

```text
Conteúdos com pergunta no primeiro segundo
→ desempenho médio superior
```

O sistema poderá registrar:

```text
APRENDIZADO:
Hooks interrogativos apresentam desempenho superior
```

Mas deverá guardar:

```text
amostra
evidências
confiança
```

---

# 28. Regra contra conclusões prematuras

Não transformar:

```text
1 conteúdo performou bem
```

em:

```text
regra universal
```

A confiança deverá considerar a quantidade e qualidade das evidências.

---

# 29. Fase 12 — Validação

Ao final do MVP, testar o fluxo completo:

```text
CRIAR USUÁRIO
      ↓
CRIAR PERFIL
      ↓
CONECTAR INSTAGRAM
      ↓
DESCOBRIR
      ↓
ANALISAR
      ↓
CRIAR
      ↓
APROVAR
      ↓
PUBLICAR
      ↓
MEDIR
      ↓
APRENDER
```

---

# 30. Critério de sucesso técnico

O fluxo deverá funcionar sem intervenção manual do desenvolvedor, exceto quando uma ação exigir aprovação do usuário ou interação com a plataforma.

---

# 31. Critério de sucesso de negócio

O MVP deverá responder:

```text
1. O usuário entende o produto?
2. Consegue encontrar conteúdo relevante?
3. A análise é útil?
4. A geração economiza tempo?
5. O conteúdo gerado é melhor que o processo atual?
6. O usuário publica?
7. Ele volta para usar novamente?
```

---

# 32. O que medir no MVP

Métricas de produto:

```text
usuários cadastrados
perfis criados
contas conectadas
descobertas realizadas
conteúdos analisados
conteúdos gerados
conteúdos aprovados
publicações
usuários recorrentes
```

---

# 33. Métrica mais importante

Não considerar:

```text
quantidade de funcionalidades
```

como métrica principal.

A métrica central deverá ser:

```text
USUÁRIO CONSEGUIU PRODUZIR E PUBLICAR CONTEÚDO MELHOR?
```

---

# 34. Desenvolvimento vertical

Preferir construir uma funcionalidade completa de ponta a ponta.

Exemplo:

```text
CONEXÃO INSTAGRAM
```

em vez de:

```text
fazer 20 telas
depois banco
depois serviços
depois integração
```

---

# 35. Exemplo de primeira vertical

```text
Login
 ↓
Perfil
 ↓
Conectar Instagram
 ↓
Mostrar conta conectada
```

Depois:

```text
Descoberta
 ↓
Resultado
 ↓
Salvar conteúdo
```

Depois:

```text
Análise
 ↓
Resultado
```

---

# 36. Segunda vertical

```text
Conteúdo analisado
 ↓
Gerar ideia
 ↓
Gerar roteiro
 ↓
Editar
 ↓
Aprovar
```

---

# 37. Terceira vertical

```text
Conteúdo aprovado
 ↓
Publicar
 ↓
Consultar desempenho
```

---

# 38. Quarta vertical

```text
Desempenho
 ↓
Comparar
 ↓
Aprender
 ↓
Melhorar próxima geração
```

---

# 39. Ordem de prioridade

### P0 — Obrigatório

```text
projeto executável
usuário
login
perfil
Instagram
conteúdo
análise
IA
criação
aprovação
```

### P1 — Necessário para validar ciclo

```text
publicação
métricas
aprendizado básico
planejamento simples
```

### P2 — Depois do MVP

```text
múltiplas redes
equipes
campanhas
experimentos
A/B
automação avançada
```

---

# 40. Não fazer no MVP

Não implementar inicialmente:

```text
microserviços
Kubernetes
machine learning próprio
agentes autônomos complexos
editor de vídeo completo
automação de vídeo avançada
múltiplas redes
marketplace
equipe multiempresa
billing complexo
```

---

# 41. Regra contra overengineering

Antes de criar uma abstração perguntar:

```text
Existe necessidade real agora?
```

Se a resposta for:

```text
não
```

não implementar.

---

# 42. Regra contra dívida técnica irresponsável

Simplicidade não significa código descartável.

Mesmo no MVP:

```text
testar
documentar
separar responsabilidades
proteger dados
```

---

# 43. Definition of Done

Uma funcionalidade somente estará pronta quando:

```text
código criado
+
teste criado
+
teste passando
+
API documentada
+
tratamento de erro
+
logs necessários
+
documentação atualizada
```

---

# 44. Pull Request

Quando o projeto utilizar Git colaborativo, cada mudança relevante deverá explicar:

```text
O que foi feito?
Por quê?
Como foi testado?
Existe impacto arquitetural?
```

---

# 45. Commits

Preferir commits pequenos e objetivos.

Exemplos:

```text
cria autenticação de usuários
adiciona conexão Instagram
implementa descoberta por hashtag
adiciona análise de conteúdo
implementa geração de roteiro
```

---

# 46. Migrações

Toda alteração de banco deverá possuir migração.

Não alterar manualmente o banco de produção sem registrar a mudança.

---

# 47. Testes de integração externa

Não depender do Instagram real em todos os testes.

Utilizar:

```text
mocks
fakes
ambientes de teste
```

quando possível.

---

# 48. Teste real

Apesar dos mocks, deverá existir uma rotina de validação real da integração:

```text
conta Instagram de desenvolvimento
```

para confirmar mudanças da plataforma.

---

# 49. IA

A IA deverá ser tratada como componente externo.

O sistema deverá registrar:

```text
prompt
modelo
entrada
saída
status
tokens quando disponíveis
custo estimado quando possível
```

---

# 50. Controle de custo

No MVP, acompanhar pelo menos:

```text
quantidade de chamadas
tokens
custo estimado
```

quando essas informações estiverem disponíveis.

---

# 51. Falha da IA

Se a IA falhar:

```text
não perder conteúdo
não corromper estado
registrar erro
permitir nova tentativa
```

---

# 52. Falha do Instagram

Se o Instagram falhar:

```text
registrar erro
preservar conteúdo
preservar publicação
permitir nova tentativa quando seguro
```

---

# 53. Idempotência

Operações que podem causar duplicidade deverão ser protegidas.

Principalmente:

```text
publicação
```

---

# 54. Assincronicidade

O MVP poderá executar algumas operações de forma síncrona quando forem rápidas.

Operações demoradas poderão posteriormente utilizar fila.

Não criar uma infraestrutura de filas antes de existir necessidade real.

---

# 55. Fila futura

Quando necessário:

```text
API
 ↓
Fila
 ↓
Worker
 ↓
IA / Instagram
```

Essa arquitetura poderá ser adicionada posteriormente.

---

# 56. Deploy inicial

O projeto deverá ser executável localmente antes do primeiro deploy.

Depois:

```text
Git
 ↓
VPS Hostinger
 ↓
Configuração
 ↓
Migrações
 ↓
Aplicação
```

---

# 57. Ambiente de produção

A primeira produção poderá continuar sendo um único servidor VPS, desde que o volume do MVP permita.

Não criar infraestrutura distribuída prematuramente.

---

# 58. Backup

Antes de considerar o MVP em produção:

```text
backup MySQL
```

deverá estar configurado.

---

# 59. Monitoramento

No mínimo:

```text
health check
logs
uso de disco
uso de memória
uso de CPU
status do banco
```

A solução detalhada ficará no documento de infraestrutura.

---

# 60. Segurança antes de produção

Validar:

```text
HTTPS
segredos
CORS
autenticação
permissões
banco
backup
logs
```

---

# 61. Checklist de lançamento

```text
[ ] Frontend funcionando
[ ] Backend funcionando
[ ] Banco funcionando
[ ] Migrações funcionando
[ ] Login funcionando
[ ] Isolamento testado
[ ] Instagram conectado
[ ] Descoberta validada
[ ] Análise funcionando
[ ] IA funcionando
[ ] Criação funcionando
[ ] Aprovação funcionando
[ ] Publicação funcionando ou fluxo manual definido
[ ] Métricas funcionando
[ ] Aprendizado básico funcionando
[ ] Backup configurado
[ ] HTTPS configurado
[ ] Logs funcionando
```

---

# 62. Regra para agentes de IA

Antes de desenvolver uma funcionalidade:

1. identificar em qual fase do MVP ela pertence;
2. verificar se está no escopo;
3. ler os documentos relacionados;
4. não antecipar funcionalidades P2;
5. implementar verticalmente quando possível;
6. criar testes;
7. atualizar documentação.

---

# 63. Regra de prioridade

Quando houver conflito entre:

```text
arquitetura perfeita
```

e:

```text
validar o produto
```

no MVP, priorizar:

```text
VALIDAÇÃO
```

desde que não comprometa segurança, integridade dos dados ou possibilidade de evolução.

---

# 64. Fluxo final

O MVP deve chegar a:

```text
              ┌───────────────┐
              │    USUÁRIO    │
              └───────┬───────┘
                      ↓
                  CONECTA
                      ↓
                 INSTAGRAM
                      ↓
                 DESCOBRE
                      ↓
                  ANALISA
                      ↓
                  ENTENDE
                      ↓
                    CRIA
                      ↓
                  APROVA
                      ↓
                  PUBLICA
                      ↓
                   MEDE
                      ↓
                 APRENDE
                      ↓
              CRIA MELHOR
```

---

# 65. Regra final

> **Construir o menor produto completo que permita validar o ciclo de valor do ViralCode.**

Não construir:

```text
um sistema enorme que um dia poderá funcionar.
```

Construir:

```text
um sistema pequeno que já funcione,
seja usado,
gere dados,
e permita aprender.
```

Essa é a estratégia oficial de implementação do MVP.

**Versão:** 1.0  
**Status:** Documento oficial da Estratégia de Desenvolvimento e Implementação do MVP
