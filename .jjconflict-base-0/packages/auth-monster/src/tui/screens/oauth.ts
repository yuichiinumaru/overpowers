import { Navigation, ScreenController } from '../navigation';
import { Layout } from '../components/layout';
import { AuthProvider, ManagedAccount } from '../../core/types';
import { StrategyScreen } from './strategy';
import { generatePKCE } from '../../utils/oauth-server';
import { proxyFetch } from '../../core/proxy';
import * as blessed from 'blessed';
import * as crypto from 'crypto';

const ANTHROPIC_CLIENT_ID = "9d1c250a-e61b-44d9-88ed-5944d1962f5e";
const REDIRECT_URI = "http://localhost:1455/callback";

export class OAuthScreen implements ScreenController {
  private nav: Navigation;
  private queue: AuthProvider[] = [];
  private currentProvider: AuthProvider | null = null;
  private layout: Layout | null = null;
  private form: blessed.Widgets.FormElement<any> | null = null;
  
  // State for OAuth flows
  private pkceVerifier: string | null = null;
  private geminiClientId: string = "";
  private geminiClientSecret: string = "";

  constructor(nav: Navigation, context: any) {
    this.nav = nav;
    // Filter out duplicates if any
    this.queue = Array.from(new Set(context.selectedProviders || [])) as AuthProvider[];
  }

  render(layout: Layout): void {
    this.layout = layout;
    this.processNext();
  }

  private processNext() {
    if (this.queue.length === 0) {
        this.nav.navigate(StrategyScreen);
        return;
    }

    this.currentProvider = this.queue.shift() || null;
    if (!this.currentProvider) return;

    this.showConfigFor(this.currentProvider);
  }

  private showConfigFor(provider: AuthProvider) {
    if (!this.layout) return;
    
    this.layout.updateTitle(`Configure ${provider}`);
    
    // Clear previous elements
    this.layout.container.children.slice(1).forEach(c => c.destroy());
    if (this.form) {
        this.form.destroy();
        this.form = null;
    }

    if (provider === AuthProvider.Gemini) {
        this.renderGeminiSetup();
    } else if (provider === AuthProvider.Anthropic) {
        this.renderAnthropicFlow();
    } else {
        this.renderApiKeyFlow(provider);
    }
  }

  // Gemini requires Client ID/Secret first
  private renderGeminiSetup() {
      // Check if we have them in env (mocked here, in reality we check process.env)
      const envId = process.env.GEMINI_CLIENT_ID;
      const envSecret = process.env.GEMINI_CLIENT_SECRET;

      if (envId && envSecret) {
          this.geminiClientId = envId;
          this.geminiClientSecret = envSecret;
          this.renderGeminiFlow();
          return;
      }

      // Ask for them
      if (!this.layout) return;

      const info = blessed.box({
          parent: this.layout.container,
          top: 4,
          left: 2,
          right: 2,
          height: 3,
          content: 'Gemini requires a custom OAuth Client ID & Secret.\nCreate one at https://console.cloud.google.com/apis/credentials'
      });

      this.form = blessed.form({
          parent: this.layout.container,
          top: 8,
          left: 2,
          right: 2,
          keys: true
      });

      const idInput = blessed.textbox({
          parent: this.form,
          name: 'client_id',
          inputOnFocus: true,
          border: { type: 'line' },
          height: 3,
          label: ' Client ID ',
          top: 0
      });

      const secretInput = blessed.textbox({
          parent: this.form,
          name: 'client_secret',
          inputOnFocus: true,
          border: { type: 'line' },
          height: 3,
          label: ' Client Secret ',
          top: 4
      });
      
      const submit = blessed.button({
          parent: this.form,
          name: 'submit',
          content: ' Next ',
          top: 8,
          left: 0,
          shrink: true,
          padding: { left: 1, right: 1 },
          style: { bg: 'blue', fg: 'white', focus: { bg: 'green' } },
          border: { type: 'line' }
      });

      submit.on('press', () => {
         this.form?.submit();
      });

      this.form.on('submit', (data) => {
          this.geminiClientId = data.client_id;
          this.geminiClientSecret = data.client_secret;
          if (this.geminiClientId && this.geminiClientSecret) {
              this.renderGeminiFlow();
          } else {
              // Show error? For now just skip
              this.processNext();
          }
      });

      idInput.focus();
      this.layout.screen.render();
  }

  private async renderGeminiFlow() {
      if (!this.layout) return;
      this.layout.container.children.slice(1).forEach(c => c.destroy()); // clear form

      const pkce = await generatePKCE();
      this.pkceVerifier = pkce.verifier;
      
      const url = new URL("https://accounts.google.com/o/oauth2/v2/auth");
      url.searchParams.set("client_id", this.geminiClientId);
      url.searchParams.set("response_type", "code");
      url.searchParams.set("redirect_uri", REDIRECT_URI);
      url.searchParams.set("scope", "https://www.googleapis.com/auth/cloud-platform https://www.googleapis.com/auth/userinfo.email");
      url.searchParams.set("code_challenge", pkce.challenge);
      url.searchParams.set("code_challenge_method", "S256");
      url.searchParams.set("access_type", "offline");
      url.searchParams.set("prompt", "consent");

      this.renderAuthLink(url.toString(), async (code) => {
          // Exchange code
          try {
              const res = await proxyFetch("https://oauth2.googleapis.com/token", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: new URLSearchParams({
                    client_id: this.geminiClientId,
                    client_secret: this.geminiClientSecret,
                    code: code,
                    grant_type: "authorization_code",
                    redirect_uri: REDIRECT_URI,
                    code_verifier: this.pkceVerifier!
                })
              });
              
              if (!res.ok) throw new Error(await res.text());
              const json = await res.json() as any;
              
              // Get Email
              const userRes = await proxyFetch("https://www.googleapis.com/oauth2/v1/userinfo?alt=json", {
                  headers: { "Authorization": `Bearer ${json.access_token}` }
              });
              const userJson = userRes.ok ? await userRes.json() as any : { email: 'gemini@user' };

              this.saveAccount(AuthProvider.Gemini, {
                  accessToken: json.access_token,
                  refreshToken: json.refresh_token,
                  expiryDate: Date.now() + (json.expires_in * 1000),
                  tokenType: json.token_type
              }, undefined, userJson.email);
              
          } catch (e) {
               // Log error in context or show message?
          }
          this.processNext();
      });
  }

  private async renderAnthropicFlow() {
      const url = `https://console.anthropic.com/v1/oauth/authorize?response_type=code&client_id=${ANTHROPIC_CLIENT_ID}&redirect_uri=${encodeURIComponent(REDIRECT_URI)}&scope=offline_access`;
      
      this.renderAuthLink(url, async (code) => {
          try {
            const res = await proxyFetch("https://console.anthropic.com/v1/oauth/token", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    grant_type: "authorization_code",
                    code,
                    client_id: ANTHROPIC_CLIENT_ID,
                    redirect_uri: REDIRECT_URI,
                }),
            });
            
            if (!res.ok) throw new Error(await res.text());
            const json = await res.json() as any;
            
            this.saveAccount(AuthProvider.Anthropic, {
                  accessToken: json.access_token,
                  refreshToken: json.refresh_token,
                  expiryDate: Date.now() + (json.expires_in * 1000),
                  tokenType: json.token_type
            }, undefined, 'claude@user');

          } catch (e) {
              // Error handling
          }
          this.processNext();
      });
  }

  private renderAuthLink(url: string, onCode: (code: string) => void) {
      if (!this.layout) return;

      const instructions = blessed.box({
          parent: this.layout.container,
          top: 4,
          left: 2,
          right: 2,
          height: 6,
          content: `1. Open this URL in your browser:\n${url}\n\n2. If it redirects to localhost and fails, copy the 'code' parameter from the URL bar.\n3. Paste the code below:`
      });

      this.form = blessed.form({
          parent: this.layout.container,
          top: 11,
          left: 2,
          right: 2,
          keys: true
      });

      const input = blessed.textbox({
          parent: this.form,
          name: 'code',
          inputOnFocus: true,
          border: { type: 'line' },
          height: 3,
          label: ' Auth Code '
      });

      input.on('submit', (value) => {
          onCode(value);
      });
      
      input.focus();
      this.layout.screen.render();
  }

  private renderApiKeyFlow(provider: AuthProvider) {
      if (!this.layout) return;

      const instructions = blessed.box({
          parent: this.layout.container,
          top: 4,
          left: 2,
          right: 2,
          height: 3,
          content: `Enter API Key for ${provider}:`
      });

      this.form = blessed.form({
          parent: this.layout.container,
          top: 8,
          left: 2,
          right: 2,
          keys: true
      });

      const input = blessed.textbox({
          parent: this.form,
          name: 'apikey',
          inputOnFocus: true,
          censor: true,
          border: { type: 'line' },
          height: 3,
          label: ' API Key '
      });

      input.on('submit', (value) => {
          this.saveAccount(provider, { accessToken: value }, value);
          this.processNext();
      });

      input.focus();
      this.layout.screen.render();
  }

  private saveAccount(provider: AuthProvider, tokens: any, apiKey?: string, email?: string) {
      const accounts = this.nav.getContext()['accounts'] || [];
      const newAccount: ManagedAccount = {
          id: `${provider}-${Date.now()}`,
          email: email || 'manual@setup',
          provider: provider,
          tokens: tokens,
          apiKey: apiKey,
          isHealthy: true,
          metadata: {
              source: 'wizard'
          }
      };
      
      this.nav.updateContext('accounts', [...accounts, newAccount]);
  }

  destroy(): void {
      if (this.form) this.form.destroy();
  }
}
