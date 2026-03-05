#!/bin/bash

# Scaffold a Penpot design snippet.
# Usage: ./scaffold_snippet.sh <snippet_type>

TYPE="$1"

case $TYPE in
  discovery)
    cat <<EOF > penpot_discovery.js
// Discover existing design patterns in current file
const allShapes = penpotUtils.findShapes(() => true, penpot.root);

// Find existing colors in use
const colors = new Set();
allShapes.forEach(s => {
  if (s.fills) s.fills.forEach(f => colors.add(f.fillColor));
});

// Find existing text styles (font sizes, weights)
const textStyles = allShapes
  .filter(s => s.type === 'text')
  .map(s => ({ fontSize: s.fontSize, fontWeight: s.fontWeight }));

// Find existing components
const components = penpot.library.local.components;

console.log({ colors: [...colors], textStyles, componentCount: components.length });
EOF
    echo "Discovery snippet created: penpot_discovery.js"
    ;;
  board)
    cat <<EOF > penpot_new_board.js
// Find all existing boards and calculate next position
const boards = penpotUtils.findShapes(s => s.type === 'board', penpot.root);
let nextX = 0;
const gap = 100; // Space between boards

if (boards.length > 0) {
  // Find rightmost board edge
  boards.forEach(b => {
    const rightEdge = b.x + b.width;
    if (rightEdge + gap > nextX) {
      nextX = rightEdge + gap;
    }
  });
}

// Create new board at calculated position
const newBoard = penpot.createBoard();
newBoard.x = nextX;
newBoard.y = 0;
newBoard.resize(375, 812);
newBoard.name = "New Screen";

console.log("New board created at x:", nextX);
EOF
    echo "Board creation snippet created: penpot_new_board.js"
    ;;
  *)
    echo "Usage: $0 {discovery|board}"
    exit 1
    ;;
esac
