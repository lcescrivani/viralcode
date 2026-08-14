# 13 — MOTOR DE PUBLICAÇÃO

**Versão:** 1.0  
**Status:** Documento oficial do projeto  
**Idioma oficial:** Português do Brasil  
**Projeto:** ViralCode

---

## 1. Objetivo

O Motor de Publicação será responsável por transformar um conteúdo aprovado em uma publicação efetivamente enviada para uma rede social.

Seu papel será separar:

```text
CRIAR
```

de:

```text
PUBLICAR
```

Fluxo:

```text
Motor de Criação
      ↓
Conteúdo aprovado
      ↓
Motor de Publicação
      ↓
Conector da Rede Social
      ↓
Instagram
```

No MVP, a primeira rede social será:

```text
Instagram
```

---

# 2. Princípio fundamental

O Motor de Publicação não deverá criar conteúdo.

Ele recebe um conteúdo já produzido e aprovado.

```text
Motor de Criação
→ cria

Motor de Publicação
→ publica
```

Essa separação permitirá futuramente publicar o mesmo conteúdo em diferentes redes.

---

# 3. Arquitetura

```text
React
  ↓
FastAPI
  ↓
Motor de Publicação
  ↓
Conector da Rede Social
  ↓
Instagram
```

O Motor de Publicação não deverá conhecer detalhes específicos da API do Instagram.

Esses detalhes pertencem ao:

```text
ConectorInstagram
```

---

# 4. Responsabilidades

O Motor de Publicação será responsável por:

- receber conteúdo aprovado;
- validar se está pronto;
- verificar conta conectada;
- validar plataforma;
- preparar publicação;
- enviar ao conector;
- controlar estado;
- registrar resultado;
- tratar erros;
- permitir reprocessamento controlado;
- registrar identificador externo da publicação.

---

# 5. O que não pertence ao Motor de Publicação

Não deverá ser responsabilidade dele:

```text
analisar viralidade
criar roteiro
gerar legenda
definir estratégia
criar conteúdo
analisar desempenho
```

Essas funções pertencem a outros componentes.

---

# 6. Conta Social

Toda publicação deverá estar associada a uma conta social.

Exemplo:

```text
Conteúdo
   ↓
Perfil ViralCode
   ↓
Conta Social
   ↓
Instagram
```

O sistema deverá verificar se a conta está:

```text
CONECTADA
```

antes de iniciar uma publicação.

---

# 7. Estado da conta

Se a conta estiver:

```text
EXPIRADA
REVOGADA
ERRO
REAUTENTICACAO_NECESSARIA
```

a publicação não deverá prosseguir.

O sistema deverá informar que a conexão precisa ser corrigida.

---

# 8. Conteúdo publicável

O conteúdo deverá possuir informações mínimas.

Exemplo:

```text
formato
mídia
legenda
CTA
conta_social
plataforma
```

Dependendo do formato, poderão existir outros campos.

---

# 9. Status do conteúdo

O conteúdo poderá possuir estados:

```text
RASCUNHO
EM_REVISAO
APROVADO
AGENDADO
PUBLICANDO
PUBLICADO
ERRO_PUBLICACAO
CANCELADO
```

No MVP, poderá ser utilizado um conjunto menor:

```text
RASCUNHO
APROVADO
PUBLICANDO
PUBLICADO
ERRO_PUBLICACAO
```

---

# 10. Regra de aprovação

No MVP:

> **Nenhum conteúdo deverá ser publicado automaticamente sem aprovação explícita do usuário.**

Fluxo:

```text
Gerado
  ↓
Rascunho
  ↓
Usuário revisa
  ↓
Aprovado
  ↓
Publicação
```

A publicação automática será uma evolução posterior.

---

# 11. Publicação imediata

O primeiro fluxo poderá ser:

```text
Usuário clica:
PUBLICAR
        ↓
Validação
        ↓
Conector Instagram
        ↓
Instagram
        ↓
Confirmação
```

---

# 12. Agendamento

O Motor de Publicação deverá ser preparado para agendamento futuro.

Exemplo:

```text
Conteúdo
   ↓
Agendado para:
20/08/2026 19:00
   ↓
Fila
   ↓
Publicação
```

O agendamento não precisa ser implementado no primeiro MVP se não for necessário para validar o negócio.

---

# 13. Separação entre criação e agendamento

O Motor de Criação:

```text
O que publicar?
```

O Motor de Planejamento/Calendário:

```text
Quando publicar?
```

O Motor de Publicação:

```text
Executar a publicação.
```

Essa separação deverá ser preservada.

---

# 14. Conector Instagram

O Motor de Publicação deverá utilizar:

```text
ConectorInstagram
```

Fluxo:

```text
Motor de Publicação
       ↓
ConectorInstagram
       ↓
Instagram
```

O conector será responsável pelos detalhes técnicos da plataforma.

---

# 15. Abstração

O sistema deverá possuir uma abstração semelhante a:

```python
class ConectorRedeSocial:
    def publicar_conteudo(self, conteudo, conta_social):
        ...
```

Implementação inicial:

```python
class ConectorInstagram(ConectorRedeSocial):
    def publicar_conteudo(self, conteudo, conta_social):
        ...
```

No futuro:

```python
class ConectorTikTok(ConectorRedeSocial):
    ...
```

---

# 16. Validação antes da publicação

Antes de publicar, o Motor deverá verificar:

```text
conteúdo existe
conteúdo aprovado
conta existe
conta conectada
plataforma suportada
formato suportado
mídia válida
dados obrigatórios presentes
```

Se alguma condição falhar:

```text
não publicar
```

---

# 17. Preparação da publicação

Fluxo:

```text
Conteúdo aprovado
       ↓
Validação
       ↓
Preparação
       ↓
Conector
       ↓
Instagram
```

A preparação poderá incluir:

- formato;
- mídia;
- legenda;
- parâmetros;
- configurações da publicação.

---

# 18. Mídia

Dependendo do tipo de conteúdo, poderá existir:

```text
imagem
vídeo
carrossel
```

A arquitetura deverá permitir diferentes tipos de mídia.

No MVP, implementar somente o formato necessário para o primeiro caso de uso.

---

# 19. Upload

Quando a publicação exigir upload ou disponibilização da mídia, essa etapa deverá ser controlada pelo conector.

O Motor de Publicação não deverá possuir código específico de transporte do Instagram.

---

# 20. Identificador externo

Após uma publicação bem-sucedida, o sistema deverá armazenar o identificador retornado pela plataforma quando disponível.

Exemplo:

```text
Publicacao
├── id
├── conteudo_id
├── conta_social_id
├── plataforma
├── identificador_externo
├── url
└── data_publicacao
```

---

# 21. Histórico

O sistema deverá manter o histórico das tentativas.

Exemplo:

```text
Tentativa 1 → erro
Tentativa 2 → sucesso
```

Isso será importante para diagnóstico.

---

# 22. Registro de publicação

Conceito:

```text
Publicacao
├── id
├── conteudo_id
├── conta_social_id
├── status
├── identificador_externo
├── url
├── erro
├── criado_em
├── iniciado_em
└── finalizado_em
```

---

# 23. Idempotência

O sistema deverá evitar publicar duas vezes o mesmo conteúdo por engano.

Exemplo:

```text
Usuário clica PUBLICAR
       ↓
requisição enviada
       ↓
usuário clica novamente
```

O sistema deverá identificar que já existe uma publicação em andamento ou concluída.

---

# 24. Estados de publicação

Exemplo:

```text
PENDENTE
VALIDANDO
PUBLICANDO
PUBLICADO
ERRO
CANCELADO
```

Fluxo normal:

```text
PENDENTE
   ↓
VALIDANDO
   ↓
PUBLICANDO
   ↓
PUBLICADO
```

Fluxo de erro:

```text
PUBLICANDO
   ↓
ERRO
```

---

# 25. Retry

Retentativas deverão ser controladas.

Erros temporários poderão permitir nova tentativa.

Exemplos:

```text
timeout
erro temporário
falha de rede
```

Erros permanentes deverão interromper o processo.

Exemplos:

```text
permissão negada
conta desconectada
formato inválido
dados obrigatórios ausentes
```

---

# 26. Não fazer retry infinito

Uma publicação não deverá ficar tentando indefinidamente.

Poderá existir futuramente:

```text
tentativas_maximas
```

Exemplo:

```text
3 tentativas
```

---

# 27. Timeout

Toda comunicação com a rede social deverá possuir timeout.

Objetivo:

> evitar que uma publicação permaneça indefinidamente em estado de processamento.

---

# 28. Erros

Os erros deverão ser classificados.

Exemplo:

```text
ERRO_AUTENTICACAO
ERRO_PERMISSAO
ERRO_VALIDACAO
ERRO_REDE
ERRO_TIMEOUT
ERRO_PLATAFORMA
ERRO_DESCONHECIDO
```

---

# 29. Mensagem para o usuário

O usuário não deverá receber detalhes técnicos desnecessários.

Exemplo interno:

```text
HTTP 401 / token inválido
```

Mensagem externa:

```text
A conta do Instagram precisa ser reconectada.
```

---

# 30. Logs

Os logs poderão registrar:

```text
publicação iniciada
publicação concluída
erro
tempo
identificador interno
```

Nunca registrar:

```text
token
senha
credencial
segredo
```

---

# 31. Publicação automática

Não será implementada como comportamento padrão no MVP.

Futuro:

```text
Conteúdo aprovado
      ↓
Agendamento
      ↓
Fila
      ↓
Motor de Publicação
      ↓
Instagram
```

A publicação automática deverá possuir controles de segurança e autorização.

---

# 32. Fila futura

Quando houver volume suficiente, poderá existir:

```text
Fila de Publicação
       ↓
Worker
       ↓
Motor de Publicação
       ↓
Conector
```

Isso permitirá processar várias publicações sem bloquear as requisições HTTP.

No MVP, uma execução síncrona poderá ser suficiente, desde que respeite os limites da operação.

---

# 33. Scheduler futuro

Para conteúdos agendados:

```text
Banco
 ↓
Scheduler
 ↓
Publicações vencidas
 ↓
Fila
 ↓
Worker
 ↓
Instagram
```

Essa camada não precisa existir no primeiro MVP.

---

# 34. Múltiplas contas

O sistema deverá permitir futuramente:

```text
Perfil
  ├── Instagram A
  ├── Instagram B
  └── TikTok A
```

Cada publicação deverá identificar explicitamente a conta utilizada.

---

# 35. Múltiplas redes

O conteúdo poderá futuramente ser adaptado para:

```text
Instagram
TikTok
YouTube
```

O Motor de Publicação deverá delegar a execução ao conector correspondente.

---

# 36. Publicação multiplataforma

Fluxo futuro:

```text
Conteúdo base
      ↓
Adaptações por plataforma
      ↓
┌──────────────┬──────────────┬──────────────┐
↓              ↓              ↓
Instagram      TikTok         YouTube
```

Cada publicação terá seu próprio estado e identificador externo.

---

# 37. Relação com desempenho

Depois da publicação:

```text
Publicação
    ↓
Conteúdo publicado
    ↓
Métricas
    ↓
Motor de Inteligência
```

Isso permitirá medir se os padrões utilizados na criação funcionaram.

---

# 38. Ciclo completo

```text
DESCOBRIR
   ↓
ANALISAR
   ↓
APRENDER
   ↓
CRIAR
   ↓
APROVAR
   ↓
PUBLICAR
   ↓
MEDIR
   ↓
APRENDER
```

Esse ciclo representa a arquitetura estratégica do ViralCode.

---

# 39. Segurança

O Motor de Publicação nunca deverá:

- receber senha da rede social;
- expor tokens;
- salvar credenciais em código;
- ignorar validações;
- publicar conteúdo não autorizado;
- contornar permissões da plataforma.

---

# 40. Permissões

A publicação deverá utilizar somente as permissões necessárias para a funcionalidade.

O sistema deverá validar se a conta possui autorização suficiente antes de tentar publicar.

---

# 41. Capacidade real da plataforma

O ViralCode não deverá assumir que qualquer formato pode ser publicado em qualquer rede.

Antes de implementar:

```text
formato
+
mídia
+
legenda
+
configuração
```

deverá ser verificado se a plataforma suporta aquela operação.

---

# 42. MVP

O MVP deverá implementar somente:

```text
1 rede social
      ↓
Instagram

1 conta conectada
      ↓
publicação manual

1 formato principal
      ↓
formato definido pelo primeiro caso de uso

1 fluxo
      ↓
aprovar → publicar → registrar resultado
```

---

# 43. O que NÃO fazer no MVP

Não implementar inicialmente:

```text
fila distribuída
scheduler complexo
publicação em massa
multiplataforma
A/B automático
republicação automática
agentes autônomos
otimização automática
```

Essas funcionalidades poderão ser adicionadas após a validação do negócio.

---

# 44. Primeiro caso de uso

O primeiro fluxo recomendado:

```text
Usuário cria conteúdo
       ↓
Motor de Criação
       ↓
Rascunho
       ↓
Usuário revisa
       ↓
Aprova
       ↓
Clica PUBLICAR
       ↓
Motor de Publicação
       ↓
Conector Instagram
       ↓
Instagram
       ↓
Resultado
```

---

# 45. Critério de sucesso

O Motor de Publicação será considerado funcional quando o usuário conseguir:

> **criar ou selecionar um conteúdo aprovado, escolher uma conta Instagram conectada, publicar e visualizar claramente se a operação foi concluída ou falhou.**

---

# 46. Testes

O Motor deverá possuir testes para:

```text
conteúdo aprovado
conteúdo não aprovado
conta conectada
conta desconectada
formato válido
formato inválido
publicação com sucesso
timeout
erro de autenticação
erro de permissão
retry
duplicidade
```

---

# 47. Testes sem Instagram real

Os serviços deverão ser testáveis com um conector falso.

```text
Teste
 ↓
Motor de Publicação
 ↓
Conector falso
 ↓
Resposta simulada
```

Isso permitirá testar a regra de negócio sem depender da plataforma.

---

# 48. Observabilidade futura

O sistema poderá acompanhar:

```text
publicações
sucessos
falhas
tempo médio
taxa de erro
erros por plataforma
erros por conta
```

Essas métricas ajudarão a identificar problemas de integração.

---

# 49. Auditoria futura

Ações importantes poderão ser registradas:

```text
conteúdo aprovado
publicação solicitada
publicação iniciada
publicação concluída
publicação cancelada
erro de publicação
conta desconectada
```

---

# 50. Regra para agentes de IA

Antes de alterar o Motor de Publicação:

1. ler este documento;
2. verificar o estado atual do conteúdo;
3. verificar a conta social;
4. respeitar a abstração `ConectorRedeSocial`;
5. não colocar código específico do Instagram no serviço;
6. não expor credenciais;
7. evitar publicação duplicada;
8. tratar erros;
9. criar testes;
10. atualizar a documentação quando a arquitetura mudar.

---

# 51. Arquitetura do Motor de Publicação

```text
                 CONTEÚDO APROVADO
                         │
                         ▼
                 MOTOR DE PUBLICAÇÃO
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
          VALIDAÇÃO    CONTA      FORMATO
              │          │          │
              └──────────┼──────────┘
                         ▼
                  CONECTOR REDE SOCIAL
                         │
                         ▼
                      INSTAGRAM
                         │
                         ▼
                    RESULTADO
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
         PUBLICADO                  ERRO
             │                       │
             └───────────┬───────────┘
                         ▼
                     HISTÓRICO
```

---

# 52. Arquitetura-alvo

```text
                         VIRALCODE
                             │
      ┌──────────────────────┼──────────────────────┐
      ▼                      ▼                      ▼
 DESCOBERTA             INTELIGÊNCIA            CRIAÇÃO
      │                      │                      │
      └──────────────────────┼──────────────────────┘
                             ▼
                       CONTEÚDO APROVADO
                             │
                             ▼
                    MOTOR DE PUBLICAÇÃO
                             │
                    CONECTOR DE REDE
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
          Instagram        TikTok        YouTube
              │              │              │
              ▼              ▼              ▼
           MÉTRICAS       MÉTRICAS       MÉTRICAS
              └──────────────┼──────────────┘
                             ▼
                   MOTOR DE INTELIGÊNCIA
```

---

# 53. Regra final

> **O Motor de Publicação executa a decisão de publicar; ele não decide sozinho o que criar nem deve conhecer os detalhes internos de cada rede social.**

A responsabilidade deverá permanecer separada:

```text
MOTOR DE INTELIGÊNCIA
→ entende o que funciona

MOTOR DE CRIAÇÃO
→ cria

USUÁRIO
→ aprova no MVP

MOTOR DE PUBLICAÇÃO
→ executa

CONECTOR
→ conversa com a rede social

MOTOR DE DESEMPENHO
→ mede

MOTOR DE INTELIGÊNCIA
→ aprende
```

Essa separação permitirá que o ViralCode cresça de uma ferramenta simples para uma plataforma completa de inteligência, criação e publicação de conteúdo.

**Versão:** 1.0  
**Status:** Documento oficial do Motor de Publicação
