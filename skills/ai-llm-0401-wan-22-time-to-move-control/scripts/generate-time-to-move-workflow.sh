#!/bin/bash
# Generate Time-To-Move ComfyUI workflow
echo "Generating Time-To-Move motion control workflow..."
cat << 'WORKFLOW_CONTENT' > time_to_move_workflow.json
{
  "description": "ComfyUI workflow for Wan 2.2 using Time-To-Move for precise motion control."
}
WORKFLOW_CONTENT
echo "Workflow saved to time_to_move_workflow.json"
