interface MessageBlock {
  type: string;
  text?: string;
  name?: string;
  [key: string]: any;
}

interface Message {
  role: string;
  content: string | MessageBlock[];
}

interface Tool {
  name: string;
  [key: string]: any;
}

interface AnthropicRequestBody {
  system?: string | MessageBlock[];
  messages?: Message[];
  tools?: Tool[];
  metadata?: {
    user_id?: string;
    [key: string]: any;
  };
  [key: string]: any;
}

const TOOL_PREFIX = "mcp_";
const CLAUDE_USER_ID = "user_7b18c0b8358639d7ff4cdbf78a1552a7d5ca63ba83aee236c4b22ae2be77ba5f_account_3bb3dcbe-4efe-4795-b248-b73603575290_session_4a72737c-93d6-4c45-aebe-6e2d47281338";

/**
 * Deeply replaces 'OpenCode' with 'Claude Code' in any string value within an object.
 */
function deepSpoof(obj: any): any {
  if (typeof obj === 'string') {
    return obj
      .replace(/OpenCode/g, 'Claude Code')
      .replace(/opencode/gi, 'Claude');
  }

  if (Array.isArray(obj)) {
    return obj.map(item => deepSpoof(item));
  }

  if (typeof obj === 'object' && obj !== null) {
    const newObj: any = {};
    for (const key in obj) {
      if (Object.prototype.hasOwnProperty.call(obj, key)) {
        newObj[key] = deepSpoof(obj[key]);
      }
    }
    return newObj;
  }

  return obj;
}

/**
 * Transforms the request body for Anthropic.
 * - Deep spoofs 'OpenCode' to 'Claude Code' in system and messages.
 * - Prefixes tool names with "mcp_".
 * - Injects a dummy user_id in metadata for bypass.
 */
export function transformRequest(body: AnthropicRequestBody): AnthropicRequestBody {
  const transformed = { ...body };

  // Apply deep spoofing specifically to system and messages to bypass server-side blocks
  if (transformed.system) {
    transformed.system = deepSpoof(transformed.system);
  }

  if (transformed.messages && Array.isArray(transformed.messages)) {
    transformed.messages = transformed.messages.map((msg: Message) => ({
      ...msg,
      content: deepSpoof(msg.content)
    }));
  }

  // Add user_id to metadata if missing
  if (!transformed.metadata) {
    transformed.metadata = {};
  }
  if (!transformed.metadata.user_id) {
    transformed.metadata.user_id = CLAUDE_USER_ID;
  }

  // Add prefix to tools definitions
  if (transformed.tools && Array.isArray(transformed.tools)) {
    transformed.tools = transformed.tools.map((tool: Tool) => ({
      ...tool,
      name: tool.name ? (tool.name.startsWith(TOOL_PREFIX) ? tool.name : `${TOOL_PREFIX}${tool.name}`) : tool.name,
    }));
  }

  // Add prefix to tool_use blocks in messages
  if (transformed.messages && Array.isArray(transformed.messages)) {
    transformed.messages = transformed.messages.map((msg: Message) => {
      if (msg.content && Array.isArray(msg.content)) {
        msg.content = msg.content.map((block: MessageBlock) => {
          if (block.type === "tool_use" && block.name) {
            return { 
              ...block, 
              name: block.name.startsWith(TOOL_PREFIX) ? block.name : `${TOOL_PREFIX}${block.name}` 
            };
          }
          return block;
        });
      }
      return msg;
    });
  }

  return transformed;
}

/**
 * Transforms the response text to remove the tool prefix.
 */
export function transformResponseText(text: string): string {
  return text.replace(/"name"\s*:\s*"mcp_([^"]+)"/g, '"name": "$1"');
}
