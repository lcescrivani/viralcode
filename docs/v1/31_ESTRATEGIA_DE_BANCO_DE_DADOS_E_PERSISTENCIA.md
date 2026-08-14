# 31 — ESTRATÉGIA DE BANCO DE DADOS E PERSISTÊNCIA

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define como o ViralCode utilizará o MySQL para armazenar os dados do produto.

O objetivo é estabelecer regras para:

```text
modelos
relacionamentos
persistência
transações
migrações
integridade
histórico
isolamento
```

---

# 2. Banco oficial

O banco de dados do projeto será:

```text
MySQL
```

A aplicação utilizará:

```text
SQLAlchemy
```

como camada de acesso ao banco.

---

# 3. Princípio fundamental

O banco deverá representar o estado do negócio.

```text
BANCO
→ estado persistente

LOG
→ diagnóstico técnico

CACHE
→ dado temporário

ARQUIVO
→ mídia/documento quando aplicável
```

Não utilizar logs ou memória da aplicação como fonte de verdade do negócio.

---

# 4. Arquitetura

```text
FastAPI
   ↓
Serviço
   ↓
Repositório
   ↓
SQLAlchemy
   ↓
MySQL
```

O serviço não deverá construir SQL diretamente.

---

# 5. Responsabilidade do modelo

Os modelos deverão representar entidades persistentes.

Exemplos:

```text
Usuario
Perfil
ContaSocial
Conteudo
Analise
Insight
Aprendizado
Planejamento
Publicacao
Metrica
```

Os nomes definitivos deverão seguir o documento oficial de modelo de dados.

---

# 6. Responsabilidade do repositório

O repositório deverá concentrar operações de persistência.

Exemplos:

```text
buscar
criar
atualizar
listar
contar
```

A regra de negócio não deverá ficar escondida dentro do repositório.

---

# 7. Regra de negócio

Exemplo:

```text
"somente conteúdo aprovado pode ser publicado"
```

é regra de negócio.

Portanto deverá estar no:

```text
Serviço
```

e não somente no:

```text
Repositório
```

---

# 8. Integridade

O banco deverá proteger integridade quando apropriado por meio de:

```text
chaves primárias
chaves estrangeiras
índices
restrições
unicidade
NOT NULL
```

---

# 9. Identificadores

Cada entidade persistente deverá possuir identificador estável.

Preferir uma estratégia consistente em todo o projeto.

A decisão definitiva entre:

```text
inteiro
UUID
```

deverá seguir o modelo de dados oficial.

---

# 10. Identificador interno x externo

Entidades integradas com redes sociais poderão possuir:

```text
id_interno
id_externo
```

Exemplo:

```text
id interno ViralCode
+
id externo Instagram
```

Não utilizar o identificador externo como única referência interna sem justificativa.

---

# 11. Identificadores externos

Quando uma plataforma fornecer identificador estável, armazená-lo quando necessário para:

```text
deduplicação
consulta
sincronização
reconciliação
```

---

# 12. Multiusuário

O banco deverá suportar isolamento por usuário.

Conceitualmente:

```text
Usuario
   ├── Perfil A
   │     ├── Conteúdos
   │     └── Conta social
   │
   └── Perfil B
         ├── Conteúdos
         └── Conta social
```

---

# 13. Perfil

O perfil representa uma unidade de contexto do produto.

Poderá possuir:

```text
nicho
subnicho
público
posicionamento
tom de voz
objetivos
```

---

# 14. Conta social

A conta social deverá estar associada ao perfil ou à estrutura definida no modelo de dados.

Deverá permitir identificar:

```text
usuário
perfil
plataforma
identificador externo
estado
```

---

# 15. Credenciais

Credenciais técnicas não deverão ser tratadas como dados comuns.

Quando forem armazenadas:

```text
acesso restrito
proteção adequada
nunca expostas em consultas da API
```

---

# 16. Conteúdo externo

Conteúdos encontrados na rede social deverão ser persistidos quando fizer sentido para:

```text
análise
comparação
histórico
aprendizado
```

---

# 17. Conteúdo externo x conteúdo próprio

Distinguir claramente:

```text
CONTEÚDO EXTERNO
→ encontrado na rede

CONTEÚDO PRÓPRIO
→ criado pelo usuário/ViralCode
```

Não misturar os dois conceitos.

---

# 18. Análise

Uma análise deverá estar vinculada ao conteúdo analisado.

Conceitualmente:

```text
Conteudo
   ↓
Analise
```

Uma nova versão de análise poderá ser registrada quando necessário.

---

# 19. Versionamento de análise

Quando o sistema evoluir seus prompts ou modelos, poderá ser necessário preservar:

```text
versão do prompt
modelo IA
data
resultado
```

Isso permite compreender como uma análise foi produzida.

---

# 20. Execução de IA

Quando necessário, registrar uma execução separada:

```text
ExecucaoIA
```

contendo informações técnicas como:

```text
tipo
modelo
versão
status
tempo
tokens
custo estimado
```

A estrutura definitiva deverá seguir o modelo de dados.

---

# 21. Insight

Insights deverão poder ser associados às evidências que os sustentam.

Conceitualmente:

```text
Insight
   ↓
Evidências
   ↓
Conteúdos / métricas
```

---

# 22. Aprendizado

O aprendizado deverá possuir contexto suficiente para saber:

```text
o que foi aprendido
de qual perfil
com base em quais evidências
quando foi criado
qual sua confiança
```

---

# 23. Evidências

Não guardar somente:

```text
"hooks curtos funcionam melhor"
```

quando o sistema puder guardar também:

```text
quais conteúdos
quais métricas
qual período
```

deram origem à conclusão.

---

# 24. Publicação

Uma publicação deverá relacionar:

```text
conteúdo
conta social
plataforma
estado
identificador externo quando houver
```

---

# 25. Estado da publicação

O modelo deverá permitir diferenciar estados como:

```text
PENDENTE
ENVIANDO
PUBLICADA
ERRO
CANCELADA
```

Os valores definitivos deverão seguir o documento de domínio.

---

# 26. Métricas

Métricas deverão ser persistidas como medições associadas a uma publicação ou conteúdo externo.

Exemplo:

```text
Publicação
   ↓
Métrica
   ├── data/hora
   ├── visualizações
   ├── curtidas
   ├── comentários
   └── outras disponíveis
```

---

# 27. Histórico

Evitar sobrescrever métricas históricas quando o objetivo for acompanhar evolução.

Exemplo:

```text
10:00 → 10.000 visualizações
14:00 → 18.000 visualizações
18:00 → 27.000 visualizações
```

---

# 28. NULL x zero

Regra importante:

```text
NULL
→ informação não disponível

0
→ informação disponível e valor igual a zero
```

Nunca transformar automaticamente uma métrica ausente em zero.

---

# 29. Datas

As entidades deverão possuir datas consistentes.

Quando necessário, diferenciar:

```text
criado_em
atualizado_em
publicado_em
coletado_em
```

---

# 30. Fuso horário

O sistema deverá definir uma estratégia consistente para armazenar datas e horários.

A recomendação arquitetural é:

```text
persistir timestamps de forma consistente
+
converter para o fuso do usuário na interface
```

A implementação definitiva deverá seguir a configuração oficial do projeto.

---

# 31. Soft delete

O uso de exclusão lógica não deverá ser aplicado automaticamente a todas as entidades.

Deverá ser decidido conforme o domínio.

Exemplo:

```text
usuário
```

poderá possuir regras diferentes de:

```text
conteúdo temporário
```

---

# 32. Exclusão física

Quando uma entidade precisar ser apagada definitivamente:

```text
avaliar dependências
avaliar auditoria
avaliar legislação
avaliar recuperação
```

antes da exclusão.

---

# 33. Cascata

Não utilizar:

```text
CASCADE
```

indiscriminadamente.

Cada relacionamento deverá avaliar o impacto de excluir um registro pai.

---

# 34. Unicidade

Utilizar restrições de unicidade quando uma combinação não puder se repetir.

Exemplos possíveis:

```text
usuário + e-mail
plataforma + identificador externo
```

Os campos definitivos serão definidos no modelo.

---

# 35. Deduplicação

Conteúdos externos deverão possuir estratégia para evitar duplicidade.

Exemplo:

```text
plataforma
+
id_externo
```

pode formar uma chave lógica de identificação.

---

# 36. Índices

Criar índices para consultas frequentes.

Prioridade para campos utilizados em:

```text
filtros
relacionamentos
ordenação
busca
deduplicação
```

---

# 37. Não indexar tudo

Índices possuem custo.

Cada índice deverá existir porque existe uma necessidade real de consulta.

---

# 38. Consultas

Evitar:

```text
SELECT *
```

quando somente alguns campos forem necessários em consultas críticas.

---

# 39. Paginação

Listagens potencialmente grandes deverão possuir paginação.

Exemplos:

```text
conteúdos
publicações
métricas
análises
```

---

# 40. Paginação futura

O modelo poderá evoluir de:

```text
offset
```

para:

```text
cursor
```

quando o volume justificar.

No MVP, paginação simples poderá ser suficiente.

---

# 41. Ordenação

A ordenação deverá ser explícita.

Não depender da ordem "natural" do banco.

---

# 42. Filtros

Filtros deverão ser aplicados no banco quando isso for mais eficiente.

Evitar carregar milhares de registros para depois filtrar em Python sem necessidade.

---

# 43. Transações

Operações que alteram múltiplas entidades deverão avaliar o uso de transação.

Exemplo:

```text
criar publicação
+
atualizar conteúdo
```

---

# 44. Rollback

Se uma transação falhar:

```text
ROLLBACK
```

deverá impedir estado parcialmente persistido.

---

# 45. Integrações externas

Não assumir que uma chamada externa pode participar da mesma transação do MySQL.

Exemplo:

```text
MySQL
   ↓
Instagram
```

Se o Instagram concluir e o banco falhar, poderá existir inconsistência.

A aplicação deverá prever:

```text
estado intermediário
reconciliação
idempotência
```

quando necessário.

---

# 46. Publicação externa

Exemplo:

```text
Criar tentativa
 ↓
Enviar Instagram
 ↓
Instagram confirma
 ↓
Salvar identificador
```

Se o passo final falhar:

```text
não assumir automaticamente que não publicou
```

---

# 47. Reconciliação

Para operações externas importantes, poderá existir uma rotina para verificar:

```text
estado local
vs.
estado externo
```

---

# 48. Concorrência

O sistema deverá considerar operações simultâneas.

Exemplo:

```text
duas requisições
 ↓
mesmo conteúdo
 ↓
mesma publicação
```

A proteção deverá evitar duplicidade.

---

# 49. Locks

Não utilizar locks pessimistas indiscriminadamente.

Usar somente quando a regra realmente exigir.

---

# 50. Integridade referencial

Relacionamentos deverão ser protegidos por:

```text
foreign keys
```

quando apropriado.

---

# 51. Migrações

Toda alteração estrutural deverá ser feita através de migração.

Fluxo:

```text
modelo
 ↓
migração
 ↓
banco
```

---

# 52. Migração reversível

Sempre que possível, alterações deverão possuir caminho seguro de rollback.

Alterações destrutivas exigem atenção especial.

---

# 53. Migrações em produção

Antes de migração importante:

```text
backup
```

deverá ser considerado obrigatório.

---

# 54. Compatibilidade

Quando uma mudança de banco exigir mudança de aplicação, avaliar a ordem:

```text
banco primeiro
ou
aplicação primeiro
```

para evitar indisponibilidade ou incompatibilidade.

---

# 55. Seed

O projeto poderá possuir dados iniciais para desenvolvimento.

Exemplo:

```text
nichos
configurações
dados de teste
```

Não utilizar dados fictícios de desenvolvimento em produção sem intenção explícita.

---

# 56. Dados de teste

Dados de teste deverão ser identificáveis.

Não utilizar dados reais de usuários em testes sem autorização e proteção apropriadas.

---

# 57. Backup

O banco deverá possuir:

```text
backup automático
retenção
teste de restauração
```

conforme definido no documento de infraestrutura.

---

# 58. Recuperação

O objetivo do backup é permitir:

```text
perda
↓
restauração
↓
continuidade
```

---

# 59. Performance

O banco deverá ser monitorado quando houver volume suficiente.

Observar:

```text
consultas lentas
CPU
RAM
conexões
tamanho
índices
```

---

# 60. N+1

A aplicação deverá evitar consultas repetitivas desnecessárias.

Exemplo problemático:

```text
1 consulta para conteúdos
+
1 consulta por conteúdo
```

Quando uma estratégia de carregamento adequado resolver o problema.

---

# 61. Dados derivados

Não armazenar como dado principal algo que pode ser calculado facilmente, a menos que exista motivo de:

```text
performance
histórico
auditoria
```

---

# 62. Cache

Cache não deverá substituir o banco.

Exemplo:

```text
MySQL
→ fonte de verdade

Cache
→ aceleração
```

---

# 63. Redis

Redis não é requisito do MVP.

Poderá ser adicionado futuramente para:

```text
cache
fila
locks
```

se houver necessidade.

---

# 64. Arquivos

Mídias grandes não deverão ser armazenadas no MySQL como estratégia padrão.

Preferir armazenamento de arquivos separado quando necessário.

---

# 65. JSON no banco

Campos JSON poderão ser utilizados quando fizer sentido para dados:

```text
flexíveis
externos
metadados
configurações
```

Mas não utilizar JSON para esconder um modelo relacional mal definido.

---

# 66. Dados externos

A resposta bruta de uma plataforma poderá ser armazenada somente quando existir justificativa.

Não armazenar indiscriminadamente respostas gigantes.

---

# 67. Normalização

O banco deverá normalizar dados importantes.

Entretanto, pequenas desnormalizações poderão ser utilizadas quando houver benefício claro de:

```text
consulta
performance
histórico
```

---

# 68. Regra de domínio

O modelo de banco não deverá determinar sozinho o comportamento do produto.

A regra deverá continuar no domínio/serviço.

---

# 69. Repositórios

O repositório não deverá retornar detalhes técnicos desnecessários para o domínio.

Preferir objetos/modelos coerentes com a aplicação.

---

# 70. Sessão SQLAlchemy

A gestão da sessão do banco deverá ser centralizada.

Evitar criar conexões manualmente espalhadas pelo código.

---

# 71. Pool de conexões

O SQLAlchemy poderá utilizar pool de conexões.

A configuração deverá considerar:

```text
RAM da VPS
número de requisições
limite do MySQL
```

---

# 72. Timeouts

Operações de banco deverão possuir configuração adequada para não permanecerem indefinidamente bloqueadas.

---

# 73. Erros

Erros do banco deverão ser tratados no serviço/aplicação de forma apropriada.

Não retornar detalhes internos do MySQL ao usuário.

---

# 74. Integridade de dados

Se uma operação exigir vários registros consistentes:

```text
usar transação
```

quando apropriado.

---

# 75. Regra de propriedade

Consultas de recursos privados deverão considerar o usuário.

Exemplo conceitual:

```text
buscar conteúdo
WHERE id = ?
AND usuario_id = ?
```

ou equivalente através dos relacionamentos.

---

# 76. Segurança

Não permitir que o usuário manipule diretamente:

```text
usuario_id
```

para obter dados de outra pessoa.

O usuário autenticado deverá ser a fonte da identidade.

---

# 77. Auditoria

Alterações importantes poderão possuir:

```text
quem
quando
o que
```

quando necessário.

---

# 78. Histórico

Históricos relevantes deverão ser preservados quando fizerem parte do produto.

Exemplos:

```text
métricas
execuções de IA
publicações
aprendizados
```

---

# 79. Crescimento

A estrutura deverá permitir evoluir de:

```text
1 usuário
```

para:

```text
milhares de usuários
```

sem precisar reescrever todo o modelo.

Mas não otimizar prematuramente para milhões de usuários.

---

# 80. Regra para agentes de IA

Antes de alterar banco:

1. ler o modelo de dados;
2. localizar relacionamentos;
3. verificar impacto;
4. criar migração;
5. avaliar índices;
6. avaliar integridade;
7. criar/atualizar testes;
8. atualizar documentação.

---

# 81. Regra contra alteração manual

Não alterar estrutura de produção diretamente por comandos manuais sem registrar a alteração em migração.

---

# 82. Regra contra apagar coluna

Nunca remover uma coluna importante sem avaliar:

```text
dados existentes
backup
código
migração
rollback
```

---

# 83. Regra contra duplicidade

Antes de criar uma nova entidade ou relacionamento, verificar se a informação já existe em outro modelo.

Evitar armazenar:

```text
mesma informação
em três lugares
```

sem justificativa.

---

# 84. Critério de sucesso

A persistência estará adequada quando:

```text
dados possuem dono
+
relacionamentos são claros
+
integridade é protegida
+
migrações são controladas
+
consultas são previsíveis
+
histórico importante é preservado
```

---

# 85. Arquitetura resumida

```text
                    FASTAPI
                       │
                    SERVIÇO
                       │
                 REPOSITÓRIO
                       │
                   SQLAlchemy
                       │
                  ┌────┴────┐
                  │  MySQL  │
                  └────┬────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       USUÁRIOS     CONTEÚDO     MÉTRICAS
          │            │            │
          ▼            ▼            ▼
       PERFIS       ANÁLISES     APRENDIZADOS
                       │
                       ▼
                   PUBLICAÇÕES
```

---

# 86. Regra final

> **O banco do ViralCode deve ser simples, consistente e preparado para preservar a história que alimentará a inteligência do produto.**

O MySQL não será apenas armazenamento.

Ele será a base histórica que permitirá ao ViralCode saber:

```text
o que foi descoberto
o que foi analisado
o que foi criado
o que foi publicado
o que aconteceu
o que funcionou
o que foi aprendido
```

Esse histórico será fundamental para o ciclo:

```text
DADOS
 ↓
INTELIGÊNCIA
 ↓
CONTEÚDO
 ↓
DESEMPENHO
 ↓
APRENDIZADO
```

**Versão:** 1.0  
**Status:** Documento oficial da Estratégia de Banco de Dados e Persistência
