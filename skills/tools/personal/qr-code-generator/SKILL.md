---
name: tool-utility-qr-code-generator
description: Generate QR codes/barcodes, supporting content like text, URLs, WiFi configurations, etc. Allows customization of size, color, and specifies the save path.
version: 1.0.0
tags: [qr-code, utility, image, wifi]
---

# Generate QR Code Skill

## 1. Description
When users need to convert text, URLs, WiFi information, etc., into a visual QR code, use this skill to generate a QR code image and save it to a specified path (defaults to the desktop), supporting custom sizes and colors.

## 2. When to use
- User says: "Help me generate a QR code for https://openclaw.ai"
- User says: "Generate a QR code containing WiFi information, Name: MyWiFi, Password: 12345678"
- User says: "Generate a black QR code, content is 'Hello OpenClaw', save to the root directory of D drive"
- User says: "Help me make a 400px QR code, content is my phone number 13800138000"

## 3. How to use
1. Extract core parameters from the user's message:
   - Required: Content to generate (text/URL/WiFi information, WiFi format should be "WIFI:S:Name;T:Type;P:Password;;");
   - Optional: Size (defaults to 300px), Color (defaults to black), Save path (defaults to desktop);
2. If the user does not specify optional parameters, use the default values;
3. Call the `generate_qr` function in `agent.py` to perform the generation operation;
4. Return result: Inform the user of the QR code save path. If generation fails, explain the specific reason (e.g., path permission denied, empty content).

## 4. Implementation (Code Association Description)
- Dependencies: `qrcode` (for QR code generation), `Pillow` (for image processing);
- Core function: `async def generate_qr(text: str, size: int = 300, color: str = "black", save_path: str = None)`
- Parameter description:
  - `text`: QR code content (required);
  - `size`: QR code size (unit px, default 300);
  - `color`: Fill color (default black, supports English color names or hexadecimal color values, e.g., #FF0000);
  - `save_path`: Save path (defaults to desktop, filename: qr_code.png).

## 5. Edge cases
- Empty content: Reply with "Please provide the content to generate the QR code (e.g., text, URL, WiFi information)";
- No write permission for save path: Reply with "No write permission for the specified path, please change the save path (e.g., desktop)";
- Dependencies not installed: Automatically attempt to install `qrcode` and `Pillow`. If installation fails, prompt the user to manually execute "pip install qrcode pillow";
- Content with special characters: Automatically filter invalid characters to ensure the QR code can be recognized normally.
