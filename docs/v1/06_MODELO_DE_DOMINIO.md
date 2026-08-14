# 06 — MODELO DE DOMÍNIO DO VIRALCODE

**Versão:** 0.1  
**Status:** Documento inicial  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo deste documento

Este documento define o vocabulário e as principais entidades de negócio do ViralCode.

O objetivo é garantir que todas as partes do sistema utilizem os mesmos conceitos.

Isso é especialmente importante porque o ViralCode deverá evoluir de um MVP simples para uma plataforma capaz de trabalhar com:

- diferentes nichos;
- diferentes perfis;
- diferentes plataformas;
- diferentes organizações;
- diferentes tipos de conteúdo;
- diferentes fontes de dados;
- inteligência de conteúdo;
- criação;
- publicação;
- desempenho.

A regra principal é:

> **O domínio deve ser genérico desde o início, mas a implementação do MVP deve continuar simples.**

---

# 2. Conceito central

O objeto central do ViralCode é o:

> **Conteúdo**

Porém, um conteúdo não existe isoladamente.

Ele está relacionado a:

```text
Organização
    ↓
Perfil
    ↓
Nicho
    ↓
Plataforma
    ↓
Autor
    ↓
Conteúdo
    ↓
Métricas
```

No futuro:

```text
Conteúdo
    ↓
Análise
    ↓
Padrões
    ↓
Criação
    ↓
Publicação
    ↓
Desempenho
```

---

# 3. Vocabulário oficial

Os principais termos do domínio são:

```text
Organização
Usuário
Perfil
Nicho
Plataforma
Conta Social
Autor
Conteúdo
Métrica
Busca
Análise
Padrão
Viral DNA
Ideia
Conteúdo Gerado
Publicação
Desempenho
Campanha
Agendamento
```

Nem todas essas entidades serão implementadas no MVP.

---

# 4. Organização

## Definição

Representa uma empresa, pessoa ou unidade que utiliza o ViralCode.

No futuro, será a principal unidade de isolamento do SaaS.

Exemplo:

```text
Organização
└── Leonardo Escrivani
```

Ou:

```text
Organização
└── Agência XYZ
```

---

## Dados futuros

Uma organização poderá possuir:

- identificador;
- nome;
- descrição;
- status;
- plano;
- configurações;
- data de criação.

---

## MVP

A organização completa não precisa ser implementada no primeiro MVP.

O modelo deve, entretanto, evitar decisões que impeçam sua inclusão futura.

---

# 5. Usuário

## Definição

Representa uma pessoa que acessa o ViralCode.

No futuro poderá pertencer a uma ou mais organizações conforme as regras de acesso.

---

## Dados futuros

- identificador;
- nome;
- e-mail;
- senha ou identidade externa;
- status;
- data de criação.

---

## MVP

Autenticação completa não é requisito do primeiro MVP, salvo necessidade de validação do produto.

---

# 6. Perfil

## Definição

Representa a identidade de conteúdo para a qual o ViralCode trabalha.

Um perfil não é necessariamente o usuário.

Exemplo:

```text
Usuário
   ↓
Organização
   ↓
Perfil Leonardo Escrivani
```

Outro exemplo:

```text
Organização
├── Perfil Leonardo
├── Perfil Fabi
└── Perfil Destrava Matemática
```

---

## Informações futuras

Um perfil poderá possuir:

- nome;
- descrição;
- nicho principal;
- público;
- posicionamento;
- tom de voz;
- objetivos;
- identidade visual;
- regras editoriais;
- instruções para IA;
- contas sociais.

---

# 7. Nicho

## Definição

Representa o mercado, assunto ou área temática na qual um perfil ou conteúdo está inserido.

Exemplos:

```text
Casamento
Fitness
Finanças
Educação
Marketing
Imóveis
Tecnologia
Beleza
Gastronomia
```

---

## Regra importante

O nicho é um dado.

Não deverá existir código específico para cada nicho.

Evitar:

```python
if nicho == "casamento":
    regra_especial()
```

como regra permanente do domínio.

---

# 8. Tema

## Definição

Representa um assunto específico dentro de um nicho.

Exemplo:

```text
Nicho:
Casamento

Temas:
- diálogo
- confiança
- traição
- intimidade
- conflitos
- rotina
```

Um conteúdo poderá possuir um ou mais temas.

---

# 9. Subtema

Representa uma especialização de um tema.

Exemplo:

```text
Nicho:
Casamento

Tema:
Diálogo

Subtemas:
- falta de conversa
- brigas
- comunicação emocional
- silêncio
```

Essa estrutura será mais relevante quando entrar a camada de inteligência.

---

# 10. Plataforma

## Definição

Representa uma rede social ou canal de distribuição.

Exemplos:

```text
Instagram
TikTok
YouTube
Facebook
LinkedIn
```

A plataforma deverá ser tratada como entidade/configuração e não como regra espalhada pelo sistema.

---

# 11. Conta Social

## Definição

Representa uma conta específica de uma plataforma.

Exemplo:

```text
Perfil:
Leonardo Escrivani

Conta Social:
Instagram @leonardoescrivani
```

Outro exemplo:

```text
Perfil:
Fabi

Conta Social:
Instagram @perfil_fabi
```

---

## Informações futuras

- identificador;
- plataforma;
- nome de usuário;
- identificador externo;
- credenciais/token;
- status;
- data de conexão;
- configurações.

---

# 12. Autor

## Definição

Representa quem publicou um conteúdo encontrado nas redes.

Importante:

> **Autor e Perfil do ViralCode não são necessariamente a mesma entidade.**

Exemplo:

```text
Perfil do ViralCode:
Leonardo Escrivani

Autor encontrado:
@outroperfil
```

Um autor pode existir no banco mesmo que não seja usuário do ViralCode.

---

# 13. Conteúdo

## Definição

Representa uma peça de conteúdo encontrada, criada ou publicada.

No MVP, o foco será principalmente conteúdo externo encontrado no Instagram.

Exemplos:

- Reel;
- vídeo;
- post;
- carrossel;
- publicação.

---

# 14. Identidade externa do conteúdo

Cada conteúdo encontrado deverá possuir, quando disponível:

```text
plataforma
+
identificador externo
```

Essa combinação será utilizada para ajudar na deduplicação.

Exemplo:

```text
Instagram
ID: 123456789
```

---

# 15. URL do conteúdo

O conteúdo deverá possuir a URL original quando disponível.

Essa URL permite:

- abrir o conteúdo;
- verificar a origem;
- acessar a publicação;
- fornecer referência ao usuário.

A URL não deve ser considerada necessariamente como o único identificador.

---

# 16. Tipo de conteúdo

O sistema deverá futuramente distinguir diferentes formatos.

Exemplos:

```text
Reel
Vídeo
Post
Carrossel
Story
Short
Live
```

No MVP, o foco inicial será:

> Reel do Instagram.

---

# 17. Legenda

Representa o texto associado ao conteúdo quando disponível.

Pode ser utilizada futuramente para:

- análise;
- classificação;
- busca;
- inteligência;
- geração de conteúdo.

---

# 18. Mídia

Representa o recurso visual ou audiovisual associado ao conteúdo.

Poderá futuramente incluir:

- vídeo;
- imagem;
- áudio;
- miniatura;
- capa.

No MVP, não é obrigatório armazenar o arquivo original.

Podemos armazenar apenas uma referência ou URL quando disponível e permitido.

---

# 19. Métrica

## Definição

Representa um valor quantitativo observado sobre um conteúdo.

Exemplos:

```text
Visualizações
Curtidas
Comentários
Compartilhamentos
Salvamentos
Alcance
```

---

# 20. Visualizações

Representa o número de visualizações observado.

No MVP, será a métrica principal utilizada no filtro e ranking.

Exemplo:

```text
visualizações >= 1.000.000
```

---

# 21. Data da coleta

Cada métrica deverá, quando possível, possuir a data em que foi observada.

Isso é importante porque as métricas mudam.

Exemplo:

```text
Conteúdo:
123

Coleta:
13/08/2026 10:00
Visualizações:
1.200.000
```

Posteriormente:

```text
13/08/2026 18:00
Visualizações:
1.850.000
```

---

# 22. Histórico de métricas

O histórico permite acompanhar evolução.

Estrutura conceitual:

```text
Conteúdo
   ↓
Métricas
   ├── momento 1
   ├── momento 2
   ├── momento 3
   └── momento 4
```

No MVP, o histórico pode ser simples.

No futuro será importante para calcular velocidade de crescimento.

---

# 23. Busca

## Definição

Representa uma pesquisa realizada no ViralCode.

Exemplo:

```text
Termo:
casamento

Plataforma:
Instagram

Visualizações mínimas:
1.000.000

Período:
90 dias
```

Uma busca poderá gerar vários resultados.

---

# 24. Resultado de busca

Um resultado de busca representa a relação entre:

```text
Busca
+
Conteúdo
```

O mesmo conteúdo poderá aparecer em várias buscas.

Por isso não devemos duplicar o conteúdo simplesmente porque ele apareceu novamente.

---

# 25. Análise

## Definição futura

Representa uma interpretação estruturada de um conteúdo.

Poderá conter:

- tema;
- subtema;
- hook;
- emoção;
- estrutura;
- CTA;
- público;
- intenção;
- características;
- classificação.

---

# 26. Padrão

## Definição futura

Representa uma característica recorrente encontrada em vários conteúdos.

Exemplo:

```text
Padrão:
Pergunta provocativa nos primeiros segundos.
```

Um padrão deverá ser associado a vários conteúdos quando houver evidência.

---

# 27. Viral DNA

## Definição futura

Representa o conjunto estruturado de características de um conteúdo.

Exemplo:

```text
Viral DNA
│
├── Tema
├── Hook
├── Dor
├── Desejo
├── Emoção
├── Estrutura
├── CTA
├── Formato
└── Público
```

Não faz parte do MVP inicial.

---

# 28. Ideia

## Definição futura

Representa uma proposta de conteúdo antes da produção.

Exemplo:

```text
Ideia:
"5 sinais de que o casal parou de conversar."
```

Uma ideia poderá surgir de:

- análise de conteúdo;
- padrão;
- comentário;
- tendência;
- sugestão da IA;
- usuário.

---

# 29. Conteúdo Gerado

## Definição futura

Representa um conteúdo criado pelo ViralCode ou pelo usuário com apoio da plataforma.

Poderá conter:

- hook;
- roteiro;
- legenda;
- CTA;
- instruções de gravação;
- mídia;
- versão por plataforma.

---

# 30. Publicação

## Definição futura

Representa uma tentativa ou resultado de publicar um conteúdo em uma plataforma.

Exemplo:

```text
Conteúdo
   ↓
Publicação
   ↓
Instagram
```

Uma mesma peça poderá ter várias publicações.

---

# 31. Desempenho

## Definição futura

Representa os resultados obtidos por um conteúdo após publicação.

Poderá reunir:

- visualizações;
- curtidas;
- comentários;
- compartilhamentos;
- salvamentos;
- alcance;
- retenção;
- conversões.

---

# 32. Campanha

## Definição futura

Representa um conjunto organizado de conteúdos com objetivo comum.

Exemplo:

```text
Campanha:
21 Dias para Reacender o Amor

Conteúdos:
1
2
3
...
21
```

Não faz parte do MVP.

---

# 33. Agendamento

## Definição futura

Representa a programação de uma publicação para uma data e horário.

Exemplo:

```text
Conteúdo:
123

Plataforma:
Instagram

Data:
20/08/2026

Hora:
19:00
```

Não faz parte do MVP.

---

# 34. Relacionamentos principais

A visão futura do domínio pode ser representada:

```text
ORGANIZAÇÃO
     │
     ├────────────── USUÁRIOS
     │
     └────────────── PERFIS
                       │
                       ├──────── NICHO
                       │
                       └──────── CONTAS SOCIAIS
                                      │
                                      └──── PLATAFORMA


PLATAFORMA
     │
     └──── CONTEÚDOS
                │
                ├──── AUTOR
                │
                ├──── MÉTRICAS
                │
                ├──── TEMAS
                │
                ├──── ANÁLISES
                │
                └──── PADRÕES
```

---

# 35. Relação entre busca e conteúdo

```text
BUSCA
  │
  ├── parâmetros
  │
  └── resultados
          │
          ├── Conteúdo A
          ├── Conteúdo B
          ├── Conteúdo C
          └── Conteúdo D
```

O conteúdo é independente da busca.

Isso é fundamental.

---

# 36. Relação entre conteúdo e autor

```text
AUTOR
  │
  ├── Conteúdo A
  ├── Conteúdo B
  └── Conteúdo C
```

Um autor pode possuir muitos conteúdos.

Um conteúdo pertence a um autor quando essa informação estiver disponível.

---

# 37. Relação entre conteúdo e métricas

```text
CONTEÚDO
   │
   └── MÉTRICAS
        ├── coleta 1
        ├── coleta 2
        ├── coleta 3
        └── coleta 4
```

Isso permite evolução futura.

---

# 38. Relação entre conteúdo e análise

```text
CONTEÚDO
   │
   └── ANÁLISE
        ├── tema
        ├── hook
        ├── emoção
        ├── estrutura
        └── CTA
```

---

# 39. Relação entre análise e padrão

```text
Conteúdos
   ↓
Análises individuais
   ↓
Comparação
   ↓
Padrões
```

Um padrão poderá ser identificado somente quando houver dados suficientes.

---

# 40. Modelo mínimo do MVP

O domínio do MVP deverá ser muito menor:

```text
BUSCA
  │
  └──── CONTEÚDOS
            │
            ├──── AUTOR
            │
            └──── MÉTRICAS
```

Não precisamos implementar todas as entidades futuras.

---

# 41. Entidades prioritárias do MVP

### P0

```text
Conteúdo
Autor
Métrica
Busca
```

### P1

```text
Tema
Plataforma
```

### P2

```text
Perfil
Conta Social
```

### P3

```text
Organização
Usuário
Análise
Padrão
Viral DNA
Ideia
Conteúdo Gerado
Publicação
Desempenho
Campanha
Agendamento
```

A prioridade poderá mudar conforme a evolução do produto.

---

# 42. Regras de domínio

## Regra 1

Um conteúdo deve possuir uma identificação externa quando disponível.

## Regra 2

Um conteúdo não deve ser duplicado apenas porque apareceu em outra busca.

## Regra 3

Uma busca pode retornar muitos conteúdos.

## Regra 4

Um conteúdo pode aparecer em muitas buscas.

## Regra 5

Métricas são observações e podem mudar ao longo do tempo.

## Regra 6

Autor não é necessariamente usuário do ViralCode.

## Regra 7

Perfil do ViralCode não é necessariamente o autor de um conteúdo externo.

## Regra 8

Nicho é dado de domínio, não regra fixa no código.

## Regra 9

Plataforma deve ser tratada de forma abstrata.

## Regra 10

Análises de IA não devem ser confundidas com fatos observados.

---

# 43. Dados observados versus inferências

O domínio deverá diferenciar:

### Dado observado

Exemplo:

```text
Visualizações:
1.850.000
```

### Dado calculado

Exemplo:

```text
Taxa de crescimento:
15% por hora
```

### Inferência

Exemplo:

```text
O conteúdo utiliza forte apelo emocional.
```

### Hipótese

Exemplo:

```text
O hook pode ter contribuído para o desempenho.
```

Essa distinção será importante para a confiabilidade do produto.

---

# 44. Conteúdo externo versus conteúdo próprio

No futuro, o sistema deverá distinguir:

```text
Conteúdo externo
```

de:

```text
Conteúdo criado pelo usuário
```

e:

```text
Conteúdo publicado pelo ViralCode
```

Conceitualmente:

```text
ORIGEM
├── EXTERNO
├── USUÁRIO
└── VIRALCODE
```

Isso permitirá análises diferentes.

---

# 45. Estado do conteúdo

No futuro, conteúdos criados poderão possuir estados.

Exemplo:

```text
IDEIA
 ↓
ROTEIRO
 ↓
EM PRODUÇÃO
 ↓
APROVADO
 ↓
AGENDADO
 ↓
PUBLICADO
 ↓
ANALISADO
```

Essa estrutura pertence ao futuro motor de criação/publicação.

---

# 46. Identificadores

As entidades deverão possuir identificadores internos próprios.

Quando houver um identificador externo da plataforma, ele deverá ser armazenado separadamente.

Exemplo conceitual:

```text
id_interno
id_externo
plataforma
```

Não utilizar o identificador externo como chave primária universal do sistema.

---

# 47. Datas

As entidades deverão possuir datas relevantes quando aplicável.

Diferenciar:

```text
data_publicacao
data_coleta
data_atualizacao
data_criacao
```

Não utilizar uma única coluna genérica para representar eventos diferentes.

---

# 48. Status

Entidades que possuam ciclo de vida poderão ter estados controlados.

Exemplo futuro:

```text
ATIVO
INATIVO
PROCESSANDO
CONCLUIDO
ERRO
```

Os estados deverão ser definidos por domínio.

Evitar strings livres quando uma enumeração controlada for apropriada.

---

# 49. Multi-plataforma

Um conteúdo pertence a uma plataforma específica.

O modelo deverá permitir que diferentes plataformas tenham atributos diferentes sem obrigar o núcleo do domínio a conhecer todos os detalhes de cada rede.

Exemplo:

```text
Conteúdo
   │
   └── Plataforma
          ├── Instagram
          ├── TikTok
          └── YouTube
```

---

# 50. Multi-nicho

Um conteúdo poderá futuramente estar relacionado a:

- um nicho principal;
- temas;
- subtemas;
- múltiplas classificações.

Não devemos limitar o domínio a "um nicho para sempre" sem necessidade.

---

# 51. Modelo conceitual completo

```text
                           ORGANIZAÇÃO
                                │
                    ┌───────────┴───────────┐
                    │                       │
                 USUÁRIOS                PERFIS
                                            │
                                  ┌─────────┴─────────┐
                                  │                   │
                                NICHO           CONTAS SOCIAIS
                                                      │
                                                  PLATAFORMAS


                         CONTEÚDO EXTERNO
                                │
             ┌──────────────────┼──────────────────┐
             │                  │                  │
           AUTOR            MÉTRICAS            TEMAS
                                │
                           HISTÓRICO
                                │
                            ANÁLISE
                                │
                         VIRAL DNA
                                │
                            PADRÕES
                                │
                              IDEIAS
                                │
                        CONTEÚDO GERADO
                                │
                           PUBLICAÇÃO
                                │
                          DESEMPENHO
                                │
                           APRENDIZADO
```

---

# 52. Implementação gradual

O modelo conceitual é grande porque representa a visão do produto.

A implementação deverá começar pequena.

### MVP

```text
Busca
Conteúdo
Autor
Métrica
```

### Depois

```text
Plataforma
Tema
Perfil
```

### Depois

```text
Análise
Viral DNA
Padrões
```

### Depois

```text
Ideia
Conteúdo Gerado
Publicação
Desempenho
```

### Produto maduro

```text
Organização
Usuários
Equipes
Campanhas
Agendamento
Aprendizado
SaaS
```

---

# 53. Regra para agentes de inteligência artificial

Antes de criar uma nova entidade, o agente deverá verificar:

1. ela já existe neste modelo?
2. é realmente uma entidade ou apenas um atributo?
3. precisa ser persistida?
4. é necessária no MVP?
5. pode ser adicionada posteriormente?
6. cria duplicação conceitual?

Não criar tabelas ou classes apenas porque uma funcionalidade futura poderá existir.

---

# 54. Regra de nomenclatura

Todo o domínio deverá utilizar português.

Exemplos:

```text
Conteudo
Autor
Metrica
Busca
Perfil
Nicho
Plataforma
Analise
Padrao
Publicacao
```

No banco:

```text
conteudos
autores
metricas
buscas
perfis
nichos
plataformas
analises
padroes
publicacoes
```

---

# 55. Regra final

> **O modelo de domínio deve representar o negócio, não a tecnologia utilizada para implementá-lo.**

O ViralCode poderá mudar:

- provedor;
- framework;
- banco;
- plataforma;
- modelo de IA.

Mas os conceitos centrais do negócio deverão permanecer claros.

A entidade mais importante do domínio inicial é:

> **Conteúdo.**

E o relacionamento fundamental que o MVP precisa provar é:

```text
Busca
  ↓
Conteúdos relevantes
  ↓
Métricas
  ↓
Valor para o usuário
```

**Versão atual:** 0.1  
**Status:** Modelo de domínio inicial do ViralCode
