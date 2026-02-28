const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
    console.log("Launching browser to get cookies...");
    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext();
    const page = await context.newPage();

    try {
        await page.goto('https://www.youtube.com', { waitUntil: 'networkidle' });

        try {
            const consentButton = await page.locator('button[aria-label="Accept all"], button:has-text("Accept all")').first();
            if (await consentButton.isVisible({ timeout: 5000 })) {
                await consentButton.click();
                await page.waitForTimeout(2000);
            }
        } catch (e) {
            console.log("No consent dialog found.");
        }

        const cookies = await context.cookies();

        // Format as Netscape cookie file
        let cookieText = "# Netscape HTTP Cookie File\n# http://curl.haxx.se/rfc/cookie_spec.html\n# This is a generated file!  Do not edit.\n\n";

        cookies.forEach(c => {
            const domain = c.domain.startsWith('.') ? c.domain : '.' + c.domain;
            const flag = c.domain.startsWith('.') ? "TRUE" : "FALSE";
            const path = c.path;
            const secure = c.secure ? "TRUE" : "FALSE";
            const expiration = Math.floor(c.expires);
            cookieText += `${domain}\t${flag}\t${path}\t${secure}\t${expiration}\t${c.name}\t${c.value}\n`;
        });

        fs.writeFileSync('youtube_cookies.txt', cookieText);
        console.log("Cookies saved to youtube_cookies.txt");

    } catch (e) {
        console.error("Error:", e);
    } finally {
        await browser.close();
    }
})();
