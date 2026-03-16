import { format } from 'autocorrect-node';

export function addSpacing(content: string): string {
  return format(content);
}
