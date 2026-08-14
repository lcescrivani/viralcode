# AGENTS.md — Instruções do Agente de Desenvolvimento do ViralCode

## 1. Identidade do projeto

Você é o agente de desenvolvimento do **ViralCode**.

Sua responsabilidade é implementar o sistema de acordo com a documentação oficial existente no diretório:

```text
docs/
```

A documentação é a principal fonte de verdade arquitetural do projeto.

---

# 2. Regra principal

Antes de implementar qualquer funcionalidade:

1. leia este `AGENTS.md`;
2. leia os documentos relevantes em `docs/`;
3. verifique o código que já existe;
4. identifique o que já foi implementado;
5. implemente somente a próxima etapa necessária;
6. teste;
7. corrija os problemas encontrados;
8. documente mudanças arquiteturais relevantes;
9. apresente um resumo do que foi feito.

Não reescreva partes funcionais do sistema sem necessidade.

---

# 3. Objetivo do MVP

O objetivo inicial é validar o negócio com o menor sistema funcional possível.

O MVP deve priorizar:

```text
simplicidade
+
funcionalidade
+
validação do negócio
+
baixo custo
+
facilidade de manutenção
```

Não implementar funcionalidades futuras somente porque a arquitetura permite.

---

# 4. Arquitetura tecnológica

A arquitetura inicial definida para o projeto é:

```text
React
   ↓
FastAPI
   ↓
Serviços
   ↓
Repositórios / Conectores
   ↓
SQLAlchemy / Integrações
   ↓
MySQL / Serviços externos
```

Tecnologias principais:

```text
Frontend: React
Backend: FastAPI
ORM: SQLAlchemy
Banco: MySQL
Infraestrutura inicial: VPS Hostinger
```

---

# 5. Idioma oficial

O projeto deverá utilizar **Português do Brasil**.

Isso inclui, sempre que tecnicamente apropriado:

```text
classes
funções
variáveis
métodos
serviços
repositórios
entidades
rotas
mensagens
documentação
comentários
```

Exceções são permitidas para nomes próprios de tecnologias, protocolos e padrões técnicos.

Exemplos:

```text
React
FastAPI
SQLAlchemy
MySQL
HTTP
HTTPS
JSON
OAuth
Git
Docker
API
```

---

# 6. Regra absoluta sobre SocialKit

**O ViralCode NÃO utiliza SocialKit.**

Não adicionar:

```text
SocialKit
```

como dependência, serviço, conector, API ou solução intermediária.

A integração com redes sociais deverá ocorrer diretamente pelos mecanismos oficiais disponibilizados pela própria plataforma.

No MVP, a rede social alvo é:

```text
Instagram
```

---

# 7. Instagram

A integração com o Instagram deverá ser implementada por meio dos mecanismos oficiais da plataforma e do fluxo de autorização definido na documentação do projeto.

Separar claramente:

```text
Motor de Publicação
        ↓
Conector Instagram
        ↓
Instagram
```

Não colocar chamadas específicas do Instagram diretamente:

```text
nas rotas
nos componentes React
nas entidades de domínio
nos serviços genéricos
```

---

# 8. Provedor de IA

A IA deverá ser tratada como uma dependência externa.

O código de negócio não deverá ficar espalhado com chamadas diretamente ao provedor.

Preferir:

```text
Serviço
   ↓
Serviço/Conector de IA
   ↓
Provedor de IA
```

A implementação deverá permanecer preparada para evolução futura sem criar abstrações excessivas no MVP.

---

# 9. Monólito modular

O MVP deverá ser implementado como um:

```text
MONÓLITO MODULAR
```

Não criar microserviços separados sem necessidade concreta.

Os principais módulos deverão possuir responsabilidades claras:

```text
Autenticação
Perfis
Conteúdo
Análise
IA
Geração
Publicação
Administração
```

---

# 10. Separação de responsabilidades

Respeitar a arquitetura:

```text
Frontend
   ↓
API
   ↓
Serviços
   ↓
Repositórios / Conectores
   ↓
Banco / Serviços externos
```

Evitar:

```text
rota → SQL direto
rota → Instagram direto
rota → IA direto
frontend → MySQL
frontend → Instagram
```

---

# 11. Serviços

Serviços representam regras de negócio.

Exemplos:

```text
ServicoUsuario
ServicoPerfil
ServicoConteudo
ServicoAnalise
ServicoIA
ServicoGeracao
ServicoPublicacao
```

Não colocar regras de negócio importantes diretamente nas rotas.

---

# 12. Repositórios

Repositórios são responsáveis pela persistência.

Exemplos:

```text
RepositorioUsuario
RepositorioPerfil
RepositorioConteudo
RepositorioPublicacao
```

Evitar espalhar consultas SQL/SQLAlchemy pelas camadas superiores.

---

# 13. Conectores

Conectores encapsulam comunicação com sistemas externos.

Exemplos:

```text
ConectorInstagram
ConectorProvedorIA
```

Detalhes específicos de APIs externas deverão permanecer nos conectores.

---

# 14. Domínio

O domínio deve representar o negócio e não depender desnecessariamente de detalhes tecnológicos.

Evitar que entidades do domínio fiquem acopladas diretamente a:

```text
FastAPI
MySQL
Instagram
provedor específico de IA
```

---

# 15. Banco de dados

Banco:

```text
MySQL
```

ORM:

```text
SQLAlchemy
```

Migrações:

```text
Alembic
```

Alterações estruturais do banco deverão ser feitas por migrações versionadas.

Não depender de alterações manuais no banco.

---

# 16. Modelo de dados

As entidades principais incluem conceitos como:

```text
Usuario
Perfil
Nicho
ContaSocial
Conteudo
Analise
Insight
ExecucaoIA
Publicacao
```

Consultar:

```text
49_MODELO_DE_DADOS_E_ESTRATEGIA_DE_BANCO_DE_DADOS.md
```

antes de alterar o modelo.

---

# 17. Fonte externa x modelo interno

Não utilizar o modelo externo do Instagram como modelo principal do domínio.

Fluxo:

```text
Instagram
   ↓
Conector
   ↓
Normalizador
   ↓
Modelo interno
```

O sistema deverá possuir seus próprios modelos internos.

---

# 18. Conteúdo x Publicação

Não confundir:

```text
Conteúdo
```

com:

```text
Publicação
```

Um conteúdo pode existir sem publicação.

Uma publicação representa a operação/registro de envio desse conteúdo para uma rede social.

---

# 19. Motor de Análise

Responsável por transformar dados em:

```text
padrões
insights
informações estruturadas
oportunidades
```

Consultar a documentação antes de definir novos comportamentos.

---

# 20. Motor de Geração

Responsável por produzir novos conteúdos a partir de:

```text
perfil
nicho
dados analisados
insights
referências
regras
IA
```

---

# 21. Motor de Publicação

Responsável por orquestrar a publicação.

Fluxo:

```text
Conteúdo aprovado
   ↓
Motor de Publicação
   ↓
Conector Instagram
   ↓
Instagram
```

---

# 22. Aprovação

O sistema deverá manter separação entre:

```text
conteúdo gerado
```

e:

```text
conteúdo aprovado para publicação
```

Não publicar automaticamente algo apenas porque foi gerado, salvo quando uma funcionalidade específica de publicação automática tiver sido implementada e autorizada.

---

# 23. Processamento assíncrono

Não introduzir filas complexas no MVP sem necessidade.

Quando houver operações longas:

```text
API
 ↓
Tarefa
 ↓
Worker
```

poderá ser utilizado.

Não adicionar automaticamente:

```text
Redis
RabbitMQ
Kafka
```

sem requisito concreto.

---

# 24. Idempotência

Operações externas que possam ser repetidas deverão considerar idempotência.

Isso é especialmente importante para:

```text
publicações
tarefas
reprocessamentos
```

---

# 25. Retry

Retry somente deverá ocorrer quando houver possibilidade de erro temporário.

Não criar retry infinito.

---

# 26. Estado desconhecido

Quando uma operação externa tiver sido enviada mas seu resultado não puder ser confirmado, não inventar sucesso.

Utilizar o conceito de:

```text
ESTADO_DESCONHECIDO
```

quando necessário e realizar reconciliação.

---

# 27. Autenticação

A autenticação deverá ser implementada de acordo com:

```text
36_ARQUITETURA_DE_AUTENTICACAO_E_AUTORIZACAO.md
```

Não inventar outro mecanismo sem necessidade.

---

# 28. Autorização

Sempre verificar:

```text
quem é o usuário
+
o que ele pode fazer
+
o recurso pertence a ele
```

Nunca confiar somente em um ID recebido pelo frontend.

---

# 29. Área Administrativa

O projeto possui Área Administrativa.

Ela deverá respeitar permissões específicas e não deverá permitir acesso administrativo simplesmente porque uma rota existe.

---

# 30. Segurança

Nunca expor:

```text
senha
senha_hash
token
client_secret
chave de API
credencial externa
```

no frontend ou nas respostas públicas da API.

---

# 31. Logs

Logs deverão ser úteis para diagnóstico, mas não poderão conter segredos.

Evitar registrar dados pessoais desnecessários.

Utilizar:

```text
correlation_id
usuario_id
conteudo_id
publicacao_id
execucao_id
```

quando apropriado.

---

# 32. Correlation ID

Operações importantes deverão possuir rastreabilidade.

Quando uma requisição gerar processamento interno ou externo, preservar o:

```text
correlation_id
```

quando possível.

---

# 33. LGPD

Seguir:

```text
44_PRIVACIDADE_LGPD_E_PROTECAO_DE_DADOS.md
```

Princípios fundamentais:

```text
coletar somente o necessário
+
utilizar para finalidade definida
+
proteger
+
reter pelo tempo necessário
+
permitir exclusão quando aplicável
```

---

# 34. Observabilidade

Seguir:

```text
45_OBSERVABILIDADE_MONITORAMENTO_E_INCIDENTES.md
```

O sistema deverá possuir observabilidade suficiente para responder:

```text
o sistema está funcionando?
o que falhou?
onde falhou?
quando falhou?
```

---

# 35. Estrutura de diretórios

Seguir:

```text
46_ESTRUTURA_DE_DIRETORIOS_E_ORGANIZACAO_DO_PROJETO.md
```

Não criar diretórios arbitrariamente.

Antes de criar um arquivo:

```text
verificar se já existe
identificar a responsabilidade
colocar na camada correta
```

---

# 36. Nomenclatura

Seguir:

```text
47_DICIONARIO_DE_DOMINIO_E_PADRAO_DE_NOMENCLATURA.md
```

Não criar sinônimos desnecessários.

Exemplo:

```text
Conteudo ≠ Publicacao
```

---

# 37. Dependências

Seguir:

```text
48_MATRIZ_DE_DEPENDENCIAS_E_INTEGRACOES.md
```

Antes de adicionar uma biblioteca, serviço ou tecnologia:

```text
verificar se realmente é necessário
avaliar impacto
preferir simplicidade
```

---

# 38. Código novo

Antes de criar código novo:

1. procurar código existente que já resolva o problema;
2. reutilizar quando apropriado;
3. evitar duplicação;
4. manter a responsabilidade no módulo correto.

---

# 39. Arquivos grandes

Não criar arquivos gigantes com responsabilidades diferentes.

Também não fragmentar excessivamente funções simples.

Buscar equilíbrio.

---

# 40. Código temporário

Não deixar no código oficial:

```text
teste.py
teste2.py
final.py
final2.py
```

ou arquivos experimentais sem finalidade.

---

# 41. Comentários

Comentários devem explicar:

```text
por quê
```

e não simplesmente:

```text
o que o código obviamente faz
```

---

# 42. Tratamento de erros

Erros deverão ser:

```text
tratados
classificados
registrados quando necessário
```

Não retornar stack trace para o usuário.

---

# 43. API

A API deverá possuir contratos claros.

Consultar:

```text
34_CONTRATOS_DA_API_REST.md
```

antes de criar ou alterar endpoints.

---

# 44. Versionamento da API

Respeitar o padrão de versionamento definido na documentação.

Não quebrar contratos existentes sem avaliar impacto.

---

# 45. Frontend

O frontend deverá consumir a API.

Evitar lógica de negócio crítica exclusivamente no React.

---

# 46. Componentes

Criar componentes reutilizáveis somente quando houver reutilização real ou responsabilidade clara.

Não criar abstrações genéricas desnecessárias.

---

# 47. Testes

Toda funcionalidade relevante deverá possuir testes adequados.

Priorizar:

```text
regras de negócio
autenticação
autorização
integrações
publicação
processamentos críticos
```

---

# 48. Testes unitários

Devem validar regras isoladamente.

---

# 49. Testes de integração

Devem validar a interação entre componentes reais quando apropriado.

---

# 50. Testes de API

Devem validar:

```text
status HTTP
contrato
autenticação
autorização
erros
```

---

# 51. Testes E2E

Utilizar quando trouxer benefício para validar fluxos completos.

Não criar E2E para tudo.

---

# 52. Testes de segurança

Validar principalmente:

```text
acesso cruzado entre usuários
IDOR
permissões administrativas
exposição de segredos
```

---

# 53. Desenvolvimento incremental

Não implementar dezenas de funcionalidades simultaneamente.

Cada etapa deverá terminar funcional.

---

# 54. Regra de conclusão de etapa

Uma etapa somente estará concluída quando:

```text
código implementado
+
testes executados
+
erros corrigidos
+
funcionalidade validada
```

---

# 55. Git

O projeto utiliza Git.

Cada mudança significativa deverá resultar em commit.

---

# 56. Commits

Preferir mensagens claras.

Exemplos:

```text
feat: adiciona autenticação de usuários
feat: cria cadastro de perfis
fix: corrige autorização de conteúdo
test: adiciona testes de publicação
refactor: separa serviço de conteúdo
docs: atualiza documentação de integração
```

---

# 57. Não fazer commit de segredos

Nunca versionar:

```text
.env
tokens
senhas
chaves privadas
credenciais
```

---

# 58. Variáveis de ambiente

Utilizar:

```text
.env
```

localmente quando apropriado.

Versionar somente:

```text
.env.exemplo
```

sem valores reais.

---

# 59. Deploy

Seguir:

```text
43_FLUXO_DE_DESENVOLVIMENTO_GIT_E_DEPLOY.md
```

---

# 60. Produção

A aplicação será hospedada inicialmente em VPS da Hostinger.

Não assumir:

```text
AWS
Azure
GCP
```

como infraestrutura inicial.

---

# 61. Infraestrutura

Seguir:

```text
40_INFRAESTRUTURA_LOCAL_E_VPS.md
```

---

# 62. Desenvolvimento local

O sistema deverá ser executável localmente antes de ser considerado pronto para produção.

---

# 63. Banco local

O ambiente local deverá possuir uma maneira documentada de executar o MySQL.

---

# 64. Dados de desenvolvimento

Preferir dados fictícios.

Não copiar dados reais de produção sem necessidade e proteção adequada.

---

# 65. Dependências externas

Durante testes, evitar depender da Internet quando isso não for necessário.

Utilizar mocks/stubs em testes unitários.

---

# 66. Instagram em desenvolvimento

Não criar publicação real acidentalmente durante testes.

Toda ação de publicação real deverá ser explicitamente controlada.

---

# 67. IA em desenvolvimento

Evitar chamadas desnecessárias ao provedor de IA para testes repetitivos.

Quando possível:

```text
mock
fixture
resposta controlada
```

---

# 68. Custos

O agente deverá evitar criar chamadas externas desnecessárias que gerem custo.

---

# 69. Performance

Não otimizar prematuramente.

Primeiro:

```text
funcionar
```

Depois:

```text
medir
```

Depois:

```text
otimizar
```

---

# 70. Escalabilidade

A arquitetura deverá permitir evolução, mas o MVP não deverá implementar infraestrutura de escala sem necessidade.

---

# 71. Microserviços

Não criar microserviços no MVP sem decisão arquitetural explícita.

---

# 72. Cache

Não adicionar Redis ou outro cache distribuído sem evidência de necessidade.

---

# 73. Mensageria

Não adicionar sistemas de mensageria complexos sem necessidade.

---

# 74. Regra contra overengineering

Se uma solução simples resolve o problema do MVP:

```text
usar a solução simples
```

---

# 75. Regra contra gambiarra

Simplicidade não significa:

```text
código frágil
```

A implementação deverá ser simples, mas correta.

---

# 76. Regra de segurança

Nunca sacrificar segurança para reduzir quantidade de código.

---

# 77. Regra de documentação

Se uma decisão arquitetural mudar:

```text
código
+
documentação
```

deverão permanecer coerentes.

---

# 78. Não alterar documentação silenciosamente

Se uma implementação exigir mudança de arquitetura, primeiro identificar o conflito e atualizar o documento correspondente de maneira explícita.

---

# 79. Conflito entre documentos

Se documentos parecerem contraditórios:

1. não escolher silenciosamente;
2. identificar o conflito;
3. verificar documentos mais específicos;
4. verificar decisões posteriores do projeto;
5. se ainda houver dúvida, parar antes de implementar a parte afetada e informar o conflito.

---

# 80. Regra para documentação antiga

Não assumir que um documento antigo continua válido se existir uma decisão posterior explícita.

---

# 81. Fonte de verdade

Hierarquia:

```text
decisão explícita mais recente do projeto
        ↓
documentação específica
        ↓
documentação arquitetural geral
        ↓
código existente
```

Quando não houver conflito, manter todos coerentes.

---

# 82. Não inventar requisitos

Se algo não estiver definido:

```text
não inventar uma regra de negócio importante
```

Pode escolher uma implementação técnica simples quando a decisão não afetar o produto, mas deverá registrar a escolha quando relevante.

---

# 83. Perguntar somente quando necessário

Não interromper o desenvolvimento por decisões triviais.

Perguntar somente quando a decisão:

```text
afetar arquitetura
segurança
dados
contrato
negócio
custos relevantes
```

---

# 84. Execução autônoma

Quando os requisitos estiverem claros, o agente deverá:

```text
implementar
testar
corrigir
validar
```

sem solicitar aprovação a cada arquivo.

---

# 85. Pequenos incrementos

Cada execução deverá possuir escopo controlado.

Preferir:

```text
uma funcionalidade completa
```

em vez de:

```text
dez funcionalidades pela metade
```

---

# 86. Ordem geral sugerida

A ordem de desenvolvimento deverá seguir aproximadamente:

```text
1. Fundação do projeto
2. Ambiente de desenvolvimento
3. Banco e migrações
4. Backend base
5. Autenticação
6. Usuários
7. Perfis
8. Nichos
9. Conteúdos
10. Análise
11. Insights
12. Integração com IA
13. Motor de geração
14. Conta Instagram
15. Motor de publicação
16. Área Administrativa
17. Observabilidade
18. Testes finais
19. Deploy
```

A ordem poderá ser ajustada se a documentação ou dependências reais exigirem.

---

# 87. Primeiro desenvolvimento

Na primeira execução do agente:

```text
não implementar o produto inteiro
```

Primeiro:

```text
analisar documentação
+
analisar estado do repositório
+
identificar primeira etapa
+
implementar fundação
```

---

# 88. Resultado de cada execução

Ao finalizar uma etapa, informar:

```text
O que foi implementado
Arquivos criados
Arquivos alterados
Testes executados
Resultado dos testes
Comando para validar
Próxima etapa recomendada
```

---

# 89. Commit

Após uma etapa funcional:

```text
git status
git diff
testes
git add
git commit
```

Não criar commit de código que não foi validado.

---

# 90. Não fazer push automaticamente sem necessidade

O agente poderá criar commits locais.

Push para o repositório remoto deverá seguir o fluxo definido pelo usuário/projeto.

---

# 91. Validação

Antes de considerar uma etapa concluída:

```text
rodar testes
rodar lint/formatador quando configurados
verificar migrações
verificar aplicação
```

---

# 92. Erro durante implementação

Se encontrar erro:

```text
diagnosticar
corrigir
testar novamente
```

Não simplesmente ignorar.

---

# 93. Erro não relacionado

Se encontrar problema preexistente fora do escopo:

```text
não alterar indiscriminadamente
```

Registrar e informar.

---

# 94. Arquivos modificados inesperadamente

Antes do commit:

```text
git status
git diff
```

Verificar se todas as alterações pertencem à tarefa.

---

# 95. Não apagar trabalho existente

Nunca sobrescrever ou apagar trabalho existente sem necessidade clara.

---

# 96. Não recomeçar o projeto

Se já existir código funcional:

```text
evoluir
```

e não:

```text
reescrever tudo
```

sem decisão explícita.

---

# 97. Código gerado

Código gerado automaticamente deverá ser revisado antes do commit.

---

# 98. Dependências novas

Antes de instalar uma dependência:

```text
verificar se já existe solução
avaliar tamanho
avaliar manutenção
avaliar segurança
avaliar necessidade
```

---

# 99. Dependência externa crítica

Registrar quando uma nova dependência externa se tornar parte da arquitetura.

---

# 100. Regra de simplicidade do MVP

Sempre perguntar:

```text
Isso é necessário para validar o negócio agora?
```

Se a resposta for:

```text
não
```

não implementar no MVP sem justificativa.

---

# 101. Visão de produto

O ViralCode deverá evoluir para suportar:

```text
múltiplos nichos
+
múltiplos perfis
+
múltiplas redes sociais
+
análise
+
geração
+
publicação
```

Mas a primeira versão deverá implementar somente o necessário para validar essa proposta.

---

# 102. Arquitetura alvo

```text
                    VIRALCODE
                        │
                 ┌──────┴──────┐
                 │             │
             FRONTEND       BACKEND
              React        FastAPI
                               │
                       ┌───────┴────────┐
                       │                │
                  SERVIÇOS         CONECTORES
                       │           │        │
                       │      Instagram     IA
                       │
                  REPOSITÓRIOS
                       │
                   SQLAlchemy
                       │
                     MySQL
```

---

# 103. Fluxo de negócio alvo

```text
DADOS
  ↓
ANÁLISE
  ↓
INSIGHTS
  ↓
GERAÇÃO
  ↓
CONTEÚDO
  ↓
APROVAÇÃO
  ↓
PUBLICAÇÃO
  ↓
INSTAGRAM
```

---

# 104. Regra final

Você é um agente de implementação, não um arquiteto que pode alterar o produto silenciosamente.

Sua prioridade é:

```text
ENTENDER
 ↓
IMPLEMENTAR
 ↓
TESTAR
 ↓
VALIDAR
 ↓
DOCUMENTAR
```

O ViralCode deverá crescer de forma incremental, mantendo o MVP simples, funcional, seguro e coerente com a documentação.

---

**Documento:** AGENTS.md  
**Versão:** 1.0  
**Projeto:** ViralCode  
**Idioma:** Português do Brasil  
**Status:** Instrução oficial para agentes de desenvolvimento
