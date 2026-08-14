# 18 — ESTRATÉGIA DE DESCOBERTA DO INSTAGRAM

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define como o ViralCode deverá tratar a descoberta de conteúdos no Instagram no MVP.

A descoberta é uma função estratégica porque o conceito central do ViralCode envolve encontrar conteúdos relevantes, analisar seu desempenho e utilizar os padrões identificados para orientar novas criações.

O objetivo deste documento é separar claramente:

```text
O QUE A PLATAFORMA PERMITE
```

de:

```text
O QUE O VIRALCODE GOSTARIA DE FAZER
```

e impedir que a implementação seja construída sobre uma capacidade não confirmada.

---

# 2. Descoberta desejada pelo produto

A experiência ideal do ViralCode seria:

```text
Usuário informa:

Nicho:
casamento

Tema:
diálogo

Visualizações mínimas:
1.000.000
```

Depois:

```text
Instagram
   ↓
Conteúdos encontrados
   ↓
ViralCode
   ↓
Filtro
   ↓
≥ 1.000.000 visualizações
   ↓
Ranking
   ↓
Análise
```

Essa é a experiência desejada.

Ela não deve ser confundida com uma capacidade garantida da API oficial.

---

# 3. Decisão técnica atual

A integração oficial do Instagram é direcionada a contas profissionais — Business e Creator. A documentação atual diferencia o acesso via Instagram Login e via Facebook Login. O Instagram Login utiliza Instagram User access tokens e `graph.instagram.com`; o Facebook Login utiliza Facebook User/Page access tokens e `graph.facebook.com`. citeturn0search0turn0search1

Para o ViralCode, a primeira implementação deverá priorizar a integração oficial e as capacidades efetivamente disponíveis para a conta conectada.

---

# 4. O que está confirmado para a conta conectada

A API oficial permite que uma aplicação gerencie a presença de uma conta Instagram profissional conectada.

Entre as capacidades documentadas estão:

```text
consultar mídia da conta
publicar conteúdo
obter insights
gerenciar determinados recursos da conta
```

As capacidades exatas dependem do modelo de login, permissões e nível de acesso da aplicação. citeturn0search0turn0search1

---

# 5. Métricas da própria conta

A API oficial permite obter insights de contas profissionais e de suas mídias.

Exemplos documentados incluem métricas de:

```text
alcance
impressões
visualizações/engajamento conforme o recurso
comentários
compartilhamentos
```

A disponibilidade exata varia por endpoint, tipo de mídia, conta e permissão. citeturn0search1turn0search11

---

# 6. Limitação crítica

A API com Instagram Login não deve ser tratada como uma API de pesquisa geral do Instagram.

A documentação de Insights informa que os dados de mídia retornados são referentes a mídia pertencente a contas profissionais do usuário da aplicação; não é um mecanismo geral para obter insights de qualquer mídia pública de qualquer usuário. citeturn0search1

Portanto, não assumir que:

```text
usuário conecta sua conta
        ↓
pesquisa "casamento"
        ↓
Instagram retorna todos os Reels públicos
        ↓
ViralCode ordena por visualizações
```

seja possível usando somente esse fluxo.

---

# 7. Descoberta de conteúdo de terceiros

Existe uma diferença importante entre:

```text
DADOS DA CONTA CONECTADA
```

e:

```text
CONTEÚDOS DE TERCEIROS
```

O primeiro é claramente suportado em diversos recursos da API.

O segundo possui limitações e depende do recurso específico utilizado.

A arquitetura não deverá considerar descoberta irrestrita de terceiros como requisito garantido do MVP.

---

# 8. Hashtags

A documentação da API com Facebook Login descreve capacidade de encontrar mídia associada a hashtags e obter determinados metadados e métricas de outros perfis profissionais. citeturn0search0turn0search2

Isso representa uma possibilidade técnica relevante para a estratégia de descoberta.

Entretanto, essa modalidade possui requisitos próprios e não deve ser confundida com uma busca livre por palavra-chave.

---

# 9. Ordenação

A documentação do fluxo com Facebook Login informa que a ordenação dos resultados não é suportada pelo endpoint.

Portanto, o ViralCode não deverá assumir que poderá solicitar:

```text
ordene os resultados por visualizações DESC
```

diretamente ao Instagram. citeturn0search0turn0search5

Quando os dados permitirem, a ordenação deverá ser realizada pelo próprio ViralCode depois da coleta.

---

# 10. Estratégia de ranking do ViralCode

Quando o ViralCode receber dados suficientes:

```text
Instagram
   ↓
Resultados
   ↓
Normalização
   ↓
Banco
   ↓
Filtro
   ↓
Ranking ViralCode
```

Exemplo:

```text
visualizações DESC
```

O ranking é responsabilidade do ViralCode.

---

# 11. Filtro de visualizações

Se a resposta da plataforma disponibilizar a métrica necessária, o ViralCode poderá aplicar:

```text
visualizacoes >= 1.000.000
```

Exemplo:

```text
Conteúdo A → 3.200.000
Conteúdo B → 1.800.000
Conteúdo C → 700.000
Conteúdo D → 120.000
```

Resultado:

```text
A
B
```

Não incluir C ou D apenas para preencher resultados.

---

# 12. Dados ausentes

Se a plataforma não fornecer a métrica de visualizações:

```text
visualizacoes = NULL
```

Não utilizar:

```text
0
```

como substituto de informação desconhecida.

---

# 13. Busca por palavra-chave

O produto poderá possuir no frontend:

```text
campo:
"Digite o nicho ou tema"
```

Mas esse texto não deve ser enviado automaticamente para a API como se existisse uma operação oficial equivalente.

O backend deverá transformar a intenção do usuário em uma estratégia de descoberta compatível com os recursos disponíveis.

---

# 14. Estratégia de descoberta

Conceito:

```text
Intenção do usuário
        ↓
Serviço de Descoberta
        ↓
Estratégia disponível
        ↓
Conector Instagram
        ↓
Instagram
        ↓
Resultados
```

A estratégia poderá utilizar diferentes mecanismos conforme a capacidade disponível.

---

# 15. Fontes de descoberta possíveis

A arquitetura deverá permitir estratégias como:

```text
hashtags
contas
mídias da conta conectada
mídias relacionadas aos recursos disponíveis
outros mecanismos oficialmente disponíveis
```

Não implementar mecanismos que dependam de contornar restrições da plataforma.

---

# 16. Descoberta por hashtag

Quando o recurso estiver disponível para o modelo de integração escolhido:

```text
#casamento
```

poderá funcionar como ponto de descoberta.

Fluxo:

```text
Hashtag
   ↓
Instagram
   ↓
Mídias disponíveis
   ↓
ViralCode
   ↓
Normalização
   ↓
Filtro
```

---

# 17. Limitação da hashtag

Encontrar mídia associada a uma hashtag não significa automaticamente:

```text
retornar todos os conteúdos
```

nem:

```text
retornar todos os conteúdos em ordem de visualizações
```

O ViralCode deverá trabalhar com os resultados efetivamente retornados pela plataforma.

---

# 18. Descoberta por conta

Outra estratégia possível é analisar contas profissionais específicas.

Exemplo:

```text
Conta A
Conta B
Conta C
```

Depois:

```text
mídias disponíveis
   ↓
métricas disponíveis
   ↓
ranking
```

---

# 19. Descoberta de concorrentes

Futuramente o usuário poderá informar:

```text
@perfil1
@perfil2
@perfil3
```

O ViralCode poderá analisar o que estiver oficialmente disponível para essas contas.

Essa funcionalidade não deve ser considerada garantida para qualquer conta ou qualquer métrica.

---

# 20. Descoberta híbrida

A arquitetura poderá combinar:

```text
hashtag
+
contas conhecidas
+
conteúdos previamente armazenados
```

Exemplo:

```text
Hashtag casamento
        ↓
Contas identificadas
        ↓
Novas mídias
        ↓
Banco ViralCode
```

---

# 21. Banco como fonte histórica

Uma vez que o ViralCode tenha coletado um conteúdo legitimamente:

```text
Instagram
   ↓
ViralCode
   ↓
MySQL
```

o banco poderá ser utilizado como fonte histórica interna.

Exemplo:

```text
Pesquisa atual
+
Conteúdos já coletados
```

Isso permite enriquecer o produto com o tempo.

---

# 22. Descoberta incremental

O sistema deverá preferir:

```text
coletar
   ↓
armazenar
   ↓
atualizar
```

em vez de tentar reconstruir todo o universo de conteúdos a cada pesquisa.

Isso reduz custo e dependência da plataforma.

---

# 23. Deduplicação

O mesmo conteúdo poderá aparecer por diferentes estratégias.

Exemplo:

```text
#casamento
   ↓
Conteúdo A

Conta @perfil
   ↓
Conteúdo A
```

O ViralCode deverá armazenar o conteúdo uma única vez.

Chave conceitual:

```text
plataforma
+
identificador_externo
```

---

# 24. Ranking interno

O ViralCode poderá criar um ranking próprio.

Primeiro critério:

```text
visualizações
```

Depois poderão existir:

```text
engajamento
crescimento
velocidade
compartilhamentos
salvamentos
```

---

# 25. Conteúdo viral

O ViralCode não deverá definir:

```text
viral = necessariamente > 1 milhão
```

como regra universal.

O limite de:

```text
1.000.000
```

deverá ser tratado como filtro configurável pelo usuário.

---

# 26. Filtro configurável

Exemplo:

```json
{
  "visualizacoes_minimas": 1000000
}
```

Outro usuário poderá escolher:

```json
{
  "visualizacoes_minimas": 100000
}
```

---

# 27. Outros filtros

Futuramente:

```text
data mínima
data máxima
tipo de mídia
autor
hashtag
tema
idioma
```

Somente filtros suportados pelos dados disponíveis deverão ser aplicados.

---

# 28. Resultado da pesquisa

O frontend deverá receber uma estrutura interna do ViralCode.

Exemplo:

```json
{
  "conteudos": [
    {
      "id": 123,
      "plataforma": "instagram",
      "autor": "@perfil",
      "url": "...",
      "visualizacoes": 1500000
    }
  ]
}
```

Os campos definitivos serão definidos no contrato da API.

---

# 29. Estratégia de descoberta no MVP

A primeira implementação deverá ser feita em duas etapas.

### Etapa 1 — Validação técnica

Confirmar:

```text
login
permissões
conta profissional
acesso aos recursos
retorno de mídia
retorno de métricas
```

### Etapa 2 — Descoberta

Implementar somente os mecanismos oficialmente disponíveis e úteis após a validação.

---

# 30. Regra de bloqueio

Se o requisito:

```text
"encontrar qualquer Reel público por palavra-chave
e ordenar por visualizações"
```

não puder ser realizado pelo acesso oficial escolhido, o desenvolvimento não deverá tentar contornar a limitação.

O requisito deverá ser revisto.

---

# 31. Alternativas legítimas

Se a descoberta ampla de terceiros não for possível no primeiro modelo de integração, o MVP poderá ser adaptado para:

```text
analisar contas conectadas
```

ou:

```text
analisar conteúdos obtidos por recursos oficialmente disponíveis
```

ou:

```text
criar um banco próprio de conteúdos coletados ao longo do uso
```

---

# 32. Banco próprio como vantagem

Mesmo que a descoberta inicial seja limitada, o ViralCode poderá construir um ativo próprio:

```text
COLETAR
   ↓
NORMALIZAR
   ↓
ARMAZENAR
   ↓
ENRIQUECER
   ↓
ANALISAR
```

Com o tempo:

```text
Banco ViralCode
=
histórico de conteúdos + métricas + padrões + aprendizados
```

---

# 33. Não depender de uma única consulta

O produto não deverá depender de uma única operação:

```text
buscar tudo
```

A estratégia deverá ser incremental.

Exemplo:

```text
Hashtags
   ↓
Contas
   ↓
Conteúdos
   ↓
Atualizações
   ↓
Histórico
```

---

# 34. Conector Instagram

O conector deverá expor operações internas abstratas.

Exemplo conceitual:

```python
class ConectorInstagram:
    def obter_midias_da_conta(self, conta):
        ...

    def obter_insights_midia(self, midia):
        ...

    def pesquisar_por_hashtag(self, hashtag):
        ...
```

Somente métodos realmente suportados deverão ser implementados.

---

# 35. Serviço de Descoberta

O serviço deverá decidir qual estratégia usar.

Exemplo:

```python
class ServicoDescoberta:
    def descobrir(self, criterios):
        ...
```

Ele poderá:

```text
validar critérios
selecionar estratégia
chamar conector
normalizar resultados
filtrar
classificar
salvar
```

---

# 36. Separação de responsabilidades

```text
FastAPI
   ↓
ServicoDescoberta
   ↓
EstrategiaDescoberta
   ↓
ConectorInstagram
   ↓
Instagram
```

Persistência:

```text
ServicoDescoberta
   ↓
RepositorioConteudo
   ↓
SQLAlchemy
   ↓
MySQL
```

---

# 37. Estratégias intercambiáveis

A arquitetura deverá permitir:

```text
EstrategiaPorHashtag
EstrategiaPorConta
EstrategiaPorHistorico
```

No futuro:

```text
EstrategiaPorOutroRecurso
```

Isso evita acoplar o produto a um único mecanismo de descoberta.

---

# 38. Testes

Deverão existir testes para:

```text
critérios válidos
critérios inválidos
nenhum resultado
resultado duplicado
métrica ausente
filtro de visualizações
paginação
erro de permissão
conta desconectada
timeout
```

---

# 39. Testes sem Instagram

Utilizar um conector falso:

```text
ServicoDescoberta
      ↓
ConectorInstagramFalso
      ↓
dados simulados
```

Isso permite desenvolver o motor de descoberta antes de depender da integração real.

---

# 40. Segurança

A descoberta deverá utilizar somente:

```text
credenciais protegidas
conta autorizada
permissões concedidas
```

Nunca utilizar:

```text
senha do usuário
credenciais expostas
mecanismos de bypass
```

---

# 41. Privacidade

O ViralCode deverá armazenar somente os dados necessários para sua finalidade.

Dados de terceiros deverão ser tratados de acordo com as permissões e regras aplicáveis.

---

# 42. Conformidade

A implementação deverá respeitar:

```text
documentação da plataforma
permissões
limites
políticas
termos aplicáveis
legislação pertinente
```

---

# 43. Métricas da própria conta

A integração com Instagram permite consultar insights de mídias pertencentes às contas profissionais conectadas, observadas as permissões e requisitos do recurso. citeturn0search1turn0search11

Essa será uma capacidade segura para a arquitetura do Motor de Desempenho.

---

# 44. Publicação

A API oficial também documenta publicação de conteúdo para contas profissionais, incluindo fluxo de publicação de Reels. citeturn0search0

Portanto, o fluxo:

```text
Motor de Criação
   ↓
Aprovação
   ↓
Motor de Publicação
   ↓
Conector Instagram
```

permanece compatível com a direção arquitetural do projeto, sujeito às permissões e requisitos da plataforma.

---

# 45. Decisão para o MVP

A decisão oficial é:

> **Não prometer no MVP uma pesquisa irrestrita de todos os Reels públicos do Instagram por palavra-chave e ordenação por visualizações.**

Primeiro será validado o conjunto de recursos efetivamente disponível para a aplicação e para a conta conectada.

---

# 46. Caso a descoberta ampla seja viável

Se a validação técnica demonstrar que o recurso necessário está disponível:

```text
Usuário
   ↓
Critérios
   ↓
ServicoDescoberta
   ↓
ConectorInstagram
   ↓
Resultados
   ↓
Filtro
   ↓
Ranking
   ↓
Motor de Inteligência
```

---

# 47. Caso a descoberta ampla não seja viável

O MVP deverá utilizar uma alternativa oficialmente suportada.

Prioridade:

```text
1. Recursos oficiais do Instagram
2. Banco próprio acumulado
3. Estratégia de contas/hashtags suportada
4. Redução temporária do escopo
```

Não implementar mecanismos para burlar limitações.

---

# 48. Critério de sucesso

A estratégia de descoberta será considerada tecnicamente validada quando conseguirmos demonstrar, com uma conta e aplicação de teste:

```text
autenticação
      ↓
permissão
      ↓
consulta
      ↓
resultado
      ↓
métrica
      ↓
persistência
```

e soubermos exatamente quais dados podem ser obtidos de forma suportada.

---

# 49. Primeira prova de conceito

Antes de construir toda a interface, executar uma POC mínima:

```text
1. Criar aplicação Meta/Instagram
2. Conectar conta profissional de teste
3. Obter autorização
4. Obter token
5. Consultar identidade da conta
6. Consultar mídias próprias
7. Consultar métricas disponíveis
8. Testar recursos de descoberta oficialmente disponíveis
9. Registrar limitações
```

Somente depois fechar a implementação definitiva.

---

# 50. Regra para agentes de IA

Antes de alterar a descoberta:

1. ler este documento;
2. verificar a documentação atual da plataforma;
3. não assumir que um endpoint existe;
4. não inventar métricas;
5. não assumir acesso a conteúdo de terceiros;
6. não implementar bypass;
7. respeitar permissões;
8. testar com conta real de desenvolvimento;
9. registrar limitações;
10. atualizar este documento quando a capacidade da plataforma mudar.

---

# 51. Arquitetura

```text
                    USUÁRIO
                       │
                       ▼
                CRITÉRIOS DE BUSCA
                       │
                       ▼
                SERVIÇO DE DESCOBERTA
                       │
            ┌──────────┼──────────┐
            ▼          ▼          ▼
        HASHTAG      CONTA     HISTÓRICO
            │          │          │
            └──────────┼──────────┘
                       ▼
                CONECTOR INSTAGRAM
                       │
                       ▼
                    INSTAGRAM
                       │
                       ▼
                  NORMALIZAÇÃO
                       │
                       ▼
                   DEDUPLICAÇÃO
                       │
                       ▼
                      FILTRO
                       │
                       ▼
                    RANKING
                       │
                       ▼
                    MYSQL
                       │
                       ▼
              MOTOR DE INTELIGÊNCIA
```

---

# 52. Arquitetura-alvo

```text
                         INSTAGRAM
                             │
                             ▼
                    CONECTOR INSTAGRAM
                             │
                             ▼
                    SERVIÇO DE DESCOBERTA
                             │
                  ┌──────────┼──────────┐
                  ▼          ▼          ▼
               HASHTAG     CONTAS    HISTÓRICO
                  │          │          │
                  └──────────┼──────────┘
                             ▼
                         CONTEÚDOS
                             │
                             ▼
                           MYSQL
                             │
                             ▼
                   MOTOR DE INTELIGÊNCIA
                             │
                             ▼
                      MOTOR DE CRIAÇÃO
                             │
                             ▼
                      MOTOR DE PUBLICAÇÃO
                             │
                             ▼
                         INSTAGRAM
                             │
                             ▼
                    MOTOR DE DESEMPENHO
                             │
                             ▼
                    MOTOR DE APRENDIZADO
```

---

# 53. Regra final

> **O ViralCode deverá construir sua inteligência sobre dados que consegue obter legitimamente e de forma tecnicamente comprovada.**

Não vamos construir o produto em cima da hipótese:

```text
"o Instagram certamente fornece tudo que precisamos."
```

Vamos trabalhar com:

```text
RECURSO CONFIRMADO
        ↓
IMPLEMENTAÇÃO
        ↓
DADO REAL
        ↓
VALIDAÇÃO
```

E somente depois expandir a descoberta.

**Versão:** 1.0  
**Status:** Documento oficial da Estratégia de Descoberta do Instagram
