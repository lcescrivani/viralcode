# 29 — FLUXOS PRINCIPAIS DO SISTEMA

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento descreve os principais fluxos funcionais do ViralCode de ponta a ponta.

Enquanto os documentos anteriores definem:

```text
arquitetura
dados
API
módulos
motores
infraestrutura
```

este documento mostra:

```text
COMO O SISTEMA FUNCIONA
```

na prática.

---

# 2. Princípio fundamental

Cada fluxo deverá possuir uma responsabilidade clara.

O sistema deverá evitar:

```text
rota gigante
+
regra espalhada
+
integração direta
+
persistência misturada
```

Preferir:

```text
ROTA
 ↓
SERVIÇO
 ↓
DOMÍNIO
 ↓
REPOSITÓRIO / CONECTOR
 ↓
RESULTADO
```

---

# 3. Fluxo macro do ViralCode

O ciclo principal será:

```text
USUÁRIO
   ↓
PERFIL
   ↓
CONECTA INSTAGRAM
   ↓
DESCOBRE CONTEÚDOS
   ↓
SALVA CONTEÚDOS
   ↓
ANALISA
   ↓
EXTRAI PADRÕES
   ↓
GERA INSIGHTS
   ↓
CRIA NOVO CONTEÚDO
   ↓
USUÁRIO APROVA
   ↓
PLANEJA
   ↓
PUBLICA
   ↓
COLETA DESEMPENHO
   ↓
APRENDE
   ↓
MELHORA PRÓXIMAS CRIAÇÕES
```

---

# 4. Fluxo 01 — Cadastro

```text
Usuário
 ↓
Tela de cadastro
 ↓
POST /api/v1/usuarios
 ↓
Esquema
 ↓
Serviço de autenticação
 ↓
Validar dados
 ↓
Verificar e-mail
 ↓
Gerar hash da senha
 ↓
Repositório
 ↓
MySQL
 ↓
Usuário criado
```

---

# 5. Fluxo 02 — Login

```text
Usuário
 ↓
E-mail + senha
 ↓
POST /api/v1/autenticacao/login
 ↓
Serviço de autenticação
 ↓
Buscar usuário
 ↓
Validar senha
 ↓
Gerar token
 ↓
Resposta
```

---

# 6. Fluxo 03 — Requisição autenticada

Toda requisição protegida deverá seguir:

```text
Frontend
 ↓
Bearer Token
 ↓
FastAPI
 ↓
Validar token
 ↓
Identificar usuario_id
 ↓
Rota
 ↓
Serviço
```

A partir desse ponto, o serviço deverá validar a propriedade do recurso.

---

# 7. Fluxo 04 — Criar perfil

```text
Frontend
 ↓
POST /api/v1/perfis
 ↓
Autenticação
 ↓
Serviço de perfil
 ↓
Validar dados
 ↓
Associar ao usuário
 ↓
RepositorioPerfil
 ↓
MySQL
 ↓
Perfil criado
```

---

# 8. Fluxo 05 — Editar perfil

```text
Frontend
 ↓
PUT /api/v1/perfis/{id}
 ↓
Autenticação
 ↓
Validar propriedade
 ↓
Serviço de perfil
 ↓
Atualizar
 ↓
MySQL
```

Não confiar apenas no `perfil_id` enviado pelo frontend.

---

# 9. Fluxo 06 — Conectar Instagram

A conexão da conta social deverá ser separada do login do ViralCode.

```text
Usuário autenticado
 ↓
Conectar Instagram
 ↓
Fluxo oficial de autorização
 ↓
Instagram
 ↓
Autorização
 ↓
Callback
 ↓
Backend
 ↓
Validar retorno
 ↓
Obter credenciais necessárias
 ↓
Proteger credencial
 ↓
Salvar conta social
 ↓
Conta conectada
```

---

# 10. Regra de conexão

O sistema deverá saber:

```text
qual usuário
qual perfil
qual conta social
qual plataforma
qual estado da conexão
```

---

# 11. Estado da conta social

Exemplo:

```text
CONECTANDO
CONECTADA
REAUTENTICACAO_NECESSARIA
DESCONECTADA
ERRO
```

Os estados definitivos deverão ser compatíveis com o modelo de dados.

---

# 12. Fluxo 07 — Verificar conta conectada

```text
Frontend
 ↓
GET /api/v1/contas-sociais
 ↓
Autenticação
 ↓
Serviço
 ↓
RepositorioContaSocial
 ↓
MySQL
 ↓
Contas do usuário
```

---

# 13. Fluxo 08 — Desconectar Instagram

```text
Usuário
 ↓
Desconectar
 ↓
API
 ↓
Validar propriedade
 ↓
Serviço
 ↓
Revogar/invalidar credencial quando aplicável
 ↓
Atualizar conta social
 ↓
MySQL
```

---

# 14. Fluxo 09 — Iniciar descoberta

Entrada conceitual:

```text
nicho
tema
palavra-chave
conta
hashtag
filtros
```

Fluxo:

```text
Frontend
 ↓
POST /api/v1/descobertas
 ↓
Serviço de descoberta
 ↓
Validar perfil
 ↓
Validar conta social
 ↓
Montar consulta
 ↓
Conector Instagram
 ↓
Instagram
```

---

# 15. Fluxo 10 — Receber descoberta

```text
Instagram
 ↓
Conector
 ↓
Normalização
 ↓
Validação
 ↓
Deduplicação
 ↓
Ranking
 ↓
RepositorioConteudo
 ↓
MySQL
 ↓
Resposta
```

---

# 16. Regra de normalização

Dados externos deverão ser convertidos para o modelo interno do ViralCode.

Exemplo:

```text
Instagram
   ↓
dados específicos da plataforma
   ↓
ConteudoExterno
```

O restante do sistema não deverá depender diretamente do formato bruto da plataforma.

---

# 17. Regra de deduplicação

Se o mesmo conteúdo aparecer por diferentes critérios:

```text
hashtag
+
conta
+
tema
```

o sistema deverá evitar criar múltiplos registros do mesmo conteúdo externo quando for possível identificá-lo.

---

# 18. Regra de métricas ausentes

Se a plataforma não fornecer uma métrica:

```text
NULL
```

não utilizar:

```text
0
```

como substituição automática.

---

# 19. Fluxo 11 — Selecionar conteúdo para análise

```text
Usuário
 ↓
Seleciona conteúdo
 ↓
POST /api/v1/conteudos/{id}/analisar
 ↓
Validar propriedade
 ↓
Serviço de análise
```

---

# 20. Fluxo 12 — Analisar conteúdo

```text
Conteúdo
 ↓
Carregar dados
 ↓
Montar contexto
 ↓
Selecionar prompt
 ↓
Selecionar versão
 ↓
Provedor de IA
 ↓
Resposta
 ↓
Validar estrutura
 ↓
Salvar análise
 ↓
Resultado
```

---

# 21. Falha na análise

Se a IA falhar:

```text
erro
 ↓
registrar execução
 ↓
preservar conteúdo
 ↓
retornar erro controlado
```

O conteúdo original não deverá ser perdido.

---

# 22. Fluxo 13 — Analisar vários conteúdos

Quando o usuário selecionar vários conteúdos:

```text
Lista
 ↓
Validar itens
 ↓
Processar
 ↓
Salvar análises
 ↓
Consolidar resultados
```

A implementação poderá ser síncrona no MVP se o volume for pequeno.

---

# 23. Fluxo futuro de processamento assíncrono

Quando o volume crescer:

```text
API
 ↓
Fila
 ↓
Worker
 ↓
IA
 ↓
Banco
```

Não é obrigatório no MVP.

---

# 24. Fluxo 14 — Extrair padrões

Entrada:

```text
análises
```

Fluxo:

```text
Análises
 ↓
Serviço de insights
 ↓
Agrupar características
 ↓
Comparar desempenho
 ↓
Identificar recorrências
 ↓
Gerar padrão
 ↓
Salvar
```

---

# 25. Fluxo 15 — Gerar insight

```text
Padrões
+
métricas
+
contexto do perfil
 ↓
Serviço de insights
 ↓
IA / regras
 ↓
Insight
 ↓
Validar
 ↓
Salvar evidências
```

---

# 26. Regra de evidência

Um insight relevante deverá ser associado às informações que justificaram sua criação.

Exemplo:

```text
Insight
 ↓
Conteúdo 10
Conteúdo 18
Conteúdo 24
```

---

# 27. Fluxo 16 — Gerar ideia

Entrada:

```text
perfil
nicho
objetivo
padrões
insights
aprendizados
```

Fluxo:

```text
Frontend
 ↓
POST /api/v1/conteudos/gerar
 ↓
Serviço de criação
 ↓
Montar contexto
 ↓
Provedor IA
 ↓
Validar saída
 ↓
Salvar conteúdo
 ↓
Retornar
```

---

# 28. Fluxo 17 — Gerar roteiro

```text
Conteúdo
 ↓
Contexto
 ↓
Prompt de roteiro
 ↓
IA
 ↓
Validação
 ↓
Roteiro
 ↓
Salvar
```

---

# 29. Fluxo 18 — Gerar legenda

```text
Roteiro
+
perfil
+
tom
+
objetivo
 ↓
IA
 ↓
Legenda
```

---

# 30. Fluxo 19 — Gerar CTA

```text
Objetivo
+
conteúdo
+
plataforma
 ↓
IA
 ↓
CTA
```

---

# 31. Fluxo 20 — Conteúdo completo

O sistema poderá combinar:

```text
IDEIA
+
HOOK
+
ROTEIRO
+
LEGENDA
+
CTA
```

em uma entidade de conteúdo.

---

# 32. Fluxo 21 — Editar conteúdo

```text
Usuário
 ↓
Editar
 ↓
API
 ↓
Validar propriedade
 ↓
Serviço
 ↓
Atualizar
 ↓
MySQL
```

A edição manual do usuário deverá ser preservada.

---

# 33. Fluxo 22 — Aprovar conteúdo

```text
Usuário
 ↓
Aprovar
 ↓
API
 ↓
Validar propriedade
 ↓
Serviço
 ↓
Verificar estado
 ↓
Atualizar status
 ↓
MySQL
```

---

# 34. Estados do conteúdo

Conceitualmente:

```text
RASCUNHO
GERADO
EM_REVISAO
APROVADO
PLANEJADO
PUBLICADO
ARQUIVADO
```

Os estados definitivos deverão ser alinhados ao modelo de dados.

---

# 35. Regra de publicação

Somente conteúdo apto para publicação poderá avançar.

No MVP:

```text
APROVADO
```

é o requisito mínimo.

---

# 36. Fluxo 23 — Planejar conteúdo

```text
Conteúdo aprovado
 ↓
Escolher data
 ↓
Escolher horário
 ↓
Selecionar conta
 ↓
Salvar planejamento
```

---

# 37. Fluxo 24 — Publicação

```text
Conteúdo aprovado
        ↓
Conta conectada
        ↓
Data/hora
        ↓
Serviço de publicação
        ↓
Validação
        ↓
Conector Instagram
        ↓
Instagram
        ↓
Resposta
        ↓
Atualizar publicação
```

---

# 38. Regra de idempotência

Uma mesma publicação não deverá ser enviada duas vezes por uma repetição acidental da requisição.

O serviço deverá possuir uma estratégia para identificar a operação.

---

# 39. Falha na publicação

Se a publicação falhar:

```text
conteúdo permanece preservado
publicação fica em estado de erro
erro é registrado
usuário recebe informação
```

Não apagar o conteúdo.

---

# 40. Fluxo 25 — Publicação manual

Caso uma capacidade necessária não esteja disponível pela integração oficial:

```text
Conteúdo aprovado
 ↓
ViralCode disponibiliza conteúdo
 ↓
Usuário publica
 ↓
Usuário registra/integra resultado quando possível
```

O MVP não deverá depender de uma única capacidade de publicação para validar a proposta de valor.

---

# 41. Fluxo 26 — Coletar desempenho

```text
Publicação
 ↓
Conta Instagram
 ↓
Conector
 ↓
Consultar métricas disponíveis
 ↓
Normalizar
 ↓
Salvar histórico
```

---

# 42. Fluxo 27 — Histórico de métricas

Uma publicação poderá possuir várias medições:

```text
Medição 1
Medição 2
Medição 3
...
```

Isso permitirá acompanhar evolução.

---

# 43. Fluxo 28 — Analisar desempenho

```text
Publicação
+
métricas
+
perfil
 ↓
Serviço de desempenho
 ↓
Comparações
 ↓
Indicadores
 ↓
Resultado
```

---

# 44. Fluxo 29 — Aprendizado

```text
Desempenho
 ↓
Comparar conteúdos
 ↓
Identificar padrões
 ↓
Avaliar evidências
 ↓
Gerar aprendizado
 ↓
Salvar
```

---

# 45. Fluxo 30 — Alimentar próxima criação

```text
Aprendizado
 ↓
Repositório
 ↓
Serviço de criação
 ↓
Selecionar aprendizados relevantes
 ↓
Contexto
 ↓
IA
```

Esse é o ponto em que o ViralCode começa a criar um ciclo próprio de inteligência.

---

# 46. Fluxo 31 — Feedback humano

O usuário poderá informar:

```text
aprovar
rejeitar
editar
gostar
não gostar
```

Esses sinais poderão ser utilizados posteriormente como dados de aprendizado.

---

# 47. Fluxo 32 — Erro de autenticação

```text
Requisição
 ↓
Token inválido
 ↓
401
```

---

# 48. Fluxo 33 — Acesso indevido

```text
Usuário A
 ↓
Solicita recurso do Usuário B
 ↓
Serviço verifica propriedade
 ↓
403 ou 404 conforme estratégia
```

---

# 49. Fluxo 34 — Erro do Instagram

```text
Serviço
 ↓
Conector
 ↓
Instagram
 ↓
Erro
 ↓
Normalização
 ↓
Código interno
 ↓
Log
 ↓
Resposta controlada
```

---

# 50. Fluxo 35 — Erro da IA

```text
Serviço
 ↓
Provedor IA
 ↓
Erro
 ↓
Registrar execução
 ↓
Tentativa controlada quando apropriado
 ↓
Erro final
```

---

# 51. Fluxo 36 — Timeout

Para integrações externas:

```text
requisição
 ↓
timeout
 ↓
interromper
 ↓
registrar
 ↓
retornar erro controlado
```

Nunca esperar indefinidamente.

---

# 52. Fluxo 37 — Configuração ausente

```text
Aplicação inicia
 ↓
Validação
 ↓
Configuração obrigatória ausente
 ↓
Erro de inicialização
```

---

# 53. Fluxo 38 — Banco indisponível

```text
API
 ↓
Banco
 ↓
falha
 ↓
erro controlado
 ↓
log
```

Não retornar sucesso falso.

---

# 54. Fluxo 39 — Reinício da aplicação

```text
VPS reinicia
 ↓
MySQL
 ↓
Backend
 ↓
Nginx
 ↓
Health check
 ↓
Sistema disponível
```

---

# 55. Fluxo 40 — Deploy

```text
Código
 ↓
Testes
 ↓
Git
 ↓
VPS
 ↓
Backup quando necessário
 ↓
Migrações
 ↓
Build
 ↓
Reinício
 ↓
Health check
 ↓
Smoke test
```

---

# 56. Fluxo 41 — Backup

```text
Agendamento
 ↓
Backup MySQL
 ↓
Arquivo
 ↓
Verificação
 ↓
Retenção
```

---

# 57. Fluxo 42 — Restauração

```text
Backup
 ↓
Banco de teste
 ↓
Restaurar
 ↓
Validar
```

O teste de restauração deverá ocorrer periodicamente.

---

# 58. Fluxo 43 — Diagnóstico

Quando um usuário relatar um problema:

```text
Usuário
 ↓
Correlation ID
 ↓
Logs
 ↓
Serviço
 ↓
Conector / Banco / IA
 ↓
Diagnóstico
```

---

# 59. Fluxo 44 — Conteúdo externo até criação

O fluxo mais importante do produto poderá ser resumido:

```text
CONTEÚDO EXTERNO
       ↓
COLETA
       ↓
NORMALIZAÇÃO
       ↓
ANÁLISE
       ↓
PADRÕES
       ↓
INSIGHTS
       ↓
CONTEXTO
       ↓
NOVA IDEIA
       ↓
ROTEIRO
       ↓
APROVAÇÃO
```

---

# 60. Fluxo 45 — Ciclo completo de aprendizado

```text
DESCUBRIR
   ↓
ANALISAR
   ↓
CRIAR
   ↓
PUBLICAR
   ↓
MEDIR
   ↓
COMPARAR
   ↓
APRENDER
   ↓
CRIAR NOVAMENTE
```

---

# 61. Regra de estado

O estado principal do negócio deverá estar persistido.

Não depender exclusivamente de:

```text
frontend
memória
logs
```

---

# 62. Regra de transação

Operações que alteram múltiplas entidades deverão avaliar a necessidade de transação.

Exemplo:

```text
criar publicação
+
atualizar conteúdo
```

---

# 63. Consistência

Se uma operação falhar no meio, o sistema deverá evitar estados inconsistentes.

---

# 64. Operações externas

Integrações externas não possuem a mesma transação do banco.

Portanto, o sistema deverá considerar:

```text
estado
+
tentativa
+
idempotência
+
reconciliação
```

quando necessário.

---

# 65. Reconciliação futura

Quando houver publicação assíncrona ou falhas intermediárias, poderá existir:

```text
estado interno
      ↓
consulta externa
      ↓
reconciliação
```

---

# 66. Não esconder erros

Se uma operação não foi concluída:

```text
não marcar como concluída
```

---

# 67. Regra de sucesso

Só registrar:

```text
CONCLUÍDO
```

quando houver evidência suficiente de conclusão.

---

# 68. Fluxo de IA com persistência

```text
Solicitação
 ↓
Criar execução IA
 ↓
Executar
 ↓
Receber resposta
 ↓
Validar
 ↓
Salvar resultado
 ↓
Atualizar execução
```

---

# 69. Fluxo de publicação com persistência

```text
Criar tentativa
 ↓
Enviar
 ↓
Receber resposta
 ↓
Salvar identificador externo quando existir
 ↓
Atualizar status
```

---

# 70. Fluxo de métrica com persistência

```text
Coletar
 ↓
Normalizar
 ↓
Identificar publicação
 ↓
Salvar medição
```

---

# 71. Regra de identificação externa

Sempre que a plataforma fornecer um identificador estável, armazenar o identificador necessário para permitir:

```text
consulta
deduplicação
reconciliação
```

---

# 72. Fluxo multi-perfil

```text
Usuário
 ├── Perfil A
 │    └── Instagram A
 │
 └── Perfil B
      └── Instagram B
```

As operações deverão respeitar o perfil selecionado.

---

# 73. Fluxo multi-nicho

```text
Usuário
 ↓
Perfil
 ↓
Nicho
 ↓
Conteúdo
```

O sistema não deverá assumir que todos os conteúdos do usuário pertencem ao mesmo nicho.

---

# 74. Fluxo futuro multi-rede

Arquitetura prevista:

```text
Conteúdo ViralCode
       ↓
Adaptador da plataforma
       ├── Instagram
       ├── TikTok
       └── YouTube
```

No MVP:

```text
somente Instagram
```

---

# 75. Regra contra acoplamento

Não colocar:

```text
regras do Instagram
```

dentro do:

```text
modelo de conteúdo
```

quando elas forem específicas da plataforma.

---

# 76. Regra de responsabilidade

```text
Rota
→ recebe requisição

Serviço
→ decide o que fazer

Repositório
→ acessa banco

Conector
→ conversa com plataforma externa

Provedor IA
→ conversa com modelo

Modelo
→ representa persistência

Esquema
→ representa contrato
```

---

# 77. Fluxo de desenvolvimento

Para implementar qualquer funcionalidade:

```text
DOCUMENTO
 ↓
MODELO
 ↓
ESQUEMA
 ↓
SERVIÇO
 ↓
REPOSITÓRIO / CONECTOR
 ↓
ROTA
 ↓
TESTES
 ↓
FRONTEND
```

A ordem poderá variar quando necessário, mas a separação deverá ser preservada.

---

# 78. Regra para agentes de IA

Antes de implementar um novo fluxo:

1. identificar o fluxo neste documento;
2. localizar os módulos envolvidos;
3. verificar os contratos da API;
4. verificar o modelo de dados;
5. implementar sem atravessar responsabilidades;
6. criar testes;
7. atualizar este documento se o fluxo mudar.

---

# 79. Critério de sucesso

Um fluxo estará corretamente implementado quando for possível rastreá-lo de:

```text
INTERFACE
 ↓
API
 ↓
SERVIÇO
 ↓
BANCO / INTEGRAÇÃO
 ↓
RESULTADO
```

sem existir lógica crítica escondida em outra camada.

---

# 80. Regra final

> **O ViralCode deverá ser compreensível como uma sequência de fluxos de negócio, e não apenas como uma coleção de arquivos e endpoints.**

O fluxo central do produto é:

```text
DESCOBRIR
   ↓
ENTENDER
   ↓
CRIAR
   ↓
PUBLICAR
   ↓
MEDIR
   ↓
APRENDER
   ↓
MELHORAR
```

Esse ciclo deverá orientar as decisões de implementação do MVP e a evolução futura do ViralCode.

**Versão:** 1.0  
**Status:** Documento oficial dos Fluxos Principais do Sistema
