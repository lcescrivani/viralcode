# 17 — DEFINIÇÃO OFICIAL DO MVP

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

Este documento define oficialmente o escopo do MVP do ViralCode.

O objetivo é impedir que o projeto cresça em complexidade antes da validação do negócio.

A regra principal é:

> **Construir o mínimo necessário para provar que existe valor real em descobrir oportunidades de conteúdo, transformar inteligência em conteúdo e acompanhar o resultado.**

---

# 2. O problema que o MVP deve validar

O ViralCode deverá validar se existe valor em oferecer ao usuário um fluxo integrado para:

```text
DESCUBRIR
   ↓
ANALISAR
   ↓
ENTENDER
   ↓
CRIAR
   ↓
PUBLICAR
   ↓
MEDIR
```

A partir dos resultados:

```text
APRENDER
   ↓
CRIAR MELHOR
```

---

# 3. Hipótese principal do negócio

A hipótese que o MVP deverá testar é:

> **Criadores e profissionais de conteúdo podem obter valor significativo ao utilizar dados e padrões de conteúdos de alto desempenho para orientar a criação de novos conteúdos.**

O MVP deverá fornecer evidências para validar ou rejeitar essa hipótese.

---

# 4. Primeira plataforma

A primeira rede social do ViralCode será:

```text
Instagram
```

Não implementar outras redes no MVP.

Futuras plataformas:

```text
TikTok
YouTube
outras
```

serão adicionadas posteriormente.

---

# 5. Público inicial

O MVP deverá ser estruturado para permitir diferentes nichos.

O primeiro caso de uso poderá utilizar:

```text
Nicho:
Casamento
```

Mas o código não deverá ser construído especificamente para casamento.

A arquitetura deverá trabalhar com:

```text
nicho
perfil
tema
público
objetivo
```

---

# 6. Perfil

O conceito de perfil será central.

Um perfil representa uma identidade editorial dentro do ViralCode.

Exemplo:

```text
Perfil
├── nome
├── nicho
├── público
├── posicionamento
├── tom de voz
├── objetivos
└── regras editoriais
```

O sistema deverá ser preparado para mais de um perfil no futuro.

No MVP, poderá existir inicialmente apenas um perfil por usuário.

---

# 7. Conta social

O perfil poderá possuir uma conta social conectada.

No MVP:

```text
Perfil
   ↓
Conta Instagram
```

A arquitetura deverá permitir futuramente:

```text
Perfil
   ├── Instagram
   ├── TikTok
   └── YouTube
```

---

# 8. Descoberta

A descoberta será uma das funções estratégicas do produto.

O usuário deverá informar critérios como:

```text
nicho
tema
palavra-chave
período
mínimo de visualizações
```

Exemplo:

```json
{
  "nicho": "casamento",
  "tema": "dialogo",
  "visualizacoes_minimas": 1000000
}
```

O sistema deverá então utilizar os recursos de descoberta efetivamente disponíveis para o Instagram.

---

# 9. Limitação importante da descoberta

O MVP não deverá assumir que o Instagram disponibiliza diretamente uma operação equivalente a:

```text
"retorne todos os Reels públicos
sobre casamento
com mais de 1 milhão de visualizações"
```

A capacidade real deverá ser validada antes da implementação definitiva da descoberta.

A estratégia oficial de descoberta deverá ser documentada separadamente no documento de integração/descoberta do Instagram.

---

# 10. Resultado da descoberta

Quando os dados estiverem disponíveis, o ViralCode deverá normalizar os resultados para um modelo interno.

Exemplo:

```text
Conteúdo
├── plataforma
├── identificador externo
├── autor
├── URL
├── tipo
├── legenda
├── data
└── métricas disponíveis
```

---

# 11. Armazenamento

Os dados deverão ser armazenados no:

```text
MySQL
```

Utilizando:

```text
SQLAlchemy
```

Arquitetura:

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

---

# 12. Motor de Inteligência

O MVP deverá possuir um Motor de Inteligência capaz de transformar dados coletados em informações úteis.

Primeira versão:

```text
Conteúdos
   ↓
Métricas
   ↓
Padrões
   ↓
Insights
```

Não implementar inteligência excessivamente complexa no primeiro momento.

---

# 13. O que o Motor de Inteligência deverá analisar

Priorizar:

```text
tema
formato
hook
estrutura
emoção
CTA
visualizações
engajamento
```

A disponibilidade de cada métrica dependerá da plataforma.

---

# 14. Motor de Criação

O MVP deverá permitir transformar inteligência em conteúdo.

Fluxo:

```text
Padrões
   ↓
Insights
   ↓
Contexto do perfil
   ↓
Motor de Criação
   ↓
Conteúdo
```

O conteúdo deverá ser original.

O sistema não deverá simplesmente copiar conteúdos encontrados.

---

# 15. Formato inicial

O MVP deverá priorizar:

```text
Reel
```

Outros formatos poderão existir na arquitetura, mas não precisam ser implementados imediatamente.

---

# 16. Geração

O primeiro caso de uso poderá gerar múltiplas opções.

Exemplo:

```text
Tema:
diálogo

Opção 1
Opção 2
Opção 3
```

O usuário escolhe a opção que deseja utilizar.

---

# 17. Aprovação

O MVP deverá possuir aprovação humana.

Fluxo:

```text
IA gera
   ↓
Rascunho
   ↓
Usuário revisa
   ↓
Aprova
```

Nenhum conteúdo deverá ser publicado automaticamente sem aprovação explícita no MVP.

---

# 18. Motor de Publicação

O MVP deverá possuir capacidade de publicação no Instagram, dentro das capacidades e permissões efetivamente disponíveis para a conta conectada.

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

# 19. Publicação manual

O primeiro fluxo será:

```text
Usuário
   ↓
Seleciona conteúdo
   ↓
Clica em PUBLICAR
   ↓
Sistema valida
   ↓
Instagram
```

Não implementar publicação automática complexa inicialmente.

---

# 20. Motor de Desempenho

Depois da publicação, o ViralCode deverá conseguir obter e armazenar as métricas disponíveis.

Fluxo:

```text
Publicação
   ↓
Instagram
   ↓
Conector
   ↓
Métricas
   ↓
Motor de Desempenho
   ↓
MySQL
```

---

# 21. Histórico

Sempre que possível, armazenar:

```text
data da publicação
data da coleta
visualizações
curtidas
comentários
compartilhamentos
salvamentos
```

Somente métricas realmente disponíveis deverão ser armazenadas.

---

# 22. Motor de Aprendizado

O MVP deverá possuir uma primeira camada de aprendizado.

Não será machine learning próprio.

Será:

```text
Resultados
   ↓
Comparação
   ↓
Evidências
   ↓
Aprendizados
```

---

# 23. Aprendizados

Exemplo:

```text
Padrão:
hook em pergunta

Resultados:
5 conteúdos acima da mediana
```

O sistema poderá registrar:

```text
Aprendizado:
hooks em pergunta apresentaram desempenho acima da mediana
neste contexto.
```

O aprendizado deverá possuir evidências.

---

# 24. Confiança

O MVP poderá trabalhar com:

```text
BAIXA
MEDIA
ALTA
```

A confiança deverá considerar principalmente:

```text
quantidade de evidências
consistência
contexto
```

Não transformar uma observação isolada em regra.

---

# 25. Motor de Planejamento

O planejamento será incluído, mas de forma simples.

O usuário poderá definir:

```text
data
tema
formato
objetivo
prioridade
status
```

---

# 26. Calendário

O MVP deverá permitir visualizar os conteúdos planejados.

Exemplo:

```text
20/08
Reel
Tema: diálogo

22/08
Reel
Tema: confiança
```

Não implementar um sistema avançado de calendário no primeiro momento.

---

# 27. IA

O MVP poderá utilizar um provedor externo de inteligência artificial por meio de uma abstração interna.

Arquitetura:

```text
Motor de Criação
      ↓
Abstração de IA
      ↓
Provedor de IA
      ↓
Modelo
```

O restante do sistema não deverá ficar acoplado diretamente ao fornecedor.

---

# 28. Prompts

Os prompts principais deverão ser:

```text
versionados
organizados
reutilizáveis
```

Não espalhar prompts críticos dentro das rotas da API.

---

# 29. Frontend

O frontend será:

```text
React
```

O MVP deverá priorizar uma interface simples.

Telas mínimas:

```text
Dashboard
Perfil
Conectar Instagram
Descoberta
Conteúdos
Criação
Planejamento
Publicações
Desempenho
```

Não é necessário construir uma interface visual complexa inicialmente.

---

# 30. Backend

O backend será:

```text
FastAPI
```

Arquitetura:

```text
Rotas
  ↓
Serviços
  ↓
Repositórios
  ↓
SQLAlchemy
  ↓
MySQL
```

---

# 31. Regras arquiteturais

Não colocar regras de negócio:

```text
diretamente nas rotas
```

Não colocar acesso ao banco:

```text
diretamente nas rotas
```

Não colocar chamadas ao Instagram:

```text
diretamente nas rotas
```

As responsabilidades deverão permanecer separadas.

---

# 32. Estrutura lógica

```text
React
  ↓
FastAPI
  ↓
Serviços
  ↓
Conectores / Repositórios
  ↓
Instagram / MySQL
```

---

# 33. Segurança

O MVP deverá possuir:

```text
autenticação
controle de acesso
proteção de tokens
variáveis de ambiente
logs sem credenciais
```

Senhas e segredos nunca deverão ser armazenados em código.

---

# 34. Conta Instagram

O sistema deverá utilizar uma conta conectada pelo usuário.

A integração deverá respeitar:

```text
autenticação
permissões
limites
políticas
capacidades reais da plataforma
```

---

# 35. O que o MVP NÃO terá

Não implementar inicialmente:

```text
TikTok
YouTube
```

---

# 36. O que o MVP NÃO terá — IA

Não implementar inicialmente:

```text
agentes autônomos
machine learning próprio
treinamento de modelos
IA que publica sozinha
IA que decide toda a estratégia
```

---

# 37. O que o MVP NÃO terá — conteúdo

Não implementar inicialmente:

```text
avatar
voz sintética
edição automática de vídeo
geração de vídeo complexa
animações automáticas
```

---

# 38. O que o MVP NÃO terá — infraestrutura

Não implementar inicialmente:

```text
arquitetura distribuída
Kubernetes
microserviços independentes
filas complexas
processamento distribuído
```

A arquitetura poderá evoluir posteriormente.

---

# 39. O que o MVP NÃO terá — automação

Não implementar inicialmente:

```text
publicação automática em massa
calendário totalmente automático
A/B automático
otimização automática
```

---

# 40. O que o MVP NÃO terá — analytics avançado

Não implementar inicialmente:

```text
previsão de viralização
machine learning preditivo
benchmark avançado
modelos estatísticos complexos
```

---

# 41. Critério principal do MVP

O MVP será considerado validado quando for possível executar:

```text
1. Conectar Instagram
       ↓
2. Descobrir conteúdos dentro do que a plataforma permitir
       ↓
3. Armazenar dados
       ↓
4. Analisar padrões
       ↓
5. Gerar conteúdo
       ↓
6. Aprovar
       ↓
7. Publicar
       ↓
8. Medir
       ↓
9. Aprender
```

---

# 42. Critério de negócio

Além de funcionar tecnicamente, o MVP deverá responder:

```text
O usuário percebe valor?
```

E:

```text
Ele usaria novamente?
```

E:

```text
Ele pagaria por isso?
```

Essas perguntas são mais importantes do que possuir dezenas de funcionalidades.

---

# 43. Métricas de validação

Durante a validação poderão ser observadas:

```text
tempo até primeiro valor
quantidade de conteúdos analisados
quantidade de conteúdos criados
quantidade de publicações
frequência de uso
retenção
uso recorrente
conversão para pagamento
```

---

# 44. Primeiro valor

O usuário deverá chegar rapidamente a um resultado útil.

Idealmente:

```text
Entrar
   ↓
Conectar
   ↓
Pesquisar
   ↓
Encontrar oportunidade
   ↓
Gerar conteúdo
```

O tempo entre entrada e primeiro resultado deverá ser minimizado.

---

# 45. Simplicidade

Regra:

> **Se uma funcionalidade não ajuda diretamente a validar o negócio, ela deve ficar fora do MVP.**

---

# 46. Arquitetura preparada para crescer

Embora o MVP seja simples, a arquitetura deverá preservar:

```text
múltiplos nichos
múltiplos perfis
múltiplas contas
múltiplas redes
múltiplos provedores de IA
múltiplos formatos
```

A preparação não significa implementar tudo agora.

---

# 47. Escalabilidade futura

A arquitetura deverá permitir evoluir:

```text
MVP
 ↓
Produto
 ↓
SaaS
 ↓
Múltiplos usuários
 ↓
Múltiplos perfis
 ↓
Múltiplas redes
```

---

# 48. Ambiente inicial

O desenvolvimento será realizado:

```text
LOCAL
```

Depois:

```text
LOCAL
   ↓
VPS HOSTINGER
```

---

# 49. Banco inicial

Banco:

```text
MySQL
```

ORM:

```text
SQLAlchemy
```

---

# 50. Deployment inicial

O primeiro deployment deverá priorizar simplicidade.

A arquitetura de produção deverá ser definida em documento próprio.

Não adicionar infraestrutura desnecessária antes da necessidade.

---

# 51. Regra de tecnologia

Tecnologias oficiais do MVP:

```text
Frontend:
React

Backend:
FastAPI

ORM:
SQLAlchemy

Banco:
MySQL
```

Novas tecnologias somente deverão ser adicionadas quando existir necessidade clara.

---

# 52. Regra de idioma

Todo o projeto deverá utilizar português do Brasil como idioma padrão.

Isso inclui:

```text
documentação
nomes de conceitos
API
modelos
serviços
variáveis
mensagens
interface
```

Exceções técnicas inevitáveis poderão existir quando uma biblioteca ou protocolo exigir nomenclatura externa.

---

# 53. Regra para agentes de IA

Qualquer IA que trabalhar no projeto deverá:

1. ler este documento;
2. respeitar o escopo do MVP;
3. não adicionar funcionalidades não solicitadas;
4. não trocar tecnologias sem justificativa;
5. não criar arquitetura desnecessariamente complexa;
6. respeitar os documentos anteriores;
7. não assumir capacidades não confirmadas do Instagram;
8. não utilizar provedores externos de dados não definidos pelo projeto;
9. manter todos os códigos e APIs em português;
10. atualizar a documentação quando uma decisão arquitetural mudar.

---

# 54. Ordem de implementação

A implementação deverá seguir aproximadamente:

```text
1. Fundação do projeto
        ↓
2. Banco de dados
        ↓
3. Usuário / Perfil
        ↓
4. Conta Instagram
        ↓
5. Conector Instagram
        ↓
6. Descoberta
        ↓
7. Conteúdos
        ↓
8. Motor de Inteligência
        ↓
9. Motor de Criação
        ↓
10. Aprovação
        ↓
11. Publicação
        ↓
12. Desempenho
        ↓
13. Aprendizado
        ↓
14. Planejamento
```

A ordem poderá ser ajustada após a validação técnica da integração do Instagram.

---

# 55. Regra de bloqueio

Se uma dependência crítica do Instagram não estiver tecnicamente disponível:

```text
NÃO contornar a limitação de forma inadequada.
```

Deverá ser feita uma revisão do requisito.

Possibilidades:

```text
alterar estratégia
reduzir escopo
substituir funcionalidade
adiar funcionalidade
```

---

# 56. Definição de pronto

Uma funcionalidade do MVP somente será considerada pronta quando:

```text
funciona
+
possui teste mínimo
+
possui tratamento de erro
+
respeita segurança
+
está documentada
```

---

# 57. Regra contra crescimento de escopo

Qualquer nova ideia deverá ser classificada como:

```text
MVP
```

ou:

```text
PÓS-MVP
```

Não adicionar automaticamente uma nova funcionalidade ao MVP.

---

# 58. Arquitetura resumida do MVP

```text
                         USUÁRIO
                            │
                            ▼
                         REACT
                            │
                            ▼
                         FASTAPI
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
        AUTENTICAÇÃO    DESCOBERTA    PLANEJAMENTO
                            │
                            ▼
                    CONECTOR INSTAGRAM
                            │
                            ▼
                        INSTAGRAM
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
                       APROVAÇÃO
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
                            │
                            └──────────→ CRIAÇÃO
```

---

# 59. Visão do produto

O MVP do ViralCode não deverá ser tratado apenas como:

```text
"uma ferramenta para gerar posts"
```

A proposta é construir um ciclo:

```text
DADOS
 ↓
INTELIGÊNCIA
 ↓
CRIAÇÃO
 ↓
PUBLICAÇÃO
 ↓
RESULTADO
 ↓
APRENDIZADO
```

Essa é a base do produto.

---

# 60. Regra final

> **O MVP deve provar valor antes de provar escala.**

Primeiro:

```text
funcionar
```

Depois:

```text
ser útil
```

Depois:

```text
ser usado novamente
```

Depois:

```text
ser pago
```

E somente então:

```text
escalar
```

Essa ordem deverá orientar as decisões técnicas e de produto do ViralCode.

**Versão:** 1.0  
**Status:** Documento oficial de definição do MVP
