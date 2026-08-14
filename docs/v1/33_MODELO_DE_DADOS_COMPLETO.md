# 33 — MODELO DE DADOS COMPLETO

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define o modelo lógico de dados do ViralCode para o MVP.

O objetivo é transformar a arquitetura conceitual em uma estrutura concreta de persistência:

```text
ENTIDADE
   ↓
ATRIBUTOS
   ↓
RELACIONAMENTOS
   ↓
REGRAS DE INTEGRIDADE
   ↓
MYSQL
```

Este documento será a referência para:

```text
SQLAlchemy
migrações
repositórios
serviços
API
testes
```

---

# 2. Banco

Banco oficial:

```text
MySQL
```

ORM/camada de persistência:

```text
SQLAlchemy
```

Migrações:

```text
Alembic
```

---

# 3. Princípio de modelagem

O modelo deverá representar o domínio do ViralCode, e não simplesmente reproduzir telas.

A estrutura central será:

```text
USUÁRIO
   ↓
PERFIL
   ↓
CONTA SOCIAL

PERFIL
   ↓
CONTEÚDOS
   ↓
ANÁLISES
   ↓
INSIGHTS
   ↓
APRENDIZADOS

CONTEÚDO
   ↓
PUBLICAÇÃO
   ↓
MÉTRICAS
```

---

# 4. Entidades principais

O MVP deverá trabalhar principalmente com:

```text
Usuario
Perfil
ContaSocial
Conteudo
Analise
Insight
Aprendizado
Publicacao
Metrica
ExecucaoIA
Auditoria
```

---

# 5. Entidade Usuario

Representa a pessoa que utiliza o ViralCode.

Campos conceituais:

```text
id
nome
email
senha_hash
status
criado_em
atualizado_em
ultimo_acesso_em
```

---

# 6. Regras de Usuario

```text
email obrigatório
email único
senha nunca armazenada em texto puro
status obrigatório
criado_em obrigatório
```

---

# 7. Status de Usuario

Valores iniciais:

```text
ATIVO
BLOQUEADO
PENDENTE
```

O conjunto poderá evoluir.

---

# 8. Relacionamento Usuario → Perfil

Um usuário poderá possuir vários perfis.

```text
Usuario 1 ───── N Perfil
```

Exemplo:

```text
Leonardo
 ├── Perfil Casamento
 ├── Perfil Fitness
 └── Perfil Educação
```

O sistema não deverá limitar a arquitetura a um único perfil por usuário.

---

# 9. Entidade Perfil

Representa uma unidade estratégica de conteúdo.

Campos conceituais:

```text
id
usuario_id
nome
descricao
nicho
subnicho
publico_alvo
posicionamento
tom_de_voz
objetivo
status
criado_em
atualizado_em
```

---

# 10. Regra de Perfil

Cada perfil deverá pertencer a exatamente um usuário.

```text
Perfil.usuario_id → Usuario.id
```

---

# 11. Nicho

O nicho será tratado como dado de contexto.

Exemplo:

```text
casamento
fitness
educação
finanças
```

Não criar lógica de código específica para um nicho.

---

# 12. Subnicho

O subnicho permitirá maior precisão.

Exemplo:

```text
Nicho: casamento
Subnicho: restauração de casamentos
```

---

# 13. Público-alvo

Campo destinado ao contexto de criação.

Exemplo:

```text
casais de 30 a 50 anos
```

---

# 14. Posicionamento

Descrição de como o perfil deseja ser percebido.

Exemplo:

```text
especialista em restauração de relacionamentos
```

---

# 15. Tom de voz

Informação utilizada pelo motor de criação.

Exemplo:

```text
direto
acolhedor
provocativo
didático
```

---

# 16. Objetivo

Exemplo:

```text
crescimento
engajamento
autoridade
vendas
relacionamento
```

---

# 17. Entidade ContaSocial

Representa uma conta de rede social conectada ao ViralCode.

Campos conceituais:

```text
id
perfil_id
plataforma
identificador_externo
nome_externo
usuario_externo
status
token_criptografado
token_expira_em
conectado_em
atualizado_em
```

A estrutura definitiva de credenciais deverá seguir as regras de segurança.

---

# 18. Plataforma

No MVP:

```text
INSTAGRAM
```

A arquitetura deverá permitir futuramente:

```text
TIKTOK
YOUTUBE
OUTRAS
```

---

# 19. Identificador externo

O `identificador_externo` representa o ID fornecido pela plataforma.

A combinação:

```text
plataforma
+
identificador_externo
```

deverá ser avaliada como candidata a unicidade.

---

# 20. Status de ContaSocial

Valores iniciais:

```text
CONECTADA
REAUTENTICACAO_NECESSARIA
DESCONECTADA
ERRO
```

---

# 21. Regra de credencial

Nunca retornar para o frontend:

```text
token_criptografado
```

ou qualquer credencial equivalente.

---

# 22. Entidade Conteudo

Representa um conteúdo conhecido pelo ViralCode.

É importante distinguir:

```text
conteúdo externo
```

de:

```text
conteúdo próprio
```

---

# 23. Campos de Conteudo

Campos conceituais:

```text
id
perfil_id
conta_social_id
tipo
origem
identificador_externo
url_externa
titulo
descricao
legenda
hook
roteiro
cta
status
criado_em
atualizado_em
```

Nem todos os campos precisarão estar preenchidos em todos os conteúdos.

---

# 24. Origem do conteúdo

Valores:

```text
EXTERNO
GERADO
MANUAL
```

---

# 25. Tipo de conteúdo

O MVP deverá suportar pelo menos a distinção necessária para:

```text
REEL
POST
```

A arquitetura poderá evoluir para:

```text
CARROSSEL
STORY
VIDEO
OUTROS
```

---

# 26. Conteúdo externo

Conteúdo descoberto na rede deverá possuir, quando disponível:

```text
plataforma
identificador externo
URL
autor/conta externa
data de publicação
métricas
```

Campos adicionais poderão ser incorporados conforme os dados realmente fornecidos pela integração.

---

# 27. Conteúdo gerado

Conteúdo criado pelo ViralCode deverá possuir:

```text
ideia
hook
roteiro
legenda
cta
```

quando aplicável.

---

# 28. Status de Conteudo

Valores iniciais:

```text
RASCUNHO
GERADO
EM_REVISAO
APROVADO
PLANEJADO
PUBLICADO
ARQUIVADO
```

---

# 29. Regra de propriedade

Um conteúdo próprio deverá estar associado a um perfil.

A API deverá validar que:

```text
perfil
→ pertence ao usuário autenticado
```

---

# 30. Entidade Analise

Representa uma análise realizada sobre um conteúdo.

Campos conceituais:

```text
id
conteudo_id
execucao_ia_id
versao_prompt
modelo
status
resultado
criado_em
atualizado_em
```

---

# 31. Resultado da análise

O resultado deverá ser estruturado.

Exemplo conceitual:

```json
{
  "tema": "...",
  "subtema": "...",
  "hook": "...",
  "estrutura": [],
  "emocao": "...",
  "cta": "..."
}
```

A estrutura final será definida pelos esquemas da aplicação.

---

# 32. Status da análise

Valores iniciais:

```text
PENDENTE
PROCESSANDO
CONCLUIDA
ERRO
```

---

# 33. Entidade ExecucaoIA

Representa uma chamada ao provedor de inteligência artificial.

Campos conceituais:

```text
id
usuario_id
perfil_id
tipo
provedor
modelo
versao_prompt
status
tempo_execucao_ms
tokens_entrada
tokens_saida
custo_estimado
erro_codigo
erro_mensagem
criado_em
finalizado_em
```

---

# 34. Objetivo da ExecucaoIA

Permitir:

```text
diagnóstico
auditoria técnica
controle de custo
medição de performance
```

---

# 35. Não armazenar segredos

A execução de IA não deverá armazenar:

```text
chave do provedor
segredo
credencial
```

---

# 36. Status da ExecucaoIA

Valores iniciais:

```text
PENDENTE
PROCESSANDO
CONCLUIDA
ERRO
CANCELADA
```

---

# 37. Tipos de ExecucaoIA

Exemplos:

```text
ANALISE
INSIGHT
CRIACAO
ROTEIRO
LEGENDA
CTA
APRENDIZADO
```

O conjunto poderá evoluir.

---

# 38. Entidade Insight

Representa uma conclusão derivada de análises e dados.

Campos conceituais:

```text
id
perfil_id
titulo
descricao
tipo
confianca
status
criado_em
atualizado_em
```

---

# 39. Confiança do Insight

Poderá utilizar:

```text
BAIXA
MEDIA
ALTA
```

No futuro poderá evoluir para uma pontuação quantitativa.

---

# 40. Evidências do Insight

Um insight deverá poder apontar para os dados que o sustentam.

A implementação poderá utilizar uma entidade intermediária:

```text
InsightEvidencia
```

relacionando:

```text
Insight
+
Conteudo
+
Metrica
```

quando necessário.

---

# 41. Entidade Aprendizado

Representa uma conclusão reutilizável pelo motor de criação.

Campos conceituais:

```text
id
perfil_id
insight_id
titulo
descricao
confianca
status
criado_em
atualizado_em
```

---

# 42. Diferença entre Insight e Aprendizado

```text
INSIGHT
→ conclusão sobre determinado conjunto de dados

APRENDIZADO
→ conclusão considerada útil para orientar ações futuras
```

---

# 43. Exemplo

Insight:

```text
3 conteúdos com perguntas diretas tiveram desempenho acima da média.
```

Aprendizado:

```text
Perguntas diretas são uma estratégia promissora para este perfil.
```

---

# 44. Entidade Publicacao

Representa uma tentativa/resultado de publicação de um conteúdo em uma rede social.

Campos conceituais:

```text
id
conteudo_id
conta_social_id
status
identificador_externo
agendado_para
publicado_em
tentativas
erro_codigo
erro_mensagem
criado_em
atualizado_em
```

---

# 45. Status de Publicacao

Valores:

```text
PENDENTE
ENVIANDO
PUBLICADA
ERRO
CANCELADA
```

---

# 46. Idempotência da publicação

Uma publicação deverá possuir mecanismo para evitar envio duplicado.

O modelo deverá suportar uma chave ou identificador de operação apropriado.

---

# 47. Entidade Metrica

Representa uma medição de desempenho.

Campos conceituais:

```text
id
conteudo_id
publicacao_id
tipo
valor
coletado_em
```

---

# 48. Tipos de métrica

Exemplos:

```text
VISUALIZACOES
CURTIDAS
COMENTARIOS
COMPARTILHAMENTOS
SALVAMENTOS
ALCANCE
```

Somente métricas efetivamente disponíveis deverão ser armazenadas.

---

# 49. Histórico de métricas

Uma publicação poderá possuir várias medições:

```text
Publicação
 ├── Medição 10:00
 ├── Medição 14:00
 └── Medição 18:00
```

---

# 50. NULL x zero

Regra:

```text
NULL
→ métrica não disponível

0
→ métrica disponível e igual a zero
```

---

# 51. Entidade Auditoria

Representa ações administrativas ou eventos importantes que precisam de rastreabilidade.

Campos conceituais:

```text
id
administrador_id
acao
entidade
entidade_id
detalhes
ip
criado_em
```

---

# 52. Regra de Auditoria

Não armazenar em `detalhes`:

```text
senha
token
client_secret
```

---

# 53. Administrador

A arquitetura poderá utilizar o próprio usuário com uma função/permissão administrativa ou possuir uma entidade administrativa separada.

Para o MVP, preferir uma estrutura simples de:

```text
Usuario
+
perfil/permissão administrativa
```

evitando duplicação de identidade.

---

# 54. Relacionamentos principais

```text
Usuario
  1 ─── N Perfil

Perfil
  1 ─── N ContaSocial

Perfil
  1 ─── N Conteudo

Conteudo
  1 ─── N Analise

Conteudo
  1 ─── N Publicacao

Publicacao
  1 ─── N Metrica

Perfil
  1 ─── N Insight

Perfil
  1 ─── N Aprendizado

ExecucaoIA
  1 ─── N Analise
```

A cardinalidade final deverá ser ajustada quando os casos de uso forem implementados.

---

# 55. Relacionamento de ExecucaoIA

Uma execução de IA poderá produzir diferentes tipos de resultado.

Por isso, o modelo deverá evitar acoplá-la exclusivamente à análise.

Conceitualmente:

```text
ExecucaoIA
   ↓
Análise
ou
Insight
ou
Criação
ou
Aprendizado
```

A implementação poderá usar referências específicas conforme o domínio.

---

# 56. Conteúdo externo e perfil

Um conteúdo externo poderá ser descoberto no contexto de um perfil.

Isso permite:

```text
Perfil
 ↓
Conteúdos analisados
```

sem tornar o conteúdo externo propriedade do usuário original da rede.

---

# 57. Identidade do autor externo

Quando disponível, poderá ser armazenada em campos de referência externa ou entidade própria futuramente.

Não é necessário criar um cadastro completo do autor externo no MVP.

---

# 58. Nichos no banco

No MVP, o nicho poderá ser armazenado diretamente no perfil.

Exemplo:

```text
Perfil.nicho
Perfil.subnicho
```

Uma tabela de catálogo de nichos poderá ser adicionada posteriormente.

---

# 59. Por que não criar catálogo agora

Para o MVP:

```text
menos tabelas
menos regras
menos complexidade
```

O catálogo será necessário quando houver necessidade real de:

```text
padronização
administração
relatórios
taxonomia
```

---

# 60. Estados

Estados importantes deverão ser representados de forma consistente.

Preferir:

```text
enum no domínio
+
validação na aplicação
```

e, quando apropriado:

```text
restrição no banco
```

---

# 61. Datas

Entidades principais deverão possuir timestamps.

Padrão conceitual:

```text
criado_em
atualizado_em
```

e campos específicos quando necessário.

---

# 62. Auditoria temporal

Não adicionar dezenas de campos de data sem necessidade.

Adicionar somente quando houver significado de negócio ou operacional.

---

# 63. Índices prioritários

O modelo deverá avaliar índices para:

```text
Usuario.email

Perfil.usuario_id

ContaSocial.perfil_id

ContaSocial.plataforma + identificador_externo

Conteudo.perfil_id

Conteudo.identificador_externo

Analise.conteudo_id

Publicacao.conteudo_id

Publicacao.conta_social_id

Metrica.publicacao_id

ExecucaoIA.usuario_id
```

Os índices definitivos serão validados pelas consultas reais.

---

# 64. Unicidade

Possíveis restrições:

```text
Usuario.email
ContaSocial.plataforma + identificador_externo
```

Outras regras de unicidade deverão ser definidas pelos casos de uso.

---

# 65. Chaves estrangeiras

Relacionamentos importantes deverão utilizar foreign keys.

Exemplo:

```text
Perfil.usuario_id → Usuario.id
```

---

# 66. Exclusão

Não aplicar cascatas indiscriminadamente.

Antes de excluir:

```text
Usuario
Perfil
Conteudo
Publicacao
```

deverá ser avaliado o impacto no histórico.

---

# 67. Histórico

O sistema deverá preservar dados necessários para:

```text
análise histórica
aprendizado
auditoria
diagnóstico
```

---

# 68. Conteúdo publicado

Mesmo depois de arquivado, o conteúdo poderá precisar continuar existindo para:

```text
métricas
aprendizados
histórico
```

---

# 69. Aprendizado e evidência

Um aprendizado não deverá depender de um texto solto sem possibilidade de rastreamento.

Quando relevante:

```text
Aprendizado
 ↓
Insight
 ↓
Evidências
 ↓
Conteúdos / Métricas
```

---

# 70. Dados derivados

Alguns valores poderão ser calculados.

Exemplo:

```text
taxa de engajamento
```

Não necessariamente precisa ser armazenada no MVP se puder ser calculada de forma eficiente.

---

# 71. Quando armazenar derivado

Armazenar um valor derivado quando houver necessidade de:

```text
histórico
performance
auditoria
```

---

# 72. JSON

Campos JSON poderão ser utilizados para:

```text
resultado da análise
metadados externos
configurações flexíveis
```

Mas informações centrais do domínio não deverão ser escondidas em JSON sem necessidade.

---

# 73. Resultado de IA

O resultado estruturado poderá ser armazenado como JSON inicialmente.

Posteriormente, campos de alto uso poderão ser promovidos para colunas próprias.

---

# 74. Evolução do modelo

O banco deverá evoluir por migrações.

Nunca editar produção manualmente como prática normal.

---

# 75. Migrações

Ferramenta:

```text
Alembic
```

Fluxo:

```text
alterar modelo
 ↓
gerar/revisar migração
 ↓
testar
 ↓
aplicar
```

---

# 76. Backup antes de alteração crítica

Migrações destrutivas deverão considerar:

```text
backup
teste
rollback
```

---

# 77. Dados de teste

O projeto deverá possuir dados de desenvolvimento controlados.

Não utilizar dados reais como seed padrão.

---

# 78. Escalabilidade

O modelo deverá suportar:

```text
múltiplos usuários
múltiplos perfis
múltiplas contas sociais
múltiplos conteúdos
múltiplas publicações
histórico de métricas
```

---

# 79. Não otimizar prematuramente

Não criar:

```text
sharding
banco distribuído
event sourcing
```

no MVP.

---

# 80. Arquitetura lógica

```text
USUARIO
   │
   └── PERFIL
         │
         ├── CONTA_SOCIAL
         │
         ├── CONTEUDO
         │      │
         │      ├── ANALISE
         │      │      └── EXECUCAO_IA
         │      │
         │      └── PUBLICACAO
         │             └── METRICA
         │
         ├── INSIGHT
         │
         └── APRENDIZADO

USUARIO
   │
   └── EXECUCAO_IA

ADMIN
   │
   └── AUDITORIA
```

---

# 81. Modelo mínimo do MVP

As entidades indispensáveis são:

```text
Usuario
Perfil
ContaSocial
Conteudo
Analise
ExecucaoIA
Publicacao
Metrica
```

As entidades:

```text
Insight
Aprendizado
Auditoria
```

fazem parte da arquitetura e poderão ter implementação progressiva conforme o escopo do MVP.

---

# 82. Prioridade de implementação

### P0

```text
Usuario
Perfil
ContaSocial
Conteudo
```

### P1

```text
Analise
ExecucaoIA
Publicacao
Metrica
```

### P2

```text
Insight
Aprendizado
Auditoria avançada
```

---

# 83. Regra para agentes de IA

Antes de criar uma tabela:

1. verificar se a entidade já existe;
2. verificar se o dado pertence a outra entidade;
3. verificar relacionamento;
4. verificar necessidade de histórico;
5. verificar índices;
6. verificar segurança;
7. criar migração;
8. criar testes;
9. atualizar documentação.

---

# 84. Regra contra duplicação

Não criar:

```text
TabelaConteudoInstagram
TabelaConteudoTikTok
TabelaConteudoYouTube
```

para representar o mesmo conceito.

Preferir:

```text
Conteudo
+
plataforma
```

ou uma abstração equivalente.

---

# 85. Regra contra acoplamento

O modelo central do ViralCode não deverá depender de campos exclusivos do Instagram quando eles não forem necessários ao domínio.

---

# 86. Regra de evolução multi-rede

Arquitetura:

```text
Conteudo
   ↓
Publicacao
   ↓
ContaSocial
   ↓
Plataforma
```

Isso permitirá futuramente:

```text
Instagram
TikTok
YouTube
```

sem duplicar o modelo de conteúdo.

---

# 87. Regra de histórico

Métricas não deverão simplesmente substituir o valor anterior quando o produto precisar acompanhar evolução.

Preferir:

```text
Metrica
   ↓
medição temporal
```

---

# 88. Regra de fonte de verdade

```text
MySQL
→ fonte de verdade do negócio

Instagram
→ fonte de verdade dos dados externos

IA
→ fonte de geração/análise, não de estado do negócio
```

---

# 89. Regra final

> **O modelo de dados do ViralCode deve preservar a história necessária para transformar observação em inteligência.**

A estrutura essencial é:

```text
USUÁRIO
   ↓
PERFIL
   ↓
CONTEÚDO
   ↓
ANÁLISE
   ↓
CRIAÇÃO
   ↓
PUBLICAÇÃO
   ↓
MÉTRICAS
   ↓
INSIGHTS
   ↓
APRENDIZADOS
```

Esse histórico será a base para o ViralCode evoluir de uma ferramenta de geração de conteúdo para um sistema que aprende com o desempenho de cada perfil.

**Versão:** 1.0  
**Status:** Documento oficial do Modelo de Dados Completo
