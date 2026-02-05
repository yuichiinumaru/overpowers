import { AuthProvider } from './types';
import { getProviderEndpoint } from './endpoints';

export interface IAuthMonster {
  request(model: string, url: string, options: any): Promise<Response>;
  getAuthDetails(modelOrProvider?: string | AuthProvider): Promise<any>;
}

export class DialecticsEngine {
  constructor(private monster: IAuthMonster) {}

  async synthesize(prompt: string, modelA: string, modelB: string, synthesizerModel: string): Promise<string> {
    // 1. Get Details and URLs
    const detailsA = await this.monster.getAuthDetails(modelA);
    const detailsB = await this.monster.getAuthDetails(modelB);

    if (!detailsA) throw new Error(`Could not resolve model: ${modelA}`);
    if (!detailsB) throw new Error(`Could not resolve model: ${modelB}`);

    const urlA = getProviderEndpoint(detailsA.provider, detailsA.account, detailsA.modelInProvider);
    const urlB = getProviderEndpoint(detailsB.provider, detailsB.account, detailsB.modelInProvider);

    // 2. Prepare Requests
    const body = {
        messages: [{ role: 'user', content: prompt }],
        model: detailsA.modelInProvider, // Some providers need model in body
        temperature: 0.7
    };
    const bodyB = {
        messages: [{ role: 'user', content: prompt }],
        model: detailsB.modelInProvider,
        temperature: 0.7
    };

    // 3. Send Requests
    console.log(`[Dialectics] Sending to ${modelA} (${detailsA.provider}) and ${modelB} (${detailsB.provider})...`);

    const [resA, resB] = await Promise.all([
        this.monster.request(modelA, urlA, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: body
        }).then(r => r.json().catch(e => ({ error: 'JSON Parse Error', details: e }))),

        this.monster.request(modelB, urlB, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: bodyB
        }).then(r => r.json().catch(e => ({ error: 'JSON Parse Error', details: e })))
    ]);

    // 4. Extract Content
    const contentA = this.extractContent(detailsA.provider, resA);
    const contentB = this.extractContent(detailsB.provider, resB);

    // 5. Synthesize
    const synthesisPrompt = `
I have two responses to the following prompt: "${prompt}"

=== Response A (${modelA}) ===
${contentA}

=== Response B (${modelB}) ===
${contentB}

Please synthesize these two responses into a single, comprehensive answer.
`;

    const detailsC = await this.monster.getAuthDetails(synthesizerModel);
    if (!detailsC) throw new Error(`Could not resolve synthesizer model: ${synthesizerModel}`);

    const urlC = getProviderEndpoint(detailsC.provider, detailsC.account, detailsC.modelInProvider);

    console.log(`[Dialectics] Synthesizing with ${synthesizerModel} (${detailsC.provider})...`);

    const resC = await this.monster.request(synthesizerModel, urlC, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: {
            messages: [{ role: 'user', content: synthesisPrompt }],
            model: detailsC.modelInProvider
        }
    });

    const jsonC = await resC.json();
    return this.extractContent(detailsC.provider, jsonC);
  }

  private extractContent(provider: AuthProvider, response: any): string {
      if (!response) return "No response";
      if (response.error) return `Error: ${JSON.stringify(response.error)}`;

      if (provider === AuthProvider.Gemini) {
          return response.candidates?.[0]?.content?.parts?.[0]?.text || JSON.stringify(response);
      }
      if (provider === AuthProvider.Anthropic) {
          return response.content?.[0]?.text || JSON.stringify(response);
      }

      // Default OpenAI structure (used by OpenAI, Grok, DeepSeek, etc.)
      return response.choices?.[0]?.message?.content || JSON.stringify(response);
  }
}
