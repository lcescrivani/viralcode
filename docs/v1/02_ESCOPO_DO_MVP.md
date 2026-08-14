# 02 — ESCOPO DO MVP

**Versão:** 0.1  
**Status:** Documento inicial  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo deste documento

Este documento define exatamente o que entra e o que não entra no primeiro MVP do ViralCode.

O objetivo é impedir que o projeto cresça em complexidade antes de validarmos a hipótese principal do negócio.

A regra central é:

> **O MVP deve ser o menor produto capaz de provar se existe valor em descobrir conteúdos de alto desempenho por nicho e apresentá-los de forma organizada.**

---

## 2. Hipótese que o MVP precisa validar

A hipótese principal é:

> **Usuários que produzem conteúdo consideram valioso pesquisar um nicho, encontrar conteúdos de alto desempenho e visualizar esses resultados organizados em um único lugar.**

Queremos validar principalmente:

- se a busca é útil;
- se os resultados são relevantes;
- se o filtro por visualizações é útil;
- se o ranking economiza tempo;
- se o usuário voltaria a utilizar a ferramenta;
- se existe interesse em pagar por esse recurso;
- quais informações são mais importantes para o usuário.

---

## 3. Pergunta principal do MVP

O MVP precisa responder:

> **"Se eu digitar um nicho e pedir conteúdos com alto número de visualizações, o ViralCode me entrega uma lista útil o suficiente para eu querer usar novamente?"**

Se a resposta for positiva, avançamos para a próxima camada.

---

## 4. O que o MVP fará

A primeira versão terá um fluxo simples:

```text
Usuário
   ↓
Informa termo ou nicho
   ↓
Define filtros
   ↓
Executa busca
   ↓
ViralCode consulta o provedor
   ↓
Normaliza os resultados
   ↓
Remove duplicados
   ↓
Armazena no MySQL
   ↓
Ordena os resultados
   ↓
Exibe no React
```

---

## 5. Funcionalidades do MVP

### 5.1 Pesquisa

O usuário deverá informar:

- termo;
- nicho ou palavra-chave;
- plataforma;
- número mínimo de visualizações;
- período da pesquisa.

Exemplo:

```text
Nicho: casamento
Plataforma: Instagram
Visualizações mínimas: 1.000.000
Período: últimos 90 dias
```

---

### 5.2 Consulta ao provedor externo

O sistema deverá utilizar inicialmente um provedor externo de dados.

O primeiro provedor considerado é a SocialKit.

A integração deverá ficar isolada em uma camada de provedor.

Não devemos espalhar chamadas da SocialKit pelo restante do sistema.

---

### 5.3 Normalização

Os dados recebidos do provedor deverão ser convertidos para o modelo interno do ViralCode.

Exemplo conceitual:

```text
Dados do provedor
      ↓
Adaptador
      ↓
Modelo interno ViralCode
```

O restante da aplicação não deverá depender do formato específico retornado pela SocialKit.

---

### 5.4 Deduplicação

O mesmo conteúdo poderá aparecer em diferentes consultas.

O sistema deverá identificar duplicados utilizando identificadores adequados, como:

- identificador da plataforma;
- código do conteúdo;
- URL normalizada.

O mesmo conteúdo não deverá ser armazenado repetidamente como se fosse um conteúdo diferente.

---

### 5.5 Armazenamento

Os resultados relevantes deverão ser persistidos no MySQL.

No MVP, o banco deverá armazenar pelo menos:

- conteúdo;
- plataforma;
- autor;
- URL;
- legenda, quando disponível;
- data de publicação, quando disponível;
- visualizações;
- curtidas, quando disponíveis;
- comentários, quando disponíveis;
- imagem de capa ou referência equivalente, quando disponível;
- data da coleta.

---

### 5.6 Ranking

Os resultados deverão ser ordenados inicialmente por:

> **número de visualizações, do maior para o menor.**

Exemplo:

```text
1º — 18.400.000 visualizações
2º — 12.700.000 visualizações
3º — 8.900.000 visualizações
4º — 5.400.000 visualizações
```

Critérios avançados de ranking ficam para fases futuras.

---

### 5.7 Exibição dos resultados

A interface deverá apresentar, de forma simples:

- autor;
- conteúdo;
- imagem;
- visualizações;
- curtidas, quando disponíveis;
- comentários, quando disponíveis;
- data, quando disponível;
- plataforma;
- link para o conteúdo original.

O usuário deverá conseguir abrir o conteúdo original.

---

## 6. Interface do MVP

A interface deverá ser simples.

Não precisamos criar um dashboard complexo.

### Tela principal

```text
┌──────────────────────────────────────────────┐
│                  VIRALCODE                   │
│                                              │
│  Pesquise conteúdos de alto desempenho      │
│                                              │
│  Nicho / termo                               │
│  [ casamento                         ]       │
│                                              │
│  Plataforma                                  │
│  [ Instagram ▼ ]                             │
│                                              │
│  Visualizações mínimas                       │
│  [ 1.000.000 ]                               │
│                                              │
│  Período                                     │
│  [ 90 dias ▼ ]                               │
│                                              │
│              [ PESQUISAR ]                   │
└──────────────────────────────────────────────┘
```

Depois da busca:

```text
┌──────────────────────────────────────────────┐
│ RESULTADOS                                   │
│                                              │
│ 37 conteúdos encontrados                     │
│                                              │
│ ┌──────────────────────────────────────────┐ │
│ │ Imagem                                   │ │
│ │ @perfil                                  │ │
│ │ 18.400.000 visualizações                 │ │
│ │ 820.000 curtidas                         │ │
│ │ 12.000 comentários                       │ │
│ │ [ VER CONTEÚDO ]                         │ │
│ └──────────────────────────────────────────┘ │
│                                              │
│ ┌──────────────────────────────────────────┐ │
│ │ ...                                      │ │
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
```

A interface poderá evoluir depois.

---

## 7. Modelo inicial de dados

O MVP deverá começar com um modelo de dados pequeno.

Entidades iniciais:

```text
Busca
Conteúdo
Autor
Métrica do conteúdo
```

### Busca

Representa uma pesquisa realizada pelo usuário.

Possíveis dados:

- identificador;
- termo;
- plataforma;
- visualizações mínimas;
- período;
- data da pesquisa.

### Conteúdo

Representa o conteúdo encontrado.

Possíveis dados:

- identificador interno;
- identificador externo;
- plataforma;
- URL;
- legenda;
- data de publicação;
- imagem;
- data da primeira coleta;
- data da última atualização.

### Autor

Representa o perfil que publicou o conteúdo.

Possíveis dados:

- identificador externo;
- nome;
- nome de usuário;
- URL do perfil;
- seguidores, quando disponível.

### Métrica do conteúdo

Representa métricas observadas.

Possíveis dados:

- visualizações;
- curtidas;
- comentários;
- compartilhamentos, quando disponíveis;
- data da coleta.

---

## 8. Arquitetura do MVP

A arquitetura obrigatória do MVP será:

```text
React
   ↓
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

Integração externa:

```text
Serviço de busca
       ↓
Provedor SocialKit
       ↓
API externa
```

---

## 9. Responsabilidade de cada camada

### React

Responsável pela interface e interação com o usuário.

Não deverá conter regras de negócio importantes.

### FastAPI

Responsável pela API REST.

Recebe requisições, valida dados e encaminha a operação para os serviços.

### Serviços

Responsáveis pelas regras de negócio.

Exemplo:

```text
Serviço de busca
   ↓
validar pesquisa
   ↓
consultar provedor
   ↓
normalizar
   ↓
deduplicar
   ↓
persistir
   ↓
retornar resultado
```

### Repositórios

Responsáveis pelo acesso aos dados persistidos.

### SQLAlchemy

Responsável pelo mapeamento entre objetos Python e banco de dados.

### MySQL

Responsável pela persistência.

---

## 10. Provedor externo

O MVP deverá utilizar a SocialKit como primeiro provedor de descoberta, caso os testes confirmem que seus dados e custos são adequados.

A arquitetura deverá permitir substituir o provedor futuramente.

Exemplo:

```text
Provedor de conteúdo
│
├── SocialKit
├── Provedor futuro
└── Outro provedor futuro
```

O código do negócio não deverá depender diretamente da implementação específica da SocialKit.

---

## 11. O que NÃO entra no MVP

Para proteger o escopo, os seguintes itens ficam explicitamente fora da primeira versão:

### Inteligência avançada

- análise automática do hook;
- análise de emoção;
- análise de estrutura;
- análise de CTA;
- Viral DNA;
- classificação semântica avançada;
- análise de comentários por IA;
- identificação automática de padrões virais;
- recomendações de conteúdo.

### Geração

- geração de posts;
- geração de Reels;
- geração de carrosséis;
- geração de Stories;
- geração de legendas por IA;
- geração de roteiros;
- geração de vídeos;
- editor de vídeo.

### Publicação

- publicação automática;
- agendamento;
- calendário editorial;
- gerenciamento de contas sociais;
- conexão com contas do Instagram;
- conexão com TikTok;
- conexão com YouTube;
- conexão com Facebook;
- conexão com LinkedIn.

### Inteligência própria

- comparação com desempenho do usuário;
- aprendizado automático;
- recomendações personalizadas;
- previsão de desempenho;
- detecção avançada de tendências.

### SaaS

- múltiplas organizações;
- planos;
- assinaturas;
- cobrança;
- créditos;
- equipes;
- permissões avançadas.

Essas funcionalidades podem fazer parte das fases futuras.

---

## 12. O que também não devemos construir

O MVP não deve receber complexidade técnica desnecessária.

Não implementar inicialmente:

- microsserviços;
- Kubernetes;
- arquitetura distribuída;
- múltiplos bancos;
- filas complexas sem necessidade;
- infraestrutura de nuvem complexa;
- sistema de eventos distribuídos;
- observabilidade empresarial;
- arquitetura orientada a eventos completa.

A aplicação deve ser simples e modular.

---

## 13. Primeiro nicho para validação

O sistema não deverá ser construído especificamente para casamento.

Entretanto, o primeiro teste de negócio poderá utilizar:

> **Casamento**

como nicho de validação.

Isso significa que "casamento" é um dado de teste, não uma regra de negócio.

O sistema deve funcionar da mesma forma para:

```text
casamento
fitness
finanças
educação
marketing
imóveis
tecnologia
```

---

## 14. Primeira plataforma

A primeira plataforma considerada será:

> **Instagram**

com foco inicial em:

> **Reels**

Isso é uma decisão de escopo, não uma limitação arquitetural permanente.

A arquitetura deverá permitir adicionar outras plataformas posteriormente.

---

## 15. Dados mínimos necessários

Para o MVP, o sistema deverá priorizar os dados que realmente ajudam a validar a hipótese.

Dados prioritários:

### Obrigatórios quando disponíveis

- identificador do conteúdo;
- URL;
- autor;
- plataforma;
- visualizações.

### Importantes

- curtidas;
- comentários;
- legenda;
- data de publicação;
- imagem de capa.

### Futuramente

- compartilhamentos;
- salvamentos;
- duração;
- áudio;
- transcrição;
- retenção;
- histórico detalhado de crescimento.

Não devemos impedir a exibição de um conteúdo apenas porque um campo secundário não está disponível.

---

## 16. Critérios de aceitação do MVP

O MVP será considerado tecnicamente funcional quando:

1. o sistema iniciar localmente;
2. React conseguir conversar com FastAPI;
3. FastAPI conseguir executar uma busca;
4. o serviço conseguir chamar o provedor;
5. os dados forem normalizados;
6. duplicados forem tratados;
7. resultados forem persistidos no MySQL;
8. resultados puderem ser consultados;
9. a interface exibir o ranking;
10. o usuário conseguir abrir o conteúdo original;
11. erros externos forem tratados de maneira controlada;
12. nenhuma chave secreta estiver exposta no código.

---

## 17. Critérios de validação do negócio

Além do funcionamento técnico, devemos observar:

### Utilidade

O usuário encontra conteúdos que realmente queria encontrar?

### Relevância

Os resultados fazem sentido para o termo pesquisado?

### Economia de tempo

O ViralCode torna a pesquisa mais rápida do que fazer isso manualmente?

### Retorno

O usuário faria outra pesquisa depois da primeira?

### Frequência

Existe motivo para utilizar o produto regularmente?

### Disposição para pagar

O usuário considera o recurso valioso o suficiente para pagar?

Essas respostas determinarão o próximo estágio.

---

## 18. Métricas de validação

No início, devemos observar:

- quantidade de pesquisas;
- quantidade de resultados por pesquisa;
- termos mais pesquisados;
- filtros mais utilizados;
- conteúdos mais acessados;
- quantidade de usuários que retornam;
- frequência de uso;
- feedback qualitativo;
- interesse em funcionalidades futuras.

Não precisamos criar um sistema completo de analytics no primeiro dia.

Podemos começar registrando eventos essenciais e evoluir depois.

---

## 19. Segurança no MVP

Mesmo sendo um projeto local inicialmente, algumas regras são obrigatórias:

- nenhuma chave de API dentro do código;
- utilizar variáveis de ambiente;
- não versionar `.env`;
- não armazenar segredos no banco sem necessidade;
- não registrar chaves nos logs;
- validar dados recebidos;
- tratar erros de provedores externos;
- utilizar consultas parametrizadas através do SQLAlchemy.

---

## 20. Desenvolvimento local

O ambiente inicial será local.

A estrutura prevista é:

```text
viralcode/
├── frontend/
├── backend/
├── docs/
└── infraestrutura/
```

O projeto deverá ser executável em ambiente de desenvolvimento sem depender da VPS.

A VPS da Hostinger será utilizada posteriormente.

---

## 21. Deploy futuro

O MVP será desenvolvido localmente.

Após a validação, o sistema poderá ser publicado em uma VPS da Hostinger.

Fluxo:

```text
Desenvolvimento local
        ↓
Git
        ↓
VPS Hostinger
        ↓
Docker
        ↓
Aplicação
```

A configuração de produção não faz parte da implementação inicial do MVP, mas a arquitetura não deve impedir esse caminho.

---

## 22. Estratégia de evolução

Depois de validar o MVP, as próximas funcionalidades deverão ser adicionadas de forma incremental.

Ordem prevista:

```text
MVP
 ↓
Análise de conteúdo
 ↓
Viral DNA
 ↓
Padrões virais
 ↓
Geração de conteúdo
 ↓
Calendário
 ↓
Publicação
 ↓
Métricas próprias
 ↓
Aprendizado
```

Essa ordem pode mudar de acordo com o resultado da validação.

---

## 23. Regra contra aumento de escopo

Qualquer solicitação de nova funcionalidade deverá ser classificada como:

- necessária para o MVP;
- importante para validação;
- melhoria;
- futura;
- fora do produto.

Antes de implementar uma funcionalidade que não esteja neste documento, deve-se avaliar se ela é realmente necessária para a hipótese atual.

---

## 24. Regra para agentes de IA

Ao trabalhar neste MVP, agentes de inteligência artificial devem:

1. ler `00_CONTEXTO_DO_PROJETO.md`;
2. ler `01_VISAO_DO_PRODUTO.md`;
3. ler este documento;
4. respeitar a arquitetura definida;
5. não implementar funcionalidades futuras;
6. não criar abstrações desnecessárias;
7. manter o código em português;
8. utilizar nomes claros;
9. testar alterações;
10. atualizar a documentação quando houver mudança relevante.

Se uma solicitação parecer pertencer à visão futura, mas não ao MVP, o agente deverá reconhecer essa diferença antes de implementar.

---

## 25. Definição de pronto

Uma funcionalidade do MVP somente será considerada concluída quando:

```text
Código
  +
Teste
  +
Integração
  +
Tratamento de erro
  +
Documentação mínima
```

estiverem funcionando.

"Funcionou uma vez na minha máquina" não é suficiente.

---

## 26. Regra de simplicidade

A primeira versão do ViralCode deve ser simples.

A pergunta para qualquer nova implementação será:

> **"Precisamos realmente disso para validar o negócio agora?"**

Se a resposta for não, a funcionalidade deve ser registrada para uma fase futura em vez de ser implementada imediatamente.

---

## 27. Resultado esperado do MVP

Ao final do MVP, deveremos conseguir executar algo semelhante a:

```text
1. Abrir o ViralCode.

2. Digitar:
   casamento

3. Selecionar:
   Instagram
   mínimo de 1.000.000 visualizações
   últimos 90 dias

4. Clicar em pesquisar.

5. O sistema consultar o provedor.

6. Os resultados serem normalizados.

7. Duplicados serem eliminados.

8. Os dados serem salvos no MySQL.

9. O ranking ser exibido.

10. O usuário abrir o Reel original.
```

Esse é o produto mínimo que queremos colocar diante de um usuário real.

---

## 28. Resumo do MVP

```text
                    VIRALCODE MVP

                         React
                           │
                           ▼
                        FastAPI
                           │
                           ▼
                     Serviço de Busca
                           │
                           ▼
                  Provedor SocialKit
                           │
                           ▼
                     Normalização
                           │
                           ▼
                     Deduplicação
                           │
                           ▼
                      Repositório
                           │
                           ▼
                       SQLAlchemy
                           │
                           ▼
                         MySQL
                           │
                           ▼
                        Ranking
                           │
                           ▼
                    Usuário acessa
                    conteúdo original
```

---

## 29. Regra final do MVP

> **Não estamos construindo ainda o ViralCode completo. Estamos construindo a menor prova possível de que a ideia do ViralCode merece ser construída.**

Se o mercado validar a descoberta e o ranking de conteúdos, avançaremos.

Se não validar, devemos aprender rapidamente e mudar a direção antes de investir nos motores de inteligência, criação e publicação.

**Versão atual:** 0.1  
**Status:** Escopo inicial do MVP
