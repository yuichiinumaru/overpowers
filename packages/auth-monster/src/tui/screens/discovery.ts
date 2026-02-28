import { Navigation, ScreenController } from '../navigation';
import { Layout } from '../components/layout';
import { Spinner } from '../components/spinner';
import { CheckboxList, CheckboxItem } from '../components/checkbox-list';
import { TokenExtractor } from '../../utils/extractor';
import { ManagedAccount } from '../../core/types';
import { ProvidersScreen } from './providers';
import * as blessed from 'blessed';

export class DiscoveryScreen implements ScreenController {
  private nav: Navigation;
  private spinner: Spinner | null = null;
  private list: CheckboxList | null = null;
  private continueBtn: blessed.Widgets.BoxElement | null = null;
  private accounts: ManagedAccount[] = [];

  constructor(nav: Navigation, _context: any) {
    this.nav = nav;
  }

  render(layout: Layout): void {
    layout.updateTitle('Auto Discovery');

    this.spinner = new Spinner(layout.container, 'Scanning for local accounts...');
    this.spinner.start();

    // Async discovery
    TokenExtractor.discoverAll().then((accounts) => {
      this.accounts = accounts;
      if (this.spinner) {
        this.spinner.destroy();
        this.spinner = null;
      }
      this.showResults(layout);
    }).catch(err => {
        // Handle error
         if (this.spinner) {
            this.spinner.destroy();
            this.spinner = null;
        }
    });
  }

  private showResults(layout: Layout) {
    layout.updateFooter('Space: Toggle | Enter: Continue');

    const items: CheckboxItem[] = this.accounts.map(acc => ({
      label: `${acc.provider} (${acc.email}) - ${acc.metadata?.source}`,
      value: acc,
      checked: true // Default to checked
    }));

    if (items.length === 0) {
       const msg = blessed.box({
           parent: layout.container,
           top: 'center',
           left: 'center',
           content: 'No accounts found.',
           style: { fg: 'yellow' }
       });

       // Delay then move on
       setTimeout(() => {
           this.nav.navigate(ProvidersScreen);
       }, 2000);
       return;
    }

    this.list = new CheckboxList(layout.container, items, () => {
        if (this.list) {
             const selected = this.list.getSelected();
             // Save discovered accounts to context
             const existing = this.nav.getContext()['accounts'] || [];
             this.nav.updateContext('accounts', [...existing, ...selected]);
             this.nav.navigate(ProvidersScreen);
        }
    });
  }

  destroy(): void {
    if (this.spinner) this.spinner.destroy();
    if (this.list) this.list.destroy();
    if (this.continueBtn) this.continueBtn.destroy();
  }
}
