import * as blessed from 'blessed';
import { Navigation } from './navigation';
import { WelcomeScreen } from './screens/welcome';

export function startTui() {
  const screen = blessed.screen({
    smartCSR: true,
    title: 'Auth Monster Setup'
  });

  const nav = new Navigation(screen);

  // Initial context setup
  nav.updateContext('accounts', []);
  nav.updateContext('config', {});

  // Global key bindings
  screen.key(['q', 'C-c'], () => {
    return process.exit(0);
  });

  nav.navigate(WelcomeScreen);
}
