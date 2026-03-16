---
name: hunyuan-3d
description: "Tencent Hunyuan 3D API (OpenAI-compatible interface) - 3D model generation based on the Hunyuan large model"
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# Hunyuan 3D - Tencent Hunyuan 3D (OpenAI Compatible API)

3D model generation service based on Tencent's Hunyuan large model, using an OpenAI compatible API, supporting text-to-3D and image-to-3D.

## ⚠️ Important Notes

**This skill uses an OpenAI compatible API**, which is different from traditional Tencent Cloud APIs:
- Uses **API Key** authentication (not SecretId/SecretKey)
- Interface style is consistent with OpenAI
- **Professional Edition only** (Express Edition is not supported)

## 🚀 Quick Start

### Step 1: Activate Hunyuan 3D Service

**You must** activate the service in the Tencent Cloud console first:

1. Visit the [Tencent Hunyuan 3D Console](https://console.cloud.tencent.com/ai3d)
2. Click "Activate Now" or "Apply to Activate"
3. Read and agree to the service agreement
4. Wait for the service to be activated (usually effective immediately)

**Common Issues**:
- If it shows "Insufficient resources", the service is initializing. Please wait 5-10 minutes and try again.
- If activation fails, you may need to complete real-name verification or contact customer service.

### Step 2: Obtain API Key

1. Visit the [Hunyuan 3D API Key Management Page](https://console.cloud.tencent.com/ai3d/api-key)
2. Click "Create API Key"
3. Enter a name (e.g., hunyuan-3d-key)
4. Copy the generated API Key (format: `sk-xxxxx`)

**⚠️ Important**: The API Key is displayed only once, please save it carefully!

**Backup Link**: If the above link is inaccessible, you can also create it on the [Hunyuan Large Model API Key Page](https://console.cloud.tencent.com/hunyuan/start)

### Step 3: Configure Environment Variables

**⚠️ Important Distinction**:
- hunyuan-image and hunyuan-video use **Tencent Cloud SecretId/SecretKey**
- hunyuan-3d uses a **Hunyuan 3D specific API Key** (format: `sk-xxxxx`)

**Required Environment Variables**:
- `HUNYUAN_3D_API_KEY` - Hunyuan 3D API Key

**Windows PowerShell**:
```powershell
# Set temporarily (current session)
$env:HUNYUAN_3D_API_KEY = "sk-xxxxx"

# Set permanently (recommended)
[Environment]::SetEnvironmentVariable("HUNYUAN_3D_API_KEY", "sk-xxxxx", "User")
```

**Linux/Mac**:
```bash
# Set temporarily
export HUNYUAN_3D_API_KEY="sk-xxxxx"

# Set permanently (add to ~/.bashrc or ~/.zshrc)
echo 'export HUNYUAN_3D_API_KEY="sk-xxxxx"' >> ~/.bashrc
source ~/.bashrc
```

### Step 4: Verify Configuration

```powershell
# Check environment variable
Write-Host "API Key: $($env:HUNYUAN_3D_API_KEY.Substring(0,15))..."

# Test generation
python scripts/generate.py --mode text --prompt "A puppy"
```

**If you get an error "Insufficient resources"**: The service is initializing. Wait 5-10 minutes and retry.

```bash
python scripts/generate.py --mode text --prompt "A puppy"
```

If you see "Task submitted successfully", your configuration is correct!

## Features

- **Text-to-3D**: Generate 3D models from text descriptions
- **Image-to-3D**: Generate 3D models from images
- **Multi-version Support**: Supports model versions 3.0 and 3.1

## Usage

### Basic Usage

```bash
# Text-to-3D
python scripts/generate.py --mode text --prompt "A cute little pig"

# Image-to-3D
python scripts/generate.py --mode image --image-url "https://example.com/pig.jpg"

# Use version 3.1 model
python scripts/generate.py --mode text --prompt "Puppy" --model 3.1
```

### Parameter Description

| Parameter | Description | Example |
|------|------|------|
| --mode | Generation mode | `text` (Text-to-3D), `image` (Image-to-3D) |
| --prompt | Text description (Text-to-3D) | "A cute little pig" |
| --image-url | Image URL (Image-to-3D) | "https://example.com/pig.jpg" |
| --model | Model version | `3.0` (default), `3.1` |
| --output | Output directory | ./models |

### Model Version Description

| Version | Features |
|------|------|
| 3.0 | Default version, full functionality |
| 3.1 | New version, but LowPoly and Sketch parameters are unavailable |

### Input Requirements

**Text-to-3D**:
- Text description: Up to 1024 UTF-8 characters
- Supports Chinese prompts

**Image-to-3D**:
- Image format: jpg, png, jpeg, webp
- Image size: ≤8MB
- Resolution: 128px ~ 5000px (single side)

## Output

Generated 3D models are saved in the `{output}/{date}/{job_id}/` directory:
- `model.{format}` - 3D model file (obj/glb format)
- `info.json` - Task information

**Output Format**:
- Returns both `.glb` and `.obj` formats
- Includes texture maps
- Comes with a preview image

## API Information

- **Base URL**: `https://api.ai3d.cloud.tencent.com`
- **Submit Task**: `POST /v1/ai3d/submit`
- **Query Task**: `POST /v1/ai3d/query`
- **Authentication**: API Key (Header: `Authorization: sk-xxxxx`)

## Troubleshooting and Solutions

### 1. Service Not Activated - ResourceUnavailable

**Error Message**:
```
ResourceUnavailable.NotExist - Billing status unknown
```

**Solution**:
1. Visit https://console.cloud.tencent.com/ai3d
2. Click "Activate Now"
3. Wait 5-10 minutes for the service to initialize
4. Retry

### 2. Insufficient Resources - ResourceInsufficient

**Error Message**:
```
ResourceInsufficient - Insufficient resources
```

**Solution**:
- May occur when the service is newly activated. Wait 5-10 minutes and retry.
- If it persists, contact Tencent Cloud customer service.

### 3. API Key Error - Unauthorized

**Error Message**:
```
HTTP 401: Unauthorized
Incorrect API key provided
```

**Solution**:
1. Confirm you are using an **API Key** (not SecretId/SecretKey)
2. The API Key format should be `sk-xxxxx`
3. Create it at https://console.cloud.tencent.com/hunyuan/start
4. Check if the environment variable is set correctly

### 4. Response Format Issue

**Observation**: The OpenAI compatible API returns the format:
```json
{
  "Response": {
    "JobId": "xxx",
    "Status": "DONE",
    "ResultFile3Ds": [...]
  }
}
```

**Note**: The status field is `Status`, not `StatusCode`. The success status is `DONE`, not `SUCCESS`.

### 5. Limitations of Model Version 3.1

**Note**: When selecting version 3.1, the LowPoly and Sketch parameters are unavailable.

### 6. Unsupported Image Format

**Error**: Image upload failed.

**Solution**: Only jpg, png, jpeg, and webp formats are supported.

## Complete Examples

```bash
# Example 1: Generate a pig 3D model
python scripts/generate.py --mode text --prompt "A cute little pig, pink, cartoon style"

# Example 2: Generate 3D from an image
python scripts/generate.py --mode image --image-url "https://example.com/pig-photo.jpg"

# Example 3: Use version 3.1
python scripts/generate.py --mode text --prompt "Puppy" --model 3.1

# Example 4: Specify output directory
python scripts/generate.py --mode text --prompt "Kitten" --output ./my_models
```

## Notes

1. **Asynchronous API**: Divided into two steps: submitting a task and querying a task.
2. **Task Validity**: 24 hours.
3. **Concurrency Limit**: 3 concurrent tasks by default.
4. **Professional Edition Only**: The OpenAI compatible API does not support the Express Edition.
5. **API Key**: Use a separate API Key, not Tencent Cloud SecretId/SecretKey.
6. **Generation Time**: 3D generation takes a relatively long time (1-5 minutes), please be patient.

## Related Links

- [OpenAI Compatible API Documentation](https://cloud.tencent.com/document/product/1804/126189)
- [API Key Management](https://console.cloud.tencent.com/hunyuan/start)
- [Hunyuan 3D Console](https://console.cloud.tencent.com/ai3d)
- [Submit Task API Documentation](https://cloud.tencent.com/document/product/1804/123447)

## Debugging Tips

If you encounter issues, you can:
1. Check environment variables: `echo $env:HUNYUAN_3D_API_KEY`
2. Test if the API Key is valid (see curl example above)
3. Check the service status in the Tencent Cloud console
4. Contact customer service with the RequestId for assistance
