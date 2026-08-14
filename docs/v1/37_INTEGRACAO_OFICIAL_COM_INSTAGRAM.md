# 37 — INTEGRAÇÃO OFICIAL COM O INSTAGRAM

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode  
**Plataforma inicial:** Instagram

---

## 1. Objetivo

Este documento define a arquitetura de integração do ViralCode com o Instagram.

A integração deverá ser feita diretamente com as interfaces oficiais disponibilizadas pela Meta/Instagram, sem utilização de intermediários externos.

Princípio:

```text
ViralCode
   ↓
Conector Instagram
   ↓
API oficial da plataforma
```

---

# 2. Regra fundamental

O ViralCode não deverá assumir que qualquer informação disponível publicamente no Instagram pode ser obtida automaticamente pela API oficial.

Antes de implementar uma funcionalidade:

```text
necessidade do produto
        ↓
capacidade oficial da API
        ↓
permissão necessária
        ↓
implementação
```

---

# 3. Objetivos da integração no MVP

A integração inicial deverá priorizar:

```text
conectar conta
identificar conta conectada
consultar dados permitidos
importar conteúdos permitidos
obter métricas disponíveis
publicar conteúdo quando oficialmente suportado
```

---

# 4. Fora do escopo automático

O sistema não deverá prometer automaticamente:

```text
qualquer Reel público do Instagram
qualquer métrica pública
qualquer busca por hashtag
qualquer ranking global
qualquer dado de conta que a API não disponibilize
```

A capacidade real deverá ser validada contra a documentação oficial vigente da Meta no momento da implementação.

---

# 5. Conta do usuário

A arquitetura deverá trabalhar com uma conta social conectada ao perfil do ViralCode.

```text
Usuario
   ↓
Perfil
   ↓
ContaSocial
   ↓
Instagram
```

---

# 6. Conector isolado

Toda comunicação com o Instagram deverá ficar isolada em um conector.

Conceitualmente:

```text
backend/
└── conectores/
    └── instagram/
```

O restante do sistema não deverá conhecer detalhes HTTP específicos da plataforma.

---

# 7. Abstração

O domínio deverá trabalhar com conceitos próprios do ViralCode:

```text
ContaSocial
Conteudo
Publicacao
Metrica
```

e o conector deverá traduzir:

```text
Instagram
→
modelo interno ViralCode
```

---

# 8. Não acoplar o domínio

Evitar colocar no núcleo do sistema objetos específicos da API externa.

Exemplo ruim:

```text
Conteudo possui dezenas de campos exclusivos do Instagram
```

Preferir:

```text
Conteudo
+
dados externos quando necessários
```

---

# 9. Autorização

A conexão deverá seguir o mecanismo oficial de autorização da Meta/Instagram aplicável ao tipo de conta e operação desejada.

A implementação deverá utilizar:

```text
OAuth
```

quando exigido pelo fluxo oficial.

---

# 10. Estado OAuth

O fluxo deverá proteger contra ataques de associação indevida de conta.

Quando aplicável:

```text
state
 ↓
callback
 ↓
validação
 ↓
troca de código
```

---

# 11. Callback

O callback deverá:

```text
receber retorno
 ↓
validar state
 ↓
validar código
 ↓
obter credencial
 ↓
identificar conta
 ↓
persistir conexão
```

---

# 12. Credenciais

Credenciais recebidas da plataforma deverão ser tratadas como segredo.

Nunca:

```text
frontend
logs
resposta comum da API
mensagem de erro
```

---

# 13. Armazenamento

Quando houver necessidade de persistir credenciais:

```text
proteção adequada
acesso restrito
criptografia quando aplicável
```

A implementação definitiva deverá seguir o documento de segurança.

---

# 14. Expiração

A integração deverá controlar a validade das credenciais quando essa informação estiver disponível.

Estado:

```text
CONECTADA
```

poderá evoluir para:

```text
REAUTENTICACAO_NECESSARIA
```

---

# 15. Reautenticação

Quando a credencial deixar de ser válida:

```text
Instagram
 ↓
erro de autenticação
 ↓
ContaSocial = REAUTENTICACAO_NECESSARIA
 ↓
frontend informa usuário
```

---

# 16. Desconexão

Ao desconectar:

```text
usuário
 ↓
solicita desconexão
 ↓
ViralCode invalida/descarta credencial local quando aplicável
 ↓
ContaSocial = DESCONECTADA
```

A revogação externa deverá seguir as capacidades oficiais da plataforma.

---

# 17. Identificador externo

A conta deverá armazenar o identificador oficial necessário para futuras operações.

Exemplo:

```text
identificador_externo
```

---

# 18. Nome da conta

Quando disponível, armazenar:

```text
nome_externo
usuario_externo
```

para apresentação na interface.

---

# 19. Conta profissional

Antes de implementar recursos específicos, verificar os requisitos da Meta para:

```text
tipo de conta
permissões
produto utilizado
```

Não assumir que uma conta pessoal possui as mesmas capacidades de uma conta profissional.

---

# 20. Descoberta de conteúdo

A funcionalidade:

```text
"digitar casamento e encontrar Reels com mais de 1 milhão de visualizações"
```

deverá ser tratada como requisito separado da simples conexão da conta.

A API oficial poderá não fornecer todos os dados necessários para essa descoberta ampla.

Portanto:

```text
REQUISITO DO PRODUTO
≠
CAPACIDADE GARANTIDA DA API
```

---

# 21. Regra para descoberta

Antes de implementar o motor de descoberta:

```text
listar campos desejados
 ↓
verificar endpoint oficial
 ↓
verificar permissões
 ↓
verificar elegibilidade da conta
 ↓
verificar limites
 ↓
definir estratégia
```

---

# 22. Conteúdo externo

Se a API oficial permitir determinada descoberta, o conteúdo poderá ser normalizado para:

```text
Conteudo
```

com:

```text
origem = EXTERNO
```

---

# 23. Identificador externo do conteúdo

Para conteúdos externos, armazenar quando disponível:

```text
plataforma
identificador_externo
url_externa
```

Isso ajudará na deduplicação.

---

# 24. Deduplicação

Não importar repetidamente o mesmo conteúdo.

Chave lógica possível:

```text
plataforma
+
identificador_externo
```

---

# 25. Conteúdo próprio

Conteúdo criado pelo ViralCode será:

```text
origem = GERADO
```

ou:

```text
origem = MANUAL
```

---

# 26. Métricas

As métricas deverão ser coletadas somente quando a plataforma fornecer oficialmente o dado.

Exemplos que poderão existir, dependendo da operação:

```text
visualizações
curtidas
comentários
compartilhamentos
salvamentos
alcance
```

Não assumir disponibilidade universal.

---

# 27. Histórico de métricas

Quando permitido:

```text
publicação
 ↓
coleta
 ↓
Metrica
 ↓
nova coleta
 ↓
nova Metrica
```

Isso permitirá acompanhar evolução.

---

# 28. Publicação

A publicação deverá utilizar somente fluxos oficialmente suportados pela plataforma.

Arquitetura:

```text
Conteudo aprovado
       ↓
Publicacao
       ↓
Conector Instagram
       ↓
API oficial
       ↓
Instagram
```

---

# 29. Pré-condições para publicação

Antes de publicar:

```text
usuário autorizado
+
perfil válido
+
conta conectada
+
credencial válida
+
conteúdo aprovado
+
formato suportado
```

---

# 30. Publicação imediata

Fluxo:

```text
usuário
 ↓
aprovar
 ↓
publicar
 ↓
criar tentativa
 ↓
Instagram
 ↓
resultado
 ↓
atualizar Publicacao
```

---

# 31. Publicação agendada

Se o produto utilizar agendamento próprio:

```text
usuário
 ↓
agendar
 ↓
Publicacao = PENDENTE
 ↓
processador
 ↓
Instagram
```

A arquitetura deverá separar:

```text
agendamento do ViralCode
```

de:

```text
agendamento nativo da plataforma
```

quando ambos existirem.

---

# 32. Idempotência

A publicação deverá possuir proteção contra duplicidade.

Exemplo:

```text
mesmo conteúdo
+
mesma conta
+
mesma operação
```

não deverá gerar duas publicações por erro de retry.

---

# 33. Falha após envio

Um cenário crítico:

```text
ViralCode envia
 ↓
Instagram processa
 ↓
resposta não chega
```

O sistema não deverá concluir automaticamente:

```text
NÃO PUBLICOU
```

Deverá existir possibilidade de:

```text
reconciliação
```

quando suportada.

---

# 34. Reconciliação

Fluxo:

```text
estado local = ERRO/DESCONHECIDO
       ↓
consulta externa quando possível
       ↓
PUBLICADA
ou
NÃO PUBLICADA
ou
ESTADO DESCONHECIDO
```

---

# 35. Retry

Retries deverão existir somente para erros considerados recuperáveis.

Exemplos possíveis:

```text
timeout
erro temporário
indisponibilidade
```

Não repetir automaticamente erros como:

```text
credencial inválida
permissão insuficiente
conteúdo inválido
```

sem corrigir a causa.

---

# 36. Backoff

Quando houver retry:

```text
tentativa 1
 ↓
espera
 ↓
tentativa 2
 ↓
espera maior
 ↓
tentativa 3
```

A estratégia definitiva será definida na implementação.

---

# 37. Rate limits

A integração deverá respeitar os limites oficiais da plataforma.

Não criar loops que façam consultas repetidas sem necessidade.

---

# 38. Cache

Quando apropriado, dados que não precisam ser consultados continuamente poderão utilizar cache.

Exemplo:

```text
dados da conta
configurações
metadados
```

Cache nunca será fonte de verdade quando a plataforma for a fonte oficial.

---

# 39. Paginação

Listagens externas deverão respeitar o mecanismo de paginação fornecido pela plataforma.

O conector deverá abstrair a paginação do restante do sistema.

---

# 40. Normalização

O conector deverá transformar resposta externa em modelo interno.

Exemplo:

```text
Resposta Instagram
        ↓
normalizador
        ↓
Conteudo
```

---

# 41. Dados ausentes

Se um campo não estiver disponível:

```text
NULL
```

quando apropriado.

Não transformar ausência em:

```text
0
```

automaticamente.

---

# 42. Erros externos

Erros da plataforma deverão ser convertidos para códigos internos.

Exemplo:

```text
INSTAGRAM_AUTENTICACAO_INVALIDA
INSTAGRAM_PERMISSAO_NEGADA
INSTAGRAM_RATE_LIMIT
INSTAGRAM_INDISPONIVEL
INSTAGRAM_CONTEUDO_INVALIDO
```

---

# 43. Erro interno x externo

A API do ViralCode não deverá simplesmente repassar o erro bruto da plataforma.

Deverá:

```text
registrar detalhes técnicos internamente
+
retornar mensagem segura ao usuário
```

---

# 44. Correlation ID

Toda operação importante com o Instagram deverá possuir:

```text
correlation_id
```

para diagnóstico.

---

# 45. Logs

Registrar informações úteis:

```text
operação
conta
endpoint lógico
status
tempo
correlation_id
```

Nunca registrar:

```text
token
segredo
```

---

# 46. Auditoria

Ações relevantes poderão gerar auditoria:

```text
CONTA_INSTAGRAM_CONECTADA
CONTA_INSTAGRAM_DESCONECTADA
PUBLICACAO_SOLICITADA
PUBLICACAO_REALIZADA
```

---

# 47. Conector

O conector deverá expor métodos de domínio, não detalhes de HTTP.

Exemplo conceitual:

```text
conectar()
obter_conta()
listar_conteudos()
obter_metricas()
publicar()
desconectar()
```

Os métodos efetivos dependerão da capacidade oficial da API.

---

# 48. Interface futura para múltiplas redes

Criar uma abstração que permita:

```text
ConectorSocial
   ├── Instagram
   ├── TikTok
   └── YouTube
```

O MVP implementará:

```text
Instagram
```

---

# 49. Não criar abstração excessiva

Não construir dezenas de métodos genéricos antes de saber o que as próximas plataformas realmente exigem.

A abstração deverá representar capacidades reais compartilhadas.

---

# 50. Estado da integração

A conta social deverá possuir estado operacional.

Exemplo:

```text
CONECTADA
REAUTENTICACAO_NECESSARIA
DESCONECTADA
ERRO
```

---

# 51. Monitoramento

A Área Administrativa deverá conseguir identificar:

```text
contas conectadas
contas com erro
contas que precisam reautenticação
falhas de publicação
```

---

# 52. Testes

A integração deverá possuir testes para:

```text
autorização
callback
credencial inválida
permissão negada
timeout
rate limit
resposta inválida
publicação
retry
deduplicação
```

---

# 53. Testes sem depender sempre da API real

Criar uma camada que permita testar o sistema com:

```text
respostas simuladas
```

sem chamar a plataforma em todo teste automatizado.

---

# 54. Ambiente de desenvolvimento

As credenciais de desenvolvimento deverão ser separadas das de produção.

---

# 55. Contas de teste

Sempre que a plataforma oferecer mecanismos oficiais de teste, utilizá-los durante desenvolvimento.

---

# 56. Produção

Em produção:

```text
HTTPS
credenciais de produção
redirect URI correta
segredos protegidos
logs seguros
```

---

# 57. Redirect URI

As URLs de callback deverão ser configuradas explicitamente por ambiente.

Exemplo conceitual:

```text
DESENVOLVIMENTO
→ URL local

PRODUÇÃO
→ domínio do ViralCode
```

---

# 58. Configuração

As informações específicas da integração deverão vir de configuração:

```text
INSTAGRAM_CLIENT_ID
INSTAGRAM_CLIENT_SECRET
INSTAGRAM_REDIRECT_URI
```

Os nomes definitivos deverão seguir a convenção do projeto.

---

# 59. Não colocar segredo no React

O frontend poderá conhecer apenas informações públicas necessárias para iniciar o fluxo.

O `client_secret` deverá permanecer no backend.

---

# 60. Documentação externa

A implementação deverá consultar a documentação oficial vigente da Meta/Instagram antes de codificar cada capacidade.

Especialmente para:

```text
OAuth
permissões
métricas
publicação
limites
tipos de conta
```

---

# 61. Mudanças da plataforma

A API externa poderá mudar.

Por isso, o conector deverá ser isolado.

Quando a plataforma mudar:

```text
Instagram
 ↓
Conector
```

deverá absorver o máximo possível da mudança sem alterar todo o domínio.

---

# 62. Versionamento externo

Registrar quando necessário:

```text
versão da API externa
```

utilizada pela integração.

---

# 63. Compatibilidade

Não assumir que uma funcionalidade disponível hoje continuará disponível indefinidamente.

Testes de integração deverão ser mantidos.

---

# 64. Descoberta viral

O objetivo de negócio do ViralCode inclui encontrar conteúdos de alto desempenho.

Porém, a arquitetura deverá separar:

```text
MOTOR DE DESCOBERTA
```

de:

```text
CONECTOR INSTAGRAM
```

---

# 65. Motor de descoberta

Fluxo:

```text
usuário informa nicho
        ↓
motor de descoberta
        ↓
conector(es)
        ↓
dados permitidos
        ↓
normalização
        ↓
filtros
        ↓
ranking
        ↓
conteúdos candidatos
```

---

# 66. Filtro de visualizações

Se a fonte oficial fornecer visualizações:

```text
visualizacoes >= limite
```

poderá ser aplicado.

Exemplo:

```text
1.000.000
```

Mas o filtro só poderá ser executado sobre dados efetivamente disponíveis.

---

# 67. Ranking

O ranking poderá considerar:

```text
visualizações
engajamento
recência
relevância
```

quando os dados estiverem disponíveis.

---

# 68. Não confundir descoberta com scraping

O sistema não deverá criar automaticamente uma estratégia de scraping para contornar limitações da API oficial.

Se a capacidade oficial não atender ao requisito:

```text
registrar limitação
+
avaliar alternativa legal e técnica
```

---

# 69. Limitação conhecida

A capacidade de consultar conteúdo público de forma ampla e arbitrária deverá ser validada na implementação com a documentação oficial.

Não assumir que:

```text
"está público no Instagram"
```

significa:

```text
"está disponível para qualquer aplicação pela API"
```

---

# 70. Estratégia de fallback

Quando uma operação não puder ser realizada automaticamente:

```text
ViralCode
 ↓
identifica limitação
 ↓
informa usuário
 ↓
oferece alternativa suportada
```

quando existir.

---

# 71. Experiência do usuário

Mensagens deverão ser claras.

Evitar:

```text
Erro 190
```

como única mensagem.

Preferir algo como:

```text
Sua conexão com o Instagram precisa ser renovada.
```

---

# 72. Segurança

A integração deverá seguir:

```text
OAuth seguro
HTTPS
segredos protegidos
state
validação
rate limiting
logs sem tokens
```

---

# 73. Privacidade

Somente armazenar dados externos necessários para o produto.

---

# 74. Retenção

Dados externos deverão possuir estratégia de retenção coerente com:

```text
produto
privacidade
necessidade histórica
```

---

# 75. Exclusão

Quando uma conta for desconectada, definir separadamente:

```text
credencial
dados sincronizados
conteúdo próprio
histórico
métricas
```

A desconexão da conta não significa automaticamente apagar todo o histórico do usuário.

---

# 76. Conta desconectada

Após desconexão:

```text
não realizar novas chamadas autenticadas
```

até que exista nova autorização válida.

---

# 77. Publicações históricas

Publicações já realizadas poderão continuar no banco para:

```text
histórico
métricas
aprendizado
```

mesmo após desconexão, conforme regras de retenção.

---

# 78. Regra de domínio

O domínio não deverá saber:

```text
como o OAuth funciona
```

ou:

```text
qual endpoint HTTP foi chamado
```

Isso pertence ao conector.

---

# 79. Arquitetura resumida

```text
                    REACT
                      │
                      ▼
                   FASTAPI
                      │
                 SERVIÇO
                      │
              CONECTOR SOCIAL
                      │
                 INSTAGRAM
                      │
              API OFICIAL
```

---

# 80. Fluxo completo de conexão

```text
Usuário
  ↓
Conectar Instagram
  ↓
ViralCode
  ↓
Autorização oficial
  ↓
Callback
  ↓
Validação
  ↓
Credencial
  ↓
Identificação da conta
  ↓
ContaSocial
  ↓
CONECTADA
```

---

# 81. Fluxo completo de descoberta

```text
Nicho
 ↓
Motor de descoberta
 ↓
Conector Instagram
 ↓
Dados oficialmente disponíveis
 ↓
Normalização
 ↓
Deduplicação
 ↓
Filtros
 ↓
Ranking
 ↓
Conteúdos
 ↓
Análise
```

---

# 82. Fluxo completo de publicação

```text
Conteúdo aprovado
 ↓
Publicação
 ↓
Validação
 ↓
Conector Instagram
 ↓
API oficial
 ↓
Instagram
 ↓
Resultado
 ↓
Publicação atualizada
```

---

# 83. Critério de sucesso

A integração estará adequada quando:

```text
conta pode ser conectada
+
credencial é protegida
+
dados permitidos são sincronizados
+
conteúdo é normalizado
+
métricas disponíveis são coletadas
+
publicação suportada funciona
+
erros são tratados
+
operações podem ser diagnosticadas
```

---

# 84. Regra para agentes de IA

Antes de alterar a integração:

1. consultar este documento;
2. consultar documentação oficial vigente;
3. confirmar endpoint;
4. confirmar permissão;
5. confirmar tipo de conta;
6. confirmar limites;
7. atualizar conector;
8. criar/atualizar testes;
9. não criar workaround para burlar limitação da plataforma;
10. atualizar documentação.

---

# 85. Regra contra invenção

Uma IA não deverá implementar:

```text
endpoint imaginário
permissão imaginária
métrica imaginária
capacidade imaginária
```

Se a documentação oficial não confirmar uma capacidade:

```text
marcar como NÃO CONFIRMADA
```

e não tratá-la como disponível.

---

# 86. Regra final

> **O ViralCode deverá se adaptar à API oficial do Instagram, e não tentar forçar a API a fazer o que ela não oferece.**

A integração deverá permanecer isolada:

```text
DOMÍNIO VIRALCODE
       │
       ▼
CONECTOR INSTAGRAM
       │
       ▼
API OFICIAL
```

Isso permitirá que o núcleo do ViralCode continue preparado para múltiplas redes sociais sem contaminar o domínio com detalhes específicos de uma plataforma.

**Versão:** 1.0  
**Status:** Documento oficial da Integração com Instagram
