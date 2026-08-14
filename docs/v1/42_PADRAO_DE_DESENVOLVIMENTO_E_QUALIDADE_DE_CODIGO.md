# 42 — PADRÃO DE DESENVOLVIMENTO E QUALIDADE DE CÓDIGO

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define as regras para desenvolvimento e manutenção do código do ViralCode.

O objetivo é garantir:

```text
consistência
legibilidade
manutenção
segurança
testabilidade
evolução
```

---

# 2. Princípio fundamental

O código deverá ser escrito para:

```text
ser entendido por outra pessoa
```

e não apenas para:

```text
funcionar no momento
```

---

# 3. Idioma

O projeto deverá utilizar português como idioma principal.

Preferir:

```text
usuario
perfil
conteudo
publicacao
analise
servico
repositorio
```

quando não houver necessidade de utilizar nomenclatura oficial externa.

---

# 4. Termos externos

Tecnologias e protocolos poderão manter seus nomes oficiais:

```text
React
FastAPI
SQLAlchemy
MySQL
Instagram
OAuth
JSON
HTTP
API
```

---

# 5. Nomenclatura

Os nomes deverão ser claros e descritivos.

Evitar:

```text
x
tmp
abc
foo
bar
```

quando representarem lógica de negócio.

---

# 6. Regra de clareza

Preferir:

```text
usuario_autenticado
```

a:

```text
u
```

quando a clareza for prejudicada.

---

# 7. Python

No backend, seguir convenções idiomáticas do Python.

Exemplo:

```text
snake_case
```

para funções e variáveis.

---

# 8. Classes

Classes deverão utilizar nomenclatura consistente.

Exemplo:

```text
ServicoConteudo
RepositorioConteudo
ConectorInstagram
```

---

# 9. React

Componentes deverão utilizar nomenclatura consistente.

Exemplo:

```text
CartaoConteudo
TabelaPublicacoes
PaginaDashboard
```

---

# 10. Arquivos

Nomes de arquivos deverão ser previsíveis.

Exemplo:

```text
servico_conteudo.py
repositorio_conteudo.py
```

ou padrão equivalente adotado pelo framework.

O projeto deverá escolher um padrão e mantê-lo.

---

# 11. Funções

Funções deverão possuir uma responsabilidade clara.

Evitar funções que:

```text
consultam banco
chamam IA
enviam Instagram
formatam tela
```

ao mesmo tempo.

---

# 12. Classes

Classes não deverão acumular responsabilidades sem relação.

---

# 13. Responsabilidade única

Preferir:

```text
Serviço
 ↓
regra de negócio
```

e:

```text
Repositório
 ↓
persistência
```

---

# 14. Separação de camadas

A arquitetura oficial permanece:

```text
API
 ↓
SERVIÇOS
 ↓
REPOSITÓRIOS / CONECTORES
 ↓
INFRAESTRUTURA
```

---

# 15. Rotas

Rotas FastAPI deverão ser responsáveis principalmente por:

```text
receber requisição
validar entrada
autenticar
autorizar
chamar serviço
retornar resposta
```

---

# 16. Regra de negócio

Regras de negócio pertencem aos serviços/domínio.

Não colocar regras importantes diretamente na rota.

---

# 17. Banco

Operações de banco pertencem aos repositórios ou camada de persistência definida.

Não espalhar SQL por todo o projeto.

---

# 18. SQLAlchemy

O acesso ao MySQL deverá utilizar SQLAlchemy conforme a arquitetura definida.

---

# 19. Conectores externos

Instagram e outros serviços externos deverão permanecer isolados.

```text
Serviço
 ↓
Conector
 ↓
Serviço externo
```

---

# 20. IA

Chamadas de IA deverão passar pelo Serviço de IA definido na arquitetura.

Não chamar diretamente o provedor em qualquer serviço.

---

# 21. Frontend

Componentes React não deverão conter regras críticas de negócio.

---

# 22. Comunicação

Preferir:

```text
Componente
 ↓
Serviço frontend
 ↓
API
```

---

# 23. Duplicação

Antes de criar código novo:

```text
procurar implementação existente
```

---

# 24. Abstração

Não criar abstrações antecipadamente.

Criar abstração quando existir:

```text
repetição real
+
necessidade real
```

---

# 25. Código morto

Não manter:

```text
funções sem uso
imports sem uso
componentes abandonados
```

sem motivo documentado.

---

# 26. Comentários

Comentários devem explicar:

```text
por quê
```

e não apenas:

```text
o que
```

Exemplo ruim:

```python
# soma dois números
resultado = a + b
```

---

# 27. Comentário útil

Exemplo:

```python
# Mantemos a consulta limitada para evitar chamadas desnecessárias à API externa.
```

---

# 28. Código autoexplicativo

Preferir nomes claros a comentários excessivos.

---

# 29. TODO

TODOs deverão possuir contexto suficiente.

Evitar:

```text
TODO: melhorar
```

Preferir:

```text
TODO: substituir consulta por processamento assíncrono quando o volume justificar.
```

---

# 30. Tratamento de erros

Não utilizar:

```python
except:
    pass
```

para esconder erros.

---

# 31. Exceções

Capturar somente exceções que possam ser tratadas corretamente.

---

# 32. Mensagem de erro

Mensagens internas deverão ajudar diagnóstico.

Mensagens externas deverão ser seguras e compreensíveis.

---

# 33. Logs

Logs deverão conter informações úteis para investigação.

Quando aplicável:

```text
correlation_id
operacao
status
```

---

# 34. Segredos

Nunca registrar:

```text
senha
token
client_secret
chave de IA
```

---

# 35. Configuração

Configurações deverão vir da camada central de configuração.

---

# 36. Testabilidade

Código novo deverá ser criado de forma que possa ser testado.

Evitar acoplamento desnecessário a:

```text
filesystem
rede
banco
API externa
```

---

# 37. Injeção de dependência

Quando apropriado, utilizar injeção de dependência para facilitar testes e substituição de implementações.

---

# 38. Mock

Mocks deverão ser utilizados principalmente para:

```text
Instagram
IA
serviços externos
```

quando o teste não precisar chamar o serviço real.

---

# 39. Não mockar tudo

Não transformar todos os testes em mocks.

Integrações reais deverão existir em testes apropriados.

---

# 40. Tipagem

O código deverá utilizar tipagem quando ela melhorar segurança e clareza.

---

# 41. Validação

Dados externos deverão ser validados antes de entrarem no domínio.

---

# 42. Dados do usuário

Nunca confiar automaticamente em:

```text
entrada do frontend
```

---

# 43. Dados externos

Nunca confiar automaticamente em:

```text
Instagram
IA
arquivos enviados
conteúdo importado
```

---

# 44. Segurança por padrão

Preferir:

```text
bloquear por padrão
```

a:

```text
permitir por padrão
```

---

# 45. Autorização

Toda operação privada deverá verificar propriedade/permissão.

---

# 46. IDOR

Toda operação que recebe identificador de recurso deverá considerar tentativa de acesso a recurso de outro usuário.

---

# 47. SQL

Não concatenar entrada do usuário diretamente em SQL.

---

# 48. Frontend

Não renderizar conteúdo externo de forma insegura.

---

# 49. Prompt Injection

Conteúdo externo utilizado pela IA deverá ser tratado como dado.

---

# 50. Dependências

Adicionar uma biblioteca somente quando houver benefício real.

Antes de adicionar:

```text
verificar se a stack existente resolve
```

---

# 51. Dependência pequena

Evitar biblioteca pesada para resolver problema simples.

---

# 52. Atualizações

Dependências deverão ser atualizadas de maneira controlada.

Não atualizar todas indiscriminadamente em produção.

---

# 53. Versões

Versões importantes deverão ser controladas.

---

# 54. Migrações

Alterações de banco deverão passar por migração.

Nunca depender de alteração manual em produção sem registro.

---

# 55. Compatibilidade

Alterações na API deverão considerar consumidores existentes.

---

# 56. Breaking change

Mudança incompatível deverá ser tratada explicitamente.

---

# 57. API

A API deverá seguir:

```text
34_CONTRATOS_DA_API_REST.md
```

---

# 58. Frontend

O frontend deverá seguir:

```text
35_ARQUITETURA_DO_FRONTEND.md
```

---

# 59. Autenticação

Alterações deverão seguir:

```text
36_ARQUITETURA_DE_AUTENTICACAO_E_AUTORIZACAO.md
```

---

# 60. Instagram

Alterações deverão seguir:

```text
37_INTEGRACAO_OFICIAL_COM_INSTAGRAM.md
```

---

# 61. IA

Alterações deverão seguir:

```text
38_ARQUITETURA_DO_PROVEDOR_DE_INTELIGENCIA_ARTIFICIAL.md
```

---

# 62. Configuração

Alterações deverão seguir:

```text
39_CONFIGURACAO_E_VARIAVEIS_DE_AMBIENTE.md
```

---

# 63. Infraestrutura

Alterações deverão seguir:

```text
40_INFRAESTRUTURA_LOCAL_E_VPS.md
```

---

# 64. Testes

Alterações deverão seguir:

```text
41_ESTRATEGIA_DE_TESTES.md
```

---

# 65. Formato de commit

O projeto deverá adotar mensagens de commit claras.

Exemplos:

```text
feat: adicionar análise de conteúdo
fix: corrigir autorização de publicação
refactor: separar serviço de conteúdo
test: adicionar testes de publicação
docs: atualizar arquitetura do Instagram
```

---

# 66. Commits

Um commit deverá preferencialmente representar uma mudança coerente.

Evitar misturar:

```text
nova funcionalidade
+
formatação de 40 arquivos
+
alteração de infraestrutura
```

sem necessidade.

---

# 67. Pull Request

Quando houver fluxo colaborativo, uma alteração deverá informar:

```text
o que mudou
por que mudou
como foi testado
```

---

# 68. Revisão de código

Antes de integrar código:

```text
arquitetura
segurança
testes
legibilidade
```

deverão ser avaliados.

---

# 69. IA como desenvolvedora

Agentes de IA poderão gerar código, mas deverão seguir a documentação do projeto.

---

# 70. Regra para agentes de IA

Antes de codificar:

```text
ler documentação relevante
 ↓
entender arquitetura
 ↓
localizar código existente
 ↓
implementar
 ↓
testar
 ↓
documentar quando necessário
```

---

# 71. IA não deve inventar arquitetura

Se houver dúvida:

```text
não criar nova camada automaticamente
```

---

# 72. IA não deve ignorar documentos

Documentos oficiais do projeto são referência arquitetural.

---

# 73. Alteração arquitetural

Se uma necessidade exigir mudança de arquitetura:

```text
identificar conflito
 ↓
avaliar impacto
 ↓
alterar documentação
 ↓
implementar
```

---

# 74. Não alterar documento para justificar código ruim

A documentação não deve ser modificada somente para esconder um desvio.

---

# 75. Regra de simplicidade

No MVP:

```text
menor solução que resolve corretamente
```

---

# 76. Evitar overengineering

Não implementar antecipadamente:

```text
microserviços
event sourcing
CQRS complexo
Kubernetes
Kafka
```

sem necessidade.

---

# 77. Preparado para crescer

Simplicidade não significa código descartável.

A arquitetura deverá possuir pontos claros de evolução.

---

# 78. Performance

Primeiro:

```text
correção
```

depois:

```text
performance
```

quando houver evidência de gargalo.

---

# 79. Banco

Evitar otimizações prematuras.

Mas consultas críticas deverão possuir atenção a:

```text
índices
paginação
N+1
```

---

# 80. N+1

Consultas que gerem múltiplas consultas desnecessárias deverão ser identificadas e corrigidas quando relevante.

---

# 81. Paginação

Listagens potencialmente grandes deverão utilizar paginação.

---

# 82. Cache

Adicionar somente quando houver benefício mensurável.

---

# 83. Concorrência

Operações críticas deverão considerar concorrência.

Exemplo:

```text
duas solicitações de publicação
```

---

# 84. Idempotência

Operações externas ou críticas deverão possuir proteção contra duplicidade quando necessário.

---

# 85. Transações

Alterações que precisam ser atômicas deverão utilizar transação adequada.

---

# 86. Estado

Evitar estados impossíveis.

Exemplo:

```text
publicação = PUBLICADA
```

sem possuir informação mínima de sucesso.

---

# 87. Máquina de estados

Quando uma entidade possuir muitos estados, documentar explicitamente as transições.

---

# 88. Dados nulos

Não usar valores mágicos.

Evitar:

```text
""
0
-1
```

para representar ausência quando:

```text
NULL
```

for semanticamente correto.

---

# 89. Datas

Manter estratégia consistente de timezone.

---

# 90. Identificadores

Identificadores deverão possuir padrão consistente.

---

# 91. API externa

Não espalhar IDs externos sem contexto.

Preferir:

```text
identificador_externo
plataforma
```

---

# 92. Segurança

Toda alteração que envolva:

```text
autenticação
autorização
tokens
Instagram
IA
dados pessoais
```

deverá possuir revisão adicional.

---

# 93. Dados pessoais

Armazenar somente o necessário.

---

# 94. Auditoria

Ações administrativas relevantes deverão permanecer rastreáveis.

---

# 95. Documentação

Quando comportamento importante mudar:

```text
código
+
teste
+
documentação
```

deverão permanecer coerentes.

---

# 96. Definition of Done

Uma tarefa estará pronta quando:

```text
[ ] código implementado
[ ] testes relevantes
[ ] tratamento de erro
[ ] segurança considerada
[ ] documentação atualizada se necessário
[ ] lint/verificações executadas
[ ] sem segredo no código
[ ] arquitetura respeitada
```

---

# 97. Definition of Done — P0

Para funcionalidades críticas:

```text
[ ] testes unitários
[ ] teste de integração
[ ] teste de autorização
[ ] tratamento de erro
[ ] logs adequados
[ ] documentação
```

---

# 98. Antes de criar arquivo

Perguntar:

```text
já existe algo equivalente?
```

---

# 99. Antes de criar serviço

Perguntar:

```text
isso é uma responsabilidade nova?
```

---

# 100. Antes de criar dependência

Perguntar:

```text
a stack atual resolve?
```

---

# 101. Antes de criar abstração

Perguntar:

```text
há repetição real?
```

---

# 102. Antes de alterar banco

Perguntar:

```text
precisa de migração?
```

---

# 103. Antes de alterar API

Perguntar:

```text
quebra o contrato?
```

---

# 104. Antes de alterar Instagram

Perguntar:

```text
a API oficial suporta?
```

---

# 105. Antes de alterar IA

Perguntar:

```text
qual modelo?
qual prompt?
qual custo?
qual validação?
```

---

# 106. Antes de deploy

Perguntar:

```text
backup existe?
testes passaram?
configuração está correta?
```

---

# 107. Checklist de código

```text
[ ] nome claro
[ ] responsabilidade clara
[ ] sem duplicação desnecessária
[ ] sem segredo
[ ] erros tratados
[ ] testes
[ ] arquitetura respeitada
```

---

# 108. Critério de qualidade

Código bom no ViralCode é código:

```text
simples
claro
testável
seguro
modular
evolutivo
```

Não é código:

```text
mais sofisticado
```

sem necessidade.

---

# 109. Regra final

> **No ViralCode, primeiro entendemos a arquitetura, depois escrevemos o código.**

O código deverá ser consequência dos documentos, contratos, regras de negócio e testes — e não o contrário.

**Versão:** 1.0  
**Status:** Documento oficial do Padrão de Desenvolvimento e Qualidade de Código
