#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 <WorkflowName>"
    exit 1
fi
echo "Scaffolding Temporal workflow: $1"
cat << TEMPLATE > "${1}Workflow.ts"
import { proxyActivities } from '@temporalio/workflow';
// import type * as activities from './activities';

// const { someActivity } = proxyActivities<typeof activities>({
//   startToCloseTimeout: '1 minute',
// });

export async function $1(params: any): Promise<any> {
  // Workflow implementation
  return "Done";
}
TEMPLATE
echo "Created ${1}Workflow.ts"
