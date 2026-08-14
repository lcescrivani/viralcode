# 14 — MOTOR DE DESEMPENHO

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

O Motor de Desempenho será responsável por coletar, organizar e interpretar as métricas dos conteúdos publicados pelo ViralCode.

Seu objetivo é responder:

> **O que aconteceu depois que o conteúdo foi publicado?**

O fluxo será:

```text
CONTEÚDO
   ↓
PUBLICAÇÃO
   ↓
REDE SOCIAL
   ↓
MÉTRICAS
   ↓
MOTOR DE DESEMPENHO
   ↓
INDICADORES
   ↓
MOTOR DE INTELIGÊNCIA
   ↓
NOVOS APRENDIZADOS
```

---

# 2. Princípio fundamental

O Motor de Desempenho deverá separar:

```text
DADO COLETADO
```

de:

```text
INTERPRETAÇÃO
```

Exemplo:

```text
Dado:
1.200.000 visualizações

Interpretação:
conteúdo teve alto alcance
```

A interpretação estratégica pertence ao Motor de Inteligência.

---

# 3. Responsabilidades

O Motor de Desempenho será responsável por:

- identificar publicações monitoradas;
- consultar métricas disponíveis;
- armazenar histórico;
- normalizar métricas;
- calcular indicadores derivados;
- comparar períodos;
- registrar evolução;
- disponibilizar dados para análise;
- informar falhas de coleta.

---

# 4. O que não pertence ao Motor de Desempenho

Não deverá ser responsabilidade dele:

```text
criar conteúdo
publicar conteúdo
definir estratégia
interpretar padrões de conteúdo
gerar roteiros
```

Essas funções pertencem a outros componentes.

---

# 5. Origem das métricas

As métricas deverão ser obtidas através dos conectores das redes sociais.

Arquitetura:

```text
Instagram
   ↓
ConectorInstagram
   ↓
Métricas
   ↓
Motor de Desempenho
   ↓
Banco de Dados
```

O Motor de Desempenho não deverá acessar diretamente a rede social.

---

# 6. Relação com a publicação

Cada publicação deverá possuir relação com suas métricas.

Exemplo:

```text
Publicação
   ↓
Conteúdo
   ↓
Instagram
   ↓
Métricas
```

Isso permitirá identificar exatamente qual publicação gerou cada conjunto de dados.

---

# 7. Métricas básicas

O MVP deverá priorizar métricas que estejam efetivamente disponíveis para a conta e a plataforma.

Exemplos:

```text
visualizações
curtidas
comentários
compartilhamentos
salvamentos
```

Nem todas as métricas estarão disponíveis em todas as plataformas.

---

# 8. Regra sobre dados indisponíveis

O sistema não deverá inventar métricas.

Se uma métrica não estiver disponível:

```text
NULL
```

ou ausência controlada.

Não transformar automaticamente:

```text
desconhecido
```

em:

```text
0
```

---

# 9. Histórico

O Motor de Desempenho deverá ser preparado para registrar várias medições do mesmo conteúdo.

Exemplo:

```text
Conteúdo ABC

10:00 → 100.000 visualizações
14:00 → 180.000 visualizações
18:00 → 310.000 visualizações
22:00 → 500.000 visualizações
```

Isso permite acompanhar evolução.

---

# 10. Snapshot de métricas

Cada coleta poderá representar um snapshot.

Modelo conceitual:

```text
MetricasPublicacao
├── id
├── publicacao_id
├── coletado_em
├── visualizacoes
├── curtidas
├── comentarios
├── compartilhamentos
└── salvamentos
```

---

# 11. Crescimento

A partir do histórico será possível calcular:

```text
crescimento_absoluto
```

Exemplo:

```text
500.000 - 310.000
=
190.000 novas visualizações
```

---

# 12. Crescimento percentual

Exemplo:

```text
(500.000 - 310.000) / 310.000
```

O sistema deverá tratar divisão por zero e ausência de histórico.

---

# 13. Velocidade

Quando existirem horários suficientes:

```text
novas_visualizações
÷
tempo
```

Exemplo:

```text
190.000 visualizações
em 4 horas

= 47.500 visualizações/hora
```

Essa métrica será útil para entender tração.

---

# 14. Aceleração

Futuramente poderá ser calculada a variação da velocidade.

```text
Velocidade 1
   ↓
Velocidade 2
   ↓
Aceleração
```

Não é requisito do MVP.

---

# 15. Engajamento

Poderão ser calculadas taxas derivadas.

Exemplo:

```text
taxa_curtidas =
curtidas / visualizacoes
```

Outros indicadores:

```text
taxa_comentarios
taxa_compartilhamentos
taxa_salvamentos
```

A fórmula definitiva deverá ser documentada antes de ser utilizada como indicador oficial.

---

# 16. Comparação entre conteúdos

O Motor deverá permitir comparar conteúdos.

Exemplo:

```text
Conteúdo A
1.000.000 visualizações

Conteúdo B
350.000 visualizações
```

A comparação poderá considerar:

```text
tema
formato
hook
data
perfil
plataforma
métricas
```

A interpretação desses fatores pertence ao Motor de Inteligência.

---

# 17. Comparação entre períodos

Futuramente:

```text
Semana 1
versus
Semana 2
```

Indicadores:

```text
total de publicações
visualizações
engajamento
crescimento
média por conteúdo
```

---

# 18. Desempenho por perfil

O sistema deverá permitir:

```text
Perfil
   ↓
Publicações
   ↓
Métricas
```

Isso permitirá descobrir quais estratégias funcionam melhor para cada perfil.

---

# 19. Desempenho por nicho

Também poderá existir comparação:

```text
Nicho
   ↓
Conteúdos
   ↓
Métricas
```

O sistema deverá separar:

```text
padrão geral do nicho
```

de:

```text
resultado específico do perfil
```

---

# 20. Desempenho por tema

Exemplo:

```text
Diálogo
→ média de 400 mil visualizações

Intimidade
→ média de 700 mil

Conflitos
→ média de 1,1 milhão
```

Esses dados poderão alimentar o Motor de Inteligência.

---

# 21. Desempenho por formato

Exemplo:

```text
Reel falando para câmera
Reel storytelling
Carrossel
Post
```

O sistema poderá comparar resultados.

---

# 22. Desempenho por padrão

Uma das funções estratégicas será relacionar:

```text
padrão identificado
        ↓
conteúdo criado
        ↓
publicação
        ↓
desempenho
```

Exemplo:

```text
Padrão:
hook em pergunta

Conteúdos:
A
B
C

Desempenho:
A → 800k
B → 1,2M
C → 300k
```

Isso permite verificar o comportamento real do padrão no perfil.

---

# 23. Feedback para a inteligência

O Motor de Desempenho alimentará o Motor de Inteligência.

```text
Motor de Desempenho
        ↓
Dados reais
        ↓
Motor de Inteligência
        ↓
Aprendizados
```

Essa conexão é fundamental para o ciclo do ViralCode.

---

# 24. Feedback para criação

O resultado poderá posteriormente influenciar o Motor de Criação.

```text
Conteúdo criado
     ↓
Publicado
     ↓
Desempenho
     ↓
Aprendizado
     ↓
Nova criação
```

---

# 25. Identificador da publicação

Toda coleta deverá estar vinculada a:

```text
publicacao_id
```

Quando disponível, também:

```text
identificador_externo
```

Isso permite relacionar o dado interno ao conteúdo publicado na plataforma.

---

# 26. Conta social

As métricas deverão estar associadas à conta social utilizada na publicação.

Exemplo:

```text
Perfil ViralCode
      ↓
Conta Instagram
      ↓
Publicação
      ↓
Métricas
```

---

# 27. Data de coleta

Não confundir:

```text
data_publicacao
```

com:

```text
data_coleta_metricas
```

Exemplo:

```text
Publicação:
10/08/2026

Coleta:
11/08/2026
```

Ambas são importantes.

---

# 28. Métrica atual versus histórico

A interface poderá apresentar:

```text
Atual:
1.500.000 visualizações
```

e também:

```text
Histórico:
100k → 400k → 900k → 1,5M
```

---

# 29. Coleta periódica futura

No futuro, o sistema poderá coletar métricas automaticamente.

Exemplo:

```text
Publicação
   ↓
Coleta inicial
   ↓
+1 hora
   ↓
+6 horas
   ↓
+24 horas
   ↓
+7 dias
```

A frequência deverá ser definida conforme necessidade e limites da plataforma.

---

# 30. MVP

No MVP, a coleta poderá ser simples.

Fluxo:

```text
Publicação
   ↓
Usuário solicita atualização
   ↓
Conector Instagram
   ↓
Métricas
   ↓
Banco
```

Não é obrigatório implementar monitoramento automático no primeiro momento.

---

# 31. O que NÃO fazer no MVP

Não implementar inicialmente:

```text
streaming de métricas
monitoramento em tempo real
machine learning próprio
previsão automática
alertas complexos
benchmark avançado
múltiplas redes
```

Essas funções podem ser adicionadas depois da validação do negócio.

---

# 32. Benchmark futuro

Futuramente o ViralCode poderá comparar:

```text
Perfil
versus
Nicho
```

ou:

```text
Conteúdo
versus
conteúdos semelhantes
```

O benchmark deverá ser apresentado como comparação estatística, não como garantia de desempenho.

---

# 33. Métrica de referência

Futuramente poderão existir métricas como:

```text
mediana de visualizações
percentil
média
crescimento médio
taxa média de engajamento
```

A mediana poderá ser especialmente útil para reduzir distorções causadas por poucos conteúdos extremamente virais.

---

# 34. Outliers

Um conteúdo com desempenho excepcional poderá distorcer médias.

Exemplo:

```text
100k
120k
150k
200k
10M
```

A média poderá não representar bem o conjunto.

O sistema deverá considerar medidas robustas quando necessário.

---

# 35. Janela de análise

O desempenho poderá ser analisado em janelas.

Exemplo:

```text
1 hora
6 horas
24 horas
7 dias
30 dias
```

A janela deverá ser registrada claramente.

---

# 36. Desempenho absoluto versus relativo

Exemplo:

```text
1 milhão de visualizações
```

é desempenho absoluto.

Já:

```text
3x a média do perfil
```

é desempenho relativo.

O segundo pode ser mais útil para comparar perfis de tamanhos diferentes.

---

# 37. Score futuro

Futuramente poderá existir:

```text
score_desempenho
```

com base em múltiplos indicadores.

No MVP, evitar um score complexo sem dados suficientes.

---

# 38. Ranking

O Motor poderá produzir rankings internos.

Exemplo:

```text
1º Conteúdo A
2º Conteúdo B
3º Conteúdo C
```

Critério inicial:

```text
visualizações
```

No futuro:

```text
score de desempenho
```

---

# 39. Relatórios

O sistema poderá futuramente gerar:

```text
Resumo diário
Resumo semanal
Resumo mensal
```

Com:

```text
conteúdos publicados
melhores conteúdos
piores conteúdos
crescimento
temas
formatos
padrões
```

A geração de relatórios poderá ser responsabilidade de outro módulo de apresentação.

---

# 40. Dados para dashboard

O Motor deverá fornecer dados estruturados para o frontend.

Exemplo:

```text
Total de visualizações
Publicações
Média
Mediana
Melhor conteúdo
Crescimento
```

O React deverá apenas apresentar esses dados.

---

# 41. Não colocar regras no frontend

Evitar:

```text
React
 ↓
calcula regras estratégicas
```

Preferir:

```text
FastAPI
 ↓
Serviço de Desempenho
 ↓
Resultado pronto
 ↓
React
```

---

# 42. API

O backend poderá possuir endpoints conceituais:

```text
GET /desempenho/publicacoes/{id}

GET /desempenho/perfis/{id}

POST /desempenho/publicacoes/{id}/atualizar

GET /desempenho/conteudos/{id}/historico
```

Os nomes definitivos deverão seguir o padrão de nomenclatura da API do projeto.

---

# 43. Serviço

Exemplo conceitual:

```python
class ServicoDesempenho:
    def atualizar_metricas(self, publicacao_id):
        ...
```

O serviço não deverá chamar diretamente o Instagram.

Deverá utilizar o conector.

---

# 44. Conector

Exemplo conceitual:

```python
class ConectorInstagram:
    def obter_metricas_publicacao(self, publicacao):
        ...
```

O conector traduz a operação para os mecanismos disponíveis na plataforma.

---

# 45. Persistência

O repositório deverá cuidar do banco.

Exemplo:

```python
class RepositorioMetricas:
    def salvar_snapshot(self, metricas):
        ...
```

O serviço não deverá conhecer detalhes de SQL.

---

# 46. Separação de responsabilidades

```text
FastAPI
   ↓
ServicoDesempenho
   ↓
ConectorRedeSocial
   ↓
Instagram
```

Persistência:

```text
ServicoDesempenho
   ↓
RepositorioMetricas
   ↓
SQLAlchemy
   ↓
MySQL
```

---

# 47. Tratamento de erros

O sistema deverá distinguir:

```text
ERRO_AUTENTICACAO
ERRO_PERMISSAO
ERRO_REDE
ERRO_TIMEOUT
ERRO_DADO_INDISPONIVEL
ERRO_PLATAFORMA
ERRO_DESCONHECIDO
```

---

# 48. Dados indisponíveis na plataforma

Não assumir que toda métrica existente no aplicativo estará disponível para integração.

Antes de utilizar uma métrica:

```text
A plataforma fornece?
        ↓
A conta possui acesso?
        ↓
A aplicação possui permissão?
        ↓
O conector consegue obter?
```

Somente então registrar como métrica disponível.

---

# 49. Segurança

O Motor de Desempenho não deverá manipular diretamente:

```text
senha
segredo
token exposto
```

O acesso deverá ocorrer através da conta social conectada e do conector.

---

# 50. Testes

Devem existir testes para:

```text
métrica válida
métrica ausente
conta desconectada
erro de permissão
timeout
erro de plataforma
histórico
crescimento
taxas
duplicidade
```

---

# 51. Testes sem Instagram real

Utilizar conector falso:

```text
Teste
 ↓
ServicoDesempenho
 ↓
Conector falso
 ↓
Métricas simuladas
```

Isso permite testar os cálculos sem depender da rede social.

---

# 52. Idempotência

Coletar a mesma métrica duas vezes não deverá criar registros inconsistentes.

O sistema deverá possuir uma estratégia para identificar snapshots ou atualizações equivalentes.

---

# 53. Integridade temporal

O sistema deverá preservar:

```text
quando o conteúdo foi publicado
```

e:

```text
quando a métrica foi coletada
```

Não sobrescrever o histórico sem necessidade.

---

# 54. Aprendizado

O Motor de Desempenho não deverá decidir sozinho:

```text
"esse hook é melhor"
```

Ele fornece evidências:

```text
hook A
→ desempenho

hook B
→ desempenho
```

O Motor de Inteligência interpreta esses dados.

---

# 55. Ciclo de aprendizado

```text
DESCOBERTA
    ↓
INTELIGÊNCIA
    ↓
CRIAÇÃO
    ↓
PUBLICAÇÃO
    ↓
DESEMPENHO
    ↓
INTELIGÊNCIA
    ↓
NOVA CRIAÇÃO
```

Esse ciclo é uma das principais vantagens arquiteturais do ViralCode.

---

# 56. Evolução futura

### Fase 1

```text
Coleta manual
```

### Fase 2

```text
Coleta automática
```

### Fase 3

```text
Histórico e crescimento
```

### Fase 4

```text
Comparações
```

### Fase 5

```text
Benchmark
```

### Fase 6

```text
Predições e recomendações
```

As fases posteriores somente deverão ser implementadas depois que houver dados suficientes.

---

# 57. Critério de sucesso do MVP

O Motor de Desempenho será considerado funcional quando o ViralCode conseguir:

> **publicar um conteúdo no Instagram, obter as métricas disponíveis, armazená-las com histórico e disponibilizar os dados para análise posterior.**

---

# 58. Regra para agentes de IA

Antes de modificar o Motor de Desempenho:

1. ler este documento;
2. verificar o modelo de publicação;
3. verificar o conector da rede social;
4. não acessar diretamente a plataforma dentro do serviço;
5. preservar histórico;
6. não inventar métricas;
7. separar coleta de interpretação;
8. criar testes;
9. respeitar permissões;
10. atualizar a documentação quando a arquitetura mudar.

---

# 59. Arquitetura do Motor de Desempenho

```text
                    PUBLICAÇÃO
                        │
                        ▼
                 MOTOR DE DESEMPENHO
                        │
                        ▼
                CONECTOR DA REDE SOCIAL
                        │
                        ▼
                     INSTAGRAM
                        │
                        ▼
                     MÉTRICAS
                        │
                        ▼
                  NORMALIZAÇÃO
                        │
                        ▼
                  SNAPSHOT / HISTÓRICO
                        │
                        ▼
                    MYSQL
                        │
                        ▼
              ┌─────────┴─────────┐
              ▼                   ▼
        DASHBOARD           INTELIGÊNCIA
                                  │
                                  ▼
                               CRIAÇÃO
```

---

# 60. Arquitetura-alvo do ViralCode

```text
                         REDE SOCIAL
                              │
                              ▼
                           CONECTOR
                              │
                              ▼
                         DESCOBERTA
                              │
                              ▼
                         BANCO DE DADOS
                              │
                              ▼
                    MOTOR DE INTELIGÊNCIA
                              │
                         PADRÕES / INSIGHTS
                              │
                              ▼
                       MOTOR DE CRIAÇÃO
                              │
                              ▼
                           CONTEÚDO
                              │
                              ▼
                           APROVAÇÃO
                              │
                              ▼
                    MOTOR DE PUBLICAÇÃO
                              │
                              ▼
                         REDE SOCIAL
                              │
                              ▼
                    MOTOR DE DESEMPENHO
                              │
                              ▼
                    MOTOR DE INTELIGÊNCIA
```

---

# 61. Regra final

> **O Motor de Desempenho transforma o resultado das publicações em dados históricos confiáveis para que o ViralCode possa aprender com aquilo que realmente aconteceu.**

A separação deverá permanecer:

```text
CONECTOR
→ acessa a rede social

MOTOR DE PUBLICAÇÃO
→ publica

MOTOR DE DESEMPENHO
→ coleta e organiza métricas

MOTOR DE INTELIGÊNCIA
→ interpreta

MOTOR DE CRIAÇÃO
→ cria

MOTOR DE APRENDIZADO FUTURO
→ evolui as recomendações
```

**Versão:** 1.0  
**Status:** Documento oficial do Motor de Desempenho
