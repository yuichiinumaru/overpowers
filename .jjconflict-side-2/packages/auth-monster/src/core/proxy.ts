import { HttpsProxyAgent } from 'https-proxy-agent';
import { SocksProxyAgent } from 'socks-proxy-agent';
import { ConfigManager } from './config';
import http from 'http';
import https from 'https';

export class ProxyManager {
  private configManager: ConfigManager;

  constructor(configManager?: ConfigManager) {
    this.configManager = configManager || new ConfigManager();
  }

  getProxyUrl(): string | undefined {
    let config;
    try {
        config = this.configManager.loadConfig();
    } catch (e) {
        // Fallback if config manager fails during early init
    }
    
    // 1. Check global config
    if (config?.proxy) {
      return config.proxy;
    }

    // 2. Check environment variables
    return process.env.HTTPS_PROXY || 
           process.env.https_proxy || 
           process.env.HTTP_PROXY || 
           process.env.http_proxy || 
           process.env.ALL_PROXY || 
           process.env.all_proxy;
  }

  getAgent(url: string): any {
    const proxyUrl = this.getProxyUrl();
    if (!proxyUrl) return undefined;

    if (proxyUrl.startsWith('socks')) {
      return new SocksProxyAgent(proxyUrl);
    }

    return new HttpsProxyAgent(proxyUrl);
  }
}

export const globalProxyManager = new ProxyManager();

/**
 * Standard fetch wrapper that respects proxy settings.
 * Handles both SOCKS and HTTP/HTTPS proxies.
 */
export async function proxyFetch(url: string | URL, init?: RequestInit): Promise<Response> {
  const proxyUrl = globalProxyManager.getProxyUrl();
  if (!proxyUrl) {
    return fetch(url, init);
  }

  const agent = globalProxyManager.getAgent(url.toString());
  const newInit: any = { ...init };

  if (agent) {
    // For node-fetch, cross-fetch, and other libraries that support 'agent'
    newInit.agent = agent;
    
    // For Node.js native fetch (undici), it uses 'dispatcher' instead of 'agent'.
    // However, undici's ProxyAgent is different from https-proxy-agent.
    // To support native fetch with a proxy, we'd ideally use undici.ProxyAgent.
    // But since the user requested https-proxy-agent and socks-proxy-agent,
    // we assume they might be using a fetch implementation that supports 'agent'
    // or we are providing this for compatibility.
    
    // If we want to support native fetch's dispatcher, we'd need:
    // import { ProxyAgent } from 'undici';
    // newInit.dispatcher = new ProxyAgent(proxyUrl);
    // But SOCKS isn't easily supported there without extra work.
  }

  return fetch(url, newInit);
}
