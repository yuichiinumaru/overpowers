#!/usr/bin/env python3
"""
EvDD Validation Script - Validates skills against JSON schemas
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml
from jsonschema import validate, ValidationError

# Base paths
WORKSPACE_ROOT = Path(__file__).parent.parent
SCHEMAS_DIR = WORKSPACE_ROOT / ".agents" / "schemas"

# Schema paths
FRONTMATTER_SCHEMA_PATH = SCHEMAS_DIR / "skill_frontmatter.schema.json"
EVALS_SCHEMA_PATH = SCHEMAS_DIR / "evals.schema.json"
OPENAI_YAML_SCHEMA_PATH = SCHEMAS_DIR / "openai_yaml.schema.json"


def load_schema(schema_path: Path) -> Dict:
    with open(schema_path, "r") as f:
        return json.load(f)


def validate_json(data: Dict, schema: Dict) -> List[str]:
    errors = []
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        # Extract a more readable error message
        path = " -> ".join([str(p) for p in e.path]) if e.path else "root"
        errors.append(f"[{path}] {e.message}")
    return errors


def validate_skill_frontmatter(skill_path: Path, schema: Dict) -> List[str]:
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return ["SKILL.md missing"]

    content = skill_md.read_text()
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return ["Invalid or missing YAML frontmatter in SKILL.md"]

    try:
        frontmatter = yaml.safe_load(match.group(1))
        if not isinstance(frontmatter, dict):
            return ["Frontmatter must be a YAML dictionary"]
    except yaml.YAMLError as e:
        return [f"YAML parsing error: {e}"]

    return validate_json(frontmatter, schema)


def validate_evals(skill_path: Path, schema: Dict) -> List[str]:
    evals_json_path = skill_path / "evals" / "evals.json"
    if not evals_json_path.exists():
        # Evals are optional but recommended
        return []

    try:
        with open(evals_json_path, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return [f"evals/evals.json: JSON parsing error: {e}"]

    return validate_json(data, schema)


def validate_openai_yaml(skill_path: Path, schema: Dict) -> List[str]:
    openai_yaml_path = skill_path / "agents" / "openai.yaml"
    if not openai_yaml_path.exists():
        return []

    try:
        with open(openai_yaml_path, "r") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return [f"agents/openai.yaml: YAML parsing error: {e}"]

    return validate_json(data, schema)


def validate_skill(skill_path: Path) -> Dict:
    """Run all validations for a single skill"""
    results = {
        "skill_name": skill_path.name,
        "path": str(skill_path.relative_to(WORKSPACE_ROOT)),
        "errors": [],
        "valid": True
    }

    # Load schemas
    fm_schema = load_schema(FRONTMATTER_SCHEMA_PATH)
    evals_schema = load_schema(EVALS_SCHEMA_PATH)
    openai_schema = load_schema(OPENAI_YAML_SCHEMA_PATH)

    # Run validations
    results["errors"].extend(validate_skill_frontmatter(skill_path, fm_schema))
    results["errors"].extend(validate_evals(skill_path, evals_schema))
    results["errors"].extend(validate_openai_yaml(skill_path, openai_schema))

    if results["errors"]:
        results["valid"] = False

    return results


def main():
    if len(sys.argv) > 1:
        target_paths = [Path(p).resolve() for p in sys.argv[1:]]
    else:
        # Default to all skills
        skills_dir = WORKSPACE_ROOT / "skills"
        target_paths = sorted([p.resolve() for p in skills_dir.iterdir() if p.is_dir()])

    total_skills = 0
    invalid_skills = 0
    all_results = []

    for path in target_paths:
        if not path.is_dir():
            if (path / "SKILL.md").exists() or (path.parent / "SKILL.md").exists():
                # It might be a specific path to a skill or its parent
                pass
            else:
                continue
        
        # Check if it's actually a skill dir
        if not (path / "SKILL.md").exists():
            # If target was 'skills/', it shouldn't try to validate non-skill subdirs
            if path.parent.name == "skills":
                # Some subdirectories in 'skills/' might not be skills yet (e.g. legacy structure)
                pass
            else:
                continue

        total_skills += 1
        result = validate_skill(path)
        all_results.append(result)
        
        if not result["valid"]:
            invalid_skills += 1
            print(f"❌ {result['path']}")
            for err in result["errors"]:
                print(f"  - {err}")
        else:
            # Only print valid ones if specifically requested or if only a few
            if len(target_paths) < 10:
                print(f"✅ {result['path']}")

    print(f"\nSummary: {total_skills} skills checked, {invalid_skills} invalid.")
    sys.exit(1 if invalid_skills > 0 else 0)


if __name__ == "__main__":
    main()
