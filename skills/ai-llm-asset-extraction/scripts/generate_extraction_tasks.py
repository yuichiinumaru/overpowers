import os
import json
import math

STAGING_MANIFEST = "/home/sephiroth/Work/overpowers/.archive/staging/manifest.json"
TASKS_DIR = "/home/sephiroth/Work/overpowers/.docs/tasks"
TASKLIST_FILE = "/home/sephiroth/Work/overpowers/.docs/tasklist.json"
BATCH_SIZE = 25

TEMPLATE = """# Extraction Task: {task_id}

**Batch Type:** {category}
**Total Items:** {item_count}

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/{category}/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets {task_id}` to execute this task or follow these manual steps for each item:

1. **Read & Analyze**: Read the staged file to understand its purpose.
2. **Format & Standardize**: 
   - Inject the appropriate YAML frontmatter (name, description, tags, version: 1.0.0).
   - Ensure the name follows the standard convention (e.g., `domain-subdomain-name`).
   - Fix any broken internal links or outdated formatting.
3. **Move to Destination**: Save the formatted file to its final destination:
   - Skills -> `skills/<domain>-<subdomain>-<name>/SKILL.md`
   - Agents -> `agents/ovp-<name>.md`
   - Workflows -> `workflows/ovp-<name>.md`
4. **Clean Up**: Delete the file from the staging folder.
5. **Check off**: Mark the checkbox below.

## Batch Items

{checkboxes}

---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
"""

def generate_tasks():
    if not os.path.exists(STAGING_MANIFEST):
        print(f"Manifest not found at {STAGING_MANIFEST}. Run deduplicate_candidates.py first.")
        return
        
    with open(STAGING_MANIFEST, 'r') as f:
        manifest = json.load(f)
        
    os.makedirs(TASKS_DIR, exist_ok=True)
    
    # Load existing tasklist to append to it
    with open(TASKLIST_FILE, 'r') as f:
        tasklist_data = json.load(f)
        
    new_task_paths = []
    task_counter = 0
    
    for category, items in manifest.items():
        if not items:
            continue
            
        num_batches = math.ceil(len(items) / BATCH_SIZE)
        print(f"Generating {num_batches} tasks for {len(items)} {category}...")
        
        for b in range(num_batches):
            task_counter += 1
            batch_items = items[b * BATCH_SIZE : (b + 1) * BATCH_SIZE]
            
            task_id = f"0500-extraction-{category}-batch-{str(b+1).zfill(3)}"
            task_file = f"{task_id}.md"
            task_path = os.path.join(TASKS_DIR, task_file)
            
            checkboxes = ""
            for item in batch_items:
                staged_path = item['staged_path']
                # Make path relative for the markdown
                rel_path = staged_path.split("overpowers/")[1] if "overpowers/" in staged_path else staged_path
                checkboxes += f"- [ ] `{rel_path}` (Original: {item['name']})\n"
                
            content = TEMPLATE.format(
                task_id=task_id,
                category=category,
                item_count=len(batch_items),
                checkboxes=checkboxes
            )
            
            with open(task_path, 'w') as f:
                f.write(content)
                
            new_task_paths.append(f".docs/tasks/{task_file}")

    # Append new tasks to tasklist.json
    if new_task_paths:
        existing_tasks = tasklist_data.get("tasks", [])
        if existing_tasks:
            # Add to the first list of tasks
            current_list = existing_tasks[0].get("task", [])
            for tp in new_task_paths:
                if tp not in current_list:
                    current_list.append(tp)
            current_list.sort() # Keep it tidy
            existing_tasks[0]["task"] = current_list
        else:
            tasklist_data["tasks"] = [{"prompt": "prompts/foreman.json", "task": sorted(new_task_paths)}]
            
        with open(TASKLIST_FILE, 'w') as f:
            json.dump(tasklist_data, f, indent=2)
            
    print(f"\nGenerated {task_counter} task files in {TASKS_DIR}")
    print(f"Updated {TASKLIST_FILE} with {len(new_task_paths)} new task references.")

if __name__ == "__main__":
    generate_tasks()
