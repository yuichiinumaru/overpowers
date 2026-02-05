import * as blessed from 'blessed';

export class Layout {
  public screen: blessed.Widgets.Screen;
  public container: blessed.Widgets.BoxElement;
  public header: blessed.Widgets.BoxElement;
  public footer: blessed.Widgets.BoxElement;

  constructor(screen: blessed.Widgets.Screen, title: string) {
    this.screen = screen;

    // Main Container
    this.container = blessed.box({
      parent: this.screen,
      top: 0,
      left: 0,
      width: '100%',
      height: '100%',
      style: {
        bg: 'black',
        fg: 'white'
      }
    });

    // Header
    this.header = blessed.box({
      parent: this.container,
      top: 0,
      left: 0,
      width: '100%',
      height: 3,
      content: ` 👹 AUTH MONSTER SETUP | ${title}`,
      border: {
        type: 'line'
      },
      style: {
        border: {
          fg: 'green'
        },
        header: {
          fg: 'green',
          bold: true
        }
      }
    });

    // Footer
    this.footer = blessed.box({
      parent: this.container,
      bottom: 0,
      left: 0,
      width: '100%',
      height: 3,
      content: ' ↑↓ Navigate | Enter Select | Q Quit',
      border: {
        type: 'line'
      },
      style: {
        border: {
          fg: 'gray'
        },
        fg: 'gray'
      }
    });
  }

  public updateTitle(title: string) {
    this.header.setContent(` 👹 AUTH MONSTER SETUP | ${title}`);
    this.screen.render();
  }

  public updateFooter(text: string) {
    this.footer.setContent(` ${text}`);
    this.screen.render();
  }

  public destroy() {
    this.container.destroy();
  }
}
