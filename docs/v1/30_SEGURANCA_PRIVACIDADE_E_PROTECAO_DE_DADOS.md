# 30 — SEGURANÇA, PRIVACIDADE E PROTEÇÃO DE DADOS

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define os princípios e controles de segurança e privacidade do ViralCode.

O objetivo é proteger:

```text
usuários
credenciais
contas sociais
conteúdos
dados de desempenho
dados internos
infraestrutura
```

A segurança deverá existir desde o MVP, sem criar complexidade desnecessária.

---

# 2. Princípio fundamental

O sistema deverá seguir:

```text
MENOR PRIVILÉGIO
+
MÍNIMO DE DADOS
+
SEGREDOS PROTEGIDOS
+
ISOLAMENTO
+
RASTREABILIDADE
```

---

# 3. Segurança por camadas

A proteção deverá existir em:

```text
Frontend
   ↓
API
   ↓
Autenticação
   ↓
Autorização
   ↓
Serviços
   ↓
Banco
   ↓
Infraestrutura
```

Nenhuma camada deverá ser considerada suficiente sozinha.

---

# 4. Autenticação

O usuário deverá provar sua identidade antes de acessar recursos protegidos.

O sistema deverá possuir:

```text
cadastro
login
token
expiração
renovação quando aplicável
logout/invalidação quando aplicável
```

---

# 5. Senhas

Senhas nunca deverão ser armazenadas em texto puro.

Deverá ser utilizado um mecanismo seguro de hash de senha.

O sistema não deverá registrar a senha em:

```text
banco
logs
arquivos
respostas da API
```

---

# 6. Token de autenticação

Tokens deverão possuir:

```text
expiração
assinatura segura
validação
```

A chave utilizada para assinatura deverá permanecer fora do código-fonte.

---

# 7. Segredo da aplicação

Exemplos:

```text
chave de assinatura
senha MySQL
credencial Instagram
client secret
chave do provedor de IA
```

Nunca deverão ser colocados diretamente no código.

---

# 8. Variáveis de ambiente

Segredos de infraestrutura deverão ser carregados por configuração segura.

Exemplo conceitual:

```text
BANCO_SENHA
CHAVE_JWT
INSTAGRAM_CLIENT_SECRET
CHAVE_PROVEDOR_IA
```

---

# 9. Repositório Git

Nunca versionar:

```text
.env
senhas
tokens
chaves privadas
credenciais
backups
```

---

# 10. Arquivo de exemplo

O projeto deverá possuir:

```text
.env.example
```

contendo somente:

```text
nomes das variáveis
exemplos não secretos
```

---

# 11. Isolamento entre usuários

Este é um dos controles mais importantes.

Exemplo:

```text
Usuário A
   ↓
Perfil A
   ↓
Conteúdo A
```

não poderá acessar:

```text
Perfil B
Conteúdo B
```

---

# 12. Regra de propriedade

Toda operação sobre recurso privado deverá validar:

```text
usuario autenticado
+
proprietário do recurso
```

ou uma permissão equivalente.

---

# 13. Não confiar no frontend

O frontend poderá enviar:

```text
perfil_id
conteudo_id
conta_social_id
```

mas isso não significa que o usuário tenha acesso.

A autorização deverá ser feita no backend.

---

# 14. Autorização

A autenticação responde:

```text
Quem é você?
```

A autorização responde:

```text
Você pode fazer isso?
```

As duas verificações deverão permanecer separadas conceitualmente.

---

# 15. IDs

Não assumir que conhecer um ID concede acesso.

Exemplo:

```text
GET /api/v1/conteudos/123
```

deverá verificar se o conteúdo pertence ao usuário ou está autorizado para ele.

---

# 16. Dados pessoais

O sistema deverá armazenar somente os dados necessários para o funcionamento do produto.

Exemplos:

```text
nome
e-mail
configurações
perfil
```

---

# 17. Minimização de dados

Não coletar:

```text
dados pessoais
```

somente porque estão disponíveis.

A pergunta deverá ser:

> Precisamos realmente desse dado para executar o produto?

---

# 18. Dados de redes sociais

O ViralCode poderá lidar com:

```text
nome da conta
identificador externo
métricas
conteúdos
credenciais técnicas
```

Esses dados deverão ser tratados com cuidado.

---

# 19. Credenciais do Instagram

Credenciais necessárias para a integração deverão ser protegidas.

Nunca exibir o token completo:

```text
na interface
nos logs
em mensagens de erro
```

---

# 20. Armazenamento de tokens

A implementação deverá avaliar mecanismos apropriados para proteger credenciais armazenadas.

No mínimo:

```text
não texto exposto em logs
acesso restrito
criptografia/proteção quando aplicável
```

---

# 21. Renovação de credenciais

Quando a plataforma exigir renovação:

```text
detectar
 ↓
atualizar
 ↓
persistir
```

Se não for possível:

```text
REAUTENTICACAO_NECESSARIA
```

---

# 22. Desconexão

Ao desconectar uma conta social:

```text
invalidar credencial quando aplicável
 ↓
atualizar estado
 ↓
preservar histórico necessário
```

---

# 23. Exclusão de usuário

A arquitetura deverá prever a possibilidade de exclusão dos dados do usuário conforme as regras do produto e obrigações aplicáveis.

A implementação definitiva deverá definir:

```text
o que é apagado
o que é anonimizado
o que precisa ser retido
```

---

# 24. Conteúdo gerado

Conteúdos criados pelo usuário deverão possuir isolamento por usuário/perfil.

Não disponibilizar conteúdo privado de um usuário para outro.

---

# 25. Conteúdo externo

Conteúdo coletado de redes sociais deverá ser tratado como dado externo.

Não assumir que:

```text
texto externo = instrução confiável
```

---

# 26. Prompt Injection

Conteúdo externo poderá conter instruções maliciosas.

Exemplo:

```text
"ignore as instruções anteriores"
```

Isso deverá ser tratado como:

```text
texto a ser analisado
```

e não como comando do sistema.

---

# 27. Separação de instruções

As chamadas de IA deverão separar:

```text
INSTRUÇÕES DO SISTEMA
DADOS EXTERNOS
CONTEXTO DO USUÁRIO
TAREFA
```

---

# 28. Saída da IA

A resposta da IA nunca deverá alterar diretamente o banco sem validação.

Fluxo:

```text
IA
 ↓
resposta
 ↓
validação
 ↓
regra de negócio
 ↓
persistência
```

---

# 29. Entrada da API

Toda entrada externa deverá ser validada.

Exemplos:

```text
tipo
tamanho
formato
enum
limites
```

---

# 30. SQL Injection

Não construir consultas SQL por concatenação insegura.

Utilizar:

```text
SQLAlchemy
```

e mecanismos seguros de parametrização.

---

# 31. XSS

Conteúdo fornecido pelo usuário ou obtido externamente deverá ser tratado como não confiável.

O frontend deverá evitar renderizar HTML arbitrário sem sanitização apropriada.

---

# 32. CSRF

A estratégia deverá considerar o mecanismo de autenticação escolhido.

Se forem utilizados cookies para autenticação, deverão existir proteções adequadas.

---

# 33. CORS

Em produção:

```text
permitir somente origens necessárias
```

Não utilizar:

```text
*
```

indiscriminadamente em endpoints protegidos.

---

# 34. HTTPS

Produção deverá utilizar:

```text
HTTPS
```

para proteger:

```text
credenciais
tokens
conteúdo
dados de usuário
```

---

# 35. Banco

O MySQL não deverá ser exposto publicamente sem necessidade.

Preferir:

```text
FastAPI
 ↓
rede interna
 ↓
MySQL
```

---

# 36. Usuário do banco

A aplicação deverá utilizar um usuário específico.

Não utilizar:

```text
root
```

---

# 37. Privilégio mínimo

O usuário da aplicação deverá possuir somente os privilégios necessários.

---

# 38. Backup

Backups deverão ser protegidos.

Não disponibilizar:

```text
backup do banco
```

através do servidor web.

---

# 39. Logs

Logs não deverão conter:

```text
senha
token
client secret
chave privada
```

---

# 40. Erros

Respostas públicas não deverão expor:

```text
stack trace
SQL
caminho do servidor
credenciais
detalhes internos
```

---

# 41. Correlation ID

Erros deverão possuir um identificador de correlação para diagnóstico sem expor informações internas.

Exemplo:

```text
X-Correlation-ID
```

---

# 42. Rate limiting

O MVP deverá avaliar limitação de requisições principalmente para:

```text
login
cadastro
endpoints públicos
operações caras
```

---

# 43. Operações caras

Considerar proteção para:

```text
geração IA
descoberta
análise em lote
publicação
```

---

# 44. Custo como vetor de segurança

Uma API sem limite pode permitir abuso que gere:

```text
muitas chamadas de IA
muitos custos
muitas consultas externas
```

Por isso, limites também são uma proteção financeira.

---

# 45. Idempotência

Operações que geram efeitos externos deverão possuir proteção contra duplicidade.

Principalmente:

```text
publicação
```

---

# 46. Auditoria

Algumas ações críticas deverão poder ser rastreadas.

Exemplos:

```text
conexão Instagram
desconexão
aprovação
publicação
alteração de configuração
```

---

# 47. Auditoria ≠ log

```text
LOG
→ diagnóstico técnico

AUDITORIA
→ histórico de ação relevante
```

Não misturar as duas responsabilidades quando isso prejudicar clareza.

---

# 48. Sessão

Sessões/token deverão possuir tempo de vida apropriado.

Não utilizar credenciais eternas.

---

# 49. Logout

O mecanismo de logout deverá invalidar ou encerrar a sessão conforme o mecanismo de autenticação adotado.

---

# 50. Conta comprometida

Futuramente poderá existir:

```text
revogar sessões
alterar senha
reconectar conta social
```

---

# 51. Dependências

Dependências do projeto deverão ser mantidas sob controle.

Periodicamente avaliar:

```text
vulnerabilidades
versões
compatibilidade
```

---

# 52. Atualizações

Não atualizar dependências críticas diretamente em produção sem:

```text
teste
validação
rollback
```

---

# 53. Imagens e arquivos

Arquivos enviados pelo usuário deverão ser tratados como não confiáveis.

Quando houver upload:

```text
tipo
tamanho
extensão
conteúdo
```

deverão ser validados.

---

# 54. Mídia

No MVP, evitar armazenar mídia desnecessariamente.

Quando houver necessidade:

```text
armazenamento controlado
```

deverá ser utilizado.

---

# 55. Privacidade de conteúdo

Conteúdo privado do usuário não deverá ser utilizado para outro usuário sem base legítima e controle do produto.

---

# 56. Dados utilizados pela IA

Antes de enviar dados ao provedor de IA, avaliar:

```text
é necessário?
é permitido?
contém dado sensível?
pode ser minimizado?
```

---

# 57. Retenção

O sistema deverá evitar retenção indefinida de:

```text
logs
execuções de IA
dados temporários
```

sem necessidade.

---

# 58. Exclusão

Quando o usuário solicitar exclusão, o sistema deverá possuir processo definido para os dados abrangidos.

---

# 59. LGPD

O produto deverá considerar os princípios e obrigações aplicáveis da legislação brasileira de proteção de dados, incluindo a LGPD.

Este documento não substitui análise jurídica específica.

---

# 60. Bases legais e políticas

As bases legais, política de privacidade, termos de uso e demais documentos jurídicos deverão ser definidos antes de uma operação comercial em escala.

---

# 61. Direitos do usuário

O produto deverá considerar mecanismos para atender solicitações aplicáveis relacionadas aos dados pessoais.

---

# 62. Incidente de segurança

Se houver suspeita de incidente:

```text
identificar
 ↓
conter
 ↓
preservar evidências
 ↓
avaliar impacto
 ↓
corrigir
 ↓
documentar
```

---

# 63. Não apagar evidências

Durante investigação:

```text
não apagar logs relevantes
```

antes de preservar as evidências necessárias.

---

# 64. Segredos comprometidos

Se uma chave for comprometida:

```text
revogar
 ↓
gerar nova
 ↓
atualizar ambiente
 ↓
verificar uso indevido
```

---

# 65. Chaves de produção

Não reutilizar desnecessariamente:

```text
segredos de desenvolvimento
```

em produção.

---

# 66. Ambiente local

Credenciais de desenvolvimento deverão ser diferentes das de produção.

---

# 67. Ambiente de testes

Quando possível:

```text
dados fictícios
credenciais próprias
contas de teste
```

---

# 68. Produção

Produção deverá possuir:

```text
segredos próprios
banco próprio
contas próprias
domínio próprio
```

---

# 69. Princípio de não exposição

O frontend nunca deverá receber:

```text
client_secret
senha de banco
chave privada
token administrativo
```

---

# 70. APIs externas

As chamadas externas deverão ocorrer preferencialmente pelo backend quando envolverem credenciais privadas.

---

# 71. Instagram

Arquitetura:

```text
Frontend
   ↓
FastAPI
   ↓
Conector Instagram
   ↓
Instagram
```

Não colocar segredos do aplicativo no frontend.

---

# 72. IA

Arquitetura:

```text
Frontend
   ↓
FastAPI
   ↓
Provedor IA
```

A chave do provedor não deverá ficar no React.

---

# 73. Segurança do frontend

O frontend deverá considerar:

```text
XSS
exposição de dados
armazenamento inseguro de credenciais
origens não confiáveis
```

---

# 74. Segurança do backend

O backend deverá considerar:

```text
autenticação
autorização
validação
rate limiting
segredos
logs
erros
```

---

# 75. Segurança do banco

Considerar:

```text
usuário dedicado
senha forte
rede restrita
backup
atualização
```

---

# 76. Segurança da VPS

Considerar:

```text
SSH
firewall
HTTPS
atualizações
usuário não-root
backup
```

---

# 77. Segurança por padrão

Novas funcionalidades deverão nascer:

```text
protegidas
```

e não serem protegidas posteriormente.

---

# 78. Checklist de segurança do MVP

```text
[ ] HTTPS
[ ] autenticação
[ ] autorização
[ ] isolamento entre usuários
[ ] senha com hash seguro
[ ] tokens protegidos
[ ] segredos fora do código
[ ] CORS restrito
[ ] MySQL não exposto
[ ] usuário de banco dedicado
[ ] validação de entrada
[ ] SQL seguro
[ ] tratamento de erro
[ ] logs sem segredos
[ ] backup
[ ] dependências revisadas
[ ] proteção das integrações
```

---

# 79. Regra para agentes de IA

Antes de alterar código:

1. verificar se a mudança cria nova superfície de ataque;
2. validar autenticação;
3. validar autorização;
4. verificar dados expostos;
5. verificar logs;
6. verificar segredos;
7. criar testes de segurança quando aplicável;
8. atualizar documentação.

---

# 80. Regra contra atalhos

Não aceitar como solução:

```text
desabilitar autenticação
abrir MySQL
colocar token no frontend
liberar CORS total
remover validação
ignorar erro
```

somente para facilitar desenvolvimento.

Se for necessário um atalho local:

```text
somente ambiente local
claramente documentado
```

---

# 81. Critério de sucesso

A segurança do MVP estará adequada quando:

```text
usuário só acessa seus dados
+
credenciais estão protegidas
+
integrações não expõem segredos
+
banco não está aberto
+
erros não vazam informações internas
+
operações críticas são rastreáveis
```

---

# 82. Arquitetura resumida

```text
                    INTERNET
                       │
                      HTTPS
                       │
                       ▼
                     NGINX
                       │
                       ▼
                    FASTAPI
                 ┌─────┼─────┐
                 ▼     ▼     ▼
              AUTENT. SERV. CONECTORES
                 │     │     │
                 │     │     ├── Instagram
                 │     │     └── IA
                 │     │
                 └─────┼──────────► MySQL
                       │
                    LOGS/AUDITORIA
```

---

# 83. Regra final

> **O ViralCode deverá ser simples no MVP, mas nunca inseguro por ser simples.**

A arquitetura deverá proteger primeiro:

```text
IDENTIDADE
   ↓
ACESSO
   ↓
DADOS
   ↓
CREDENCIAIS
   ↓
INTEGRAÇÕES
   ↓
INFRAESTRUTURA
```

E somente depois adicionar mecanismos de segurança mais sofisticados conforme o produto crescer.

**Versão:** 1.0  
**Status:** Documento oficial de Segurança, Privacidade e Proteção de Dados
