---
name: longtask-progress
description: "|"
metadata:
  openclaw:
    category: "productivity"
    tags: ['productivity', 'task', 'management']
    version: "1.0.0"
---

# LongTask Progress - Long Task Forced Progress Reporting

Prevent loss of focus during long-running tasks by maintaining task continuity through a timed forced reporting mechanism.

## Problem Scenarios

When performing long tasks (e.g., writing articles, batch image generation, data downloading), it's easy to encounter:
- Loss of focus during task execution, entering a "sleep" state
- Users unaware of current progress, forced to wait idly
- Inability to recover context after task interruption
- Poor user experience due to prolonged lack of feedback

## Solution

**Forced Progress Reporting Mechanism**:
- Timed automatic reporting (default every 5 minutes)
- Instant reporting upon step completion
- Precise display of progress percentage
- Runs in a background thread, does not block the main task

## Installation

No installation required, import and use directly:

```python
import sys
sys.path.insert(0, '~/.openclaw/workspace-bibi/skills/longtask_progress')
from longtask_progress import LongTaskProgress, track_progress
```

## Usage

### Method 1: Context Manager (Recommended)

The most concise way to use, automatically handles startup and shutdown:

```python
from longtask_progress import LongTaskProgress

# Use the 'with' statement for automatic lifecycle management
with LongTaskProgress(
    task_name="Article Writing",
    total_steps=6,
    interval=300  # Report every 5 minutes
) as reporter:
    
    for section in ["Introduction", "Background", "Analysis", "Conclusion"]:
        write_section(section)
        reporter.step(f"Completed {section}")

# Automatically stops upon exiting the 'with' block
```

### Method 2: Decorator

Automatically adds progress tracking to functions:

```python
from longtask_progress import track_progress

@track_progress(
    task_name="Image Generation",
    total_steps=5,
    interval=120  # Report every 2 minutes
)
def generate_images(reporter):
    for i in range(5):
        generate_image(i)
        reporter.step(f"Generated image {i+1}")

# Automatically tracked upon invocation
generate_images()
```

### Method 3: Manual Invocation

Use when fine-grained control is needed:

```python
from longtask_progress import LongTaskProgress

reporter = LongTaskProgress(
    task_name="Data Analysis",
    total_steps=100,
    interval=60  # Report every 1 minute
)

reporter.start()

try:
    for i in range(100):
        process_data(i)
        
        # Report every 10 data points
        if i % 10 == 0:
            reporter.step(f"Processed {i}/100")
            
        # Stage update (does not count as a step)
        if i == 50:
            reporter.update("Completed 50%, halfway there")
            
finally:
    reporter.stop()  # Ensure stopping
```

## Parameter Description

### LongTaskProgress Class

| Parameter | Type | Default | Description |
|------|------|--------|------|
| task_name | str | Required | Task name, used for report identification |
| total_steps | int | None | Total number of steps, used for percentage calculation |
| interval | int | 300 | Forced report interval (seconds) |
| callback | callable | None | Custom callback function |

### Methods

| Method | Purpose |
|------|------|
| start() | Start progress reporting |
| step(message) | Complete a step and report |
| update(message) | Update status (does not increment step count) |
| stop() | Stop progress reporting |

## Report Format

**Forced Report Output (triggered automatically every 5 minutes):**

```
【Forced Report - 19:33:08】
  Task: Article Writing
  Time Elapsed: 12.5 minutes
  Time Since Last Report: 5.0 minutes
  Progress: 3/6 (50%)
  Status: Still executing...
```

**Step Completion Report:**

```
【Step Completed】Article Writing - Step 3 completed
  Details: Completed GameStop short squeeze chapter
  Overall Progress: 50%
```

**Task Completion Report:**

```
【Task Completed】Article Writing - Total time 25.3 minutes
```

## Practical Application Scenarios

### Scenario 1: Article Writing Workflow

```python
# Step 4: Writing
with LongTaskProgress("Article Writing", total_steps=6, interval=300) as reporter:
    for section in ["Introduction", "History", "Event", "Impact", "Risks", "Conclusion"]:
        write(section)
        reporter.step(f"{section} completed approx. 800 words")

# Step 5: Humanizer polishing
with LongTaskProgress("Humanizer Polishing", total_steps=23, interval=180) as reporter:
    for check in check_list:
        humanize_check(check)
        reporter.step(check)

# Step 6: Image generation
with LongTaskProgress("Article Image Generation", total_steps=3, interval=120) as reporter:
    for img in ["Header Image", "Section 1 Image", "Section 2 Image"]:
        generate_and_download(img)
        reporter.step(f"{img} completed")
```

### Scenario 2: Batch File Download

```python
@track_progress(task_name="Batch Download", total_steps=10, interval=60)
def batch_download(urls, reporter):
    for i, url in enumerate(urls, 1):
        download_file(url)
        reporter.step(f"Downloading {url}")

batch_download(url_list)
```

### Scenario 3: API Polling Wait

```python
with LongTaskProgress("API Polling", interval=30) as reporter:
    while True:
        status = check_api_status()
        
        if status == "completed":
            reporter.step("API returned completion")
            break
        elif status == "failed":
            reporter.step("API failed")
            raise Exception("API call failed")
        else:
            reporter.update(f"Status: {status}, continuing to poll...")
            time.sleep(5)
```

## Advanced Usage

### Custom Callback

Send reports to other destinations (e.g., log files, message queues):

```python
def my_callback(data):
    """Custom processing of report data"""
    if data['event'] == 'progress':
        # Send to logging system
        logger.info(f"Progress: {data.get('progress_percent', 'N/A')}%")
    elif data['event'] == 'step':
        # Send to user interface
        ui.update_status(data['message'])

with LongTaskProgress(
    task_name="Custom Task",
    total_steps=10,
    callback=my_callback
) as reporter:
    # ... execute task
```

### Nested Usage

Complex tasks can nest multiple progress reporters:

```python
with LongTaskProgress("Article Writing", total_steps=3, interval=300) as outer:
    
    for article in ["Article 1", "Article 2", "Article 3"]:
        
        with LongTaskProgress(f"{article} Image Generation", total_steps=3, interval=120) as inner:
            for img in ["Header", "Image 1", "Image 2"]:
                generate_image(img)
                inner.step(f"{img} completed")
                
        outer.step(f"{article} completed")
```

## Best Practices

1. **Set interval reasonably**
   - Writing tasks: 300 seconds (5 minutes)
   - Image generation tasks: 120 seconds (2 minutes)
   - API polling: 30-60 seconds

2. **Break down steps appropriately**
   - Steps should not be too long (>10 minutes)
   - Steps should not be too short (<10 seconds)
   - Aim for 5-20 steps

3. **Provide meaningful step messages**
   - ❌ "Completed step 1"
   - ✅ "Completed Introduction chapter (approx. 800 words)"

4. **Use context managers**
   - Ensures stop() is called
   - Correct cleanup even during exceptions

5. **Avoid excessive nesting**
   - Maximum 2 levels of nesting
   - Too much nesting can lead to confusion

## Troubleshooting

**Problem: No report output**
- Check if start() was called
- Check if interval is set too large
- Check if stderr is being redirected

**Problem: Incorrect step count**
- Ensure step() is called correctly
- Check if total_steps is set correctly

**Problem: Thread does not stop**
- Ensure stop() is called or use a 'with' statement
- Check for unhandled exceptions

## Technical Details

- Uses `threading.Timer` for timed reporting
- Background thread is a daemon thread, automatically terminates when the main thread exits
- Thread-safe, can be used in multi-threaded environments
- Supports nested usage without interference

## Changelog

- **v1.0** (2026-03-08)
  - Initial release
  - Supports three usage methods
  - Supports custom callbacks
  - Supports nested usage

---

*Stay focused, and let long tasks stop "sleeping"*
