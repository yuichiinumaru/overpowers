const fs = require('fs');

const files = [
  '.agents/knowledge/kb_agent_orchestration_core.json',
  '.agents/knowledge/kb_autocontinue.json',
  '.agents/knowledge/kb_problem_solving_network.json',
  '.agents/knowledge/kb_reasoning_knowledge_base.json',
  '.agents/knowledge/kb_agent_reasoning_validation.json'
];

files.forEach(f => {
  try {
    JSON.parse(fs.readFileSync(f, 'utf8'));
    console.log(f + ': OK');
  } catch (e) {
    console.log(f + ': ERROR: ' + e.message);
  }
});
