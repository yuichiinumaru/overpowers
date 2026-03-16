import os
import argparse

def scaffold_app(project_name):
    print(f"🏗️ Scaffolding LLM Application: {project_name}")
    
    dirs = [
        "src",
        "src/api",
        "src/rag",
        "src/utils",
        "tests"
    ]
    
    for d in dirs:
        os.makedirs(os.path.join(project_name, d), exist_ok=True)
        
    # Create sample files based on SKILL.md patterns
    files = {
        "src/api/openai.ts": """import OpenAI from 'openai';

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

export async function chat(messages: any[]): Promise<string> {
  const response = await openai.chat.completions.create({
    model: 'gpt-4',
    messages,
    temperature: 0.7,
  });
  return response.choices[0].message.content ?? '';
}""",
        "src/rag/pipeline.ts": """export async function ragQuery(question: string): Promise<string> {
  // 1. Embed, 2. Search, 3. Build Context, 4. Generate
  console.log('Running RAG query for:', question);
  return 'Grounded answer';
}""",
        "src/utils/chunking.ts": """export function chunkDocument(text: string, size = 1000, overlap = 200): string[] {
  const chunks = [];
  let start = 0;
  while (start < text.length) {
    chunks.push(text.slice(start, start + size));
    start += size - overlap;
  }
  return chunks;
}""",
        "package.json": f"""{{
  "name": "{project_name}",
  "version": "1.0.0",
  "dependencies": {{
    "openai": "^4.0.0",
    "@anthropic-ai/sdk": "^0.20.0"
  }}
}}"""
    }
    
    for path, content in files.items():
        full_path = os.path.join(project_name, path)
        with open(full_path, 'w') as f:
            f.write(content)
            
    print(f"✅ Application scaffolded in ./{project_name}")

def main():
    parser = argparse.ArgumentParser(description='Scaffold a boilerplate LLM application')
    parser.add_argument('name', help='Project name')
    
    args = parser.parse_args()
    scaffold_app(args.name)

if __name__ == "__main__":
    main()
