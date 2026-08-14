# 44 — PRIVACIDADE, LGPD E PROTEÇÃO DE DADOS

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode  
**Jurisdição inicial:** Brasil

---

## 1. Objetivo

Este documento define os princípios de privacidade e proteção de dados que deverão orientar o desenvolvimento do ViralCode.

O objetivo é estabelecer regras para:

```text
coleta
armazenamento
processamento
uso
compartilhamento
retenção
exclusão
segurança
```

dos dados tratados pelo sistema.

---

# 2. Princípio fundamental

O ViralCode deverá coletar e processar somente os dados necessários para executar suas funcionalidades.

Regra:

```text
necessidade
+
finalidade
+
segurança
```

---

# 3. LGPD

O projeto deverá considerar a:

```text
Lei Geral de Proteção de Dados Pessoais — LGPD
```

A implementação técnica não substitui análise jurídica especializada quando necessária.

---

# 4. Papel da documentação

Este documento define requisitos técnicos e de produto.

Não deverá ser interpretado como parecer jurídico.

---

# 5. Dados tratados

O ViralCode poderá tratar dados como:

```text
dados de cadastro
dados de autenticação
dados de perfil
dados de configuração
dados de conta social
dados de conteúdo
dados de métricas
dados de publicação
dados de uso do sistema
logs técnicos
```

---

# 6. Dados pessoais

Quando um dado puder identificar ou tornar identificável uma pessoa natural, deverá ser tratado com os cuidados correspondentes.

---

# 7. Minimização

Não armazenar dados apenas porque:

```text
"poderão ser úteis algum dia"
```

---

# 8. Finalidade

Cada grupo relevante de dados deverá possuir uma finalidade clara.

Exemplo:

```text
e-mail
→ autenticação/comunicação

conta Instagram
→ integração social

conteúdo
→ análise/criação/publicação
```

---

# 9. Dados de terceiros

Conteúdos ou dados obtidos de redes sociais poderão envolver informações de terceiros.

O sistema deverá evitar coletar dados que não sejam necessários para a finalidade do produto.

---

# 10. Conteúdo externo

Conteúdo do Instagram deverá ser tratado como:

```text
dado externo
```

e não como dado pertencente automaticamente ao ViralCode.

---

# 11. Dados de conta social

Credenciais e tokens de integração são dados críticos.

Deverão possuir proteção reforçada.

---

# 12. Tokens

Tokens não deverão aparecer em:

```text
frontend
logs
respostas API
prints
mensagens de erro
banco em texto exposto
```

---

# 13. Criptografia

Dados sensíveis em trânsito deverão utilizar:

```text
HTTPS/TLS
```

---

# 14. Segredos armazenados

Segredos persistidos deverão possuir proteção adequada.

Quando tecnicamente possível:

```text
criptografia em repouso
```

ou mecanismo equivalente.

---

# 15. Senhas

Senhas de usuários nunca deverão ser armazenadas em texto puro.

Deverão ser armazenadas utilizando mecanismo seguro de hash apropriado.

---

# 16. Autenticação

A arquitetura deverá seguir:

```text
36_ARQUITETURA_DE_AUTENTICACAO_E_AUTORIZACAO.md
```

---

# 17. Autorização

Um usuário deverá acessar somente os dados aos quais possui autorização.

---

# 18. Isolamento

O banco deverá manter relacionamento claro entre:

```text
usuário
perfil
conteúdo
publicação
conta social
```

para impedir acesso cruzado indevido.

---

# 19. IDOR

Toda API que recebe identificador deverá verificar:

```text
recurso pertence ao usuário?
```

Não confiar somente no ID fornecido pelo frontend.

---

# 20. Admin

A Área Administrativa deverá possuir autorização específica.

---

# 21. Administrador

Acesso administrativo deverá ser limitado às pessoas autorizadas.

---

# 22. Logs

Logs são dados operacionais e também podem conter informações pessoais.

Portanto:

```text
registrar somente o necessário
```

---

# 23. Não registrar dados desnecessários

Evitar colocar em logs:

```text
e-mail completo
telefone
token
senha
conteúdo sensível
```

quando não forem necessários para diagnóstico.

---

# 24. Correlation ID

Preferir identificação técnica:

```text
correlation_id
```

em vez de registrar grandes quantidades de dados pessoais para rastrear uma operação.

---

# 25. Dados enviados à IA

Antes de enviar dados ao provedor de IA:

```text
identificar
 ↓
minimizar
 ↓
remover dados desnecessários
 ↓
enviar somente contexto necessário
```

---

# 26. Conteúdo do usuário

Se o conteúdo do usuário for enviado para IA, isso deverá ocorrer somente quando necessário para a funcionalidade.

---

# 27. Provedor de IA

A integração com o provedor de IA deverá considerar:

```text
dados enviados
finalidade
retenção
segurança
contrato/termos aplicáveis
```

antes de colocar a funcionalidade em produção.

---

# 28. Instagram

A integração deverá respeitar as regras oficiais da plataforma.

Consultar:

```text
37_INTEGRACAO_OFICIAL_COM_INSTAGRAM.md
```

---

# 29. Dados obtidos do Instagram

Não assumir que todo dado acessível tecnicamente pode ser:

```text
armazenado
redistribuído
utilizado indefinidamente
```

---

# 30. Origem dos dados

Quando relevante, o sistema deverá saber se o dado é:

```text
PRÓPRIO
EXTERNO
GERADO
MANUAL
```

---

# 31. Conteúdo gerado por IA

Conteúdo gerado pelo sistema deverá possuir identificação interna de origem.

Exemplo:

```text
origem = GERADO
```

---

# 32. Histórico

Histórico deverá ser mantido somente quando houver finalidade operacional, analítica, contratual ou de segurança que justifique sua retenção.

---

# 33. Retenção

Cada tipo de dado deverá possuir uma estratégia de retenção.

Não manter dados indefinidamente sem necessidade.

---

# 34. Exemplos de retenção

Conceitualmente:

```text
logs técnicos
→ período limitado

tokens
→ enquanto integração estiver ativa

conteúdos
→ enquanto necessários ao produto

dados de auditoria
→ conforme necessidade operacional/legal
```

Os prazos definitivos deverão ser definidos conforme requisitos legais e de negócio.

---

# 35. Exclusão

Quando um usuário solicitar exclusão de dados, o sistema deverá possuir capacidade de identificar os dados relacionados à sua conta.

---

# 36. Exclusão de conta

O fluxo deverá considerar:

```text
usuário
 ↓
dados de perfil
 ↓
conteúdos
 ↓
publicações
 ↓
contas sociais
 ↓
execuções
 ↓
dados derivados
```

A exclusão definitiva deverá respeitar eventuais obrigações de retenção.

---

# 37. Desconexão não é exclusão

Desconectar Instagram significa:

```text
encerrar integração
```

Não necessariamente:

```text
apagar todo o histórico
```

Essas operações deverão ser separadas.

---

# 38. Revogação

Quando aplicável, a desconexão deverá também considerar a revogação da autorização na plataforma externa.

---

# 39. Backup

Dados excluídos da aplicação poderão continuar temporariamente presentes em backups.

A política de backup deverá considerar isso.

---

# 40. Restauração

Uma restauração de backup não deverá ser utilizada para reintroduzir intencionalmente dados que deveriam estar definitivamente excluídos sem avaliação adequada.

---

# 41. Exportação

O sistema deverá ser arquitetado de forma que seja possível identificar e exportar dados relevantes de um usuário quando necessário.

---

# 42. Portabilidade

Se uma funcionalidade de portabilidade for necessária, deverá ser definida separadamente.

---

# 43. Correção

Dados de usuário deverão poder ser corrigidos quando houver funcionalidade correspondente.

---

# 44. Consentimento

Consentimento é somente uma das possíveis bases jurídicas para tratamento.

A base aplicável deverá ser definida conforme a finalidade e orientação jurídica.

---

# 45. Não presumir base jurídica

O desenvolvedor não deverá decidir sozinho:

```text
"isso sempre precisa de consentimento"
```

ou:

```text
"isso nunca precisa"
```

sem análise adequada.

---

# 46. Termos e política

O produto deverá possuir, antes de uma operação comercial relevante:

```text
Termos de Uso
Política de Privacidade
```

revisados adequadamente.

---

# 47. Aceite

Quando houver necessidade de aceite:

```text
versão do documento
+
data/hora
+
usuário
```

poderão ser registrados.

---

# 48. Versionamento de política

Não sobrescrever silenciosamente versões antigas de documentos aceitos.

---

# 49. Registro de aceite

Quando relevante:

```text
usuario_id
documento
versao
data_aceite
```

---

# 50. Transparência

A interface deverá explicar de maneira compreensível:

```text
o que será conectado
o que será analisado
o que será publicado
```

---

# 51. Publicação

O usuário deverá saber claramente quando uma ação resultará em publicação no Instagram.

---

# 52. IA

O usuário deverá entender quando o conteúdo foi:

```text
gerado ou auxiliado por IA
```

quando isso for relevante para a experiência e transparência do produto.

---

# 53. Decisões automatizadas

O ViralCode deverá evitar apresentar a saída da IA como:

```text
verdade absoluta
```

especialmente em análises ou recomendações.

---

# 54. Revisão humana

Para ações relevantes, a arquitetura deverá permitir:

```text
IA gera
 ↓
usuário revisa
 ↓
usuário aprova
```

---

# 55. Publicação automática

A publicação automática deverá ser tratada como funcionalidade específica e exigir configuração explícita do usuário.

---

# 56. Segurança por padrão

Novas funcionalidades deverão começar com:

```text
menor privilégio
```

---

# 57. Privilégio mínimo

Um serviço deverá possuir somente as permissões necessárias.

---

# 58. Banco

Usuários da aplicação e usuários do banco deverão possuir permissões compatíveis com sua função.

---

# 59. MySQL

A aplicação não deverá utilizar uma conta MySQL com privilégios administrativos desnecessários.

---

# 60. Backup

Backups deverão possuir proteção contra acesso não autorizado.

---

# 61. VPS

A VPS deverá seguir:

```text
40_INFRAESTRUTURA_LOCAL_E_VPS.md
```

---

# 62. Configuração

Seguir:

```text
39_CONFIGURACAO_E_VARIAVEIS_DE_AMBIENTE.md
```

---

# 63. Segurança de desenvolvimento

Seguir:

```text
42_PADRAO_DE_DESENVOLVIMENTO_E_QUALIDADE_DE_CODIGO.md
```

---

# 64. Testes

Seguir:

```text
41_ESTRATEGIA_DE_TESTES.md
```

---

# 65. Incidentes

O projeto deverá possuir um processo para responder a:

```text
vazamento
acesso indevido
token comprometido
banco exposto
```

---

# 66. Incidente de segurança

Fluxo inicial:

```text
detectar
 ↓
conter
 ↓
preservar evidências
 ↓
revogar credenciais
 ↓
corrigir
 ↓
avaliar impacto
 ↓
documentar
```

---

# 67. Token comprometido

Se um token de Instagram for exposto:

```text
revogar/invalidar
+
reautenticar
+
investigar
```

---

# 68. Chave de IA comprometida

Se a chave do provedor de IA for exposta:

```text
revogar
+
gerar nova
+
atualizar produção
+
verificar consumo indevido
```

---

# 69. Senha comprometida

Se uma credencial de usuário for comprometida:

```text
invalidar sessão quando aplicável
+
permitir redefinição
+
avaliar impacto
```

---

# 70. Auditoria

Ações administrativas e operações de segurança relevantes deverão possuir rastreabilidade.

---

# 71. Dados de auditoria

Exemplo:

```text
usuario_id
acao
recurso
data_hora
correlation_id
resultado
```

---

# 72. Não registrar segredo na auditoria

Auditoria não deverá armazenar:

```text
senha
token
client_secret
chave privada
```

---

# 73. Subprocessadores

Serviços externos que recebam dados deverão ser identificados conforme a arquitetura do produto.

Exemplos:

```text
Meta/Instagram
provedor de IA
provedor de hospedagem
serviço de e-mail
```

quando utilizados.

---

# 74. Minimização com terceiros

Enviar a terceiros somente o necessário.

---

# 75. Transferência internacional

Se dados forem processados fora do Brasil, essa possibilidade deverá ser considerada na avaliação de privacidade e nos documentos aplicáveis.

---

# 76. Dados sensíveis

O ViralCode deverá evitar coletar dados pessoais sensíveis sem necessidade.

---

# 77. Conteúdo sensível

Mesmo que o produto não solicite dados sensíveis, conteúdos enviados pelos usuários poderão eventualmente conter informações desse tipo.

O sistema deverá tratar conteúdo do usuário com cautela.

---

# 78. Uploads

Arquivos enviados deverão possuir:

```text
validação
limite
controle de acesso
```

quando essa funcionalidade existir.

---

# 79. URLs externas

Não confiar automaticamente em URLs fornecidas por usuários.

---

# 80. Segurança contra abuso

Endpoints deverão considerar:

```text
rate limit
validação
autorização
limites de tamanho
```

---

# 81. Limite de dados

Evitar aceitar payloads maiores do que a funcionalidade necessita.

---

# 82. Retenção de prompts

Prompts completos poderão conter dados do usuário.

Se armazenados:

```text
finalidade
acesso
retenção
```

deverão ser definidos.

---

# 83. Retenção de respostas de IA

Mesma regra:

```text
armazenar somente se houver finalidade
```

---

# 84. Execução de IA

A entidade:

```text
ExecucaoIA
```

deverá evitar armazenar dados sensíveis desnecessariamente.

---

# 85. Métricas

Métricas de uso deverão ser coletadas somente na medida necessária para:

```text
produto
diagnóstico
segurança
melhoria
```

---

# 86. Analytics

Se futuramente houver analytics de produto, deverá ser avaliado quais dados realmente precisam ser coletados.

---

# 87. Cookies

Se o frontend utilizar cookies, deverá existir estratégia definida para:

```text
autenticação
sessão
preferências
analytics
```

---

# 88. Sessão

A sessão deverá ser protegida contra:

```text
roubo
fixação
reutilização indevida
```

---

# 89. Logout

Logout deverá invalidar a sessão conforme o mecanismo de autenticação utilizado.

---

# 90. Cache

Dados privados não deverão ser armazenados em cache compartilhado de forma que outro usuário possa acessá-los.

---

# 91. Frontend

Não armazenar segredos no:

```text
localStorage
sessionStorage
JavaScript público
```

quando isso representar risco de segurança.

A estratégia final dependerá do mecanismo de autenticação adotado.

---

# 92. API

Respostas deverão conter somente os campos necessários.

---

# 93. Overfetching

Não retornar indiscriminadamente o objeto inteiro do banco quando a tela necessita de poucos campos.

---

# 94. Underfetching

Também evitar múltiplas chamadas desnecessárias quando uma resposta adequada puder atender à tela.

---

# 95. Princípio de necessidade

Toda informação retornada deve responder:

```text
a tela/cliente precisa disso?
```

---

# 96. Admin

O administrador poderá acessar dados de usuários somente quando necessário para sua função.

---

# 97. Acesso administrativo

Ações administrativas críticas deverão ser auditáveis.

---

# 98. Desenvolvimento

Não copiar banco de produção para ambiente local sem anonimização ou justificativa adequada.

---

# 99. Dados reais

Preferir:

```text
dados fictícios
```

em desenvolvimento.

---

# 100. Dump de produção

Se um dump real for indispensável para diagnóstico:

```text
proteger
limitar acesso
anonimizar quando possível
eliminar após uso
```

---

# 101. Exclusão técnica

A exclusão de dados deverá considerar:

```text
banco principal
cache
arquivos
índices
backups
```

conforme aplicável.

---

# 102. Dados derivados

Excluir um usuário deverá considerar dados derivados relacionados à conta.

Exemplo:

```text
análises
insights
execuções
métricas internas
```

---

# 103. Dados agregados

Dados agregados e anonimizados poderão possuir tratamento diferente de dados identificáveis, desde que realmente não permitam identificação indevida.

---

# 104. Não assumir anonimização

Remover o nome não significa automaticamente:

```text
anonimizar
```

---

# 105. Pseudonimização

Quando apropriado, utilizar identificadores internos em vez de dados diretamente identificáveis.

---

# 106. Chaves internas

Preferir:

```text
usuario_id
```

em registros técnicos a repetir:

```text
e-mail
nome
```

sem necessidade.

---

# 107. Privacidade desde a concepção

Toda funcionalidade nova deverá considerar privacidade desde o início.

---

# 108. Checklist de nova funcionalidade

Antes de implementar:

```text
[ ] quais dados serão coletados?
[ ] por que são necessários?
[ ] onde serão armazenados?
[ ] quem poderá acessar?
[ ] por quanto tempo?
[ ] haverá terceiro?
[ ] haverá IA?
[ ] haverá Instagram?
[ ] como excluir?
```

---

# 109. Checklist de integração externa

```text
[ ] quais dados saem do ViralCode?
[ ] para quem?
[ ] por quê?
[ ] quais permissões?
[ ] quanto tempo?
[ ] como revogar?
```

---

# 110. Checklist de banco

```text
[ ] dado necessário
[ ] acesso restrito
[ ] índice adequado
[ ] retenção definida
[ ] exclusão possível
```

---

# 111. Checklist de API

```text
[ ] autenticação
[ ] autorização
[ ] validação
[ ] payload mínimo
[ ] resposta mínima
[ ] logs seguros
```

---

# 112. Checklist de frontend

```text
[ ] não expõe segredo
[ ] não confia no usuário
[ ] não expõe dados de outro usuário
[ ] conteúdo externo tratado com cautela
```

---

# 113. Checklist de produção

```text
[ ] HTTPS
[ ] firewall
[ ] segredos protegidos
[ ] backup
[ ] logs
[ ] acesso administrativo restrito
[ ] monitoramento
```

---

# 114. Regra para agentes de IA

Antes de implementar qualquer funcionalidade que envolva dados:

1. identificar quais dados entram;
2. identificar quais dados saem;
3. verificar finalidade;
4. verificar autorização;
5. verificar retenção;
6. verificar segurança;
7. atualizar documentação quando necessário;
8. criar testes de segurança.

---

# 115. Regra contra coleta excessiva

Uma IA não deverá criar automaticamente:

```text
novos campos pessoais
novos logs pessoais
novos dados externos
```

sem necessidade funcional.

---

# 116. Regra contra exposição

Uma IA não deverá retornar:

```text
dados de outro usuário
segredos
tokens
informações administrativas
```

por conveniência de implementação.

---

# 117. Critério de sucesso

A arquitetura estará adequada quando:

```text
dados necessários são conhecidos
+
finalidade é clara
+
acesso é controlado
+
segredos são protegidos
+
retenção é definida
+
exclusão é possível
+
integrações externas são controladas
+
logs são minimizados
+
testes protegem os cenários críticos
```

---

# 118. Regra final

> **O ViralCode deve tratar dados como responsabilidade do produto, não como simples informação disponível no banco.**

A regra arquitetural será:

```text
COLETAR O NECESSÁRIO
        ↓
USAR PARA A FINALIDADE
        ↓
PROTEGER
        ↓
RETER PELO TEMPO NECESSÁRIO
        ↓
EXCLUIR QUANDO NÃO FOR MAIS NECESSÁRIO
```

**Versão:** 1.0  
**Status:** Documento oficial de Privacidade, LGPD e Proteção de Dados
