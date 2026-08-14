# 10 — SEGURANÇA DO VIRALCODE

**Versão:** 0.2  
**Status:** Revisado — integração direta com Instagram no MVP  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define os princípios e regras de segurança do ViralCode.

O objetivo é proteger:

- código;
- banco de dados;
- credenciais;
- APIs externas;
- usuários;
- conteúdos;
- contas sociais;
- infraestrutura;
- futuras organizações e perfis.

A segurança deverá acompanhar o crescimento do produto.

A regra principal é:

> **Segurança deve ser simples no MVP, mas nunca negligenciada.**

---

# 2. Princípios

O ViralCode deverá seguir:

1. menor privilégio;
2. segredos fora do código;
3. validação de entrada;
4. separação de responsabilidades;
5. HTTPS em produção;
6. logs sem segredos;
7. dependências atualizadas;
8. banco protegido;
9. APIs externas isoladas;
10. acesso mínimo necessário.

---

# 3. Modelo de ameaça inicial

Os principais riscos previstos são:

```text
Credenciais expostas
API externa abusada
SQL Injection
XSS
CSRF
CORS incorreto
Acesso não autorizado
Banco exposto
Logs contendo segredos
Dependência vulnerável
Servidor comprometido
```

Nem todos possuem a mesma prioridade no MVP.

---

# 4. Prioridades de segurança

## P0 — obrigatório

```text
Segredos fora do código
Validação de entrada
SQLAlchemy para acesso ao banco
Banco não exposto publicamente
HTTPS em produção
CORS configurado
Logs sem credenciais
```

## P1

```text
Autenticação
Autorização
Rate limiting
Gestão de usuários
Auditoria
```

## P2

```text
2FA
detecção avançada
monitoramento
alertas
rotação automatizada
```

---

# 5. Segredos

Nunca colocar segredos diretamente no código.

Errado:

```python
INSTAGRAM_APP_SECRET = "minha-chave"
```

Correto:

```text
Variável de ambiente
        ↓
Configuração
        ↓
Aplicação
```

---

# 6. Variáveis de ambiente

Exemplo:

```text
AMBIENTE=desenvolvimento

BANCO_DADOS_URL=...

INSTAGRAM_APP_SECRET=...
INSTAGRAM_GRAPH_API_URL=...
```

Os nomes definitivos serão definidos durante a implementação.

---

# 7. Arquivo `.env`

O arquivo local:

```text
.env
```

poderá armazenar credenciais de desenvolvimento.

Esse arquivo deverá estar no `.gitignore`.

Nunca fazer commit de:

```text
.env
```

---

# 8. `.env.exemplo`

O projeto deverá possuir:

```text
.env.exemplo
```

Sem segredos reais.

Exemplo:

```text
AMBIENTE=desenvolvimento

BANCO_DADOS_URL=

INSTAGRAM_APP_SECRET=
INSTAGRAM_GRAPH_API_URL=
```

---

# 9. Git

O `.gitignore` deverá impedir o versionamento de:

```text
.env
.env.*
__pycache__
node_modules
arquivos temporários
logs locais
```

Exceção:

```text
.env.exemplo
```

poderá ser versionado.

---

# 10. Credenciais da integração com Instagram

A integração do ViralCode com o Instagram deverá ocorrer diretamente por meio da aplicação do ViralCode e de uma conta do Instagram conectada pelo usuário.

A integração deverá utilizar o mecanismo de autenticação disponibilizado pelo Instagram para contas profissionais e os recursos autorizados para a aplicação.

Arquitetura:

```text
Usuário
   ↓
Instagram Login
   ↓
Conta Instagram conectada
   ↓
Token de acesso
   ↓
Backend FastAPI
   ↓
Conector Instagram
   ↓
Instagram
```

A documentação atual do Instagram API com Instagram Login utiliza um **Instagram User access token** e o host `graph.instagram.com`. O modelo é direcionado a contas profissionais (Business e Creator). citeturn1search1turn1search4

As credenciais da aplicação deverão permanecer exclusivamente no backend.

Nunca deverão:

- aparecer no React;
- ser enviadas ao navegador;
- aparecer no HTML;
- aparecer no JavaScript do frontend;
- aparecer em logs;
- aparecer em mensagens de erro;
- ser gravadas no Git.

Exemplo conceitual de configuração:

```text
INSTAGRAM_APP_ID=
INSTAGRAM_APP_SECRET=
INSTAGRAM_GRAPH_API_URL=
INSTAGRAM_REDIRECT_URI=
```

Os nomes definitivos das variáveis serão definidos durante a implementação.

O `INSTAGRAM_APP_SECRET` nunca deverá ser enviado ao frontend.

---

# 11. Banco de dados

O MySQL não deverá ficar diretamente exposto à internet.

Arquitetura de produção:

```text
Internet
   ↓
Nginx
   ↓
FastAPI
   ↓
MySQL
```

Evitar:

```text
Internet
   ↓
MySQL:3306
```

---

# 12. Usuário do banco

A aplicação deverá utilizar um usuário de banco específico.

Não utilizar a conta administrativa do MySQL pela aplicação.

Exemplo conceitual:

```text
mysql_admin
```

para administração.

E:

```text
viralcode_app
```

para a aplicação.

O usuário da aplicação deverá possuir apenas as permissões necessárias.

---

# 13. Senha do banco

A senha deverá ficar fora do código.

Exemplo:

```text
BANCO_DADOS_URL
```

A string de conexão não deverá ser exposta em logs.

---

# 14. SQL Injection

As consultas deverão utilizar SQLAlchemy e parâmetros seguros.

Evitar construir SQL diretamente com entrada do usuário.

Errado:

```python
sql = f"SELECT * FROM conteudos WHERE legenda = '{texto}'"
```

Preferir:

```text
SQLAlchemy
+
parâmetros
```

---

# 15. Validação de entrada

Toda entrada da API deverá ser validada.

Exemplos:

```text
termo
plataforma
visualizacoes_minimas
periodo_dias
```

Não confiar nos dados enviados pelo frontend.

---

# 16. Frontend não é confiável

Mesmo que o React valide:

```text
visualizacoes_minimas >= 0
```

o backend deverá validar novamente.

Regra:

> **Toda validação importante deve existir no backend.**

---

# 17. Payloads

A API deverá limitar o tamanho das entradas quando apropriado.

Objetivo:

- evitar abuso;
- evitar consumo excessivo de memória;
- evitar requisições gigantes;
- reduzir superfície de ataque.

---

# 18. CORS

Em desenvolvimento poderá existir autorização para o frontend local.

Em produção deverá ser permitido apenas o domínio autorizado.

Evitar:

```text
origins = *
```

de forma indiscriminada.

---

# 19. HTTPS

Produção deverá utilizar HTTPS.

Fluxo:

```text
HTTPS
  ↓
Nginx
  ↓
FastAPI
```

Não transmitir:

- credenciais;
- tokens;
- cookies;
- dados de usuário;

em conexão insegura em produção.

---

# 20. Desenvolvimento local

Durante o desenvolvimento local poderá ser utilizado:

```text
http://localhost
```

Isso não representa a configuração de produção.

---

# 21. Autenticação futura

O MVP poderá funcionar sem autenticação completa se o objetivo for apenas validar a proposta.

Antes de disponibilizar publicamente a aplicação, deverá existir autenticação apropriada.

Possibilidades futuras:

```text
sessão
JWT
provedor externo
```

A escolha será definida antes da implementação.

---

# 22. Autorização futura

Autenticação responde:

> Quem é você?

Autorização responde:

> O que você pode fazer?

No futuro, o sistema deverá controlar:

```text
Usuário
   ↓
Organização
   ↓
Perfil
   ↓
Permissões
```

---

# 23. Multi-organização

Quando o SaaS for implementado, os dados deverão ser isolados por organização.

Exemplo:

```text
Organização A
   ├── Perfil A
   └── Conteúdos A

Organização B
   ├── Perfil B
   └── Conteúdos B
```

Um usuário da Organização A não poderá consultar dados da Organização B sem autorização.

---

# 24. IDOR

O backend não deverá confiar apenas no ID enviado.

Exemplo perigoso:

```text
GET /api/v1/perfis/123
```

Não basta verificar que o perfil existe.

É necessário verificar:

```text
perfil 123
   ↓
pertence à organização do usuário?
```

Essa regra será obrigatória quando existir autenticação.

---

# 25. Tokens

Tokens futuros deverão:

- possuir validade;
- ser armazenados de forma segura;
- não aparecer em logs;
- não ser expostos ao frontend sem necessidade;
- ser revogados quando necessário.

---

# 26. Contas sociais

Quando o ViralCode futuramente conectar contas de Instagram, TikTok etc., os tokens dessas contas deverão ser tratados como dados altamente sensíveis.

Não armazenar tokens em texto aberto sem necessidade.

Deverá ser avaliado:

- criptografia;
- rotação;
- expiração;
- revogação;
- armazenamento seguro.

---

# 27. Criptografia

Dados altamente sensíveis poderão exigir criptografia em repouso.

No MVP, não adicionar criptografia complexa sem necessidade.

Mas a arquitetura deverá permitir sua inclusão.

---

# 28. Senhas de usuários

Quando autenticação for implementada:

> **Nunca armazenar senha em texto puro.**

Utilizar algoritmo moderno de hash de senha apropriado.

Nunca:

```text
senha = "123456"
```

no banco.

---

# 29. Logs

Logs são necessários para diagnóstico.

Mas não devem conter:

```text
senhas
tokens
chaves API
cookies
credenciais
```

---

# 30. Exemplo de log seguro

Correto:

```text
Busca 123 iniciou consulta no provedor.
```

Evitar:

```text
Busca 123 utilizando chave sk_live_ABC123...
```

---

# 31. Erros da API

Mensagens públicas não devem revelar detalhes internos.

Errado:

```text
SQLAlchemy IntegrityError em /app/repositories/conteudo.py linha 182
```

Correto:

```text
Não foi possível concluir a operação.
```

O detalhe técnico deve ficar nos logs internos.

---

# 32. Stack trace

Stack traces não deverão ser exibidos para usuários em produção.

Durante desenvolvimento poderão ser habilitados.

Produção:

```text
erro amigável
+
log técnico interno
```

---

# 33. Ambiente de produção

Produção deverá possuir:

```text
DEBUG = false
```

ou equivalente.

Nunca executar a aplicação de produção em modo de depuração.

---

# 34. Documentação da API

A documentação automática do FastAPI poderá ser acessível em desenvolvimento.

Em produção, avaliar se deverá:

- permanecer pública;
- exigir autenticação;
- ser restrita;
- ser desabilitada.

Para uma aplicação pública, a exposição indiscriminada dos detalhes internos da API deve ser evitada.

---

# 35. Rate limiting

No MVP local pode não ser necessário.

Quando a aplicação for exposta publicamente, endpoints que geram chamadas externas deverão possuir proteção contra abuso.

Exemplo:

```text
POST /api/v1/buscas
```

poderá ter limite por:

```text
IP
usuário
organização
plano
```

---

# 36. Proteção contra abuso

Uma única requisição não deverá permitir:

```text
1000 páginas externas
10000 conteúdos
```

sem controle.

Deverão existir limites razoáveis.

---

# 37. Segurança da integração com Instagram

A integração direta com Instagram deverá respeitar:

- autenticação da plataforma;
- permissões concedidas;
- tokens de acesso;
- limites de requisição;
- políticas da plataforma;
- recursos efetivamente disponíveis para a conta;
- regras de retenção e utilização dos dados.

A documentação atual do Instagram API com Instagram Login lista permissões específicas para operações como dados básicos, publicação, comentários e insights. O ViralCode deverá solicitar somente as permissões realmente necessárias para cada funcionalidade. citeturn1search1turn1search6

## 37.1 Token de acesso

O token de acesso:

```text
Instagram
   ↓
Token
   ↓
Backend ViralCode
```

deverá:

- ficar somente no backend;
- nunca ser retornado ao React;
- nunca aparecer em logs;
- possuir controle de validade;
- ser invalidado quando a conta for desconectada ou a autorização for revogada;
- ser protegido em repouso quando armazenado.

## 37.2 Conta social

O banco deverá armazenar a relação entre:

```text
Usuário/Perfil ViralCode
        ↓
ContaSocial
        ↓
Instagram
```

Dados mínimos esperados:

```text
plataforma
identificador_externo
nome_usuario
status
token_protegido
data_conexao
data_atualizacao
```

## 37.3 Permissões mínimas

Não solicitar todas as permissões disponíveis.

Exemplo conceitual:

```text
Funcionalidade
      ↓
Permissão necessária
      ↓
Conta autorizada
```

A matriz definitiva de permissões será definida durante a implementação de cada funcionalidade.

## 37.4 Capacidades da API

O sistema não deverá assumir que a API permite qualquer operação disponível no aplicativo Instagram.

Antes de implementar uma funcionalidade, verificar:

```text
A API oferece esse recurso?
        ↓
A conta conectada pode utilizá-lo?
        ↓
A aplicação possui a permissão?
        ↓
O recurso está disponível no nível de acesso atual?
```

Em especial, a descoberta de conteúdos públicos de terceiros deverá ser validada tecnicamente antes de ser tratada como requisito garantido do MVP. A documentação oficial disponível para o Instagram API possui diferenças de capacidade entre os modelos de login e entre os recursos disponíveis. citeturn1search0turn1search4

## 37.5 Publicação futura

Quando o Motor de Publicação for implementado, a publicação deverá utilizar o mesmo princípio de conexão direta:

```text
Motor de Publicação
        ↓
Conector Instagram
        ↓
Instagram
```

A API do Instagram possui suporte a publicação de conteúdo para contas profissionais, incluindo Reels, conforme as permissões e requisitos aplicáveis. citeturn1search0turn1search7

---

# 38. Dados de redes sociais

Os dados coletados de redes sociais deverão ser tratados conforme:

- termos do fornecedor;
- políticas da plataforma;
- legislação aplicável;
- finalidade do produto;
- necessidade de retenção.

Não armazenar dados desnecessários apenas porque estão disponíveis.

---

# 39. LGPD

O ViralCode deverá considerar a legislação brasileira de proteção de dados quando processar dados pessoais.

Especialmente quando forem adicionados:

- usuários;
- organizações;
- contas sociais;
- dados de contato;
- dados pessoais;
- informações de clientes.

---

# 40. Minimização de dados

Princípio:

> **Guardar somente o que possui finalidade clara.**

Exemplo:

Se precisamos de:

```text
nome_usuario
```

não precisamos necessariamente guardar todos os dados pessoais disponíveis do autor.

---

# 41. Retenção

No futuro, deverão existir políticas para decidir:

```text
quanto tempo guardar dados
```

Exemplos:

```text
dados operacionais
dados históricos
logs
respostas brutas
tokens
```

Cada categoria poderá ter uma política diferente.

---

# 42. Exclusão

Quando existir funcionalidade de exclusão, deverá ficar claro:

- o que será excluído;
- o que será mantido;
- impacto no histórico;
- relacionamentos;
- backups.

Não implementar exclusão automática sem regra clara.

---

# 43. Backup

Produção deverá possuir backup do MySQL.

Os backups deverão ser protegidos.

Não adianta possuir backup se:

```text
qualquer pessoa consegue baixá-lo.
```

---

# 44. Backup e credenciais

Credenciais de backup não deverão ser armazenadas no código.

Devem seguir o mesmo princípio:

```text
segredo
   ↓
configuração segura
```

---

# 45. VPS Hostinger

Na VPS futura:

```text
Internet
   ↓
Firewall
   ↓
Nginx
   ↓
FastAPI
   ↓
MySQL
```

O banco deverá permanecer restrito.

---

# 46. Firewall

A VPS deverá permitir somente portas necessárias.

Exemplo conceitual:

```text
80
443
22
```

A porta SSH deverá ser protegida adequadamente.

A configuração definitiva será documentada na implantação.

---

# 47. SSH

Acesso administrativo à VPS deverá utilizar boas práticas.

Preferir:

```text
chaves SSH
```

em vez de depender apenas de senha.

---

# 48. Usuário do sistema

Evitar executar toda a aplicação como:

```text
root
```

A aplicação deverá utilizar usuário apropriado com privilégios mínimos.

---

# 49. Atualizações

A VPS e as dependências deverão ser atualizadas periodicamente.

Especialmente:

- sistema operacional;
- Python;
- Node;
- bibliotecas;
- Nginx;
- MySQL;
- Docker.

Atualizações críticas de segurança terão prioridade.

---

# 50. Dependências

Bibliotecas de terceiros representam superfície de ataque.

Antes de adicionar uma dependência:

1. verificar necessidade;
2. verificar maturidade;
3. verificar manutenção;
4. verificar vulnerabilidades conhecidas;
5. avaliar alternativas.

---

# 51. Dependências abandonadas

Evitar bibliotecas:

- abandonadas;
- sem manutenção;
- com vulnerabilidades críticas;
- com comunidade inexistente;

quando houver alternativa adequada.

---

# 52. Containers

Se Docker for utilizado:

- não executar tudo como root sem necessidade;
- limitar permissões;
- não colocar segredos na imagem;
- utilizar `.env`/secrets adequados;
- manter imagens atualizadas.

---

# 53. Imagens Docker

Nunca colocar:

```text
INSTAGRAM_APP_SECRET
SENHA_MYSQL
TOKEN
```

dentro do Dockerfile.

---

# 54. Segredos no Docker

Preferir:

```text
variáveis de ambiente
```

ou mecanismos seguros de secrets quando disponíveis.

---

# 55. Segurança do frontend

O frontend deverá:

- escapar conteúdo corretamente;
- evitar HTML arbitrário;
- validar dados para UX;
- nunca armazenar segredos de backend;
- utilizar HTTPS em produção.

---

# 56. XSS

Conteúdo vindo das redes sociais não deve ser considerado confiável.

Exemplo:

```text
legenda de Reel
```

pode conter conteúdo malicioso.

O frontend deverá renderizar texto de maneira segura.

Evitar inserir conteúdo externo diretamente como HTML.

---

# 57. CSRF

A estratégia dependerá do mecanismo de autenticação futuro.

Se forem utilizados cookies de sessão, deverão ser adotadas proteções apropriadas.

Se for utilizado outro mecanismo, avaliar o risco correspondente.

Não decidir a proteção antes de definir autenticação.

---

# 58. SSRF

Chamadas para URLs externas deverão ser controladas.

Não permitir que um usuário forneça arbitrariamente uma URL e faça o servidor consultar qualquer endereço interno.

Especialmente importante para funcionalidades futuras de:

```text
importar conteúdo por URL
```

---

# 59. Uploads futuros

Se o sistema passar a aceitar:

- imagens;
- vídeos;
- áudios;

os arquivos deverão possuir:

- limite de tamanho;
- validação de tipo;
- nome seguro;
- armazenamento controlado;
- análise quando necessário.

Essa funcionalidade não faz parte do MVP.

---

# 60. Segurança de conteúdo gerado por IA

No futuro, conteúdos gerados por IA deverão ser tratados como dados não confiáveis até serem validados.

A IA não deverá possuir automaticamente permissão para:

```text
publicar
excluir
alterar configurações
```

sem uma camada explícita de autorização.

---

# 61. Publicação automática futura

Quando o Motor de Publicação existir:

```text
IA
 ↓
Conteúdo
 ↓
Regras
 ↓
Autorização
 ↓
Publicação
```

Não permitir que um prompt isolado publique diretamente em uma conta social sem controles.

---

# 62. Auditoria futura

Ações importantes poderão gerar registros de auditoria.

Exemplos:

```text
login
alteração de senha
conexão de conta social
publicação
exclusão
alteração de configuração
```

Essa camada será necessária principalmente no SaaS.

---

# 63. Monitoramento futuro

Poderemos monitorar:

```text
erros
latência
uso de CPU
memória
disco
MySQL
chamadas externas
limites
```

Alertas serão adicionados conforme a necessidade operacional.

---

# 64. Incidentes

No futuro, deverá existir procedimento para:

```text
identificar
conter
corrigir
investigar
registrar
prevenir
```

incidentes de segurança.

No MVP, o objetivo é principalmente evitar exposição de credenciais e acesso indevido.

---

# 65. Checklist de segurança antes do deploy

Antes de produção:

```text
[ ] DEBUG desativado
[ ] HTTPS configurado
[ ] .env não versionado
[ ] chaves protegidas
[ ] MySQL não exposto
[ ] CORS restrito
[ ] logs sem segredos
[ ] usuário de banco limitado
[ ] firewall configurado
[ ] backups configurados
[ ] dependências verificadas
[ ] SSH protegido
[ ] usuário da aplicação sem privilégios excessivos
```

---

# 66. Checklist de segurança do código

Antes de aceitar uma implementação:

```text
[ ] entradas validadas
[ ] sem SQL concatenado
[ ] sem chaves no código
[ ] sem senha no código
[ ] sem token em logs
[ ] erros controlados
[ ] permissões verificadas
[ ] dependências necessárias
```

---

# 67. Regra para agentes de inteligência artificial

Antes de criar ou modificar código:

1. nunca colocar segredos diretamente no código;
2. nunca inventar credenciais;
3. nunca expor tokens;
4. utilizar configurações existentes;
5. validar entradas;
6. respeitar as camadas;
7. não acessar banco de forma insegura;
8. não desativar proteções para "fazer funcionar";
9. não liberar CORS indiscriminadamente;
10. atualizar documentação quando uma decisão de segurança mudar.

---

# 68. Regra contra atalhos perigosos

Nunca resolver problemas de desenvolvimento através de:

```text
desativar autenticação
desativar CORS
expor MySQL
colocar chave no código
executar como root
desabilitar HTTPS
ignorar validação
```

apenas para acelerar desenvolvimento.

Se um atalho for necessário temporariamente no ambiente local, ele deverá ser claramente restrito ao desenvolvimento.

---

# 69. Segurança no MVP

O MVP não precisa possuir toda a segurança de um SaaS maduro.

Mas precisa obrigatoriamente proteger:

```text
Credenciais
Banco
API externa
Código
Infraestrutura
```

---

# 70. Evolução da segurança

A segurança evoluirá em etapas:

```text
MVP
 ↓
HTTPS
 ↓
Autenticação
 ↓
Autorização
 ↓
Multi-organização
 ↓
Auditoria
 ↓
Monitoramento
 ↓
Segurança avançada
```

---

# 71. Regra final

> **O ViralCode deve ser simples de desenvolver, mas difícil de comprometer.**

No MVP:

```text
Segredos protegidos
+
Banco protegido
+
Entrada validada
+
API externa isolada
+
HTTPS em produção
```

Depois:

```text
Usuários
+
Organizações
+
Permissões
+
Auditoria
+
Monitoramento
```

A segurança deve crescer junto com o valor do sistema.

**Versão atual:** 0.1  
**Status:** Política de segurança revisada do ViralCode
