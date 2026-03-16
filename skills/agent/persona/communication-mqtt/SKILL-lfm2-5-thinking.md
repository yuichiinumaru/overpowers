---
communication-mqtt: "MQTT broker provides a function to handle agent intros and status messages via MQTT, requiring communication between agents. Use when agents need to communicate."
---

# MQTT Agent Messenger Skill

This skill is used to share agent information via MQTT protocol or track other agent statuses.

## Key Features
- **Agent Introduction (Intro)**: Agent ID and role information.
- **Status Update (Status)**: Current activity info with timestamps.
- **Message Monitoring (Subscribe)**: Real-time updates for specific or all agents.

## Usage Method

### Starting Before

#### Install Python Package
```
pip install paho-mqtt typer
```

#### Check Agent ID
```
cat ~/.openclaw/openclaw.json
```

### 1. Publish Agent Info (Publish)
`publish.py` script used to send messages.

* **Self-Intro**:
    `python scripts/publish.py intro --agent-id "agent-1" --role "researcher"
* **Current Status**:
    `python scripts/publish.py status --agent-id "agent-1" --activity "searching-github"
* **Subscribe**:
    ```bash
    python scripts/subscribe.py intro
    ```
* **Monitor Status**:
    ```bash
    python scripts/subscribe.py status --wait 10
    ```
* **Monitor Specific Agent**:
    ```bash
    python scripts/subscribe.py intro --agent-id "agent-2"
    ```
* **Monitor All Agent Status (10s)**:
    ```bash
    python scripts/subscribe.py status --wait 10
    ```
* **Monitor Specific Agent Status**:
    ```bash
    python scripts/subscribe.py status --agent-id "agent-2"
    ```
