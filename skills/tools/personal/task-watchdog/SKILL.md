---
name: sys-admin-task-watchdog
description: Monitors long-running background tasks, automatically dismisses disruptive system or ad popups, and sends alerts if the task hangs or crashes.
tags: [monitoring, task-automation, popup-killer, error-alert]
version: 1.0.0
---

# Task Watchdog

## 🎯 Core Objective
When a user initiates a task that requires hours to complete (e.g., rendering video, big data processing, large file download) and leaves their computer, you are to act as a "security guard" and take over the screen. Your responsibility is to ensure the progress bar keeps moving and to relentlessly close any pop-up windows that attempt to interrupt the task.

## 💡 Trigger Conditions
The user issues a command after starting a time-consuming task:
* "I'm leaving work, please keep an eye on this rendering task and close any pop-ups."
* "Activate pop-up killer mode until the download is complete."

## 📋 Execution Steps

### Step 1: Lock Onto the Target Progress
Use visual capabilities to identify the main task window on the current screen. Lock onto the "progress bar," "percentage number," or "estimated time remaining" as the core monitoring target.

### Step 2: Periodic Inspection and Threat Neutralization (Core Loop)
Enter a dormant state. Wake up every 5 minutes to perform the following checks:
1.  **Pop-up Scan:** Check if there are any intrusive windows on the screen that are overlaying the target window (e.g., "System Update Prompt," "Low Memory Warning," "Antivirus Advertisement," "Software Registration Prompt").
2.  **Elimination Execution:** If an irrelevant pop-up is detected, immediately identify its "X" button in the top-right corner, or buttons like "Remind Me Later," "Close," or "Ignore," and simulate a mouse click to close it.
3.  **Progress Confirmation:** Check if the target progress bar is advancing normally. If the progress percentage shows no change for 3 consecutive checks (15 minutes), determine that the task is stuck and proceed to Step 3.

### Step 3: Critical Anomaly Response
If an unclosable pop-up is encountered (e.g., a precursor to a system blue screen/kernel crash), or if the software completely crashes or the progress bar freezes:
1.  Immediately take a full screenshot of the current screen.
2.  Invoke the system or user-defined notification mechanism (if the user has configured a webhook alert) to send a notification: "Task interrupted abnormally, manual intervention required for inspection."

## ⚠️ Safety and Operational Red Lines
1.  **Do Not Terminate Processes:** Even if the task appears to be stuck, absolutely do not execute a forced process termination (`kill`) or click the "Cancel" button of the original task software.
2.  **Click Cautiously:** When closing pop-ups, precisely identify "Close" or "Later." Strictly avoid mistakenly clicking "Restart System Now" or "Update and Install."
