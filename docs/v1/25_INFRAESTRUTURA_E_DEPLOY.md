# 25 — INFRAESTRUTURA E DEPLOY

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define a infraestrutura necessária para executar o ViralCode localmente e posteriormente hospedá-lo em uma VPS da Hostinger.

A infraestrutura do MVP deverá ser simples, barata, administrável e suficiente para validar o negócio.

---

# 2. Princípio fundamental

No MVP:

```text
SIMPLICIDADE
>
COMPLEXIDADE
```

Não criar infraestrutura distribuída antes de existir necessidade real.

---

# 3. Arquitetura local

O ambiente de desenvolvimento deverá permitir:

```text
Computador local
│
├── React
├── FastAPI
└── MySQL
```

Opcionalmente:

```text
Docker Compose
```

poderá orquestrar os serviços.

---

# 4. Arquitetura inicial de produção

A primeira versão em produção poderá utilizar uma única VPS:

```text
INTERNET
    │
    ▼
   NGINX
    │
    ├──────────────► FRONTEND
    │
    └──────────────► FASTAPI
                         │
                         ▼
                       MYSQL
```

---

# 5. VPS

O primeiro ambiente de produção será hospedado em uma VPS da Hostinger.

A configuração exata da VPS deverá ser definida de acordo com:

```text
CPU
RAM
SSD
tráfego
número de usuários
volume de conteúdos
volume de chamadas de IA
```

Não dimensionar a infraestrutura definitiva antes dos primeiros dados reais de uso.

---

# 6. Sistema operacional

Preferir uma distribuição Linux estável e amplamente suportada.

A versão específica será definida durante a preparação da VPS.

---

# 7. Componentes de produção

Mínimo esperado:

```text
Linux
Nginx
Python
FastAPI
Servidor ASGI
MySQL
Node.js apenas quando necessário para build
Git
Docker, se adotado
```

---

# 8. Frontend em produção

O React deverá ser compilado para arquivos estáticos.

Fluxo:

```text
Código React
   ↓
Build
   ↓
Arquivos estáticos
   ↓
Nginx
```

Não é necessário manter o servidor de desenvolvimento React em produção.

---

# 9. Backend em produção

O FastAPI deverá ser executado por um servidor ASGI adequado.

Arquitetura:

```text
Internet
   ↓
Nginx
   ↓
Servidor ASGI
   ↓
FastAPI
```

---

# 10. Nginx

O Nginx será responsável por:

```text
HTTPS
proxy reverso
arquivos estáticos
roteamento
cabeçalhos
```

Também poderá futuramente atuar em:

```text
limitação
cache
compressão
```

---

# 11. HTTPS

Produção deverá utilizar:

```text
HTTPS
```

Não expor autenticação ou tokens através de HTTP puro.

---

# 12. Domínios

A arquitetura poderá utilizar:

```text
www.<dominio>
```

para frontend e:

```text
api.<dominio>
```

para backend.

Os domínios definitivos serão definidos quando o domínio do ViralCode for escolhido.

---

# 13. Fluxo de produção

```text
Usuário
   ↓
https://www.<dominio>
   ↓
Frontend React
   ↓
https://api.<dominio>
   ↓
FastAPI
   ↓
MySQL
```

---

# 14. Banco em produção

O MySQL poderá inicialmente permanecer na mesma VPS, desde que:

```text
volume
memória
CPU
segurança
backup
```

sejam adequados.

---

# 15. Não expor MySQL à internet

A porta do MySQL não deverá ficar publicamente acessível sem necessidade.

Preferir:

```text
FastAPI
   ↓
rede interna
   ↓
MySQL
```

---

# 16. Usuário do banco

A aplicação deverá utilizar um usuário próprio.

Não utilizar:

```text
root
```

para a aplicação.

Exemplo:

```text
usuario: viralcode_app
```

---

# 17. Privilégios do banco

O usuário da aplicação deverá possuir somente os privilégios necessários.

Não conceder:

```text
privilégios administrativos
```

sem necessidade.

---

# 18. Banco de desenvolvimento

O banco local poderá utilizar:

```text
MySQL
```

com credenciais próprias.

---

# 19. Migrações

As alterações do banco deverão ser aplicadas por migrações.

Fluxo:

```text
Código
   ↓
Migração
   ↓
Banco
```

Não depender de alterações manuais.

---

# 20. Deploy do banco

Antes de atualizar a aplicação em produção:

```text
backup
   ↓
migração
   ↓
aplicação
```

A ordem exata deverá ser avaliada conforme a alteração.

---

# 21. Git

O código deverá estar em um repositório Git.

Fluxo:

```text
Desenvolvimento
      ↓
Git
      ↓
VPS
```

---

# 22. Deploy inicial

No começo, o deploy poderá ser simples:

```text
git pull
 ↓
instalar dependências
 ↓
executar migrações
 ↓
build frontend
 ↓
reiniciar backend
 ↓
validar health check
```

---

# 23. Deploy automatizado

CI/CD poderá ser implementado posteriormente.

No MVP não é obrigatório criar um pipeline complexo.

---

# 24. Regra de deploy

Nunca executar mudanças diretamente sem saber:

```text
qual versão está instalada
qual código está sendo executado
qual banco está sendo utilizado
```

---

# 25. Versionamento

O projeto deverá possuir uma forma clara de identificar a versão em produção.

Exemplo:

```text
0.1.0
```

ou um identificador de commit Git.

---

# 26. Health check

Endpoint:

```http
GET /health
```

deverá permitir verificar se a API está viva.

---

# 27. Health detalhado

Posteriormente:

```http
GET /health/detalhado
```

poderá verificar:

```text
API
Banco
dependências essenciais
```

Sem expor segredos.

---

# 28. Monitoramento mínimo

A VPS deverá permitir observar:

```text
CPU
RAM
disco
processos
MySQL
FastAPI
Nginx
```

---

# 29. Logs

Deverão existir logs para:

```text
Nginx
FastAPI
aplicação
```

Os logs deverão possuir retenção adequada.

---

# 30. Logs e segredos

Nunca registrar:

```text
senha
token Instagram
client_secret
chave IA
token de autenticação
```

---

# 31. Backup do MySQL

Antes de colocar o MVP em produção, deverá existir backup automatizado do banco.

Estratégia inicial:

```text
backup diário
```

A retenção deverá ser definida conforme espaço disponível e criticidade.

---

# 32. Teste de restauração

Backup não será considerado válido apenas porque o arquivo foi criado.

Periodicamente deverá ser possível testar:

```text
backup
   ↓
restauração
   ↓
banco funcionando
```

---

# 33. Backup de arquivos

Caso o ViralCode passe a armazenar:

```text
imagens
vídeos
arquivos
```

será necessária uma estratégia específica.

No MVP não assumir armazenamento de mídia local permanente sem necessidade.

---

# 34. Armazenamento

Se o volume de mídia crescer, avaliar:

```text
Object Storage
```

em vez de manter tudo no disco da VPS.

---

# 35. Segurança da VPS

Aplicar pelo menos:

```text
SSH seguro
firewall
atualizações
usuário não-root
chaves SSH
HTTPS
```

---

# 36. Root

A aplicação não deverá rodar como:

```text
root
```

Criar usuário apropriado para execução do sistema.

---

# 37. Firewall

Permitir somente portas necessárias.

Exemplo conceitual:

```text
22  → SSH
80  → HTTP
443 → HTTPS
```

MySQL não deverá ser aberto publicamente.

---

# 38. SSH

Preferir autenticação por:

```text
chave SSH
```

em vez de senha quando possível.

---

# 39. Atualizações

A VPS deverá possuir rotina de atualização de:

```text
sistema operacional
pacotes
dependências
```

com cuidado para não quebrar a aplicação.

---

# 40. Processos

O backend deverá possuir um mecanismo para:

```text
iniciar
parar
reiniciar
```

automaticamente quando necessário.

Poderá ser utilizado um gerenciador de serviços do sistema ou outra solução apropriada.

---

# 41. Reinicialização

Após reinicialização da VPS, os serviços essenciais deverão voltar automaticamente.

Objetivo:

```text
VPS reinicia
   ↓
MySQL sobe
   ↓
Backend sobe
   ↓
Nginx sobe
   ↓
sistema disponível
```

---

# 42. Frontend

O build do frontend deverá ser reproduzível.

Exemplo conceitual:

```text
npm install
npm run build
```

Os comandos definitivos deverão estar documentados.

---

# 43. Backend

A instalação deverá ser reproduzível.

Exemplo conceitual:

```text
criar ambiente Python
instalar requisitos
executar migrações
iniciar FastAPI
```

---

# 44. Dependências fixadas

As versões das dependências deverão ser controladas.

Objetivo:

```text
ambiente local
≈
ambiente produção
```

---

# 45. Docker

O projeto poderá utilizar Docker para padronização.

No MVP, uma composição simples poderá ser:

```text
frontend
backend
mysql
```

---

# 46. Docker em produção

Não é obrigatório utilizar Docker em produção.

A decisão deverá considerar:

```text
facilidade
manutenção
desempenho
experiência da equipe
```

O importante é manter o processo reproduzível.

---

# 47. Ambiente local com Docker

Se Docker Compose for adotado:

```text
docker-compose.yml
```

deverá permitir iniciar o ambiente de desenvolvimento.

Exemplo conceitual:

```text
docker compose up -d
```

---

# 48. Persistência do MySQL

O MySQL em Docker deverá utilizar volume persistente.

Nunca depender somente do filesystem temporário do container.

---

# 49. Atualização do backend

Fluxo:

```text
novo código
   ↓
testes
   ↓
Git
   ↓
produção
   ↓
backup
   ↓
migração
   ↓
reinício
   ↓
health check
```

---

# 50. Atualização do frontend

Fluxo:

```text
novo código
   ↓
testes
   ↓
build
   ↓
publicação dos arquivos
   ↓
validação
```

---

# 51. Rollback

A arquitetura deverá permitir retornar para a versão anterior.

No mínimo:

```text
Git
+
backup do banco
```

deverão existir.

---

# 52. Rollback de banco

Migrações destrutivas deverão ser tratadas com cuidado.

Antes de alterações críticas:

```text
backup
```

---

# 53. Deploy sem downtime

Não é requisito do MVP.

O sistema poderá possuir uma pequena indisponibilidade durante deploy, desde que isso seja controlado.

---

# 54. Escalabilidade inicial

Uma única VPS deverá ser suficiente para validar o MVP.

Arquitetura:

```text
1 VPS
├── Nginx
├── Frontend
├── FastAPI
└── MySQL
```

---

# 55. Quando escalar

A arquitetura deverá ser revisada quando houver sinais como:

```text
CPU alta
RAM insuficiente
disco insuficiente
muitas chamadas de IA
muitos usuários
muitas publicações
tempo de resposta alto
```

---

# 56. Escalabilidade futura

Poderá evoluir para:

```text
Load Balancer
   ↓
Backend 1
Backend 2
Backend 3
   ↓
Banco
```

e:

```text
Fila
 ↓
Workers
```

Mas somente quando necessário.

---

# 57. Banco futuro

Quando o MySQL na mesma VPS deixar de ser adequado, poderá migrar para:

```text
MySQL gerenciado
```

ou servidor dedicado de banco.

---

# 58. Cache futuro

Não implementar Redis obrigatoriamente no MVP.

Poderá ser adicionado quando houver necessidade real de:

```text
cache
fila
sessão
locks
processamento
```

---

# 59. Filas futuras

Operações demoradas poderão evoluir para:

```text
API
 ↓
Fila
 ↓
Worker
 ↓
IA / Instagram
```

Isso será necessário somente quando o processamento síncrono não for suficiente.

---

# 60. Arquivos

Se o sistema passar a gerar arquivos grandes:

```text
não armazenar indiscriminadamente na VPS
```

Avaliar armazenamento externo.

---

# 61. Domínio

Quando o domínio for escolhido:

```text
DNS
 ↓
VPS
 ↓
Nginx
```

deverá ser configurado.

---

# 62. Certificado

O ambiente de produção deverá possuir certificado TLS válido.

A renovação deverá ser automatizada quando possível.

---

# 63. Proxy reverso

O Nginx deverá encaminhar:

```text
/api/*
```

para FastAPI.

E servir:

```text
frontend
```

como arquivos estáticos.

---

# 64. Separação de serviços

Conceitualmente:

```text
www.<dominio>
→ frontend

api.<dominio>
→ backend
```

---

# 65. CORS em produção

Permitir somente:

```text
www.<dominio>
```

ou as origens efetivamente utilizadas.

---

# 66. Segurança de cabeçalhos

O Nginx poderá aplicar cabeçalhos de segurança apropriados.

A configuração definitiva deverá ser validada antes da produção.

---

# 67. Compressão

Poderá utilizar compressão para respostas e arquivos quando apropriado.

Não é prioridade para o primeiro deploy.

---

# 68. Observabilidade

No MVP:

```text
logs
+
health check
+
métricas da VPS
```

serão suficientes.

Depois poderão ser adicionados:

```text
APM
monitoramento externo
alertas
rastreamento distribuído
```

---

# 69. Alertas

Futuramente criar alertas para:

```text
VPS indisponível
disco cheio
CPU alta
RAM alta
banco indisponível
API indisponível
```

---

# 70. Custos

A infraestrutura deverá ser dimensionada com foco em custo.

No início:

```text
uma VPS
+
MySQL
+
Nginx
```

deverá ser suficiente.

Os maiores custos variáveis provavelmente estarão em:

```text
IA
```

e, dependendo da estratégia adotada:

```text
armazenamento
```

---

# 71. Regra contra overengineering

Não contratar ou instalar:

```text
Kubernetes
clusters
múltiplas VPS
banco distribuído
service mesh
```

para o MVP.

---

# 72. Ambiente de produção mínimo

```text
VPS
 │
 ├── Nginx
 │
 ├── Frontend
 │
 ├── FastAPI
 │
 └── MySQL
```

---

# 73. Checklist de infraestrutura

```text
[ ] VPS criada
[ ] Linux atualizado
[ ] usuário de aplicação criado
[ ] SSH configurado
[ ] firewall configurado
[ ] Git instalado
[ ] Python instalado
[ ] Node instalado quando necessário
[ ] MySQL instalado/configurado
[ ] Nginx instalado
[ ] domínio configurado
[ ] HTTPS configurado
[ ] variáveis de ambiente configuradas
[ ] migrações executadas
[ ] backend funcionando
[ ] frontend funcionando
[ ] health check funcionando
[ ] backup funcionando
[ ] teste de restauração realizado
```

---

# 74. Checklist de deploy

Antes de cada deploy:

```text
[ ] testes passando
[ ] código versionado
[ ] backup quando necessário
[ ] migração revisada
[ ] variáveis verificadas
[ ] build realizado
[ ] deploy realizado
[ ] health check
[ ] teste funcional básico
```

---

# 75. Regra para agentes de IA

Antes de alterar infraestrutura:

1. ler este documento;
2. ler Configuração e Ambiente;
3. verificar o ambiente atual;
4. não abrir portas desnecessárias;
5. não expor MySQL;
6. não colocar segredos no código;
7. não instalar infraestrutura complexa sem necessidade;
8. testar;
9. documentar a alteração.

---

# 76. Regra para produção

Nenhuma IA ou desenvolvedor deverá assumir que pode executar alterações destrutivas na VPS.

Antes de:

```text
apagar
migrar
atualizar
reiniciar
substituir
```

deverá avaliar:

```text
impacto
backup
rollback
```

---

# 77. Critério de sucesso

A infraestrutura estará pronta quando:

```text
usuário
   ↓
domínio
   ↓
Nginx
   ↓
React
   ↓
FastAPI
   ↓
MySQL
```

funcionar de forma estável e segura em uma VPS.

---

# 78. Regra final

> **A infraestrutura do MVP deve ser pequena o suficiente para uma pessoa administrar e robusta o suficiente para suportar a validação do negócio.**

A arquitetura inicial oficial é:

```text
                    INTERNET
                       │
                       ▼
                     NGINX
                       │
              ┌────────┴────────┐
              ▼                 ▼
          FRONTEND            FASTAPI
          React                 │
                                ▼
                              MySQL
```

E deverá evoluir somente quando os dados reais do produto justificarem.

**Versão:** 1.0  
**Status:** Documento oficial de Infraestrutura e Deploy
