import * as blessed from 'blessed';

export class Spinner {
  private box: blessed.Widgets.BoxElement;
  private interval: NodeJS.Timeout | null = null;
  private frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'];
  private currentFrame = 0;

  constructor(parent: blessed.Widgets.Node, text: string) {
    this.box = blessed.box({
      parent: parent,
      top: 'center',
      left: 'center',
      width: '50%',
      height: 3,
      content: ` ${this.frames[0]} ${text}`,
      border: {
        type: 'line'
      },
      style: {
        border: {
          fg: 'cyan'
        }
      }
    });
  }

  public start() {
    this.interval = setInterval(() => {
      this.currentFrame = (this.currentFrame + 1) % this.frames.length;
      // Keep the text, just update the spinner char
      const content = this.box.getContent();
      const text = content.substring(3); // space + char + space
      this.box.setContent(` ${this.frames[this.currentFrame]} ${text}`);
      this.box.screen.render();
    }, 80);
  }

  public stop() {
    if (this.interval) {
      clearInterval(this.interval);
      this.interval = null;
    }
  }

  public destroy() {
    this.stop();
    this.box.destroy();
  }
}
