# YouTube Mining Notes

## Benji's AI Playground Batch 1

### 1. AEP v1.5 AI Music Model (https://www.youtube.com/watch?v=ho30R7W01I4)
- **Topic:** Local AI music generation using AEP v1.5 via ComfyUI.
- **Procedure:** 
  - Download the AEP v1.5 model from Hugging Face or ModelScope.
  - Set up the diffusion model workflow in ComfyUI.
  - Utilize nodes to input prompts and generate music audio files locally.
- **ROI:** 16. Highly actionable procedure for local audio generation.

### 2. Cache DiT for ComfyUI (https://www.youtube.com/watch?v=nbhxqRu21js)
- **Topic:** Speeding up inference times for Diffusion Transformers (DiT).
- **Procedure:**
  - Install the Cache DiT custom node for ComfyUI.
  - Integrate caching nodes into existing DiT workflows (like Flux or SD3).
  - Cache intermediate diffusion steps into memory to reduce redundant computation.
  - Adjust cache thresholds to balance speed vs. quality.
- **ROI:** 16. Excellent optimization technique for local AI workflows.

### 3. Qwen 3 ASR & Microsoft Vibe Voice (https://www.youtube.com/watch?v=ZXzuMx-iv1M)
- **Topic:** State-of-the-art Automatic Speech Recognition (ASR).
- **Procedure:**
  - Compare Qwen 3 ASR against Microsoft Vibe Voice for noisy environments.
  - Run the models locally (via Python/CLI or ComfyUI if nodes exist).
  - Process complex audio (e.g., songs, noisy cafes) to extract transcriptions.
- **ROI:** 16. Strong candidate for a transcription skill or updating existing audio processing skills.

---

## @fernandobrasao YouTube Mining

### Batch 1-5 Evaluation
- **A Teoria das 2 Portas: Jeff Bezos** -> Conceptual theory, not a procedural task. ROI Score: <10.
- **Sinal x Ruído: Steve Jobs e Elon Musk** -> Mindset content. ROI Score: <10.
- **7 Hacks Bizarros de Produtividade** -> Tips and tricks, likely lack a cohesive single workflow. ROI Score: ~10.
- **Como fazer um Funil de Vendas tão bom que parece ILEGAL!** -> Marketing funnel procedure. ROI Score: ~12.
- **Live #155 - O Funil de WhatsApp que Recuperou 1.3 Milhões** -> Clear procedural workflow. ROI: 17. **Skill Created:** `whatsapp-funnel-recovery`.
- **3 ESTRATÉGIAS AVANÇADAS PARA FATURAR MILHÕES COM WEBINÁRIO** -> ROI: 15. **Skill Created:** `webinar-funnel-strategy`.
- **A ESTRATÉGIA AMERICANA QUE PAGA SEU TRÁFEGO (SLO)** -> ROI: 16. **Skill Created:** `american-slo-funnel`.
- **#TIPS 63 COMO FAZER ANÚNCIOS PRA QUEM ASSITIU A LIVE?** -> ROI: 16. **Skill Created:** `live-remarketing-ads`.
- **#TIPS 62 QUAIS PASSOS DEFINE COMO MVP DE UM PRODUTO?** -> ROI: 15. **Skill Created:** `mvp-validation-process`.
- **#TIPS 61 PARA CURSO DE RELACIONAMENTO QUAL O MELHOR FUNIL?** -> ROI: 15. **Skill Created:** `relationship-niche-funnel`.

### Batch 6 (Vlogs/Motivational & Bot Block)
- **Videos:**
  - `https://www.youtube.com/watch?v=AVmof6Ptn68` ("Queria um conselho de Jesus")
  - `https://www.youtube.com/watch?v=DM2MzXxpgdE` ("SUMA por um Final de Semana!")
  - `https://www.youtube.com/watch?v=coQRluyC0nw` ("Em 8 Minutos Você Vai Repensar Sua Vida")
- **Evaluation:** Vlog/motivational style with no concrete operational steps. ROI < 10.
- **Outcome:** No skills generated. HTTP Error 429 received on the third video.

### Batch 7
- **Videos Processed:**
  - `https://www.youtube.com/watch?v=kcJK-moS5uE` ("Live #189 - Copywriting para criar conteúdos virais")
  - `https://www.youtube.com/watch?v=5dyCDW4i_-E` ("Live #192 - Do Zero Ao Incrível em Apenas 21 Dias")
  - `https://www.youtube.com/watch?v=eWLAepOdAhU` ("Live #194 - Organização Global dos Emails com os Funis")
- **Evaluation:** Conversational, unstructured long-form webinar/live formats. ROI < 15.
- **Outcome:** No skills generated. Halted due to bot protections (429 Error).

---

## Unsupervised Learning YouTube Mining

### Batch 1 & 2 Evaluation

#### Video: A conversation with Neatsun Ziv At OX.Security (ydX2EMat62E)
- **Score**: < 10
- **Notes**: Discarded. Podcast style discussing security debt. Too abstract.

#### Video: AI Is Definitely "Intelligent" (N4PI8VIFAw8)
- **Score**: < 10
- **Notes**: Discarded. Opinion piece regarding AI intelligence.

#### Video: A Conversation with Jiquan Ngiam About Agent + MCP Security (M02kXnomB2U)
- **Score**: < 10
- **Notes**: Discarded. Conversation about securing AI agents. No scriptable procedure.

#### Video: The Future of Hacking is Context (UwTTcka1Wd8)
- **Score**: < 10
- **Notes**: Discarded. High-level philosophical discussion.

#### Video: 5 Levels of LLM Understanding (YoBwMdtiWgg)
- **Score**: < 10
- **Notes**: Discarded. Educational explainer. No actionable workflow.

#### Video: The AI Bubble is Real (J1SHyk8nyOg)
- **Score**: < 10
- **Notes**: Discarded. Economic analysis.

#### Video: Using the Smartest AI to Rate Other AI
- **Score**: 16
- **Notes**: **Skill Created:** `fabric-ai-evaluator`.

#### Video: My Art Skill With Nano Banana 3
- **Score**: 16
- **Notes**: **Skill Created:** `nano-banana-art-generator`.

#### Video: Claude Code + Neovim via Ghostty Panes
- **Score**: 17
- **Notes**: **Skill Created:** `claude-code-neovim-ghostty`.

#### Video: Fabric New Integration with Raycast
- **Score**: 16
- **Notes**: **Skill Created:** `fabric-raycast-integration`.
