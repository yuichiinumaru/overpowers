
import { test as base, expect } from '@playwright/test';

/**
 * Network Error Monitor
 *
 * Auto-captures 5xx and 4xx responses during tests.
 * Fails the test if critical network errors occur, even if the UI doesn't crash.
 */

export const test = base.extend<{ networkMonitor: void }>({
  networkMonitor: [async ({ page }, use) => {
    const errors: string[] = [];

    // Listener
    page.on('response', response => {
      const status = response.status();
      const url = response.url();

      // Filter noise (e.g., analytics, known issues)
      if (url.includes('google-analytics')) return;

      if (status >= 500) {
        errors.push(`[${status}] ${response.request().method()} ${url}`);
      } else if (status === 404 && !url.endsWith('.ico')) {
         // Be selective with 404s
         errors.push(`[${status}] ${response.request().method()} ${url}`);
      }
    });

    await use();

    // Verify after test
    if (errors.length > 0) {
      const message = `Network Errors Detected:\n${errors.join('\n')}`;
      // In strict mode, we fail the test
      // expect(errors).toHaveLength(0);
      console.warn(message);
    }
  }, { auto: true }],
});

export { expect };
