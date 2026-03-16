#!/usr/bin/env python3
import sys

WORKFLOWS = {
    "list_employees": [
        "BAMBOOHR_GET_ALL_EMPLOYEES (no params)",
        "BAMBOOHR_GET_EMPLOYEE (id=<numeric_id>, fields='firstName,lastName,...')"
    ],
    "track_changes": [
        "BAMBOOHR_EMPLOYEE_GET_CHANGED (since=<ISO8601_date>, type='inserted|updated|deleted')"
    ],
    "manage_time_off": [
        "BAMBOOHR_GET_META_TIME_OFF_TYPES",
        "BAMBOOHR_GET_TIME_OFF_BALANCES (employeeId=<id>)",
        "BAMBOOHR_GET_TIME_OFF_REQUESTS (start=<date>, end=<date>, employeeId=<id>)",
        "BAMBOOHR_CREATE_TIME_OFF_REQUEST (employeeId=<id>, timeOffTypeId=<id>, start=<date>, end=<date>)",
        "BAMBOOHR_UPDATE_TIME_OFF_REQUEST (requestId=<id>, status='approved|denied|cancelled')"
    ]
}

def show_workflow(name):
    if name not in WORKFLOWS:
        print(f"Unknown workflow. Available: {', '.join(WORKFLOWS.keys())}")
        return
    
    print(f"--- BambooHR Workflow: {name} ---")
    for i, step in enumerate(WORKFLOWS[name], 1):
        print(f"{i}. {step}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <workflow_name>")
        print(f"Available workflows: {', '.join(WORKFLOWS.keys())}")
        sys.exit(1)
        
    show_workflow(sys.argv[1])
