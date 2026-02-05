import { Navigation, ScreenController } from '../navigation';
import { Layout } from '../components/layout';
import { CheckboxList, CheckboxItem } from '../components/checkbox-list';
import { AuthProvider } from '../../core/types';
import { OAuthScreen } from './oauth';
import * as blessed from 'blessed';

export class ProvidersScreen implements ScreenController {
  private nav: Navigation;
  private list: CheckboxList | null = null;

  constructor(nav: Navigation, _context: any) {
    this.nav = nav;
  }

  render(layout: Layout): void {
    layout.updateTitle('Select Providers to Configure');
    layout.updateFooter('Space: Toggle | Enter: Next');

    const allProviders = Object.values(AuthProvider);
    const contextAccounts = this.nav.getContext()['accounts'] || [];
    const configuredProviders = new Set(contextAccounts.map((a: any) => a.provider));

    const items: CheckboxItem[] = allProviders.map(p => ({
      label: p,
      value: p,
      checked: configuredProviders.has(p) // Pre-select if already has account
    }));

    this.list = new CheckboxList(layout.container, items, () => {
        this.submit();
    });
  }
  
  private submit() {
      if (this.list) {
          const selectedProviders: AuthProvider[] = this.list.getSelected();
          this.nav.updateContext('selectedProviders', selectedProviders);
          this.nav.navigate(OAuthScreen);
      }
  }

  destroy(): void {
    if (this.list) this.list.destroy();
    // Need to remove key listener if attached to screen
    // this.nav.screen.removeListener... (but need reference to function)
    // The Navigation class should handle screen clearing?
    // Blessed `screen.removeAllListeners('key')` is drastic.
    // Usually widgets capture keys when focused.
  }
}
