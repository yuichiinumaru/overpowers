import * as blessed from 'blessed';
import { Layout } from './components/layout';

export interface ScreenController {
  render(layout: Layout): void;
  destroy(): void;
}

export class Navigation {
  private screen: blessed.Widgets.Screen;
  private currentScreen: ScreenController | null = null;
  private layout: Layout | null = null;
  private context: Record<string, any> = {}; // Shared state

  constructor(screen: blessed.Widgets.Screen) {
    this.screen = screen;
  }

  public getScreen(): blessed.Widgets.Screen {
    return this.screen;
  }

  public navigate(ScreenClass: new (nav: Navigation, context: any) => ScreenController) {
    if (this.currentScreen) {
      this.currentScreen.destroy();
    }

    if (this.layout) {
      this.layout.destroy();
    }

    // Create new layout for the new screen
    // We do this to ensure clean slate
    this.layout = new Layout(this.screen, 'Init');

    this.currentScreen = new ScreenClass(this, this.context);
    this.currentScreen.render(this.layout);
    this.screen.render();
  }

  public getContext() {
    return this.context;
  }

  public updateContext(key: string, value: any) {
    this.context[key] = value;
  }

  public quit() {
    process.exit(0);
  }
}
