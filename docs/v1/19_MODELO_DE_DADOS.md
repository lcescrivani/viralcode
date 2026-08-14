# 19 — MODELO DE DADOS

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define o modelo de dados inicial do ViralCode.

O objetivo é estabelecer:

- entidades;
- responsabilidades;
- relacionamentos;
- chaves;
- estados;
- campos principais;
- regras de integridade;
- separação entre dados internos e dados externos;
- estrutura suficiente para o MVP;
- preparação para crescimento futuro.

A persistência oficial do MVP será:

```text
MySQL
```

utilizando:

```text
SQLAlchemy
```

---

# 2. Princípio fundamental

O banco deverá representar o domínio do ViralCode.

Não devemos criar tabelas apenas porque determinada tela precisa de um campo.

A regra é:

```text
DOMÍNIO
  ↓
ENTIDADES
  ↓
RELACIONAMENTOS
  ↓
BANCO
```

---

# 3. Arquitetura de persistência

```text
FastAPI
   ↓
Serviços
   ↓
Repositórios
   ↓
SQLAlchemy
   ↓
MySQL
```

As rotas não deverão acessar o banco diretamente.

---

# 4. Visão geral das entidades

O MVP deverá considerar principalmente:

```text
Usuário
Perfil
Nicho
ContaSocial
Conteúdo
ConteúdoExterno
AnáliseConteúdo
Padrão
Insight
Planejamento
ItemPlanejamento
Publicação
MétricaPublicação
Aprendizado
EvidênciaAprendizado
Prompt
ExecuçãoIA
```

Nem todas precisam ser implementadas integralmente na primeira sprint.

---

# 5. Relacionamento principal

```text
Usuário
   │
   └──< Perfil
           │
           ├── Nicho
           │
           ├──< ContaSocial
           │
           ├──< Planejamento
           │
           ├──< Conteúdo
           │
           └──< Aprendizado
```

---

# 6. Fluxo de conteúdo

```text
Conteúdo externo
      ↓
Análise
      ↓
Padrões
      ↓
Insights
      ↓
Planejamento
      ↓
Conteúdo original
      ↓
Publicação
      ↓
Métricas
      ↓
Aprendizado
```

---

# 7. Usuário

Representa a pessoa que utiliza o ViralCode.

Tabela conceitual:

```text
usuarios
```

Campos principais:

```text
id
nome
email
senha_hash
ativo
criado_em
atualizado_em
```

---

# 8. Regras do usuário

O e-mail deverá ser único.

Nunca armazenar:

```text
senha em texto puro
```

Armazenar somente:

```text
senha_hash
```

---

# 9. Perfil

Representa uma identidade editorial.

Tabela:

```text
perfis
```

Campos principais:

```text
id
usuario_id
nome
descricao
nicho_id
publico
posicionamento
tom_de_voz
objetivo_principal
ativo
criado_em
atualizado_em
```

Relacionamento:

```text
usuario 1 ─── N perfis
```

---

# 10. Nicho

Representa o segmento editorial.

Tabela:

```text
nichos
```

Campos:

```text
id
nome
descricao
ativo
criado_em
atualizado_em
```

Exemplo:

```text
Casamento
Fitness
Finanças
Educação
Tecnologia
```

O sistema não deverá possuir código específico para um único nicho.

---

# 11. Conta social

Representa uma conta de rede social conectada ao ViralCode.

Tabela:

```text
contas_sociais
```

Campos principais:

```text
id
perfil_id
plataforma
identificador_externo
nome_exibicao
nome_usuario
status
token_criptografado
token_expira_em
dados_autenticacao
criado_em
atualizado_em
```

---

# 12. Segurança da conta social

Tokens e credenciais não deverão ser armazenados em texto puro quando houver alternativa segura.

Nunca registrar tokens em:

```text
logs
respostas da API
mensagens de erro
Git
```

---

# 13. Plataforma

No MVP:

```text
instagram
```

O banco deverá utilizar uma representação extensível para futuras plataformas.

Exemplo:

```text
instagram
tiktok
youtube
```

---

# 14. Status da conta social

Estados possíveis:

```text
CONECTADA
EXPIRADA
REVOGADA
ERRO
REAUTENTICACAO_NECESSARIA
INATIVA
```

---

# 15. Conteúdo

A entidade `conteudos` representa o conteúdo utilizado pelo ViralCode.

Ela poderá representar:

```text
conteúdo descoberto
```

ou:

```text
conteúdo criado pelo ViralCode
```

A origem deverá ser identificada.

---

# 16. Tabela de conteúdos

```text
conteudos
```

Campos principais:

```text
id
perfil_id
origem
tipo
titulo
descricao
legenda
texto
status
criado_em
atualizado_em
```

---

# 17. Origem do conteúdo

Exemplos:

```text
EXTERNO
GERADO_IA
MANUAL
DERIVADO
```

---

# 18. Tipo de conteúdo

Exemplos:

```text
REEL
POST
CARROSSEL
```

No MVP, priorizar:

```text
REEL
```

---

# 19. Conteúdo externo

Conteúdos encontrados em uma rede social deverão possuir dados externos separados ou identificados de maneira clara.

Tabela sugerida:

```text
conteudos_externos
```

Campos:

```text
id
conteudo_id
plataforma
identificador_externo
url
autor_nome
autor_usuario
data_publicacao
legenda_original
dados_brutos
criado_em
atualizado_em
```

---

# 20. Identificador externo

A combinação:

```text
plataforma
+
identificador_externo
```

deverá ser única para evitar duplicidade.

---

# 21. Dados brutos

Quando necessário, poderá existir:

```text
dados_brutos
```

para preservar a resposta original normalizada ou parte dela.

Esse campo deverá ser utilizado com cuidado.

Não armazenar indiscriminadamente respostas gigantes da plataforma.

---

# 22. Análise de conteúdo

Representa a análise feita pelo ViralCode sobre um conteúdo.

Tabela:

```text
analises_conteudo
```

Campos:

```text
id
conteudo_id
hook
tema
subtema
formato
estrutura
emocao
cta
angulo
analise_textual
versao_prompt
criado_em
```

---

# 23. Padrão

Representa um comportamento ou característica recorrente identificada.

Tabela:

```text
padroes
```

Campos:

```text
id
perfil_id
tipo
nome
descricao
status
criado_em
atualizado_em
```

---

# 24. Tipos de padrão

Exemplos:

```text
HOOK
TEMA
FORMATO
ESTRUTURA
EMOCAO
CTA
ANGULO
```

---

# 25. Relação conteúdo-padrão

Um conteúdo poderá apresentar vários padrões.

Um padrão poderá aparecer em vários conteúdos.

Relacionamento:

```text
conteudos N ─── N padroes
```

Tabela associativa:

```text
conteudo_padroes
```

Campos:

```text
conteudo_id
padrao_id
evidencia
criado_em
```

---

# 26. Insight

Representa uma interpretação derivada de padrões e dados.

Tabela:

```text
insights
```

Campos:

```text
id
perfil_id
tipo
titulo
descricao
confianca
status
criado_em
atualizado_em
```

---

# 27. Relação insight-padrão

Um insight poderá utilizar vários padrões.

Tabela:

```text
insight_padroes
```

Campos:

```text
insight_id
padrao_id
```

---

# 28. Planejamento

Representa o plano editorial.

Tabela:

```text
planejamentos
```

Campos:

```text
id
perfil_id
nome
periodo_inicio
periodo_fim
status
criado_em
atualizado_em
```

---

# 29. Item de planejamento

Representa uma ação editorial específica.

Tabela:

```text
itens_planejamento
```

Campos:

```text
id
planejamento_id
perfil_id
data_planejada
horario_planejado
tema
subtema
formato
objetivo
prioridade
briefing
status
conteudo_id
criado_em
atualizado_em
```

---

# 30. Status do planejamento

Exemplos:

```text
IDEIA
PLANEJADO
EM_CRIACAO
CRIADO
APROVADO
AGENDADO
PUBLICADO
ATRASADO
CANCELADO
```

---

# 31. Conteúdo criado

Quando um item do planejamento gerar um conteúdo:

```text
item_planejamento
        ↓
conteudo
```

O campo:

```text
conteudo_id
```

poderá representar essa relação.

---

# 32. Publicação

Representa a tentativa ou execução de publicação.

Tabela:

```text
publicacoes
```

Campos:

```text
id
conteudo_id
conta_social_id
status
data_planejada
data_publicacao
identificador_externo
url_publicacao
erro_codigo
erro_mensagem
tentativas
criado_em
atualizado_em
```

---

# 33. Status da publicação

```text
PENDENTE
VALIDANDO
PUBLICANDO
PUBLICADO
ERRO
CANCELADO
```

---

# 34. Regra de publicação

Uma publicação deverá estar associada a:

```text
conteudo
```

e:

```text
conta_social
```

---

# 35. Métricas

Representam medições obtidas sobre uma publicação.

Tabela:

```text
metricas_publicacao
```

Campos:

```text
id
publicacao_id
coletado_em
visualizacoes
curtidas
comentarios
compartilhamentos
salvamentos
alcance
impressoes
dados_adicionais
```

Nem todos os campos estarão disponíveis para todas as plataformas.

---

# 36. NULL versus zero

Regra importante:

```text
NULL
=
métrica não disponível ou não conhecida
```

```text
0
=
métrica conhecida e igual a zero
```

Nunca substituir automaticamente `NULL` por `0`.

---

# 37. Histórico de métricas

A tabela de métricas deverá permitir múltiplos registros para a mesma publicação.

Exemplo:

```text
publicação 10

10:00 → 100k
14:00 → 180k
18:00 → 310k
22:00 → 500k
```

---

# 38. Aprendizado

Representa conhecimento reutilizável.

Tabela:

```text
aprendizados
```

Campos:

```text
id
perfil_id
tipo
escopo
plataforma
nicho_id
tema
afirmacao
confianca
amostra
status
criado_em
atualizado_em
ultima_evidencia_em
```

---

# 39. Tipos de aprendizado

Exemplos:

```text
HOOK
FORMATO
TEMA
EMOCAO
ESTRUTURA
CTA
HORARIO
FREQUENCIA
ANGULO
```

---

# 40. Escopo do aprendizado

Exemplos:

```text
PERFIL
NICHO
PLATAFORMA
CONTEUDO
```

---

# 41. Evidência de aprendizado

Todo aprendizado importante deverá apontar para as evidências utilizadas.

Tabela:

```text
evidencias_aprendizado
```

Campos:

```text
id
aprendizado_id
conteudo_id
publicacao_id
metricas_publicacao_id
observacao
peso
criado_em
```

---

# 42. Regra de evidência

Não criar um aprendizado sem conseguir responder:

```text
De onde veio?
```

A evidência poderá ser:

```text
conteúdo
publicação
métrica
análise
```

---

# 43. Prompt

Representa uma instrução versionada utilizada pela IA.

Tabela:

```text
prompts
```

Campos:

```text
id
nome
versao
tipo
conteudo
ativo
criado_em
atualizado_em
```

---

# 44. Tipos de prompt

Exemplos:

```text
ANALISE_CONTEUDO
IDENTIFICACAO_PADRAO
GERACAO_REEL
GERACAO_LEGENDA
GERACAO_INSIGHT
```

---

# 45. Execução de IA

Representa uma chamada feita a um provedor de IA.

Tabela:

```text
execucoes_ia
```

Campos:

```text
id
prompt_id
perfil_id
provedor
modelo
entrada
saida
status
tokens_entrada
tokens_saida
custo_estimado
erro
criado_em
finalizado_em
```

---

# 46. Objetivo da execução de IA

Poderá identificar:

```text
ANALISE
CRIACAO
INSIGHT
PLANEJAMENTO
```

---

# 47. Relação entre IA e conteúdo

Uma execução de IA poderá gerar um conteúdo.

Poderá existir:

```text
execucao_ia.conteudo_id
```

ou uma tabela associativa quando houver necessidade de múltiplas relações.

---

# 48. Relação entre IA e análise

Da mesma forma, uma execução poderá gerar:

```text
analise_conteudo
```

O objetivo é manter rastreabilidade.

---

# 49. Rastreabilidade

O sistema deverá conseguir responder:

```text
Como este conteúdo foi criado?
```

Fluxo:

```text
Conteúdo
   ↓
Execução IA
   ↓
Prompt
   ↓
Modelo
```

E:

```text
Qual aprendizado influenciou?
```

Fluxo:

```text
Conteúdo
   ↓
Planejamento
   ↓
Aprendizado
   ↓
Evidências
```

---

# 50. Relação geral

```text
USUÁRIO
   ↓
PERFIL
   ↓
NICHO
   ↓
PLANEJAMENTO
   ↓
CONTEÚDO
   ↓
PUBLICAÇÃO
   ↓
MÉTRICAS
   ↓
APRENDIZADO
```

Paralelamente:

```text
CONTEÚDO EXTERNO
   ↓
ANÁLISE
   ↓
PADRÕES
   ↓
INSIGHTS
   ↓
PLANEJAMENTO
```

---

# 51. Integridade

Toda FK deverá apontar para uma entidade existente.

Exemplo:

```text
perfil.usuario_id
```

deve apontar para:

```text
usuarios.id
```

---

# 52. Exclusão

Não apagar dados históricos críticos em cascata sem decisão explícita.

Especialmente:

```text
publicações
métricas
aprendizados
evidências
execuções de IA
```

---

# 53. Soft delete

Para entidades que possam precisar ser preservadas, considerar:

```text
ativo
```

ou:

```text
excluido_em
```

Em vez de apagar fisicamente.

No MVP, utilizar apenas onde houver necessidade real.

---

# 54. Datas

Todos os registros importantes deverão possuir:

```text
criado_em
atualizado_em
```

Quando relevante:

```text
publicado_em
coletado_em
planejado_em
```

---

# 55. Fuso horário

O sistema deverá armazenar datas de forma consistente.

A arquitetura deverá separar:

```text
instante real
```

de:

```text
horário apresentado ao usuário
```

O perfil poderá possuir um fuso horário no futuro.

---

# 56. Índices

Índices deverão ser criados para campos frequentemente utilizados em:

```text
FK
busca
filtro
ordenação
unicidade
```

Exemplos:

```text
usuarios.email
conteudos_externos.identificador_externo
publicacoes.identificador_externo
metricas_publicacao.publicacao_id
```

---

# 57. Unicidade

Exemplos de restrições:

```text
usuarios.email UNIQUE
```

e:

```text
contas_sociais
(perfil_id, plataforma, identificador_externo)
```

conforme a regra definitiva de negócio.

---

# 58. Conteúdo externo duplicado

Nunca armazenar duas vezes o mesmo conteúdo externo apenas porque foi encontrado por fontes diferentes.

Chave lógica:

```text
plataforma
+
identificador_externo
```

---

# 59. Publicação duplicada

O sistema deverá evitar criar duas publicações simultâneas para a mesma ação sem necessidade.

A regra de idempotência será definida no Motor de Publicação.

---

# 60. JSON

Campos JSON poderão ser utilizados para dados flexíveis, como:

```text
dados_brutos
dados_adicionais
```

Mas não utilizar JSON para esconder relacionamentos importantes que deveriam ser tabelas.

---

# 61. Regra de normalização

Informações importantes para consulta deverão possuir campos próprios.

Evitar:

```text
guardar tudo em JSON
```

quando o dado for utilizado frequentemente em:

```text
filtro
ranking
relatório
relacionamento
```

---

# 62. Migrações

Alterações do banco deverão ser controladas por migrações.

O projeto deverá utilizar uma ferramenta apropriada de migração compatível com SQLAlchemy.

Exemplo esperado:

```text
migração_001
migração_002
migração_003
```

---

# 63. Ambiente

O banco deverá possuir configurações separadas para:

```text
desenvolvimento
teste
produção
```

Não utilizar banco de produção para testes.

---

# 64. Testes de banco

Os testes deverão verificar:

```text
FK
UNIQUE
status
criação
atualização
relacionamentos
duplicidade
```

---

# 65. Modelo mínimo do MVP

As entidades prioritárias para o MVP são:

```text
usuarios
perfis
nichos
contas_sociais
conteudos
conteudos_externos
analises_conteudo
padroes
insights
itens_planejamento
publicacoes
metricas_publicacao
aprendizados
evidencias_aprendizado
prompts
execucoes_ia
```

---

# 66. O que pode ficar simplificado

No primeiro MVP, algumas entidades poderão ser simplificadas.

Por exemplo:

```text
Planejamento
```

poderá começar diretamente em:

```text
itens_planejamento
```

sem uma entidade de campanha completa.

---

# 67. O que não deve ser antecipado

Não criar inicialmente tabelas para:

```text
campanhas complexas
experimentos avançados
A/B testing
equipes
organizações
faturamento
assinaturas
múltiplas redes
```

a menos que uma necessidade concreta apareça.

---

# 68. Evolução futura

O modelo deverá permitir adicionar:

```text
Organização
Equipe
Membro
Campanha
Experimento
Assinatura
Plano
Pagamento
TikTok
YouTube
```

sem reescrever o núcleo.

---

# 69. Regra de nomenclatura

Como o projeto utiliza português, os nomes de tabelas e campos deverão seguir português do Brasil.

Exemplo:

```text
usuarios
perfis
conteudos
publicacoes
metricas_publicacao
```

Evitar misturar:

```text
usuario
user
usuario_profile
```

---

# 70. Regra para APIs

Os nomes externos da API também deverão utilizar a convenção definida pelo projeto em português.

Exemplo:

```text
/perfis
/conteudos
/publicacoes
/aprendizados
```

---

# 71. Regra para código

Classes, serviços e repositórios deverão seguir a mesma linguagem conceitual.

Exemplo:

```python
class ServicoConteudo:
    ...

class RepositorioConteudo:
    ...
```

---

# 72. Regra para agentes de IA

Antes de alterar o banco:

1. ler este documento;
2. verificar as entidades existentes;
3. verificar relacionamentos;
4. verificar se a informação já possui entidade própria;
5. evitar duplicação;
6. criar migração;
7. atualizar testes;
8. atualizar este documento se a arquitetura mudar.

---

# 73. Diagrama conceitual

```text
                         USUÁRIO
                            │
                            │ 1:N
                            ▼
                          PERFIL
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
           NICHO       CONTA SOCIAL    PLANEJAMENTO
                            │              │
                            │              ▼
                            │       ITEM PLANEJAMENTO
                            │              │
                            │              ▼
                            └──────────► CONTEÚDO
                                           │
                         ┌─────────────────┼─────────────────┐
                         ▼                 ▼                 ▼
                CONTEÚDO EXTERNO       ANÁLISE           PADRÕES
                         │                 │                 │
                         │                 └────────┬────────┘
                         │                          ▼
                         │                       INSIGHTS
                         │
                         ▼
                    PUBLICAÇÃO
                         │
                         ▼
                      MÉTRICAS
                         │
                         ▼
                    APRENDIZADO
                         │
                         ▼
                  EVIDÊNCIAS
```

---

# 74. IA

```text
PROMPT
   ↓
EXECUÇÃO IA
   ↓
ANÁLISE / CONTEÚDO / INSIGHT
```

Esse histórico deverá permitir rastrear como a IA foi utilizada.

---

# 75. Modelo de dados e arquitetura

O banco não deverá conter regras de negócio complexas.

A regra deverá ficar nos serviços:

```text
Banco
→ armazena

Repositório
→ acessa

Serviço
→ decide

API
→ expõe
```

---

# 76. Critério de sucesso

O Modelo de Dados será considerado adequado quando permitir executar o fluxo principal:

```text
Usuário
 ↓
Perfil
 ↓
Conta Instagram
 ↓
Conteúdo externo
 ↓
Análise
 ↓
Padrão / Insight
 ↓
Planejamento
 ↓
Conteúdo original
 ↓
Publicação
 ↓
Métricas
 ↓
Aprendizado
```

sem criar duplicação desnecessária ou acoplamento entre módulos.

---

# 77. Regra final

> **O banco deve ser simples o suficiente para o MVP, mas estruturado o suficiente para preservar o histórico que dará inteligência ao ViralCode.**

O valor futuro do produto estará justamente na relação entre:

```text
CONTEÚDO
+
CONTEXTO
+
PUBLICAÇÃO
+
MÉTRICAS
+
APRENDIZADO
```

Por isso, esses relacionamentos devem ser preservados desde o início.

**Versão:** 1.0  
**Status:** Documento oficial do Modelo de Dados
