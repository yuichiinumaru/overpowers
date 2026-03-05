export function replaceQuotes(content: string): string {
  // Simple regex to replace double quotes with fullwidth ones
  // Note: This is a basic implementation and might need refinement for complex cases
  return content.replace(/"([^"]*)"/g, '“$1”');
}
