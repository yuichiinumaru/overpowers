const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
    const channelUrl = process.argv[2] || 'https://www.youtube.com/@fernandobrasao/videos';
    console.log(`Extracting links from: ${channelUrl}`);

    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();

    try {
        await page.goto(channelUrl, { waitUntil: 'networkidle', timeout: 60000 });

        // Handle consent dialog if it appears
        try {
            const consentButton = await page.locator('button[aria-label="Accept all"]');
            if (await consentButton.isVisible({ timeout: 5000 })) {
                await consentButton.click();
                await page.waitForTimeout(2000);
            }
        } catch (e) {
            // Ignore if consent dialog doesn't appear
        }

        let links = new Set();
        let lastCount = 0;
        let retries = 0;

        console.log("Scrolling and collecting links...");
        for (let i = 0; i < 20; i++) {
            await page.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight));
            await page.waitForTimeout(2000);

            const currentElements = await page.$$eval('a#video-title-link, a#video-title', els =>
                els.map(el => el.href).filter(href => href && !href.includes('/shorts/'))
            );

            currentElements.forEach(url => {
                let cleanUrl = url.split("&")[0].split("?")[0];
                if (url.includes('watch?v=')) {
                    cleanUrl = 'https://www.youtube.com/watch?v=' + url.split('watch?v=')[1].split('&')[0];
                    links.add(cleanUrl);
                }
            });

            if (links.size === lastCount) {
                retries++;
            } else {
                retries = 0;
                lastCount = links.size;
            }

            if (retries > 3) {
                console.log("No new links found after 3 scrolls. Stopping.");
                break;
            }
        }

        const linkArray = Array.from(links);
        console.log(`Found ${linkArray.length} links.`);

        // Save to file
        const mdContent = `# Extracted Links for ${channelUrl}\n\n` + linkArray.map(link => `- ${link}`).join('\n');

        const dir = 'skills/youtube-skill-creator/references';
        if (!fs.existsSync(dir)) {
            fs.mkdirSync(dir, { recursive: true });
        }

        fs.writeFileSync(`${dir}/fernandobrasao_playwright_links.md`, mdContent);
        console.log(`Links saved to ${dir}/fernandobrasao_playwright_links.md`);

    } catch (e) {
        console.error("Error:", e);
    } finally {
        await browser.close();
    }
})();
