---
name: whatsapp-funnel-recovery
description: Procedimento operacional para criar um funil de recuperação de vendas
  via WhatsApp focado em recuperar Pix e boletos gerados não pagos de infoprodutos.
tags:
- dev
- code
version: 1.0.0
category: general
---
# Recuperação de Vendas via WhatsApp (Funil Pix/Boleto)

Esta skill documenta o workflow extraído para recuperar vendas perdidas por falta de pagamento (Pix gerado ou boleto).

## Contexto
Quando um cliente gera um Pix ou boleto de um infoproduto e não paga, é necessário ter um funil ativo via WhatsApp para reverter essa desistência em vendas. A abordagem de recuperação deve ser humanizada, rápida e estruturada em cadência.

## Workflow de Recuperação (Passo a Passo)

### Passo 1: Triagem Imediata (T0 a T+2h)
- Assim que o Pix/Boleto for gerado, o sistema (ex: ActiveCampaign, Hotmart, Eduzz) deve enviar um webhook para a plataforma de disparo de WhatsApp.
- **Ação:** Enviar uma mensagem automatizada mas com tom pessoal de "boas vindas parciais" ou oferecendo ajuda técnica.
- **Exemplo:** "Oi [Nome], vi que você gerou o Pix do [Produto]! Parabéns pela decisão. Ficou alguma dúvida sobre o acesso ou precisa de ajuda com o QR Code?"

### Passo 2: Follow-up de Escassez (T+12h ou T+24h)
- Se não houver pagamento, acionar o segundo disparo.
- **Ação:** Reforçar os bônus que podem ser perdidos ou a validade do Pix.
- **Exemplo:** "Oi [Nome], tudo bem? O seu Pix vence em breve. Só passando para lembrar que os bônus especiais expiram junto com ele. Quer que eu gere um novo código para você não perder?"

### Passo 3: Quebra de Objeção e Downsell (T+48h)
- Se o cliente ainda não pagou ou visualizou e não respondeu.
- **Ação:** Perguntar ativamente o motivo da não conversão. Se for preço, oferecer uma alternativa (Downsell) ou parcelamento (via cartão).
- **Exemplo:** "Oi [Nome], vi que você acabou não concluindo a inscrição. Foi alguma questão com o valor? Se sim, me avisa que eu consigo liberar um link de parcelamento especial para você."

## Guardrails e Melhores Práticas
- **Tom Humanizado:** As mensagens não podem parecer disparos robóticos em massa. Use gírias locais sutis e formatação amigável (emojis estratégicos).
- **Timings:** Não seja invasivo. Respeite horários comerciais.
- **Automação Híbrida:** O primeiro contato é automatizado. Assim que o cliente responde, um atendente humano (ou IA com contexto de vendas) deve assumir o fluxo para tratar a objeção de forma personalizada.

## Avaliação Scorecard (ROI)
- Frequência/Volume: 2
- Repetitividade: 2
- Regra Clara: 2
- Estabilidade: 1
- Entradas Padronizadas: 2
- Complexidade: 2
- Testabilidade: 2
- Reuso/Portabilidade: 2
- Segurança/Risco: 2
- **TOTAL:** 17 (Candidato Excelente)
