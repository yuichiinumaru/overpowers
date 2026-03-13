import re

def fix_file(file, fixes):
    with open(file, 'r') as f:
        content = f.read()
        
    for old, new in fixes:
        content = content.replace(old, new)
        
    with open(file, 'w') as f:
        f.write(content)

fix_file('.agents/knowledge/kb_autocontinue.json', [
    ('mitigate_sentinel_feedback"] }\n  },', 'mitigate_sentinel_feedback"] }\n    ]\n  },'),
    ('"cross_references": ["kb_model_evolution_playbook"] }\n      { "id": "chunk_pbr_02"',
     '"cross_references": ["kb_model_evolution_playbook"] },\n      { "id": "chunk_pbr_02"')
])

fix_file('.agents/knowledge/kb_problem_solving_network.json', [
    ('    ]\n{\n  "solver_id": "psn.ml.hrm_v1",', '    ],\n  "hrm_model": {\n  "solver_id": "psn.ml.hrm_v1",'),
    (' "Explainability & Replayability", "description": "Deterministic traces/proofs + seed logging." }\n    {\n      "principle_id": "PSN-HRM-01"',
     ' "Explainability & Replayability", "description": "Deterministic traces/proofs + seed logging." },\n    {\n      "principle_id": "PSN-HRM-01"')
])

fix_file('.agents/knowledge/kb_reasoning_knowledge_base.json', [
    (' "branching_factor": 2 } }\n      { "profile_id":"PROF-PSN-HIGH-QUALITY"',
     ' "branching_factor": 2 } },\n      { "profile_id":"PROF-PSN-HIGH-QUALITY"'),
    (' "kb_problem_solving_network#solver_library.psn.ml.hrm_v1"\n    "hrm_model":',
     ' "kb_problem_solving_network#solver_library.psn.ml.hrm_v1",\n    "hrm_model":')
])
