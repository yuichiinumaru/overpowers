import { Navigation, ScreenController } from '../navigation';
import { Layout } from '../components/layout';
import { Menu, MenuItem } from '../components/menu';
import { SummaryScreen } from './summary';

export class StrategyScreen implements ScreenController {
  private nav: Navigation;
  private menu: Menu | null = null;

  constructor(nav: Navigation, _context: any) {
    this.nav = nav;
  }

  render(layout: Layout): void {
    layout.updateTitle('Select Quota Strategy');
    layout.updateFooter('Use ↑↓ to navigate, Enter to select');

    const items: MenuItem[] = [
      { label: 'Sticky (Prefer one provider, fallback on error)', value: 'sticky' },
      { label: 'Round Robin (Distribute load evenly)', value: 'round-robin' },
      { label: 'Quota Optimized (Use cheapest/available first)', value: 'quota-optimized' },
      { label: 'Hybrid (Mix of sticky and round-robin)', value: 'hybrid' }
    ];

    this.menu = new Menu(layout.container, items, (item) => {
        const config = this.nav.getContext()['config'] || {};
        config.method = item.value;
        this.nav.updateContext('config', config);
        this.nav.navigate(SummaryScreen);
    });
  }

  destroy(): void {
    if (this.menu) this.menu.destroy();
  }
}
