#!/usr/bin/env python3
import sys

WORKFLOWS = {
    "booking": [
        "CAL_GET_AVAILABLE_SLOTS_INFO (check slots)",
        "Present slots to user",
        "CAL_POST_NEW_BOOKING_REQUEST (create booking)"
    ],
    "webhooks": [
        "CAL_RETRIEVE_WEBHOOKS_LIST",
        "CAL_UPDATE_WEBHOOK_BY_ID or CAL_POST_NEW_WEBHOOK (configure)"
    ],
    "teams": [
        "CAL_GET_TEAMS_LIST",
        "CAL_RETRIEVE_TEAM_EVENT_TYPES (id=<team_id>)"
    ]
}

def main():
    if len(sys.argv) < 2:
        print("Usage: cal_com_helper.py [booking|webhooks|teams]")
        sys.exit(1)
        
    workflow = sys.argv[1]
    if workflow in WORKFLOWS:
        print(f"--- Cal.com Workflow: {workflow} ---")
        for i, step in enumerate(WORKFLOWS[workflow], 1):
            print(f"{i}. {step}")
    else:
        print(f"Unknown workflow: {workflow}")

if __name__ == "__main__":
    main()
