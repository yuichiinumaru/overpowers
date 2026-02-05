import { AuthProvider, ManagedAccount } from './types';

export function getProviderEndpoint(provider: AuthProvider, account?: ManagedAccount, model?: string): string {
    switch (provider) {
        case AuthProvider.Anthropic:
            return account?.apiKey
                ? "https://api.anthropic.com/v1/messages"
                : "https://console.anthropic.com/api/v1/messages";
        case AuthProvider.Gemini:
            // Gemini requires model in URL often
            const modelName = model || account?.metadata?.model || 'gemini-2.0-flash';
            return `https://generativelanguage.googleapis.com/v1beta/models/${modelName}:generateContent`;
        case AuthProvider.OpenAI:
        case AuthProvider.Copilot: // Copilot is often OpenAI compatible or routed via GitHub
            return "https://api.openai.com/v1/chat/completions";
        case AuthProvider.Qwen:
            return "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions";
        case AuthProvider.Zhipu:
            return "https://open.bigmodel.cn/api/paas/v4/chat/completions";
        case AuthProvider.Minimax:
            return "https://api.minimax.chat/v1/text/chatcompletion_v2";

        // New Providers
        case AuthProvider.DeepSeek:
            return "https://api.deepseek.com/chat/completions";
        case AuthProvider.Grok:
            return "https://api.x.ai/v1/chat/completions";
        case AuthProvider.Azure:
            if (account?.metadata?.resourceName && account?.metadata?.deploymentId) {
                return `https://${account.metadata.resourceName}.openai.azure.com/openai/deployments/${account.metadata.deploymentId}/chat/completions?api-version=2023-05-15`;
            }
            return "https://api.openai.azure.com/";

        // For Cursor and Windsurf, since they use gRPC/Proto and AuthMonster doesn't fully abstract the protocol conversion
        // from JSON to Proto for 'request()', we might return a dummy URL or handle it if we knew the JSON proxy.
        // For now, we return a URL that might work if there's a JSON bridge, otherwise it might fail.
        case AuthProvider.Cursor:
            return "https://api2.cursor.sh/llm/chat";
        case AuthProvider.Windsurf:
            return "https://codeium.com/api/v1/chat";

        default:
            return "https://api.openai.com/v1/chat/completions";
    }
}
