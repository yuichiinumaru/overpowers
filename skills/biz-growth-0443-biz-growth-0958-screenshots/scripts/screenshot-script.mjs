import { chromium } from 'playwright';

const BASE_URL = '[APP_URL]';
const SCREENSHOTS_DIR = './screenshots';

// Authentication config (if needed)
const AUTH = {
  needed: [true|false],
  loginUrl: '[LOGIN_URL]',
  email: '[EMAIL]',
  password: '[PASSWORD]',
};

// Screenshots to capture
const SCREENSHOTS = [
  { name: '01-feature-name', url: '/path', waitFor: '[optional-selector]' },
  { name: '02-another-feature', url: '/another-path' },
  // ... add all planned screenshots
];

async function main() {
  const browser = await chromium.launch();

  // Create context with HiDPI settings
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 2,  // This is the key for true retina screenshots
  });

  const page = await context.newPage();

  // Handle authentication if needed
  if (AUTH.needed) {
    console.log('Logging in...');
    await page.goto(AUTH.loginUrl);

    // Smart login: try multiple common patterns for email/username field
    const emailField = page.locator([
      'input[type="email"]',
      'input[name="email"]',
      'input[id="email"]',
      'input[placeholder*="email" i]',
      'input[name="username"]',
      'input[id="username"]',
      'input[type="text"]',
    ].join(', ')).first();
    await emailField.fill(AUTH.email);

    // Smart login: try multiple common patterns for password field
    const passwordField = page.locator([
      'input[type="password"]',
      'input[name="password"]',
      'input[id="password"]',
    ].join(', ')).first();
    await passwordField.fill(AUTH.password);

    // Smart login: try multiple common patterns for submit button
    const submitButton = page.locator([
      'button[type="submit"]',
      'input[type="submit"]',
      'button:has-text("Sign in")',
      'button:has-text("Log in")',
      'button:has-text("Login")',
      'button:has-text("Submit")',
    ].join(', ')).first();
    await submitButton.click();

    await page.waitForLoadState('networkidle');
    console.log('Login complete');
  }

  // Capture each screenshot
  for (const shot of SCREENSHOTS) {
    console.log(`Capturing: ${shot.name}`);
    await page.goto(`${BASE_URL}${shot.url}`);
    await page.waitForLoadState('networkidle');

    // Optional: wait for specific element
    if (shot.waitFor) {
      await page.waitForSelector(shot.waitFor);
    }

    // Optional: perform actions before screenshot
    if (shot.actions) {
      for (const action of shot.actions) {
        if (action.click) await page.click(action.click);
        if (action.fill) await page.fill(action.fill.selector, action.fill.value);
        if (action.wait) await page.waitForTimeout(action.wait);
      }
    }

    await page.screenshot({
      path: `${SCREENSHOTS_DIR}/${shot.name}.png`,
      fullPage: shot.fullPage || false,
    });
    console.log(`  Saved: ${shot.name}.png`);
  }

  await browser.close();
  console.log('Done!');
}

main().catch(console.error);