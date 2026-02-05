import { spawn } from 'child_process';
import * as fs from 'fs';
import * as os from 'os';
import * as path from 'path';

const PYTHON_SCRIPT = `
import argparse
import json
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Extract cookies for a domain from browsers.")
    parser.add_argument("domain", help="The domain to extract cookies for (e.g., chatgpt.com)")
    parser.add_argument("--browser", help="Specific browser to use (chrome, firefox, safari, etc.)", default=None)
    args = parser.parse_args()

    domain = args.domain
    browser_name = args.browser

    try:
        import browser_cookie3
    except ImportError:
        # Fail silently or with specific error code if generic provider needs to know
        # But here we just print empty/error json
        print(json.dumps({"error": "browser_cookie3 not installed"}), file=sys.stderr)
        sys.exit(1)

    try:
        if browser_name:
            if hasattr(browser_cookie3, browser_name):
                loader = getattr(browser_cookie3, browser_name)
                cj = loader(domain_name=domain)
            else:
                print(json.dumps({"error": f"Browser {browser_name} not supported"}), file=sys.stderr)
                sys.exit(1)
        else:
            cj = browser_cookie3.load(domain_name=domain)

        # Convert to dictionary/list
        cookie_list = []
        for cookie in cj:
             cookie_list.append(f"{cookie.name}={cookie.value}")

        cookie_header = "; ".join(cookie_list)

        print(json.dumps({"cookieHeader": cookie_header}))

    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
`;

export class CookieManager {
  static async getCookiesForDomain(domain: string, browser?: string): Promise<string | null> {
    return new Promise((resolve) => {
      // Create a temporary file for the script
      const tmpDir = os.tmpdir();
      const scriptPath = path.join(tmpDir, `cookie_extractor_${Date.now()}.py`);

      try {
        fs.writeFileSync(scriptPath, PYTHON_SCRIPT);
      } catch (err) {
        console.error(`[CookieManager] Failed to write temp script: ${err}`);
        resolve(null);
        return;
      }

      const args = [scriptPath, domain];
      if (browser) {
        args.push('--browser', browser);
      }

      const pythonProcess = spawn('python3', args);

      let stdout = '';
      let stderr = '';

      pythonProcess.stdout.on('data', (data) => {
        stdout += data.toString();
      });

      pythonProcess.stderr.on('data', (data) => {
        stderr += data.toString();
      });

      pythonProcess.on('close', (code) => {
        // Cleanup temp file
        try { fs.unlinkSync(scriptPath); } catch (e) {}

        if (code !== 0) {
          // It's normal for this to fail if no cookies are found or browser_cookie3 is missing
          // console.warn(`[CookieManager] Script exited with code ${code}: ${stderr}`);
          resolve(null);
          return;
        }

        try {
          const result = JSON.parse(stdout);
          if (result.error) {
             // console.warn(`[CookieManager] Error from script: ${result.error}`);
             resolve(null);
          } else {
             resolve(result.cookieHeader || null);
          }
        } catch (e) {
          console.error(`[CookieManager] Failed to parse output: ${stdout}`);
          resolve(null);
        }
      });

      pythonProcess.on('error', (err) => {
          try { fs.unlinkSync(scriptPath); } catch (e) {}
          console.error(`[CookieManager] Failed to spawn python script: ${err}`);
          resolve(null);
      });
    });
  }
}
