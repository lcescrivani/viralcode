# 40 — INFRAESTRUTURA LOCAL E VPS

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode  
**Hospedagem alvo:** VPS Hostinger

---

## 1. Objetivo

Este documento define a infraestrutura necessária para executar o ViralCode inicialmente em ambiente local e posteriormente em uma VPS da Hostinger.

Objetivo do MVP:

```text
DESENVOLVIMENTO LOCAL
        ↓
TESTES
        ↓
DEPLOY VPS
        ↓
PRODUÇÃO
```

---

# 2. Princípio fundamental

A infraestrutura inicial deverá ser simples.

Não criar uma arquitetura distribuída antes de existir necessidade real.

---

# 3. Arquitetura alvo do MVP

```text
                    INTERNET
                       │
                       ▼
                    HTTPS
                       │
                       ▼
                    NGINX
                       │
              ┌────────┴────────┐
              ▼                 ▼
           FRONTEND           FASTAPI
            REACT                │
                                 ▼
                              MYSQL
                                 │
                 ┌───────────────┼───────────────┐
                 ▼               ▼               ▼
             INSTAGRAM          IA          ARMAZENAMENTO
```

O armazenamento de mídia será definido conforme a necessidade real do MVP.

---

# 4. Ambiente local

O desenvolvimento deverá permitir executar:

```text
React
FastAPI
MySQL
```

localmente.

---

# 5. Serviços locais

Estrutura conceitual:

```text
frontend
backend
mysql
```

Serviços externos:

```text
Instagram
provedor de IA
```

serão acessados somente quando necessário.

---

# 6. Docker

O projeto poderá utilizar Docker para padronizar o ambiente.

A recomendação para o MVP é utilizar Docker principalmente para:

```text
MySQL
backend
frontend
```

quando isso simplificar a reprodução do ambiente.

---

# 7. Docker Compose

Poderá existir:

```text
docker-compose.yml
```

ou equivalente atual do Docker Compose.

---

# 8. Princípio do Compose

O ambiente local deverá conseguir subir os serviços necessários de forma previsível.

Exemplo:

```text
docker compose up
```

---

# 9. MySQL local

O banco deverá possuir:

```text
volume persistente
```

para não perder dados ao reiniciar o container.

---

# 10. Banco local

Configuração conceitual:

```text
host: mysql
porta: 3306
banco: viralcode
```

Quando o backend estiver fora do Docker:

```text
host: localhost
```

---

# 11. Persistência

Não depender do filesystem temporário do container para dados importantes.

---

# 12. Backend

O FastAPI deverá executar como serviço independente.

Fluxo:

```text
NGINX
 ↓
FASTAPI
```

---

# 13. Frontend

O React poderá ser:

```text
servido por NGINX
```

em produção.

---

# 14. Produção

Arquitetura inicial recomendada:

```text
VPS
│
├── NGINX
├── FRONTEND
├── FASTAPI
├── MYSQL
└── PROCESSOS AUXILIARES
```

---

# 15. Uma VPS

Para o MVP, uma única VPS poderá hospedar:

```text
frontend
backend
mysql
nginx
```

desde que os recursos sejam suficientes.

---

# 16. Não criar cluster no MVP

Não utilizar inicialmente:

```text
Kubernetes
Docker Swarm
cluster distribuído
múltiplos servidores
```

sem necessidade.

---

# 17. Domínios

A infraestrutura deverá permitir separar:

```text
app.seudominio.com
api.seudominio.com
```

ou utilizar uma estrutura equivalente.

Os domínios reais serão definidos posteriormente.

---

# 18. HTTPS

Produção deverá utilizar:

```text
HTTPS
```

---

# 19. Certificado

O certificado TLS deverá ser gerenciado de forma automatizada quando possível.

---

# 20. NGINX

O NGINX terá como responsabilidades:

```text
HTTPS
proxy reverso
roteamento
arquivos estáticos
headers
```

---

# 21. Proxy reverso

Fluxo:

```text
Internet
 ↓
NGINX
 ↓
FastAPI
```

---

# 22. Frontend

Fluxo:

```text
Internet
 ↓
NGINX
 ↓
arquivos React
```

---

# 23. API

Fluxo:

```text
Internet
 ↓
NGINX
 ↓
http://backend:8000
```

---

# 24. Não expor MySQL

O MySQL não deverá ficar acessível publicamente pela Internet.

---

# 25. Firewall

A VPS deverá permitir somente portas necessárias.

Conceitualmente:

```text
80
443
```

e acesso administrativo seguro à VPS.

---

# 26. SSH

O acesso administrativo deverá ser protegido.

Preferir:

```text
chave SSH
```

em vez de senha quando possível.

---

# 27. Usuário do sistema

Evitar executar toda a aplicação como:

```text
root
```

---

# 28. Containers

Quando houver containers, utilizar usuários não privilegiados quando compatível com a aplicação.

---

# 29. Variáveis de ambiente

Segredos deverão ser configurados no ambiente da VPS.

Não colocar:

```text
.env de produção
```

no Git.

---

# 30. Deploy

Fluxo inicial:

```text
Git
 ↓
VPS
 ↓
atualizar código
 ↓
instalar/construir
 ↓
migrações
 ↓
reiniciar
```

---

# 31. Migrações

Antes de aplicar alteração estrutural importante:

```text
backup
 ↓
migração
 ↓
teste
```

---

# 32. Alembic

As alterações do MySQL deverão ser controladas pelo:

```text
Alembic
```

---

# 33. Rollback

Migrações deverão ser planejadas para permitir rollback quando tecnicamente possível.

---

# 34. Backup do MySQL

O MVP deverá possuir backup automático ou agendado do banco.

---

# 35. Backup mínimo

Recomendação inicial:

```text
backup diário
```

---

# 36. Retenção

Manter mais de uma cópia.

Exemplo conceitual:

```text
últimos 7 dias
```

A política definitiva poderá evoluir conforme criticidade e custo.

---

# 37. Backup não é teste de backup

Periodicamente deverá ser verificado se o backup realmente pode ser restaurado.

---

# 38. Restauração

Deverá existir procedimento documentado para:

```text
restaurar banco
```

---

# 39. Mídia

Reels, imagens e outros arquivos poderão exigir armazenamento próprio.

No MVP, a estratégia deverá ser simples e não prender o domínio ao armazenamento local da VPS.

---

# 40. Regra de mídia

Não armazenar arquivos grandes permanentemente dentro do container.

---

# 41. Armazenamento futuro

A arquitetura poderá evoluir para:

```text
Object Storage
```

quando houver necessidade.

---

# 42. Logs

Os serviços deverão gerar logs.

Componentes:

```text
NGINX
FastAPI
worker
MySQL
```

---

# 43. Logs da aplicação

Os logs do FastAPI deverão permitir identificar:

```text
data
nível
correlation_id
operação
erro
```

---

# 44. Não registrar segredos

Nunca registrar:

```text
senha
token
client_secret
chave IA
```

---

# 45. Rotação de logs

Logs não deverão crescer indefinidamente.

Utilizar:

```text
log rotation
```

ou mecanismo equivalente.

---

# 46. Monitoramento

O MVP deverá possuir monitoramento básico:

```text
servidor disponível?
API disponível?
MySQL disponível?
disco cheio?
memória suficiente?
```

---

# 47. Health check

Endpoint:

```http
GET /health
```

deverá indicar se a aplicação está operacional.

---

# 48. Health detalhado

Poderá existir:

```http
GET /health/detalhado
```

para verificar dependências.

Não expor detalhes sensíveis publicamente.

---

# 49. Reinício automático

Processos essenciais deverão possuir mecanismo de reinício automático quando falharem.

Pode ser:

```text
Docker restart policy
```

ou:

```text
systemd
```

ou equivalente.

---

# 50. Disponibilidade

O MVP não precisa de alta disponibilidade.

Objetivo:

```text
simplicidade
+
estabilidade
+
recuperação rápida
```

---

# 51. Escalabilidade vertical

Primeiro caminho de escala:

```text
aumentar CPU
+
aumentar RAM
+
aumentar armazenamento
```

na VPS.

---

# 52. Escalabilidade horizontal

Somente quando houver necessidade real:

```text
múltiplas instâncias FastAPI
```

---

# 53. MySQL separado

No futuro, o banco poderá sair da mesma VPS.

No MVP não é necessário.

---

# 54. Cache

Não adicionar Redis no MVP somente por precaução.

Adicionar quando existir uma necessidade concreta.

---

# 55. Filas

O processamento assíncrono poderá inicialmente utilizar um mecanismo simples.

Não adicionar Kafka ou infraestrutura pesada.

---

# 56. Worker

Quando houver necessidade de:

```text
publicação agendada
análise longa
geração longa
coleta de métricas
```

poderá existir:

```text
worker
```

---

# 57. Arquitetura futura

```text
NGINX
   │
   ├── React
   │
   └── FastAPI
          │
          ├── MySQL
          ├── Worker
          ├── Instagram
          └── IA
```

---

# 58. Segurança do servidor

A VPS deverá possuir:

```text
firewall
atualizações
SSH protegido
HTTPS
segredos protegidos
serviços desnecessários desativados
```

---

# 59. Atualizações

Sistema operacional e componentes deverão receber atualizações de segurança.

---

# 60. Timezone

A aplicação deverá definir claramente a estratégia de timezone.

Recomendação:

```text
armazenamento → UTC
apresentação → timezone do usuário
```

A decisão final deverá ser aplicada consistentemente.

---

# 61. Datas

O banco e API deverão utilizar formatos de data consistentes.

---

# 62. Recursos da VPS

A capacidade necessária dependerá do uso real.

No início, acompanhar:

```text
CPU
RAM
disco
rede
MySQL
processos
```

---

# 63. Gargalos

Possíveis gargalos:

```text
IA
Instagram
MySQL
CPU
RAM
disco
rede
```

---

# 64. Não otimizar antes de medir

Primeiro:

```text
medir
 ↓
identificar gargalo
 ↓
otimizar
```

---

# 65. Ambiente local ≠ produção

Não assumir que:

```text
funcionou no Windows
```

significa:

```text
produção pronta
```

---

# 66. Paridade

Quanto possível, manter ambientes semelhantes em:

```text
Python
Node
MySQL
Docker
dependências
```

---

# 67. Dependências

Versões deverão ser fixadas/controladas.

Evitar instalar:

```text
última versão aleatória
```

durante cada deploy.

---

# 68. Build frontend

O React deverá gerar uma versão de produção otimizada.

---

# 69. Build backend

O backend deverá utilizar ambiente isolado com dependências declaradas.

---

# 70. Arquivos de infraestrutura

A estrutura poderá conter:

```text
docker-compose.yml
Dockerfile
Dockerfile.frontend
nginx/
.env.exemplo
```

conforme a implementação.

---

# 71. Estrutura sugerida

```text
viralcode/
│
├── backend/
├── frontend/
├── infraestrutura/
│   ├── nginx/
│   ├── docker/
│   └── scripts/
├── docs/
└── .env.exemplo
```

---

# 72. Scripts

Scripts operacionais poderão automatizar:

```text
subir ambiente
parar ambiente
backup
restauração
deploy
logs
```

---

# 73. Deploy repetível

O deploy deverá ser reproduzível.

Evitar sequência manual obscura como:

```text
"faça esses 18 comandos que eu lembro"
```

---

# 74. Checklist de deploy

Antes de produção:

```text
código atualizado
testes executados
backup realizado
variáveis configuradas
migrações revisadas
build concluído
HTTPS funcionando
health funcionando
logs funcionando
```

---

# 75. Pós-deploy

Após deploy:

```text
health
login
dashboard
banco
Instagram
IA
```

deverão ser verificados conforme o escopo alterado.

---

# 76. Rollback de aplicação

Deverá ser possível voltar para uma versão anterior do código.

---

# 77. Rollback de banco

Alterações de banco exigem cuidado adicional.

Não assumir que:

```text
rollback do código
```

implica:

```text
rollback automático do banco
```

---

# 78. Segurança de backup

Backups deverão ser protegidos contra acesso público.

---

# 79. Backup externo

Quando possível, manter cópia fora da VPS para reduzir risco de perda total.

---

# 80. Monitoramento de disco

O sistema deverá alertar antes que:

```text
disco = 100%
```

---

# 81. Monitoramento de memória

Acompanhar consumo de:

```text
RAM
swap
```

quando aplicável.

---

# 82. Monitoramento de CPU

Acompanhar picos relacionados a:

```text
IA
build
processamento
```

---

# 83. Banco

Acompanhar:

```text
tamanho
conexões
tempo de consultas
erros
```

---

# 84. Observabilidade

O mínimo necessário:

```text
logs
health
métricas básicas da VPS
```

---

# 85. Não criar observabilidade excessiva

Não instalar uma stack completa de observabilidade no MVP sem necessidade.

---

# 86. Desenvolvimento

Fluxo:

```text
desenvolvedor
 ↓
Git
 ↓
ambiente local
 ↓
testes
```

---

# 87. Produção

Fluxo:

```text
Git
 ↓
deploy
 ↓
VPS
 ↓
NGINX
 ↓
usuário
```

---

# 88. Controle de versão

O código deverá permanecer em Git.

---

# 89. Branches

A estratégia de branches deverá ser simples.

No MVP, evitar um processo excessivamente burocrático.

---

# 90. Segredos no Git

Se um segredo for acidentalmente commitado:

```text
revogar imediatamente
+
gerar novo
```

Não basta apagar o arquivo em um commit posterior.

---

# 91. Domínio

Quando o domínio estiver definido:

```text
DNS
 ↓
VPS
 ↓
NGINX
 ↓
HTTPS
```

---

# 92. DNS

Configurar registros necessários para:

```text
app
api
```

quando essa estratégia for adotada.

---

# 93. Firewall de aplicação

O NGINX poderá aplicar proteções básicas.

---

# 94. Rate limiting

O backend deverá controlar limites de API.

O NGINX poderá complementar quando necessário.

---

# 95. CORS

O backend deverá aceitar somente origens configuradas.

---

# 96. Hostinger

A VPS da Hostinger será tratada como infraestrutura de produção inicial.

As especificações exatas da VPS deverão ser registradas quando o plano contratado estiver definido.

---

# 97. Não assumir recursos

Não documentar como garantido algo que depende do plano contratado.

Exemplo:

```text
RAM
CPU
backup automático
IPv4
```

deverão ser confirmados no momento da contratação.

---

# 98. Critério de promoção

O projeto poderá sair do ambiente local quando:

```text
MVP funcional
+
testes mínimos
+
backup
+
HTTPS
+
health
+
logs
+
configuração segura
```

estiverem prontos.

---

# 99. Regra para agentes de IA

Antes de alterar infraestrutura:

1. consultar este documento;
2. consultar Configuração e Variáveis de Ambiente;
3. verificar ambiente local;
4. verificar produção;
5. evitar introduzir serviços desnecessários;
6. testar;
7. documentar;
8. considerar backup e rollback.

---

# 100. Regra contra complexidade

Não adicionar:

```text
Kubernetes
Kafka
Redis
cluster
microserviços adicionais
```

sem uma necessidade comprovada.

---

# 101. Critério de sucesso

A infraestrutura estará adequada quando:

```text
desenvolvedor consegue subir localmente
+
MySQL possui persistência
+
FastAPI funciona
+
React funciona
+
produção possui HTTPS
+
NGINX roteia corretamente
+
segredos estão protegidos
+
backup existe
+
logs existem
+
health existe
+
deploy é repetível
```

---

# 102. Arquitetura final do MVP

```text
                         INTERNET
                            │
                          HTTPS
                            │
                            ▼
                          NGINX
                       ┌────┴────┐
                       ▼         ▼
                    REACT     FASTAPI
                                 │
                         ┌───────┼────────┐
                         ▼       ▼        ▼
                       MYSQL  INSTAGRAM   IA
                         │
                       BACKUP
```

---

# 103. Evolução futura

Quando o ViralCode crescer:

```text
                 LOAD BALANCER
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
      FASTAPI 1                 FASTAPI 2
          │                         │
          └────────────┬────────────┘
                       ▼
                    MYSQL
                       │
                 ┌─────┴─────┐
                 ▼           ▼
               FILA       STORAGE
                 │
               WORKERS
```

Essa evolução somente deverá acontecer quando métricas reais justificarem.

---

# 104. Regra final

> **A infraestrutura do MVP deve ser simples o suficiente para uma pessoa operar, segura o suficiente para colocar o produto em produção e preparada o suficiente para crescer sem precisar ser reconstruída imediatamente.**

O caminho oficial será:

```text
LOCAL
 ↓
TESTES
 ↓
VPS
 ↓
PRODUÇÃO
 ↓
ESCALA CONFORME NECESSIDADE
```

**Versão:** 1.0  
**Status:** Documento oficial da Infraestrutura Local e VPS
