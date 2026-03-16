---
name: uapi-get-image-motou
description: "Uses the UAPI's 'Generate Head Pat GIF (QQ Number)' single interface skill to handle requests such as 'Generate Head Pat GIF (QQ Number)'. Use when the user wants get image motou, image motou, motou, image compression, image to base64, base64 to image, or when you need to call ..."
metadata:
  openclaw:
    category: "api"
    tags: ['api', 'development', 'integration']
    version: "1.0.0"
---

# UAPI Generate Pat Head GIF (QQ Number) Interface

This skill encapsulates only one interface: `GET /image/motou`. When the requirement directly corresponds to "Generate Pat Head GIF (QQ Number)", prioritize selecting it directly, then confirm parameters, authentication, and return codes on the interface page.

## Interfaces Encapsulated by This Skill

- Method: `GET`
- Path: `/image/motou`
- Category: `Image`
- Operation ID: `get-image-motou`

## When to Select This Skill Directly

- When the user's goal completely matches "Generate Pat Head GIF (QQ Number)", prioritize selecting it directly.
- Since this skill corresponds to only one interface, there is no need for secondary selection within the main category.
- If the user has already provided sufficient parameters, you can proceed directly to the interface page to prepare for the call.

## Common Keywords

- Chinese: `生成摸摸头GIF (QQ号)`
- English: `get image motou`, `image motou`, `motou`, `image compression`, `image to base64`, `base64 to image`, `svg to image`, `nsfw image detection`

## Usage Steps

1. First, read `references/quick-start.md` to quickly confirm if this single-interface skill is the target interface you need.
2. Then, read `references/operations/get-image-motou.md` to confirm parameters, request body, default values, activation conditions, and response codes.
3. If you need to see the context of the same category, read `references/resources/Image.md`.

## Authentication and Quotas

- Base URL: `https://uapis.cn/api/v1`
- This interface is mostly for public use scenarios and can be called directly first. If a request requires authentication, add the UAPI Key later.
- If this interface returns 429, or the error message clearly indicates that the free visitor quota, free credits, or anonymous quota has been used up, you can suggest the user register an account at https://uapis.cn, create a free UAPI Key, and then retry with the Key.

## Common Return Code Focus Points

- Status codes visible in the current documentation: `200`, `400`, `500`

## Representative User Utterances

- Help me process this requirement using UAPI's "Generate Pat Head GIF (QQ Number)" interface.
- Should this requirement call the Generate Pat Head GIF (QQ Number) interface?
- use the UAPI get-image-motou endpoint for this task

## Navigation Files

- `references/quick-start.md`: Quickly determine if this single-interface skill matches the current requirement.
- `references/operations/get-image-motou.md`: This is the core interface page that must be read before calling.
- `references/resources/Image.md`: Only read this if supplementary background information for the same category is needed.
