import * as blessed from 'blessed';

export interface MenuItem {
  label: string;
  value: string;
}

export class Menu {
  private list: blessed.Widgets.ListElement;

  constructor(parent: blessed.Widgets.Node, items: MenuItem[], onSelect: (item: MenuItem) => void) {
    this.list = blessed.list({
      parent: parent,
      top: 4, // Below header
      left: 2,
      right: 2,
      bottom: 4, // Above footer
      items: items.map(i => i.label),
      keys: true,
      vi: true,
      mouse: true,
      style: {
        selected: {
          bg: 'green',
          fg: 'black',
          bold: true
        },
        item: {
          fg: 'white'
        }
      }
    });

    this.list.on('select', (_item, index) => {
      onSelect(items[index]);
    });

    this.list.focus();
  }

  public focus() {
    this.list.focus();
  }

  public destroy() {
    this.list.destroy();
  }
}
