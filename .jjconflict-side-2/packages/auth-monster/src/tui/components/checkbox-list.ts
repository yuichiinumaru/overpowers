import * as blessed from 'blessed';

export interface CheckboxItem {
  label: string;
  value: any;
  checked: boolean;
}

export class CheckboxList {
  private list: blessed.Widgets.ListElement;
  private items: CheckboxItem[];
  private onSubmit: () => void;

  constructor(parent: blessed.Widgets.Node, items: CheckboxItem[], onSubmit: () => void) {
    this.items = items;
    this.onSubmit = onSubmit;

    this.list = blessed.list({
      parent: parent,
      top: 4,
      left: 2,
      right: 2,
      bottom: 4,
      items: this.renderItems(),
      keys: true,
      vi: true,
      mouse: true,
      style: {
        selected: {
          bg: 'blue',
          fg: 'white'
        },
        item: {
          fg: 'white'
        }
      }
    });

    // Space to toggle
    this.list.key('space', () => {
        // We can't rely on `this.list.selected` being accurate immediately in all blessed versions
        // but typically it is the index.
        // @ts-ignore: 'selected' exists on ListElement at runtime but is missing in types
        const selected = this.list.selected;
        const index = typeof selected === 'number' ? selected : this.list.getItemIndex(selected); 
        this.toggle(index);
    });
    
    // Enter to submit
    this.list.on('select', () => {
        this.onSubmit();
    });

    this.list.focus();
  }

  private renderItems(): string[] {
    return this.items.map(i => `[${i.checked ? 'x' : ' '}] ${i.label}`);
  }

  private toggle(index: number) {
    if (index >= 0 && index < this.items.length) {
        this.items[index].checked = !this.items[index].checked;
        this.list.setItems(this.renderItems());
        this.list.select(index); // Restore selection position
        this.list.screen.render();
    }
  }

  public getSelected(): any[] {
    return this.items.filter(i => i.checked).map(i => i.value);
  }

  public destroy() {
    this.list.destroy();
  }
}
