import os

def fix_file(path, old, new):
    with open(path, "r") as f:
        content = f.read()
    content = content.replace(old, new)
    with open(path, "w") as f:
        f.write(content)

fix_file('.agents/knowledge/kb_agent_orchestration_core.json',
         '"select_pattern": "ORCH-PAT-HRM-01", "expected_latency_ms": 1000 }\n      }\n      {',
         '"select_pattern": "ORCH-PAT-HRM-01", "expected_latency_ms": 1000 }\n      },\n      {')

fix_file('.agents/knowledge/kb_agent_reasoning_validation.json',
         '"plan_coverage": null, "alignment_score": null },\n        "alignment_score": null\n        "test_cases": [\n          {\n            "input": {\n            "high_level_plan": ["step1","step2"], "execution_trace": "..." },\n            "expected": { "coverage": 1.0 }\n            "execution_trace": "..."\n    },',
         '"plan_coverage": null, "alignment_score": null\n      },\n      "test_cases": [\n        {\n          "input": { "high_level_plan": ["step1","step2"], "execution_trace": "..." },\n          "expected": { "coverage": 1.0 }\n        }\n      ]\n    },')

fix_file('.agents/knowledge/kb_autocontinue.json',
         '"cross_references": ["kb_model_evolution_playbook"] }\n      { "id": "chunk_pbr_02"',
         '"cross_references": ["kb_model_evolution_playbook"] },\n      { "id": "chunk_pbr_02"')
fix_file('.agents/knowledge/kb_autocontinue.json',
         '"kb_autocontinue#context_rot_mitigation.mitigation_strategies.mitigate_sentinel_feedback"] }\n  },',
         '"kb_autocontinue#context_rot_mitigation.mitigation_strategies.mitigate_sentinel_feedback"] }\n    ]\n  },')

fix_file('.agents/knowledge/kb_common_schemas.json',
         '      "properties": {/* existing definition */},\n      "required": [/* existing fields */]',
         '      "properties": {},\n      "required": []')
fix_file('.agents/knowledge/kb_common_schemas.json', '"ContextManifest": {/* existing */},', '"ContextManifest": {},')
fix_file('.agents/knowledge/kb_common_schemas.json', '"ProblemSpec": {/* existing */},', '"ProblemSpec": {},')
fix_file('.agents/knowledge/kb_common_schemas.json', '"SolutionArtifact": {/* existing */},', '"SolutionArtifact": {},')
fix_file('.agents/knowledge/kb_common_schemas.json', '"TelemetryFrame": {/* existing */},', '"TelemetryFrame": {},')
fix_file('.agents/knowledge/kb_common_schemas.json', '"RiskFrame": {/* existing */},', '"RiskFrame": {},')
fix_file('.agents/knowledge/kb_common_schemas.json', '"WorkflowEvent": {/* existing */},', '"WorkflowEvent": {},')
fix_file('.agents/knowledge/kb_common_schemas.json', '"HRM_TaskProfile": {/* existing */},', '"HRM_TaskProfile": {},')
fix_file('.agents/knowledge/kb_common_schemas.json', '"HRM_SolutionArtifact": {/* existing */},', '"HRM_SolutionArtifact": {},')

fix_file('.agents/knowledge/kb_problem_solving_network.json',
         '    { "id": "PSN-EXPLAIN-01", "name": "Explainability & Replayability", "description": "Deterministic traces/proofs + seed logging." }\n    {\n      "principle_id": "PSN-HRM-01",',
         '    { "id": "PSN-EXPLAIN-01", "name": "Explainability & Replayability", "description": "Deterministic traces/proofs + seed logging." },\n    {\n      "principle_id": "PSN-HRM-01",')

fix_file('.agents/knowledge/kb_reasoning_knowledge_base.json',
         '    "context_rot": "kb_autocontinue#context_rot_mitigation",\n    "hrm_model": "kb_problem_solving_network#solver_library.psn.ml.hrm_v1"\n    "hrm_model": "kb_psn_lexsupremus#definitions.HRM"\n  },',
         '    "context_rot": "kb_autocontinue#context_rot_mitigation",\n    "hrm_model_v1": "kb_problem_solving_network#solver_library.psn.ml.hrm_v1",\n    "hrm_model": "kb_psn_lexsupremus#definitions.HRM"\n  },')

