import { Navigation, ScreenController } from '../navigation';
import { Layout } from '../components/layout';
import * as blessed from 'blessed';
import * as fs from 'fs';
import * as path from 'path';
import * as os from 'os';
import { AuthMonsterConfigSchema } from '../../core/types';

export class SummaryScreen implements ScreenController {
  private nav: Navigation;
  private btn: blessed.Widgets.BoxElement | null = null;
  private enterHandler: (() => void) | null = null;

  constructor(nav: Navigation, _context: any) {
    this.nav = nav;
  }

  render(layout: Layout): void {
    layout.updateTitle('Summary & Save');
    layout.updateFooter('Press Enter to Save & Exit');

    const context = this.nav.getContext();
    const accounts = context['accounts'] || [];
    const config = context['config'] || {};

    let summaryText = `Configuration Summary:\n\n`;
    summaryText += `Strategy: ${config.method || 'Default'}\n`;
    summaryText += `Accounts Configured: ${accounts.length}\n\n`;

    accounts.forEach((acc: any) => {
        summaryText += `- [${acc.provider}] ${acc.email} (${acc.isHealthy ? 'Healthy' : 'Unverified'})\n`;
    });

    const box = blessed.box({
        parent: layout.container,
        top: 4,
        left: 2,
        right: 2,
        bottom: 6,
        content: summaryText,
        scrollable: true,
        alwaysScroll: true,
        keys: true,
        vi: true,
        border: { type: 'line' }
    });

    this.enterHandler = () => {
        this.saveAndExit();
    };
    layout.screen.key('enter', this.enterHandler);
    
    box.focus();
  }

  private saveAndExit() {
      const context = this.nav.getContext();
      const accounts = context['accounts'] || [];
      const config = context['config'] || {};
      
      // Defaults
      if (!config.active && accounts.length > 0) {
          config.active = accounts[0].provider;
      }

      const home = os.homedir();
      const configDir = path.join(home, '.config', 'opencode');

      if (!fs.existsSync(configDir)) {
          fs.mkdirSync(configDir, { recursive: true });
      }

      fs.writeFileSync(
          path.join(configDir, 'auth-monster-accounts.json'), 
          JSON.stringify(accounts, null, 2)
      );

      fs.writeFileSync(
          path.join(configDir, 'auth-monster-config.json'), 
          JSON.stringify(config, null, 2)
      );
      
      console.log('Configuration saved successfully!');
      process.exit(0);
  }

  destroy(): void {
    if (this.enterHandler) {
        this.nav.getScreen().unkey('enter', this.enterHandler);
    }
  }
}
