# 48 — MATRIZ DE DEPENDÊNCIAS E INTEGRAÇÕES

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define as dependências internas e externas do ViralCode.

O objetivo é permitir que qualquer desenvolvedor ou agente de IA compreenda:

```text
quem depende de quem
o que pode falhar
onde existe acoplamento
qual componente pode ser substituído
```

---

# 2. Princípio fundamental

Dependências deverão apontar para uma direção clara.

Arquitetura principal:

```text
FRONTEND
   ↓
API
   ↓
SERVIÇOS
   ↓
REPOSITÓRIOS / CONECTORES
   ↓
BANCO / SERVIÇOS EXTERNOS
```

---

# 3. Regra de dependência

Camadas superiores podem utilizar camadas inferiores por meio das interfaces/responsabilidades definidas.

Evitar:

```text
banco chamando serviço
conector chamando frontend
modelo de banco contendo regra de negócio
```

---

# 4. Frontend

O frontend depende principalmente de:

```text
API REST
```

Não deverá depender diretamente de:

```text
MySQL
Instagram
provedor de IA
```

---

# 5. API

A API depende de:

```text
autenticação
serviços de negócio
validação
```

Não deverá concentrar toda a lógica de negócio.

---

# 6. Serviços

Serviços dependem de abstrações internas necessárias para executar regras.

Exemplo:

```text
ServicoConteudo
   ↓
RepositorioConteudo
```

ou:

```text
ServicoPublicacao
   ↓
ConectorInstagram
```

---

# 7. Repositórios

Repositórios dependem da infraestrutura de persistência.

```text
Repositorio
   ↓
SQLAlchemy
   ↓
MySQL
```

---

# 8. Conectores

Conectores dependem dos serviços externos correspondentes.

```text
ConectorInstagram
   ↓
Instagram
```

```text
ConectorProvedorIA
   ↓
Provedor de IA
```

---

# 9. Banco

O MySQL não deverá possuir dependência funcional da aplicação.

Ele fornece persistência.

---

# 10. Instagram

O Instagram é uma dependência externa.

O ViralCode deverá assumir que:

```text
API pode mudar
serviço pode ficar indisponível
credencial pode expirar
limites podem existir
```

---

# 11. Provedor de IA

O provedor de IA também é uma dependência externa.

O sistema deverá assumir:

```text
latência
erro
indisponibilidade
mudança de modelo
mudança de preço
limites
```

---

# 12. Abstração de provedor

A lógica do ViralCode não deverá ficar presa desnecessariamente a um único fornecedor de IA.

O componente interno deverá trabalhar com uma abstração própria quando isso trouxer benefício real.

---

# 13. Não criar abstração prematura

Se o MVP utilizar apenas um provedor, não criar uma estrutura excessivamente complexa somente para suportar vários fornecedores.

A arquitetura deverá permitir evolução sem antecipar complexidade.

---

# 14. Dependências internas principais

```text
React
  ↓
FastAPI
  ↓
Serviços
  ├── Repositórios
  │      ↓
  │    SQLAlchemy
  │      ↓
  │    MySQL
  │
  ├── Conector Instagram
  │      ↓
  │    Instagram
  │
  └── Serviço/Conector IA
         ↓
       Provedor IA
```

---

# 15. Motor de Análise

O Motor de Análise poderá depender de:

```text
dados persistidos
serviços de domínio
IA, quando necessário
```

---

# 16. Motor de Geração

O Motor de Geração poderá depender de:

```text
perfil
nicho
conteúdos analisados
insights
regras
serviço de IA
```

---

# 17. Motor de Publicação

O Motor de Publicação poderá depender de:

```text
conteúdo
aprovação
conta social
Conector Instagram
```

---

# 18. Fluxo de análise

```text
Fonte externa
     ↓
Conector
     ↓
Normalizador
     ↓
Banco
     ↓
Motor de Análise
     ↓
Insights
```

---

# 19. Fluxo de geração

```text
Perfil
+
Nicho
+
Insights
+
Conteúdo de referência
+
Regras
     ↓
Motor de Geração
     ↓
Serviço de IA
     ↓
Conteúdo gerado
```

---

# 20. Fluxo de publicação

```text
Conteúdo aprovado
       ↓
Motor de Publicação
       ↓
Conector Instagram
       ↓
Instagram
       ↓
Resultado
       ↓
Banco
```

---

# 21. Dependência de autenticação

A API depende do mecanismo de autenticação para identificar:

```text
quem está fazendo a requisição
```

---

# 22. Dependência de autorização

Serviços que manipulam dados privados deverão verificar:

```text
quem pode executar
```

---

# 23. Regra de isolamento de usuário

Fluxo obrigatório:

```text
requisição
 ↓
usuário autenticado
 ↓
autorização
 ↓
serviço
 ↓
recurso pertencente ao usuário
```

---

# 24. Dependência entre usuários

Um usuário nunca deverá depender de dados de outro usuário para executar uma operação comum.

---

# 25. Dependência administrativa

A Área Administrativa possui permissões especiais.

Fluxo:

```text
usuário
 ↓
autenticação
 ↓
permissão ADMIN
 ↓
serviço administrativo
```

---

# 26. Dependência do banco

Quase todos os serviços de negócio poderão depender da persistência.

Isso não significa que cada serviço deverá acessar SQL diretamente.

---

# 27. Regra contra acesso direto ao banco

Evitar:

```text
rota
 ↓
SQLAlchemy
```

quando a operação representar uma regra de negócio.

Preferir:

```text
rota
 ↓
serviço
 ↓
repositório
 ↓
SQLAlchemy
```

---

# 28. Regra contra acesso direto ao Instagram

Evitar:

```text
rota
 ↓
requisição HTTP Instagram
```

Preferir:

```text
rota
 ↓
serviço
 ↓
conector Instagram
 ↓
Instagram
```

---

# 29. Regra contra acesso direto à IA

Evitar:

```text
rota
 ↓
API do provedor IA
```

Preferir:

```text
rota
 ↓
serviço
 ↓
serviço de IA
 ↓
conector
 ↓
provedor
```

---

# 30. Dependências externas

Tabela inicial:

| Dependência | Tipo | Criticidade | MVP |
|---|---|---|---|
| MySQL | Banco | Crítica | Sim |
| Instagram | Rede social | Crítica | Sim |
| Provedor de IA | IA | Crítica | Sim |
| Hostinger VPS | Infraestrutura | Crítica em produção | Sim |
| NGINX | Infraestrutura | Alta | Sim |
| Docker | Infraestrutura | Média | Conforme adoção |

---

# 31. MySQL indisponível

Impacto:

```text
operações que exigem persistência podem falhar
```

A API deverá retornar erro tratado.

Não expor detalhes internos do banco.

---

# 32. Instagram indisponível

Impacto:

```text
publicações podem falhar
```

O conteúdo já existente no ViralCode não deverá ser perdido simplesmente porque o Instagram está indisponível.

---

# 33. IA indisponível

Impacto:

```text
análises/gerações que dependem de IA podem falhar
```

Dados já persistidos deverão permanecer disponíveis.

---

# 34. NGINX indisponível

Impacto:

```text
usuário não consegue acessar normalmente a aplicação
```

A infraestrutura deverá permitir reinício controlado.

---

# 35. Hostinger indisponível

Impacto:

```text
produção indisponível
```

No MVP não haverá alta disponibilidade.

Backups deverão reduzir o risco de perda de dados.

---

# 36. Dependências críticas

As dependências críticas do MVP são:

```text
MySQL
Instagram
Provedor de IA
VPS
```

---

# 37. Dependências substituíveis

Algumas dependências deverão ser substituíveis sem reescrever o domínio.

Exemplo:

```text
Provedor IA A
      ↓
Provedor IA B
```

A troca deverá ocorrer preferencialmente no conector/infraestrutura.

---

# 38. Instagram

A arquitetura deverá evitar colocar regras específicas do Instagram em:

```text
entidades
serviços genéricos
frontend
```

---

# 39. Dados específicos do Instagram

Campos exclusivos da plataforma poderão existir no modelo de integração.

Eles não deverão contaminar desnecessariamente o domínio genérico.

---

# 40. Abstração de rede social

No MVP, a primeira rede social será:

```text
Instagram
```

Não é necessário implementar todas as redes sociais agora.

---

# 41. Preparação para múltiplas redes

A arquitetura deverá permitir futuramente:

```text
Instagram
TikTok
YouTube
LinkedIn
outras
```

sem obrigar o MVP a implementá-las.

---

# 42. Estratégia futura

Possível arquitetura:

```text
Motor de Publicação
        ↓
Interface de Rede Social
        ↓
┌───────┼────────┐
▼       ▼        ▼
Instagram TikTok YouTube
```

---

# 43. Não implementar agora

Não criar conectores de redes sociais que não fazem parte do MVP.

---

# 44. Dependência do frontend

O frontend deverá depender do contrato da API.

Se o backend mudar o contrato:

```text
frontend poderá quebrar
```

Por isso alterações de API deverão ser coordenadas.

---

# 45. Contrato

Consultar:

```text
34_CONTRATOS_DA_API_REST.md
```

---

# 46. Dependência de versão

Quando uma alteração quebrar compatibilidade:

```text
avaliar versionamento
```

---

# 47. Dependência temporal

Algumas operações dependem de:

```text
data
hora
agendamento
timezone
```

Essas regras deverão ser centralizadas.

---

# 48. Dependência de configuração

Serviços deverão utilizar a configuração central.

Não espalhar:

```text
URL
porta
token
modelo
limite
```

pelo código.

---

# 49. Dependência de ambiente

Código deverá distinguir:

```text
desenvolvimento
produção
```

por configuração e não por alterações manuais no código.

---

# 50. Dependência de arquivos

O sistema não deverá depender de arquivos locais permanentes quando esses arquivos forem dados importantes.

---

# 51. Mídia

Se o armazenamento local deixar de ser suficiente:

```text
VPS
 ↓
Object Storage
```

poderá ser adotado futuramente.

---

# 52. Dependência de fila

No MVP, uma fila externa não é obrigatória.

Quando o processamento exigir:

```text
tarefas longas
retry
agendamento
processamento assíncrono
```

poderá ser introduzido um mecanismo de fila.

---

# 53. Worker

O Worker será introduzido quando tarefas não puderem depender de uma requisição HTTP síncrona.

---

# 54. Regra contra processamento longo na API

Operações muito longas não deverão bloquear indefinidamente uma requisição HTTP.

---

# 55. Exemplos

Podem se tornar tarefas assíncronas:

```text
análise de muitos conteúdos
geração em lote
publicações agendadas
coleta extensa
```

---

# 56. Dependência de relógio

Testes não deverão depender diretamente do relógio real quando isso dificultar reprodução.

Preferir abstração de data/hora nos pontos críticos.

---

# 57. Dependência aleatória

Operações que utilizem aleatoriedade deverão permitir controle nos testes quando necessário.

---

# 58. IA não determinística

Testes não deverão depender de uma resposta textual exatamente igual.

Validar:

```text
estrutura
campos
regras
```

---

# 59. Dependência de rede

Testes unitários não deverão exigir Internet.

---

# 60. Integrações

Testes de integração poderão utilizar:

```text
mock
stub
ambiente de teste
```

ou chamadas reais controladas quando necessário.

---

# 61. Falha de dependência

Toda dependência externa deverá possuir tratamento de falha.

---

# 62. Timeout

Conectores externos deverão possuir timeout.

---

# 63. Retry

Somente erros potencialmente temporários deverão sofrer retry automático.

---

# 64. Idempotência

Operações que possam ser repetidas deverão considerar idempotência.

Principalmente:

```text
publicação
processamentos externos
tarefas assíncronas
```

---

# 65. Circuit Breaker

Não implementar no MVP sem necessidade.

Poderá ser considerado quando uma dependência externa apresentar falhas recorrentes.

---

# 66. Cache

Não introduzir cache distribuído no MVP sem necessidade.

---

# 67. Redis

Não é dependência obrigatória do MVP.

Somente adicionar quando houver requisito concreto.

---

# 68. Mensageria

Não adicionar Kafka, RabbitMQ ou equivalente no MVP sem necessidade concreta.

---

# 69. Microserviços

O ViralCode deverá iniciar como uma aplicação modular, não como vários microserviços independentes.

---

# 70. Monólito modular

A arquitetura inicial deverá ser entendida como:

```text
MONÓLITO MODULAR
```

com módulos internos bem separados.

---

# 71. Benefício

Isso permite:

```text
simplicidade de deploy
+
baixo custo
+
desenvolvimento rápido
+
separação lógica
```

---

# 72. Evolução

Se um módulo crescer muito:

```text
módulo
 ↓
identificar dependências
 ↓
extrair somente se necessário
```

---

# 73. Regra contra microserviço prematuro

Não transformar:

```text
Motor de IA
Motor de Publicação
Motor de Análise
```

em servidores separados somente porque possuem nomes diferentes.

---

# 74. Dependências entre motores

Inicialmente:

```text
Motor de Análise
Motor de Geração
Motor de Publicação
```

podem existir dentro do mesmo backend.

---

# 75. Limites internos

Mesmo dentro do mesmo backend, cada motor deverá possuir responsabilidade clara.

---

# 76. Fluxo completo

```text
Instagram
    ↓
Conector
    ↓
Normalizador
    ↓
Banco
    ↓
Motor de Análise
    ↓
Insights
    ↓
Motor de Geração
    ↓
Conteúdo
    ↓
Aprovação
    ↓
Motor de Publicação
    ↓
Conector Instagram
    ↓
Instagram
```

---

# 77. Fluxo com IA

```text
Motor de Análise
       ↓
Serviço de IA
       ↓
Conector do Provedor
       ↓
IA
       ↓
Resultado estruturado
       ↓
Motor de Análise
```

ou:

```text
Motor de Geração
       ↓
Serviço de IA
       ↓
Conector
       ↓
IA
       ↓
Conteúdo gerado
```

---

# 78. Dependência circular

Evitar:

```text
ServicoA → ServicoB
ServicoB → ServicoA
```

---

# 79. Dependência circular entre módulos

Se houver ciclo:

```text
A → B → C → A
```

deverá ser analisado e, preferencialmente, eliminado.

---

# 80. Regra de direção

Dependências deverão seguir o fluxo arquitetural definido.

---

# 81. Interfaces

Quando uma dependência precisar ser substituível, poderá ser criada uma interface/contrato.

---

# 82. Não criar interface para tudo

Interfaces deverão existir quando houver:

```text
substituição
teste
isolamento
variação real
```

---

# 83. Dependência do domínio

O domínio não deverá depender diretamente de:

```text
FastAPI
HTTP
MySQL
Instagram
```

quando isso puder ser evitado.

---

# 84. Regra arquitetural

O domínio deve representar:

```text
o negócio
```

e não:

```text
a tecnologia usada para executar o negócio
```

---

# 85. Matriz simplificada

| Componente | React | FastAPI | Serviços | MySQL | Instagram | IA |
|---|---:|---:|---:|---:|---:|---:|
| React | — | Sim | Não direto | Não | Não | Não |
| FastAPI | Não | — | Sim | Não direto | Não direto | Não direto |
| Serviços | Não | — | — | Via repositório | Via conector | Via serviço/conector |
| Repositórios | Não | Não | — | Sim | Não | Não |
| Conector Instagram | Não | Não | — | Não | Sim | Não |
| Serviço IA | Não | Não | — | Não | Não | Via conector |
| Frontend | — | API | Não | Não | Não | Não |

---

# 86. Dependência de documentação

Antes de alterar um componente, consultar:

```text
documentação do componente
+
documentos de arquitetura
+
contratos
```

---

# 87. Regra para agentes de IA

Antes de adicionar uma dependência:

1. verificar se já existe solução interna;
2. verificar se a tecnologia é necessária;
3. verificar impacto no deploy;
4. verificar impacto nos testes;
5. verificar impacto na segurança;
6. documentar a nova dependência quando necessário.

---

# 88. Regra contra dependências ocultas

Não criar código que dependa de:

```text
variável local
arquivo manual
serviço externo não documentado
processo executado manualmente
```

sem registrar essa dependência.

---

# 89. Regra contra acoplamento

Se uma regra de negócio só funcionar porque:

```text
Instagram retorna exatamente determinado campo
```

isso deverá ficar isolado no conector/normalizador.

---

# 90. Regra contra vazamento de tecnologia

Não espalhar tipos específicos de:

```text
SQLAlchemy
Instagram
provedor de IA
```

por toda a camada de domínio sem necessidade.

---

# 91. Testes

Toda dependência crítica deverá possuir testes de falha.

---

# 92. Cenários mínimos

Para cada dependência externa:

```text
sucesso
timeout
erro
credencial inválida
resposta inesperada
```

quando aplicável.

---

# 93. Documentação de dependência

Toda dependência externa relevante deverá informar:

```text
finalidade
responsável
dados enviados
dados recebidos
credenciais
falhas esperadas
```

---

# 94. Inventário

O inventário de dependências deverá permanecer atualizado quando novas integrações forem adicionadas.

---

# 95. Dependências atuais do MVP

```text
React
FastAPI
SQLAlchemy
MySQL
Instagram
Provedor de IA
NGINX
Hostinger VPS
```

Ferramentas adicionais somente deverão entrar quando necessárias.

---

# 96. O que não faz parte da arquitetura atual

Não considerar como dependências do MVP:

```text
SocialKit
```

O projeto não utilizará SocialKit.

---

# 97. Regra explícita

A integração com o Instagram será realizada diretamente por meio dos mecanismos oficiais disponibilizados pela plataforma e pelo fluxo de conta autorizada definido na documentação do projeto.

Não criar uma camada de serviço intermediária de publicação de terceiros.

---

# 98. Evolução para múltiplas redes

Quando uma segunda rede social for adicionada:

```text
avaliar abstração
 ↓
criar conector específico
 ↓
manter domínio independente
 ↓
adicionar testes
```

---

# 99. Critério de sucesso

A matriz de dependências estará adequada quando:

```text
cada componente possui responsabilidade clara
+
integrações externas estão isoladas
+
não existem dependências circulares desnecessárias
+
o domínio não está preso à infraestrutura
+
falhas externas são tratáveis
+
novas redes/IA podem ser adicionadas sem reescrever o núcleo
```

---

# 100. Regra final

> **O ViralCode deve depender de capacidades, e não ficar acoplado desnecessariamente às tecnologias que fornecem essas capacidades.**

Arquitetura desejada:

```text
NEGÓCIO
   ↓
SERVIÇOS
   ↓
ABSTRAÇÕES
   ↓
IMPLEMENTAÇÕES
   ↓
SISTEMAS EXTERNOS
```

**Versão:** 1.0  
**Status:** Documento oficial da Matriz de Dependências e Integrações
