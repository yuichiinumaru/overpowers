/**
 * Enforces reasoning ("thinking") behavior in models by injecting instructions into the system prompt.
 */
export function enforceReasoning(body: any, model?: string): any {
    if (!body || typeof body !== 'object') return body;

    const reasoningInstruction = "You are a reasoning model. Before answering, you must think step-by-step in a <thinking> block to analyze the user's request, plan your response, and verify your logic. Output the <thinking> block first, then your response.";

    const newBody = JSON.parse(JSON.stringify(body)); // Deep copy

    // Inject into system prompt (OpenAI/Anthropic style)
    if (newBody.messages && Array.isArray(newBody.messages)) {
        // Check if system message exists
        const systemMsgIndex = newBody.messages.findIndex((m: any) => m.role === 'system');

        if (systemMsgIndex > -1) {
            const existingContent = newBody.messages[systemMsgIndex].content;
            newBody.messages[systemMsgIndex].content = `${existingContent}\n\n${reasoningInstruction}`;
        } else {
            // Prepend system message
            newBody.messages.unshift({ role: 'system', content: reasoningInstruction });
        }
    }

    // Handle Anthropic specific top-level system
    if (newBody.system) {
         newBody.system = `${newBody.system}\n\n${reasoningInstruction}`;
    }

    return newBody;
}
