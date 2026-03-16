---
name: vetmew-consultation
description: "Professional multi-turn medical consultation for pets (cats, dogs, and exotic animals). Provides symptom analysis and diagnostic suggestions based on the VetMew 3.0 API."
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# VetMew Pet Consultation Skill

## Introduction
This is a professional pet consultation skill integrated with the VetMew Open Platform. It can handle complex pet profiles (covering dogs, cats, and exotic pets like chinchillas, guinea pigs, etc.) and provides professional medical consultation advice for pets by calling deep learning models with HMAC-SHA256 security authentication.

## Setup (Automated / Environment Priority)

This skill prioritizes automated configuration via environment variables.

### 1. Automated Environment (OpenClaw / Agent Framework)
In environments like OpenClaw, the skill has declared the requirement for `VETMEW_AUTH_TOKEN` through metadata. **You only need to enter the credentials in the skill settings interface of the platform**, and the system will automatically inject them into the runtime environment.

- **Credential Format**: `API_KEY:API_SECRET` (separated by a colon).

### 2. Runtime Requirements
- **Python**: Version 3.12 or higher is required.
- **Dependency Installation**: `pip install -r requirements.txt` (usually handled by the platform in an automated environment).

> If you need to manually configure in a local development environment, please refer to the [Appendix: Manual Credential Setup](#appendix-manual-credential-setup) at the end of the document.

## Usage

> **Note**: Before executing the following scripts, ensure that the current working directory (CWD) is the root directory where the script is located.

### 1. Pet Medical Consultation
`python3 scripts/consultation.py --name <name> --breed <breed> --pet_type <pet_type> --birth <YYYY-MM-DD> --gender <1|2> --fertility <1|2> [--msg <question>] [--image <base64>] [--image_url <url>] [--image_type <1-6>] [--conversation_id <id>] [--thinking]`

### 2. Pet Care Knowledge Q&A (Lightweight)
`python3 scripts/free_chat.py --msg <question> [--online] [--conversation_id <id>]`

### 3. Exotic Pet Medical Consultation
`python3 scripts/exotic_consultation.py --name <name> --breed <breed> --pet_type 3 --gender <1|2> --msg <question> [--conversation_id <id>] [--thinking]`

## Input Parameters

### 1. Medical Consultation Parameters (Only for `consultation.py`)
- `--name`: **Pet Nickname** (String). The common name of the pet in the family.
- `--breed`: **Breed Name** (String). Must be a standard Chinese breed name, such as "Golden Retriever", "Ragdoll Cat".
- `--pet_type`: **Pet Type** (String). "1" for cat, "2" for dog. Must be consistent with the species of the breed.
- `--birth`: **Date of Birth** (YYYY-MM-DD). Used to calculate the pet's physiological stage.
- `--gender`: **Gender** (Integer). 1 for male, 2 for female.
- `--fertility`: **Neutered Status** (Integer). 1 for not neutered, 2 for neutered.
- `--msg`: **User Question / Symptom Description** (String). Optional when an image is provided.
- `--image`: **Image Base64 Data** (String). Base64 encoded string with the header removed.
- `--image_url`: **Image URL** (String). Publicly accessible link to the image.
- `--image_type`: **Visual Analysis Type** (Integer).
    - **1**: Emotion Analysis
    - **2**: Vomit Analysis
    - **3**: Stool Analysis
    - **4**: Urine Analysis
    - **5**: Skin Analysis
    - **6**: Ear Canal Analysis
- `--thinking`: **Deep Thinking Switch** (Flag). When enabled, the API will return more detailed reasoning logic (Deep Thinking).

### 2. Exotic Pet Consultation Parameters (Only for `exotic_consultation.py`)
- `--name`: **Pet Nickname** (String).
- `--breed`: **Breed Name** (String). e.g., "Chinchilla", "Guinea Pig", "Squirrel".
- `--pet_type`: **Pet Type** (String). Must be fixed to "3".
- `--gender`: **Gender** (Integer). 1 for male, 2 for female.
- `--thinking`: **Deep Thinking Switch** (Flag).

### 3. Knowledge Q&A Parameters (Only for `free_chat.py`)
- `--msg`: **User Question** (String). Maximum length 200 characters.
- `--online`: **Web Search Switch** (Flag). When enabled, the AI will retrieve the latest online information to answer.

### 3. General Interaction Information
- `--msg`: **User Question / Symptom Description** (String). Please describe the pet's mental state, diet, excretion, and other abnormal symptoms in as much detail as possible.
- `--conversation_id`: **Conversation ID** (Optional). In multi-turn conversations, the Agent should automatically extract and pass this ID to maintain context. **Note: Ensure the passed ID is consistent with the currently triggered script path (medical vs. Q&A).**

## Steps (Workflow)

1. **Intent Recognition**: This skill is triggered when a user expresses concern about their pet's health or seeks professional advice.
2. **Slot Mapping (Session Slotting)**: The Agent **must** maintain three independent slots to isolate conversations. **In OpenClaw, please persist these to the corresponding variables**:
    - `VETMEW_MEDICAL_SESSION`: Stores the ID from `consultation.py`.
    - `VETMEW_EXOTIC_SESSION`: Stores the ID from `exotic_consultation.py`.
    - `VETMEW_CHAT_SESSION`: Stores the ID from `free_chat.py`.
3. **Parameter Collection**: The Agent checks for required parameters. If the user has not mentioned the breed or age (for dogs and cats), the Agent must proactively ask for this information.
4. **Runtime Environment Ready**: Ensure dependencies are installed according to the `metadata.openclaw.install` specification and environment variables are correctly obtained.
5. **Streaming Consumption**: Parse SSE data chunks from VetMew in real-time, extract the `msg` content, and render it to the user immediately.
6. **State Capture and Synchronization**: When the script finishes normally, print `CONVERSATION_ID: <id>`.
    - **Agent Action**: Must extract this ID and update it to the corresponding Session slot mentioned above, so it can be automatically reused via `--conversation_id` in the next turn.
7. **Exception Fallback**: If the script returns an error like "Invalid session or isolation conflict", the Agent must clear the old ID from the corresponding slot and prompt the user to initiate a new conversation.

## Output (Example Output)

### Diagnosing (Streaming Markdown)
> "Based on the vomiting frequency of **Dahuang** (Golden Retriever, 8 months old, not neutered), there is a preliminary indication of acute gastritis risk. Recommendations:
> 1. **Withhold food for 12 hours**: Observe if vomiting continues.
> 2. **Monitor energy levels**: If accompanied by diarrhea or fever, seek veterinary attention immediately."

### Diagnosis Complete (Status Indicator)
> "--------------------"
> "CONVERSATION_ID: v2-chat-session-88291"

## Guardrails

- **Breed Mapping Restriction**: If the input breed cannot be found in the official library, the script will return an error and ask the user to correct it.
- **Species Matching Validation**: The system will validate if the breed belongs to the specified `pet_type`. Cross-species consultations are prohibited.
- **Security Redline**: It is strictly forbidden to include any API keys or raw signature strings in the output.
- **Medical Disclaimer**: The output content is for reference only. In critical situations, users must be guided to visit an offline veterinary hospital.

## Appendix: Manual Credential Setup

If you need to manually configure credentials in a local CLI environment, follow these steps.

### 1. Obtain Credentials
Please go to the [VetMew Open Platform](https://open.vetmew.com/) to apply for `API_KEY` and `API_SECRET`.

### 2. Initialize Configuration
Run any entry script directly (e.g., `consultation.py`). The system will detect missing credentials and automatically launch a configuration wizard:
1. Follow the terminal prompts to enter your `API_KEY` and `API_SECRET`.
2. The system will automatically create a `.env` file in the current directory and merge the credentials into `VETMEW_AUTH_TOKEN`.
3. After configuration is complete, you can use it normally.

> **Security Tip**: Do not commit the generated `.env` file containing real keys to your version control system.

## Technical Dependencies
- Python 3.12+
- `requests`, `python-dotenv`
- `consultation.py` (main program)
- `breed_manager.py` (breed management)
