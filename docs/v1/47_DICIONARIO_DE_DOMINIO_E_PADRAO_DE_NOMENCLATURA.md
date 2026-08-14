# 47 — DICIONÁRIO DE DOMÍNIO E PADRÃO DE NOMENCLATURA

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define o vocabulário oficial do ViralCode.

Seu objetivo é evitar que:

```text
documentação
código
banco
API
frontend
IA
```

utilizem nomes diferentes para representar o mesmo conceito.

---

# 2. Princípio fundamental

Um conceito do negócio deverá possuir:

```text
um nome oficial
+
um significado oficial
```

---

# 3. Regra de nomenclatura

Antes de criar uma entidade, serviço, rota ou variável, verificar este documento.

Não criar sinônimos desnecessários.

---

# 4. ViralCode

**Definição:**

Plataforma para análise de conteúdo, identificação de padrões, geração de conteúdo e publicação em redes sociais, inicialmente com foco no Instagram.

---

# 5. Usuário

**Definição:**

Pessoa que possui acesso à plataforma ViralCode.

**Exemplo:**

```text
usuario_id
```

---

# 6. Perfil

**Definição:**

Configuração estratégica que representa como determinado perfil deverá produzir conteúdo.

Pode conter informações como:

```text
nome
nicho
objetivos
tom
público
preferências
```

---

# 7. Nicho

**Definição:**

Segmento temático ou mercadológico no qual um perfil atua.

Exemplos:

```text
fitness
casamento
educação
finanças
```

O sistema deverá permitir múltiplos nichos.

---

# 8. Rede Social

**Definição:**

Plataforma externa na qual conteúdos podem ser publicados ou de onde dados podem ser obtidos.

No MVP:

```text
Instagram
```

---

# 9. Conta Social

**Definição:**

Conta de uma rede social conectada a um perfil/usuário do ViralCode.

Exemplo:

```text
ContaSocial
```

---

# 10. Instagram

**Definição:**

Rede social utilizada na primeira implementação do ViralCode.

A integração deverá utilizar os mecanismos oficiais disponíveis.

---

# 11. Conexão

**Definição:**

Estado/registro que representa a autorização e configuração necessária para o ViralCode utilizar uma conta social.

---

# 12. Token

**Definição:**

Credencial técnica utilizada para autenticação/autorização com um serviço externo.

Tokens são dados sensíveis.

---

# 13. Conteúdo

**Definição:**

Unidade de conteúdo utilizada pelo ViralCode para análise, criação, revisão ou publicação.

Pode representar:

```text
post
reel
```

ou outros formatos futuros.

---

# 14. Conteúdo Externo

**Definição:**

Conteúdo obtido de uma rede social ou outra fonte externa.

---

# 15. Conteúdo Próprio

**Definição:**

Conteúdo pertencente ao perfil/usuário dentro do contexto do ViralCode.

---

# 16. Conteúdo Gerado

**Definição:**

Conteúdo produzido pelo motor de geração do ViralCode, podendo utilizar IA.

---

# 17. Post

**Definição:**

Formato de publicação estática ou equivalente suportado pela rede social.

---

# 18. Reel

**Definição:**

Formato de vídeo curto utilizado pelo Instagram.

---

# 19. Publicação

**Definição:**

Operação de enviar um conteúdo para uma rede social para que ele seja publicado.

---

# 20. Publicação não é Conteúdo

Um:

```text
Conteúdo
```

pode existir sem ser publicado.

Uma:

```text
Publicação
```

representa uma operação/registro relacionado ao envio daquele conteúdo para uma rede social.

---

# 21. Status da Publicação

Estados possíveis deverão ser definidos pela implementação.

Conceitualmente:

```text
PENDENTE
PROCESSANDO
PUBLICADA
ERRO
CANCELADA
```

---

# 22. Análise

**Definição:**

Processamento realizado para extrair informações relevantes de conteúdos ou dados.

---

# 23. Análise de Conteúdo

**Definição:**

Processo que transforma conteúdo bruto em informações estruturadas úteis para o ViralCode.

---

# 24. Insight

**Definição:**

Informação relevante identificada durante uma análise.

Exemplos:

```text
padrão de hook
tema recorrente
estrutura
formato
abordagem
```

---

# 25. Padrão

**Definição:**

Característica recorrente identificada em um conjunto de conteúdos.

---

# 26. Tendência

**Definição:**

Comportamento ou padrão que apresenta sinais de crescimento, recorrência ou relevância dentro de determinado contexto.

---

# 27. Benchmark

**Definição:**

Conteúdo, perfil ou conjunto de dados utilizado como referência comparativa.

---

# 28. Referência

**Definição:**

Objeto utilizado para orientar análise ou geração.

Pode ser:

```text
conteúdo
perfil
tema
estrutura
padrão
```

---

# 29. Descoberta

**Definição:**

Processo de localizar conteúdos, perfis, temas ou padrões relevantes para análise.

---

# 30. Coleta

**Definição:**

Processo de obter dados de uma fonte externa e trazê-los para o contexto do ViralCode.

---

# 31. Importação

**Definição:**

Processo de persistir no ViralCode dados obtidos de uma fonte externa.

---

# 32. Normalização

**Definição:**

Processo de converter diferentes formatos externos para o modelo interno do ViralCode.

Exemplo:

```text
Instagram
 ↓
Normalizador
 ↓
Conteúdo interno
```

---

# 33. Deduplicação

**Definição:**

Processo de impedir que o mesmo conteúdo externo seja armazenado várias vezes.

---

# 34. Métrica

**Definição:**

Valor quantitativo associado a um conteúdo, perfil ou publicação.

Exemplos:

```text
visualizações
curtidas
comentários
compartilhamentos
```

---

# 35. Métrica Externa

**Definição:**

Métrica obtida de uma plataforma externa.

---

# 36. Métrica Interna

**Definição:**

Métrica calculada pelo próprio ViralCode.

---

# 37. Motor de Análise

**Definição:**

Componente responsável por processar dados e identificar:

```text
padrões
insights
métricas derivadas
```

---

# 38. Motor de Geração

**Definição:**

Componente responsável por produzir novos conteúdos utilizando:

```text
dados analisados
perfil
nicho
objetivos
regras
IA
```

---

# 39. Motor de Publicação

**Definição:**

Componente responsável por executar e acompanhar publicações em redes sociais.

---

# 40. Provedor de IA

**Definição:**

Serviço externo utilizado para processamento de inteligência artificial.

---

# 41. Modelo de IA

**Definição:**

Modelo específico utilizado por um provedor para executar determinada operação de IA.

---

# 42. Prompt

**Definição:**

Instrução enviada ao modelo de IA juntamente com o contexto necessário para executar uma operação.

---

# 43. Contexto

**Definição:**

Conjunto de informações fornecidas à IA para orientar uma execução.

Pode conter:

```text
perfil
nicho
conteúdos
insights
objetivos
regras
```

---

# 44. Execução de IA

**Definição:**

Registro de uma operação realizada pelo motor de IA.

Pode conter:

```text
modelo
entrada
resultado
status
tempo
tokens
custo
erro
```

---

# 45. Status da Execução de IA

Conceitualmente:

```text
PENDENTE
PROCESSANDO
CONCLUIDA
ERRO
CANCELADA
```

---

# 46. Geração

**Definição:**

Processo de produzir conteúdo novo a partir de contexto, regras e, quando aplicável, IA.

---

# 47. Rascunho

**Definição:**

Conteúdo ainda não aprovado para publicação.

---

# 48. Aprovação

**Definição:**

Ação pela qual o usuário autoriza que determinado conteúdo siga para publicação.

---

# 49. Publicação Manual

**Definição:**

Publicação iniciada explicitamente pelo usuário.

---

# 50. Publicação Automática

**Definição:**

Publicação executada automaticamente conforme uma configuração previamente autorizada.

Não é requisito obrigatório do primeiro MVP.

---

# 51. Agendamento

**Definição:**

Configuração que determina quando uma publicação deverá ser executada.

---

# 52. Fila

**Definição:**

Conjunto de operações aguardando processamento.

---

# 53. Worker

**Definição:**

Processo responsável por executar tarefas fora do ciclo imediato da requisição HTTP.

---

# 54. Tarefa

**Definição:**

Unidade de trabalho que pode ser executada pelo sistema.

---

# 55. Serviço

**Definição:**

Componente responsável por executar regras de negócio.

---

# 56. Repositório

**Definição:**

Componente responsável por abstrair operações de persistência.

---

# 57. Conector

**Definição:**

Componente responsável por encapsular comunicação com um sistema externo.

Exemplos:

```text
ConectorInstagram
ConectorProvedorIA
```

---

# 58. API

**Definição:**

Interface HTTP utilizada para comunicação entre frontend, backend e integrações.

---

# 59. Endpoint

**Definição:**

Rota específica disponibilizada pela API.

Exemplo:

```http
GET /api/v1/conteudos
```

---

# 60. Contrato da API

**Definição:**

Conjunto de regras que define:

```text
entrada
saída
status HTTP
erros
autenticação
```

de cada endpoint.

---

# 61. Autenticação

**Definição:**

Processo de verificar quem é o usuário.

Pergunta:

```text
Quem é você?
```

---

# 62. Autorização

**Definição:**

Processo de verificar o que o usuário pode fazer.

Pergunta:

```text
Você pode fazer isso?
```

---

# 63. Sessão

**Definição:**

Estado que representa a autenticação ativa de um usuário.

---

# 64. Administrador

**Definição:**

Usuário com permissões administrativas específicas.

---

# 65. Área Administrativa

**Definição:**

Interface destinada à operação e administração do ViralCode.

Pode conter:

```text
usuários
perfis
integrações
conteúdos
publicações
IA
erros
saúde do sistema
```

---

# 66. Dashboard

**Definição:**

Tela que apresenta informações resumidas e relevantes para acompanhamento.

---

# 67. Saúde do Sistema

**Definição:**

Estado operacional dos componentes principais.

Exemplos:

```text
API
Banco
Instagram
IA
```

---

# 68. Health Check

**Definição:**

Endpoint utilizado para verificar disponibilidade operacional.

---

# 69. Observabilidade

**Definição:**

Capacidade de compreender o comportamento interno do sistema por meio de:

```text
logs
métricas
rastreamento
```

---

# 70. Correlation ID

**Definição:**

Identificador utilizado para relacionar logs e operações pertencentes à mesma requisição ou fluxo.

---

# 71. Incidente

**Definição:**

Evento que causa impacto relevante em:

```text
disponibilidade
funcionalidade
dados
segurança
```

---

# 72. Backup

**Definição:**

Cópia de dados utilizada para recuperação.

---

# 73. Rollback

**Definição:**

Processo de retornar a uma versão anterior da aplicação ou configuração.

---

# 74. Ambiente

**Definição:**

Contexto em que o sistema é executado.

Principais:

```text
desenvolvimento
produção
```

Outros poderão ser adicionados futuramente.

---

# 75. Desenvolvimento

**Definição:**

Ambiente utilizado para criar e testar alterações.

---

# 76. Produção

**Definição:**

Ambiente utilizado pelos usuários reais.

---

# 77. VPS

**Definição:**

Servidor virtual utilizado para hospedar o ViralCode em produção inicialmente.

---

# 78. Infraestrutura

**Definição:**

Conjunto de recursos necessários para executar o sistema.

Exemplos:

```text
VPS
NGINX
Docker
MySQL
rede
armazenamento
```

---

# 79. NGINX

**Definição:**

Servidor/proxy utilizado na infraestrutura para:

```text
HTTPS
arquivos frontend
proxy reverso
```

---

# 80. MySQL

**Definição:**

Banco de dados relacional utilizado pelo ViralCode.

---

# 81. SQLAlchemy

**Definição:**

Camada utilizada pelo backend para interação com o banco de dados.

---

# 82. FastAPI

**Definição:**

Framework utilizado para construir a API backend.

---

# 83. React

**Definição:**

Tecnologia utilizada para construção do frontend.

---

# 84. Frontend

**Definição:**

Parte visual da aplicação utilizada pelo usuário.

---

# 85. Backend

**Definição:**

Parte do sistema responsável por:

```text
API
regras
persistência
integrações
```

---

# 86. Banco de Dados

**Definição:**

Camada persistente utilizada para armazenar informações estruturadas do ViralCode.

---

# 87. Variável de Ambiente

**Definição:**

Configuração fornecida pelo ambiente de execução e não incorporada diretamente ao código.

---

# 88. Segredo

**Definição:**

Informação que deve permanecer protegida.

Exemplos:

```text
senha
token
client_secret
chave de API
```

---

# 89. LGPD

**Definição:**

Lei brasileira de proteção de dados pessoais considerada na arquitetura do ViralCode.

---

# 90. Dado Pessoal

**Definição:**

Informação relacionada a pessoa natural identificada ou identificável.

---

# 91. Minimização

**Definição:**

Princípio de coletar e processar somente os dados necessários para determinada finalidade.

---

# 92. Fonte Externa

**Definição:**

Sistema ou serviço fora do controle direto do ViralCode.

Exemplos:

```text
Instagram
provedor de IA
```

---

# 93. Estado Externo

**Definição:**

Estado registrado ou existente em um sistema externo.

Exemplo:

```text
publicado no Instagram
```

---

# 94. Estado Interno

**Definição:**

Estado armazenado e controlado pelo ViralCode.

---

# 95. Reconciliação

**Definição:**

Processo de comparar o estado interno com o estado externo para identificar divergências.

---

# 96. Idempotência

**Definição:**

Capacidade de repetir uma operação sem gerar efeitos duplicados indevidos.

Exemplo:

```text
mesma publicação
+
mesma chave
=
não publicar duas vezes
```

---

# 97. Retry

**Definição:**

Nova tentativa de executar uma operação após uma falha considerada temporária.

---

# 98. Rate Limit

**Definição:**

Limite de quantidade/frequência de requisições permitido por um serviço.

---

# 99. MVP

**Definição:**

Primeira versão funcional do ViralCode criada para validar o negócio com o menor conjunto necessário de funcionalidades.

---

# 100. Escalabilidade

**Definição:**

Capacidade de aumentar o volume suportado pelo sistema sem comprometer seu funcionamento.

---

# 101. Arquitetura

**Definição:**

Organização dos componentes, responsabilidades, dependências e fluxos do ViralCode.

---

# 102. Camada

**Definição:**

Separação lógica de responsabilidades dentro da arquitetura.

Exemplo:

```text
API
 ↓
Serviço
 ↓
Repositório
 ↓
Banco
```

---

# 103. Regra de negócio

**Definição:**

Comportamento que representa uma necessidade ou decisão do produto.

---

# 104. Entidade

**Definição:**

Objeto do domínio que possui identidade própria e representa uma informação relevante do negócio.

---

# 105. Identificador interno

**Definição:**

Identificador utilizado pelo ViralCode para referenciar uma entidade.

Exemplo:

```text
usuario_id
conteudo_id
perfil_id
```

---

# 106. Identificador externo

**Definição:**

Identificador fornecido por uma plataforma externa.

Exemplo:

```text
instagram_id
```

---

# 107. Campo interno

**Definição:**

Campo pertencente ao modelo interno do ViralCode.

---

# 108. Campo externo

**Definição:**

Campo originado de uma plataforma externa.

---

# 109. Normalizador

**Definição:**

Componente responsável por transformar dados externos no modelo interno.

---

# 110. Gerador

**Definição:**

Componente responsável por produzir conteúdo novo.

---

# 111. Publicador

**Definição:**

Componente responsável por executar uma publicação através do conector correspondente.

---

# 112. Analisador

**Definição:**

Componente responsável por executar análise sobre dados ou conteúdos.

---

# 113. Perfil de Conteúdo

**Definição:**

Conjunto de características que orientam a produção de conteúdo de um perfil.

Pode incluir:

```text
nicho
público
tom
objetivos
formatos
regras
```

---

# 114. Estratégia de Conteúdo

**Definição:**

Conjunto de decisões que orientam:

```text
o que publicar
para quem
com qual objetivo
em qual formato
```

---

# 115. Calendário Editorial

**Definição:**

Planejamento temporal das publicações.

---

# 116. Tema

**Definição:**

Assunto central de determinado conteúdo.

---

# 117. Hook

**Definição:**

Elemento inicial utilizado para chamar a atenção do público.

O termo técnico poderá permanecer como:

```text
hook
```

---

# 118. CTA

**Definição:**

Chamada para ação presente em um conteúdo.

---

# 119. Legenda

**Definição:**

Texto associado a uma publicação.

---

# 120. Roteiro

**Definição:**

Estrutura textual que orienta a produção de um Reel ou outro conteúdo audiovisual.

---

# 121. Estrutura de Conteúdo

**Definição:**

Organização dos elementos que compõem determinado conteúdo.

Exemplo:

```text
hook
desenvolvimento
prova
CTA
```

---

# 122. Benchmark de Conteúdo

**Definição:**

Conjunto de conteúdos utilizados para identificar padrões e oportunidades.

---

# 123. Oportunidade

**Definição:**

Possibilidade identificada pelo motor de análise para orientar produção ou estratégia.

---

# 124. Recomendação

**Definição:**

Sugestão produzida pelo ViralCode com base em dados, regras ou IA.

---

# 125. Confiança

**Definição:**

Indicador utilizado quando o sistema precisar representar o grau de segurança de determinada inferência.

Não deve ser utilizado como garantia de verdade.

---

# 126. Evidência

**Definição:**

Dado ou informação observável que sustenta uma análise ou recomendação.

---

# 127. Inferência

**Definição:**

Conclusão produzida a partir de dados disponíveis.

---

# 128. Hipótese

**Definição:**

Possibilidade sugerida que ainda necessita de validação.

---

# 129. Regra para IA

A IA deverá distinguir, quando aplicável:

```text
EVIDÊNCIA
INFERÊNCIA
HIPÓTESE
```

para evitar apresentar suposições como fatos.

---

# 130. Status

**Definição:**

Estado atual de uma entidade ou operação.

---

# 131. Ativo

**Definição:**

Objeto atualmente habilitado para utilização.

---

# 132. Inativo

**Definição:**

Objeto existente, porém não disponível para utilização naquele momento.

---

# 133. Desconectado

**Definição:**

Estado em que uma integração social não está autorizada/disponível.

---

# 134. Expirado

**Definição:**

Credencial ou estado que deixou de ser válido.

---

# 135. Erro

**Definição:**

Resultado de uma operação que não conseguiu completar seu objetivo.

---

# 136. Cancelado

**Definição:**

Operação interrompida intencionalmente antes de sua conclusão.

---

# 137. Concluído

**Definição:**

Operação que terminou com resultado disponível.

---

# 138. Processando

**Definição:**

Operação que está sendo executada.

---

# 139. Pendente

**Definição:**

Operação aguardando processamento.

---

# 140. Regra contra sinônimos

Evitar alternar entre:

```text
conteúdo
post
material
publicação
```

quando os conceitos forem diferentes.

Exemplo:

```text
Conteúdo ≠ Publicação
```

---

# 141. Regra para Instagram

Usar:

```text
Conta Social
```

para a abstração interna.

Usar:

```text
Instagram
```

quando estiver falando especificamente da plataforma.

---

# 142. Regra para IA

Usar:

```text
Provedor de IA
```

para a abstração externa.

Usar o nome específico do fornecedor somente quando necessário.

---

# 143. Regra para geração

Usar:

```text
Motor de Geração
```

para o componente de negócio.

Não confundir com:

```text
Provedor de IA
```

---

# 144. Regra para publicação

Usar:

```text
Motor de Publicação
```

para a regra/orquestração interna.

Usar:

```text
Conector Instagram
```

para a comunicação externa.

---

# 145. Regra para análise

Usar:

```text
Motor de Análise
```

para processamento interno.

---

# 146. Regra para dados externos

O fluxo deverá ser entendido como:

```text
Fonte Externa
 ↓
Conector
 ↓
Normalizador
 ↓
Modelo Interno
 ↓
Motor de Análise
```

---

# 147. Regra para geração

Fluxo:

```text
Perfil
+
Nicho
+
Dados analisados
+
Regras
 ↓
Motor de Geração
 ↓
Conteúdo
```

---

# 148. Regra para publicação

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

# 149. Regra para IA

Fluxo:

```text
Serviço
 ↓
Motor/Serviço de IA
 ↓
Conector do Provedor
 ↓
Modelo de IA
```

---

# 150. Regra final

> **O vocabulário do ViralCode deve ser estável.**

Antes de criar um novo termo:

```text
já existe um conceito equivalente?
```

Se existir:

```text
usar o termo oficial
```

Se não existir:

```text
definir o novo termo
+
registrá-lo neste documento
```

---

## 151. Tabela resumida

| Termo | Significado |
|---|---|
| Usuário | Pessoa que utiliza o ViralCode |
| Perfil | Configuração estratégica de um perfil |
| Nicho | Segmento de atuação |
| Conta Social | Conta de rede social conectada |
| Conteúdo | Unidade de conteúdo |
| Publicação | Operação de publicar conteúdo |
| Análise | Processamento de dados/conteúdo |
| Insight | Informação relevante identificada |
| Motor de Análise | Componente de análise |
| Motor de Geração | Componente de criação |
| Motor de Publicação | Componente de publicação |
| Conector | Integração com sistema externo |
| Provedor de IA | Serviço externo de IA |
| Execução de IA | Registro de uma operação de IA |
| Métrica | Valor quantitativo |
| Descoberta | Localização de dados/conteúdos |
| Normalização | Conversão para modelo interno |
| Deduplicação | Prevenção de registros duplicados |
| Rascunho | Conteúdo não aprovado |
| Aprovação | Autorização para seguir para publicação |
| Correlation ID | Identificador de rastreamento |
| Incidente | Evento com impacto relevante |
| MVP | Primeira versão para validação do negócio |

---

**Versão:** 1.0  
**Status:** Documento oficial do Dicionário de Domínio e Padrão de Nomenclatura
