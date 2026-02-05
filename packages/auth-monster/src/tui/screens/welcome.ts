import { Navigation, ScreenController } from '../navigation';
import { Layout } from '../components/layout';
import { Menu, MenuItem } from '../components/menu';
import { DiscoveryScreen } from './discovery';

export class WelcomeScreen implements ScreenController {
  private nav: Navigation;
  private menu: Menu | null = null;

  constructor(nav: Navigation, _context: any) {
    this.nav = nav;
  }

  render(layout: Layout): void {
    layout.updateTitle('Welcome');
    layout.updateFooter('Use ↑↓ to navigate, Enter to select');

    const items: MenuItem[] = [
      { label: '[>] Start Setup', value: 'start' },
      { label: '[ ] Exit', value: 'exit' }
    ];

    this.menu = new Menu(layout.container, items, (item) => {
      if (item.value === 'start') {
        this.nav.navigate(DiscoveryScreen);
      } else {
        this.nav.quit();
      }
    });
    
    // Description text
    /*
    const text = blessed.box({
      parent: layout.container,
      top: 1,
      left: 2,
      height: 3,
      content: 'Welcome! This wizard will configure your\nAI providers for use with OpenCode.'
    });
    */
  }

  destroy(): void {
    if (this.menu) {
      this.menu.destroy();
    }
  }
}
