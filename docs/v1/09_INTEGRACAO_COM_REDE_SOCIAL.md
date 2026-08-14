# 09 — INTEGRAÇÃO COM REDE SOCIAL

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define a arquitetura oficial para integração do ViralCode com redes sociais.

O ViralCode deverá acessar as redes sociais **diretamente através de contas conectadas pelo usuário**, utilizando o mecanismo de autenticação e acesso apropriado para cada plataforma.

A primeira rede social prevista é:

```text
Instagram
```

A arquitetura deverá permitir posteriormente:

```text
TikTok
YouTube
outras redes sociais
```

---

# 2. Decisão arquitetural oficial

O ViralCode não deverá depender estruturalmente de um agregador externo de dados.

A arquitetura oficial é:

```text
Usuário
   ↓
Conta Social Conectada
   ↓
ViralCode
   ↓
Conector da Rede Social
   ↓
Rede Social
```

O conector será responsável por encapsular todos os detalhes específicos da plataforma.

---

# 3. Objetivo da conexão

A conexão com uma rede social deverá permitir que o ViralCode utilize os recursos que estiverem disponíveis para a conta conectada e para o mecanismo de integração adotado.

Entre as possibilidades futuras estão:

```text
descoberta de conteúdos
consulta de informações
coleta de métricas
análise de conteúdos
acompanhamento de desempenho
publicação
```

Nem todas essas capacidades estarão disponíveis para todas as plataformas.

A aplicação deverá trabalhar somente com aquilo que a plataforma permitir.

---

# 4. Arquitetura em camadas

O fluxo deverá seguir:

```text
React
  ↓
FastAPI
  ↓
Serviços
  ↓
Conectores de Redes Sociais
  ↓
Rede Social
```

Para descoberta:

```text
React
  ↓
FastAPI
  ↓
Serviço de Descoberta
  ↓
Conector Instagram
  ↓
Instagram
```

Para publicação futura:

```text
React
  ↓
FastAPI
  ↓
Serviço de Publicação
  ↓
Conector Instagram
  ↓
Instagram
```

---

# 5. O que é um conector

Um conector é o componente responsável por encapsular a comunicação com uma rede social específica.

Exemplo:

```text
Conectores
│
├── Conector Instagram
├── Conector TikTok
├── Conector YouTube
└── Outros conectores futuros
```

Cada conector conhece os detalhes técnicos da sua própria plataforma.

O restante do ViralCode não deverá precisar conhecer esses detalhes.

---

# 6. Primeiro conector

O primeiro conector será:

```text
ConectorInstagram
```

Ele deverá concentrar as regras específicas do Instagram.

Responsabilidades:

- autenticação;
- gerenciamento da conexão;
- comunicação;
- transformação de requisições;
- interpretação das respostas;
- paginação;
- tratamento de erros;
- controle de limites;
- normalização inicial;
- reautenticação.

---

# 7. Abstração

O sistema deverá possuir uma abstração conceitual para conectores.

Exemplo:

```python
class ConectorRedeSocial:
    def pesquisar_conteudos(self, parametros):
        ...
```

Implementação:

```python
class ConectorInstagram(ConectorRedeSocial):
    def pesquisar_conteudos(self, parametros):
        ...
```

No futuro:

```python
class ConectorTikTok(ConectorRedeSocial):
    ...
```

---

# 8. Regra de dependência

Os serviços deverão depender da abstração:

```text
ConectorRedeSocial
```

e não espalhar dependências específicas de uma plataforma.

Exemplo correto:

```text
Serviço de Descoberta
        ↓
ConectorRedeSocial
```

Exemplo que deve ser evitado:

```text
Serviço de Descoberta
        ↓
código específico do Instagram
```

---

# 9. Conta Social

A conta social conectada deverá ser uma entidade própria do sistema.

Conceito:

```text
ContaSocial
├── id
├── plataforma
├── identificador_externo
├── nome_usuario
├── status
├── data_conexao
└── dados_de_autenticacao_protegidos
```

---

# 10. Estados da conexão

A conta poderá possuir estados como:

```text
CONECTADA
EXPIRADA
REVOGADA
ERRO
REAUTENTICACAO_NECESSARIA
```

O estado deverá permitir que o sistema saiba se a conta está disponível para utilização.

---

# 11. Perfil do ViralCode versus Conta Social

São entidades diferentes.

### Perfil do ViralCode

Representa uma identidade ou projeto dentro do ViralCode.

### Conta Social

Representa uma conta real conectada em uma rede social.

Exemplo:

```text
Perfil ViralCode
       │
       ├── Conta Instagram
       ├── Conta TikTok
       └── Conta YouTube
```

Essa estrutura permitirá crescimento futuro.

---

# 12. Conta conectada versus autor encontrado

A conta utilizada para acessar a plataforma não precisa ser a autora dos conteúdos descobertos.

Exemplo:

```text
Conta conectada:
@meuperfil

Pesquisa:
casamento

Resultados:
@autor_a
@autor_b
@autor_c
```

A conta conectada é a identidade utilizada para acessar a rede.

Os autores encontrados são dados dos conteúdos analisados.

---

# 13. Autenticação

O ViralCode deverá utilizar o mecanismo de autenticação apropriado para cada rede social.

O sistema não deverá solicitar ou armazenar a senha da conta social como mecanismo normal de integração.

Quando houver:

```text
tokens
credenciais
sessões
chaves
```

esses dados deverão permanecer protegidos no backend.

---

# 14. Regra de segurança

Nunca:

```text
senha da rede social no banco
senha da rede social no frontend
token em código-fonte
token em log
credencial em resposta da API
```

Credenciais deverão ser tratadas como dados sensíveis.

---

# 15. Fluxo de conexão

Fluxo conceitual:

```text
Usuário
   ↓
Escolhe rede social
   ↓
Inicia conexão
   ↓
Autenticação na plataforma
   ↓
Autorização
   ↓
Retorno ao ViralCode
   ↓
ContaSocial criada
   ↓
Status = CONECTADA
```

O mecanismo técnico exato será definido durante a implementação do conector.

---

# 16. Reautenticação

Quando a conexão deixar de ser válida:

```text
ContaSocial
   ↓
REAUTENTICACAO_NECESSARIA
```

O sistema deverá solicitar nova conexão ao usuário.

Depois:

```text
Nova autenticação
   ↓
ContaSocial
   ↓
CONECTADA
```

---

# 17. Desconexão

O sistema deverá futuramente permitir:

```text
Desconectar conta
```

Fluxo:

```text
CONECTADA
   ↓
Desconectar
   ↓
Revogar/inutilizar conexão
   ↓
REVOGADA
```

A aplicação deverá preservar ou excluir os dados históricos de acordo com a política definida para o produto.

---

# 18. Serviço de Descoberta

O Serviço de Descoberta será responsável por transformar uma solicitação do usuário em uma operação de descoberta.

Exemplo:

```text
Usuário:
"Quero encontrar Reels sobre casamento
com mais de 1 milhão de visualizações."
```

Fluxo:

```text
Solicitação
   ↓
Serviço de Descoberta
   ↓
Conta Social
   ↓
Conector
   ↓
Rede Social
   ↓
Resultados
```

---

# 19. A pesquisa pertence ao ViralCode

O usuário poderá informar:

```json
{
  "termo": "casamento",
  "plataforma": "instagram",
  "visualizacoes_minimas": 1000000,
  "periodo_dias": 90
}
```

Esse é o modelo de intenção do ViralCode.

O conector deverá traduzir essa intenção para os recursos realmente disponíveis na plataforma.

---

# 20. A rede social pode não possuir a pesquisa exata

Não assumir que a plataforma possui uma operação equivalente a:

```text
"retorne todos os Reels de casamento
com mais de 1 milhão de visualizações"
```

O ViralCode deverá possuir sua própria lógica de descoberta.

Conceito:

```text
Critérios do usuário
       ↓
Estratégia de descoberta
       ↓
Recursos disponíveis na plataforma
       ↓
Resultados
       ↓
Filtro ViralCode
       ↓
Ranking ViralCode
```

---

# 21. Estratégias de descoberta

Dependendo dos recursos disponíveis, o conector poderá utilizar mecanismos como:

```text
pesquisa
hashtags
perfis
conteúdos relacionados
conteúdos públicos acessíveis
outros recursos disponíveis para a conta
```

A estratégia concreta deverá ser definida durante a implementação e validada tecnicamente.

---

# 22. Filtro de visualizações

Exemplo:

```text
visualizacoes_minimas = 1.000.000
```

O ViralCode deverá aplicar o filtro depois de receber os dados disponíveis.

Exemplo:

```text
Conteúdos encontrados
       ↓
Normalização
       ↓
visualizacoes >= 1.000.000
       ↓
Resultados válidos
```

---

# 23. Ranking

O ViralCode poderá criar seu próprio ranking.

MVP:

```text
visualizacoes DESC
```

Futuro:

```text
visualizações
+
crescimento
+
compartilhamentos
+
comentários
+
salvamentos
+
outros indicadores
```

---

# 24. Modelo interno de conteúdo

O ViralCode deverá possuir seu próprio modelo.

Exemplo:

```text
Conteúdo
├── id
├── plataforma
├── identificador_externo
├── tipo
├── url
├── legenda
├── data_publicacao
├── autor
└── referencia_midia
```

O banco não deverá reproduzir diretamente o modelo de dados de uma rede social.

---

# 25. Modelo interno de métricas

```text
Metrica
├── id
├── conteudo_id
├── visualizacoes
├── curtidas
├── comentarios
├── compartilhamentos
├── salvamentos
└── data_coleta
```

A disponibilidade de cada campo dependerá da plataforma e das permissões disponíveis.

---

# 26. Dados indisponíveis

O sistema não deverá inventar dados.

Se uma métrica não estiver disponível:

```text
NULL
```

ou ausência controlada.

Não transformar automaticamente:

```text
informação desconhecida
```

em:

```text
0
```

---

# 27. Normalização

Os dados externos deverão ser transformados para os modelos internos do ViralCode.

Exemplo conceitual:

```text
Campo externo
      ↓
Mapeamento
      ↓
Modelo ViralCode
```

Essa transformação deverá acontecer no conector ou em uma camada de normalização associada a ele.

---

# 28. Deduplicação

O mesmo conteúdo poderá aparecer em diferentes pesquisas.

Exemplo:

```text
Pesquisa A
   ↓
Conteúdo 123

Pesquisa B
   ↓
Conteúdo 123
```

O conteúdo deverá existir uma única vez no banco.

As pesquisas poderão possuir relações com o mesmo conteúdo.

---

# 29. Identificador externo

Quando disponível, utilizar:

```text
plataforma
+
identificador_externo
```

como referência principal para deduplicação.

---

# 30. URL

A URL do conteúdo deverá ser armazenada quando disponível.

Ela poderá ser utilizada para:

- referência;
- navegação;
- validação;
- análise;
- acesso ao conteúdo.

Não deverá ser considerada automaticamente como identificador universal.

---

# 31. Histórico de métricas

Quando for possível consultar o conteúdo novamente, o ViralCode poderá registrar novas métricas.

Exemplo:

```text
Conteúdo ABC

10:00 → 1.000.000
14:00 → 1.300.000
18:00 → 1.800.000
22:00 → 2.400.000
```

Isso permitirá futuramente calcular:

```text
crescimento
velocidade
aceleração
tendência
```

---

# 32. Paginação

Se a rede social retornar resultados paginados:

```text
Página 1
   ↓
Página 2
   ↓
Página 3
```

o conector deverá controlar a paginação.

O frontend não deverá controlar diretamente a paginação interna da plataforma.

---

# 33. Limite de paginação

Cada operação deverá possuir um limite máximo de páginas.

Objetivos:

- evitar excesso de chamadas;
- reduzir tempo;
- proteger a conta;
- proteger a infraestrutura;
- evitar operações desnecessárias.

---

# 34. Limites da plataforma

O conector deverá respeitar:

- limites de requisições;
- permissões;
- autenticação;
- políticas;
- respostas de erro;
- condições de acesso.

Nunca tentar contornar mecanismos de proteção da plataforma.

---

# 35. Timeout

Toda comunicação externa deverá possuir timeout.

Nenhuma operação poderá permanecer aguardando indefinidamente.

---

# 36. Retry

Retentativas poderão ser utilizadas para erros temporários.

Exemplos:

```text
timeout
falha temporária de conexão
erro transitório
```

Não fazer retry infinito.

Não repetir automaticamente erros permanentes como:

```text
autenticação inválida
permissão negada
parâmetro inválido
conta desconectada
```

---

# 37. Cache futuro

Resultados recentes poderão futuramente ser reutilizados.

```text
Nova pesquisa
      ↓
Existe resultado recente?
      ├── SIM → reutilizar
      └── NÃO → consultar rede social
```

Isso poderá reduzir chamadas e tempo de resposta.

Não é obrigatório no MVP.

---

# 38. Resposta bruta

O ViralCode não deverá armazenar automaticamente toda resposta recebida da plataforma.

Fluxo:

```text
Rede Social
    ↓
Conector
    ↓
Normalização
    ↓
Modelo ViralCode
    ↓
Banco
```

Caso futuramente seja necessário armazenar dados brutos para auditoria, deverá existir política específica de retenção e segurança.

---

# 39. Testes

O sistema deverá conseguir testar os serviços sem depender de uma rede social real.

Exemplo:

```text
Teste
  ↓
Serviço
  ↓
Conector falso
  ↓
Resposta controlada
```

---

# 40. Testes mínimos

Devem existir cenários para:

```text
conexão válida
conexão expirada
reautenticação
nenhum resultado
resultado válido
dados incompletos
limite de requisição
timeout
erro inesperado
duplicidade
```

---

# 41. Múltiplas contas

A arquitetura deverá permitir:

```text
Perfil ViralCode
       │
       ├── Instagram A
       ├── Instagram B
       ├── TikTok A
       └── YouTube A
```

Cada conta terá sua própria conexão e estado.

---

# 42. Múltiplos perfis

O produto deverá futuramente permitir vários perfis.

Exemplo:

```text
Organização
│
├── Perfil Casamento
│     ├── Instagram
│     └── TikTok
│
├── Perfil Fitness
│     ├── Instagram
│     └── YouTube
│
└── Perfil Educação
      └── Instagram
```

Essa estrutura deve ser considerada desde a arquitetura, mesmo que não seja implementada no MVP.

---

# 43. Relação com o Motor de Inteligência

O conector não analisa estratégia.

Ele coleta e normaliza.

Fluxo:

```text
Rede Social
     ↓
Conector
     ↓
Conteúdos
     ↓
Banco
     ↓
Motor de Inteligência
     ↓
Padrões
```

O Motor de Inteligência não deverá acessar diretamente a rede social.

---

# 44. Relação com o Motor de Criação

O Motor de Criação deverá utilizar os conhecimentos produzidos pelo Motor de Inteligência.

```text
Rede Social
     ↓
Conector
     ↓
Dados
     ↓
Inteligência
     ↓
Padrões
     ↓
Motor de Criação
     ↓
Novo conteúdo
```

---

# 45. Relação com o Motor de Publicação

A publicação será uma responsabilidade separada.

```text
Motor de Criação
       ↓
Conteúdo aprovado
       ↓
Motor de Publicação
       ↓
Conector da Rede Social
       ↓
Rede Social
```

O mesmo conector poderá possuir capacidades de leitura e publicação, mas essas capacidades deverão ficar separadas em serviços distintos.

---

# 46. Segurança das contas sociais

As credenciais de acesso deverão:

- ficar no backend;
- nunca ser expostas no frontend;
- nunca aparecer nos logs;
- possuir controle de acesso;
- possuir ciclo de vida;
- ser invalidadas quando necessário.

---

# 47. Privacidade

O ViralCode deverá utilizar somente os dados necessários para suas finalidades.

Não coletar ou armazenar informações simplesmente porque estão disponíveis.

---

# 48. Conformidade

Toda integração deverá respeitar:

- mecanismos de autenticação da plataforma;
- permissões concedidas;
- políticas da plataforma;
- termos aplicáveis;
- legislação pertinente.

O ViralCode não deverá implementar mecanismos destinados a burlar controles da plataforma.

---

# 49. Independência da plataforma

Se a rede social alterar sua API ou seu modelo de dados, o impacto deverá ficar concentrado no conector sempre que possível.

O restante do sistema deverá continuar trabalhando com os modelos internos do ViralCode.

---

# 50. Regra de isolamento

Não espalhar código específico da rede social por:

```text
rotas
serviços
repositórios
modelos
frontend
```

O código específico deverá permanecer concentrado no:

```text
ConectorInstagram
```

ou em componentes diretamente associados a ele.

---

# 51. Regra para agentes de IA

Antes de alterar uma integração:

1. ler este documento;
2. verificar se já existe conector;
3. respeitar a abstração `ConectorRedeSocial`;
4. não colocar chamadas externas nas rotas;
5. não colocar credenciais no código;
6. não armazenar senhas;
7. não expor tokens;
8. respeitar limites e permissões;
9. criar testes;
10. atualizar esta documentação quando a arquitetura mudar.

---

# 52. Fluxo oficial do MVP

```text
                         USUÁRIO
                            │
                            ▼
                    CONECTA CONTA
                            │
                            ▼
                          REACT
                            │
                            ▼
                         FASTAPI
                            │
                            ▼
                  SERVIÇO DE DESCOBERTA
                            │
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
                        REPOSITÓRIO
                            │
                            ▼
                          MYSQL
```

---

# 53. Arquitetura-alvo

O ViralCode deverá evoluir para:

```text
CONTA SOCIAL CONECTADA
          ↓
DESCOBERTA
          ↓
CONTEÚDOS
          ↓
MÉTRICAS
          ↓
INTELIGÊNCIA
          ↓
PADRÕES
          ↓
CRIAÇÃO
          ↓
PUBLICAÇÃO
          ↓
DESEMPENHO
          ↓
APRENDIZADO
```

Com múltiplas redes:

```text
                         VIRALCODE
                             │
                    CONECTOR DE REDE SOCIAL
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
          Instagram        TikTok        YouTube
              │              │              │
          Conta A         Conta B         Conta C
```

---

# 54. Critério para adicionar nova rede

Uma nova rede poderá ser adicionada quando existir:

- necessidade comercial;
- público relevante;
- mecanismo de acesso adequado;
- dados úteis;
- capacidade de integração sustentável.

Cada nova rede deverá possuir seu próprio conector.

---

# 55. Critério para alterar um conector

Uma alteração no conector deverá preservar:

```text
contrato interno
modelos de domínio
serviços
repositórios
```

sempre que possível.

Mudanças específicas da plataforma não devem contaminar o restante da arquitetura.

---

# 56. Regra de simplicidade do MVP

No MVP, implementar somente o necessário para validar:

```text
1 rede social
1 tipo principal de conta
1 fluxo de conexão
1 fluxo de descoberta
1 conjunto básico de métricas
1 persistência
```

A arquitetura deve estar preparada para crescer, mas a implementação inicial deve permanecer simples.

---

# 57. Regra final

> **O ViralCode acessa diretamente as redes sociais através de contas conectadas e transforma os dados obtidos em inteligência própria.**

A separação fundamental é:

```text
CONECTOR
→ acessa a rede social

SERVIÇO
→ aplica regras de negócio

REPOSITÓRIO
→ persiste dados

MOTOR DE INTELIGÊNCIA
→ analisa

MOTOR DE CRIAÇÃO
→ cria

MOTOR DE PUBLICAÇÃO
→ publica

MOTOR DE DESEMPENHO
→ mede

MOTOR DE APRENDIZADO
→ aprende
```

Essa separação deverá ser preservada durante toda a evolução do ViralCode.

**Versão:** 1.0  
**Status:** Arquitetura oficial de integração com redes sociais
