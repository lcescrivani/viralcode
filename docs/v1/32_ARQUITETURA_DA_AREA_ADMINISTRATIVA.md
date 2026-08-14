# 32 — ARQUITETURA DA ÁREA ADMINISTRATIVA

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define a arquitetura da Área Administrativa do ViralCode.

A Área Administrativa será utilizada para:

```text
administrar
monitorar
diagnosticar
auditar
configurar
```

o funcionamento do sistema.

Ela não deverá ser confundida com a área utilizada pelos clientes.

---

# 2. Princípio fundamental

O ViralCode terá duas experiências distintas:

```text
ÁREA DO USUÁRIO
→ utilizar o produto

ÁREA ADMINISTRATIVA
→ administrar o produto
```

---

# 3. Separação

Arquitetura:

```text
                    VIRALCODE
                       │
              ┌────────┴────────┐
              ▼                 ▼
        ÁREA DO USUÁRIO      ÁREA ADMIN
              │                 │
              ▼                 ▼
         funcionalidades     administração
         do produto           do sistema
```

---

# 4. Acesso administrativo

A Área Administrativa deverá exigir:

```text
autenticação
+
autorização administrativa
```

Não será suficiente estar autenticado.

---

# 5. Regra de segurança

Um usuário comum:

```text
PODE
→ utilizar seus recursos

NÃO PODE
→ acessar recursos administrativos
```

Um administrador:

```text
PODE
→ acessar recursos administrativos
```

de acordo com suas permissões.

---

# 6. Não confiar no frontend

O bloqueio administrativo deverá existir no backend.

Mesmo que o frontend esconda:

```text
/administracao
```

um usuário comum não poderá chamar diretamente:

```text
/api/v1/admin/*
```

---

# 7. Perfil administrativo

A arquitetura deverá permitir futuramente diferentes níveis administrativos.

Exemplo:

```text
ADMINISTRADOR
SUPORTE
OPERADOR
ANALISTA
```

No MVP poderá existir somente:

```text
ADMINISTRADOR
```

---

# 8. Regra de privilégio mínimo

Cada perfil administrativo deverá possuir somente as permissões necessárias.

Não criar:

```text
admin = acesso irrestrito
```

como regra definitiva da arquitetura.

---

# 9. Área Admin no frontend

A área poderá possuir uma estrutura separada:

```text
frontend/
└── administrativo/
```

ou estrutura equivalente.

O importante é separar:

```text
componentes
rotas
menus
permissões
```

da experiência do usuário.

---

# 10. Menu administrativo

Menu inicial:

```text
Dashboard
Usuários
Perfis
Contas Sociais
Conteúdos
Análises
Publicações
IA
Erros
Logs
Auditoria
Configurações
```

Alguns itens poderão ser implementados posteriormente.

---

# 11. Dashboard Administrativo

O Dashboard deverá apresentar uma visão rápida da saúde do produto.

Indicadores iniciais:

```text
usuários
perfis
contas Instagram
conteúdos
publicações
erros
execuções de IA
```

---

# 12. Indicadores do Dashboard

Exemplo:

```text
USUÁRIOS ATIVOS
CONTAS CONECTADAS
CONTEÚDOS GERADOS
PUBLICAÇÕES
ERROS NAS ÚLTIMAS 24H
CHAMADAS DE IA
CUSTO ESTIMADO DE IA
```

---

# 13. Saúde do sistema

O Dashboard poderá mostrar:

```text
API
BANCO
INSTAGRAM
IA
```

com estados:

```text
OK
ATENÇÃO
ERRO
```

---

# 14. Não transformar Dashboard em monitoramento técnico completo

O Dashboard administrativo deverá fornecer visão resumida.

Detalhes deverão estar em:

```text
Logs
Erros
Monitoramento
```

---

# 15. Usuários

A tela de usuários deverá permitir:

```text
listar
buscar
filtrar
visualizar
```

No MVP, alterações administrativas deverão ser limitadas.

---

# 16. Dados exibidos do usuário

Exemplo:

```text
ID
nome
e-mail
status
data de cadastro
último acesso
quantidade de perfis
```

Não exibir:

```text
senha
hash da senha
tokens
segredos
```

---

# 17. Busca de usuário

Deverá permitir busca por:

```text
nome
e-mail
ID
```

---

# 18. Status do usuário

Poderá possuir estados como:

```text
ATIVO
BLOQUEADO
PENDENTE
```

Os estados definitivos deverão seguir o modelo de domínio.

---

# 19. Bloqueio

Se implementado:

```text
ADMIN
 ↓
BLOQUEAR USUÁRIO
 ↓
usuário perde acesso
```

A ação deverá ser registrada em auditoria.

---

# 20. Perfis

A tela de perfis deverá permitir visualizar:

```text
usuário
nome do perfil
nicho
subnicho
contas sociais
quantidade de conteúdos
```

---

# 21. Contas sociais

A tela deverá permitir acompanhar:

```text
usuário
perfil
plataforma
identificador externo
status
data de conexão
```

---

# 22. Credenciais

A Área Administrativa nunca deverá exibir:

```text
token completo
client secret
senha
chave privada
```

Mesmo para administradores.

---

# 23. Estado da conta social

Exemplo:

```text
CONECTADA
REAUTENTICAÇÃO NECESSÁRIA
DESCONECTADA
ERRO
```

---

# 24. Conteúdos

A administração deverá permitir localizar conteúdos.

Filtros possíveis:

```text
usuário
perfil
nicho
tipo
status
data
```

---

# 25. Conteúdo externo

Deverá ser possível distinguir:

```text
conteúdo externo
```

de:

```text
conteúdo criado pelo ViralCode
```

---

# 26. Análises

A administração poderá permitir visualizar:

```text
conteúdo
status
modelo IA
versão do prompt
data
tempo de execução
```

Quando essas informações forem persistidas.

---

# 27. Execuções de IA

Esta será uma área importante para o MVP.

Permitir visualizar:

```text
tipo de execução
usuário
conteúdo
modelo
status
tempo
tokens quando disponíveis
custo estimado quando disponível
data
```

---

# 28. Erros de IA

Exemplo:

```text
modelo indisponível
timeout
resposta inválida
limite
erro de autenticação
```

Deverão possuir identificação suficiente para diagnóstico.

---

# 29. Custos de IA

A Área Administrativa poderá mostrar:

```text
chamadas
tokens
custo estimado
custo por período
custo por usuário
custo por operação
```

quando os dados estiverem disponíveis.

---

# 30. Publicações

A administração deverá permitir consultar:

```text
conteúdo
usuário
perfil
conta social
plataforma
status
data
identificador externo
```

---

# 31. Estados da publicação

Exemplo:

```text
PENDENTE
ENVIANDO
PUBLICADA
ERRO
CANCELADA
```

---

# 32. Diagnóstico de publicação

Quando uma publicação falhar, o administrador deverá conseguir encontrar:

```text
usuário
conteúdo
conta
tentativa
status
erro
correlation_id
```

---

# 33. Reprocessamento

Operações administrativas que possam causar efeitos externos deverão ser tratadas com extremo cuidado.

Não criar inicialmente um botão genérico:

```text
PUBLICAR NOVAMENTE
```

sem proteção contra duplicidade.

---

# 34. Reconciliação

Quando houver dúvida sobre o estado de uma publicação externa:

```text
estado interno
      ↓
consulta externa
      ↓
reconciliação
```

poderá ser utilizada.

---

# 35. Logs

A Área Administrativa poderá consultar logs relevantes da aplicação.

Filtros:

```text
nível
data
correlation_id
usuário
componente
evento
```

---

# 36. Não expor segredos nos logs

Mesmo na Área Administrativa, nunca mostrar:

```text
senha
token
client_secret
chave privada
```

---

# 37. Correlation ID

A administração deverá permitir pesquisar por:

```text
correlation_id
```

Isso permitirá acompanhar uma operação específica.

---

# 38. Exemplo de diagnóstico

Usuário informa:

```text
"Não consegui publicar."
```

Administrador pesquisa:

```text
correlation_id
```

e encontra:

```text
publicação
 ↓
serviço
 ↓
Instagram
 ↓
erro
```

---

# 39. Auditoria

A Área Administrativa deverá possuir acesso a eventos administrativos importantes.

Exemplo:

```text
administrador
ação
recurso
data
resultado
```

---

# 40. Eventos de auditoria

Exemplos:

```text
ADMIN_LOGIN
USUARIO_BLOQUEADO
USUARIO_DESBLOQUEADO
CONFIGURACAO_ALTERADA
CONTA_SOCIAL_ALTERADA
```

A lista definitiva poderá evoluir.

---

# 41. Auditoria não é log

```text
LOG
→ evento técnico

AUDITORIA
→ ação administrativa ou de negócio relevante
```

---

# 42. Configurações

A Área Administrativa poderá futuramente controlar configurações globais.

Exemplos:

```text
limites
ativação de funcionalidades
parâmetros de geração
configurações operacionais
```

---

# 43. Segredos não devem ser administrados pela interface

Não criar uma tela para exibir:

```text
CHAVE_IA
CLIENT_SECRET
SENHA_MYSQL
```

Segredos deverão permanecer no mecanismo de configuração seguro definido pelo projeto.

---

# 44. Feature Flags

Futuramente poderá existir:

```text
feature flags
```

para ativar/desativar funcionalidades.

No MVP não é obrigatório implementar um sistema sofisticado.

---

# 45. Nichos

A Área Administrativa poderá futuramente permitir administrar:

```text
nichos
subnichos
categorias
```

Isso ajudará o produto a crescer para diferentes mercados.

---

# 46. Primeiro nicho

O sistema não deverá possuir lógica administrativa específica somente para:

```text
casamento
```

O nicho deverá ser tratado como configuração/dado.

---

# 47. Suporte

Futuramente a Área Administrativa poderá possuir ferramentas para suporte:

```text
visualizar usuário
visualizar perfil
visualizar erros
visualizar histórico
```

---

# 48. Acesso como usuário

Uma funcionalidade futura poderá permitir ao suporte reproduzir a experiência de um usuário.

Porém, isso deverá possuir controles fortes e auditoria.

Não implementar no MVP sem necessidade.

---

# 49. Impersonação

Se futuramente existir:

```text
"entrar como usuário"
```

deverá:

```text
ser explícita
ser auditada
possuir duração limitada
não expor senha
```

---

# 50. Segurança da Área Admin

A Área Administrativa deverá possuir proteção superior à área comum.

Considerar futuramente:

```text
2FA
restrição de IP
sessão menor
reauthentication
```

No MVP, autenticação administrativa forte deverá ser priorizada.

---

# 51. Sessão administrativa

Sessões administrativas deverão possuir:

```text
expiração
invalidação
controle
```

---

# 52. Ações destrutivas

Ações como:

```text
bloquear
excluir
desconectar
alterar
```

deverão exigir confirmação quando apropriado.

---

# 53. Exclusão

Não oferecer exclusão definitiva de dados importantes sem:

```text
confirmação
permissão
auditoria
```

---

# 54. Operações irreversíveis

Antes de qualquer operação irreversível:

```text
avaliar impacto
backup quando necessário
confirmar
auditar
```

---

# 55. APIs administrativas

As APIs deverão ser separadas conceitualmente:

```text
/api/v1/admin/usuarios
/api/v1/admin/perfis
/api/v1/admin/contas-sociais
/api/v1/admin/conteudos
/api/v1/admin/publicacoes
/api/v1/admin/ia
/api/v1/admin/logs
/api/v1/admin/auditoria
```

Os endpoints definitivos serão definidos durante a implementação.

---

# 56. Autorização da API

Toda rota administrativa deverá verificar:

```text
usuário autenticado
+
permissão administrativa
```

---

# 57. Regra de isolamento

Mesmo um administrador não deverá receber mais dados do que o necessário para executar sua função.

---

# 58. Paginação

Listagens administrativas deverão possuir paginação.

Principalmente:

```text
usuários
conteúdos
logs
publicações
execuções IA
```

---

# 59. Filtros

A administração deverá possuir filtros por:

```text
data
status
usuário
perfil
tipo
erro
plataforma
```

quando fizer sentido.

---

# 60. Ordenação

Deverá ser possível ordenar por:

```text
data
status
tempo
custo
```

quando aplicável.

---

# 61. Exportação

Não é prioridade do MVP.

Futuramente poderá existir exportação de:

```text
relatórios
métricas
usuários
custos
```

com controle de acesso.

---

# 62. Dashboard de produto

A administração deverá poder acompanhar:

```text
usuários
retenção
conteúdos
publicações
```

quando essas métricas forem implementadas.

---

# 63. Dashboard técnico

Separadamente:

```text
API
Banco
Instagram
IA
VPS
```

---

# 64. Dashboard de IA

Futuramente poderá apresentar:

```text
chamadas
sucesso
falhas
tempo médio
tokens
custo
modelo
```

---

# 65. Dashboard de Instagram

Poderá apresentar:

```text
contas conectadas
consultas
publicações
falhas
reauthenticações
```

---

# 66. MVP — o que realmente será construído

No MVP, priorizar:

```text
Dashboard
Usuários
Perfis
Contas Instagram
Conteúdos
Publicações
Execuções IA
Erros
```

---

# 67. MVP — prioridade P0

```text
LOGIN ADMIN
DASHBOARD
USUÁRIOS
CONTAS SOCIAIS
CONTEÚDOS
PUBLICAÇÕES
ERROS
```

---

# 68. MVP — prioridade P1

```text
EXECUÇÕES IA
CUSTOS IA
AUDITORIA
MÉTRICAS
```

---

# 69. Futuro — prioridade P2

```text
SUPORTE
FEATURE FLAGS
GESTÃO DE NICHOS
EXPORTAÇÕES
IMPERSONAÇÃO CONTROLADA
DASHBOARDS AVANÇADOS
```

---

# 70. Não fazer no MVP

Não implementar inicialmente:

```text
CMS administrativo completo
gestão financeira completa
CRM
sistema de tickets
permissões extremamente granulares
impersonação
workflow de aprovação administrativo complexo
```

---

# 71. Arquitetura frontend

Conceitualmente:

```text
frontend/
├── paginas/
│   ├── usuario/
│   └── administrativo/
│
├── componentes/
│   ├── usuario/
│   └── administrativo/
│
└── servicos/
    ├── api/
    └── administrativo/
```

A estrutura definitiva poderá ser ajustada ao padrão adotado no React.

---

# 72. Arquitetura backend

Conceitualmente:

```text
backend/app/
├── rotas/
│   ├── usuario/
│   └── administrativo/
│
├── servicos/
│   ├── usuario/
│   └── administrativo/
│
└── repositorios/
```

A Área Administrativa deverá reutilizar serviços de domínio quando possível, sem duplicar regras.

---

# 73. Não duplicar regra

Exemplo:

```text
servico_publicacao
```

deverá continuar sendo responsável pela publicação.

O Admin não deverá criar:

```text
servico_publicacao_admin
```

com outra regra de publicação.

---

# 74. Regra de reutilização

A Área Administrativa deverá atuar como:

```text
interface administrativa
+
permissões administrativas
```

sobre o domínio existente.

---

# 75. Banco

Poderão existir entidades administrativas específicas, como:

```text
Administrador
Auditoria
```

quando necessário.

Não duplicar entidades de negócio somente porque existe uma tela administrativa.

---

# 76. Auditoria administrativa

Exemplo:

```text
Administrador 1
   ↓
bloqueou usuário 45
   ↓
13/08/2026 22:30
```

---

# 77. Proteção contra abuso interno

A arquitetura deverá permitir saber:

```text
qual administrador
qual ação
qual recurso
quando
```

---

# 78. Logs de acesso administrativo

Registrar pelo menos:

```text
login administrativo
logout
falha de login
ações críticas
```

---

# 79. Dados sensíveis na Área Admin

A interface deverá mascarar ou ocultar dados que não sejam necessários.

Exemplo:

```text
token:
••••••••••••••••
```

---

# 80. Regra de suporte

O administrador deverá conseguir diagnosticar problemas sem precisar acessar diretamente:

```text
MySQL
VPS
arquivos de configuração
```

para as situações comuns.

---

# 81. Exceção

Acesso direto à infraestrutura poderá continuar sendo necessário para:

```text
incidentes graves
manutenção
deploy
```

Mas não deverá ser o mecanismo normal de operação do produto.

---

# 82. Fluxo de diagnóstico administrativo

```text
Usuário relata problema
       ↓
Admin pesquisa usuário
       ↓
localiza perfil
       ↓
localiza operação
       ↓
consulta publicação/IA
       ↓
consulta correlation_id
       ↓
consulta erro
       ↓
diagnóstico
```

---

# 83. Fluxo de bloqueio

```text
Admin
 ↓
Usuários
 ↓
Seleciona usuário
 ↓
Bloquear
 ↓
Confirma
 ↓
Serviço
 ↓
Banco
 ↓
Auditoria
```

---

# 84. Fluxo de consulta de IA

```text
Admin
 ↓
Execuções IA
 ↓
Seleciona execução
 ↓
Visualiza:
modelo
status
tempo
tokens
custo
erro
```

---

# 85. Fluxo de consulta de publicação

```text
Admin
 ↓
Publicações
 ↓
Seleciona publicação
 ↓
Visualiza:
conteúdo
usuário
conta
status
tentativas
erro
correlation_id
```

---

# 86. Fluxo de auditoria

```text
Admin
 ↓
Auditoria
 ↓
Filtro
 ↓
Evento
 ↓
Detalhes
```

---

# 87. Critério de sucesso

A Área Administrativa estará adequada quando o administrador conseguir:

```text
saber se o sistema está saudável
+
encontrar um usuário
+
encontrar um conteúdo
+
ver uma publicação
+
identificar uma falha
+
diagnosticar uma integração
+
acompanhar IA
```

sem precisar consultar diretamente o banco para operações normais.

---

# 88. Regra para agentes de IA

Antes de criar ou alterar uma função administrativa:

1. verificar se ela realmente pertence ao Admin;
2. validar permissão;
3. reutilizar serviços existentes;
4. não duplicar regra de negócio;
5. proteger dados sensíveis;
6. registrar ações críticas;
7. criar testes;
8. atualizar esta documentação.

---

# 89. Regra contra acesso privilegiado

Nunca implementar:

```text
if usuario:
    mostrar_admin()
```

sem verificar autorização no backend.

A regra deverá estar no servidor.

---

# 90. Regra final

> **A Área Administrativa deve permitir administrar e diagnosticar o ViralCode sem se tornar um segundo produto.**

No MVP ela será pequena:

```text
DASHBOARD
USUÁRIOS
PERFIS
INSTAGRAM
CONTEÚDOS
PUBLICAÇÕES
IA
ERROS
```

e crescerá conforme a operação exigir.

A arquitetura oficial fica:

```text
                         VIRALCODE
                            │
               ┌────────────┴────────────┐
               ▼                         ▼
        ÁREA DO USUÁRIO             ÁREA ADMIN
               │                         │
               ▼                         ▼
          PRODUTO                   OPERAÇÃO
               │                         │
               └────────────┬────────────┘
                            ▼
                       MESMO DOMÍNIO
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
        MySQL             IA              Instagram
```

**Versão:** 1.0  
**Status:** Documento oficial da Arquitetura da Área Administrativa
