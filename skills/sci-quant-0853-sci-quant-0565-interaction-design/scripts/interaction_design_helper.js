/**
 * Interaction Design Helper script
 */
function generateInteractionConfig(targetElement, eventType, action) {
  return {
    target: targetElement,
    event: eventType,
    action: action,
    debounce: 300,
    animate: true
  };
}
module.exports = { generateInteractionConfig };
