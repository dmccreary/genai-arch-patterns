# Architecture Pattern Viewer

[Run the Architecture Pattern Viewer](./arch-pattern-viewer.html)

Perfect! I've created a comprehensive architecture pattern viewer at /docs/sims/arch-pattern-viewer/arch-pattern-viewer.html. Here's what the
  viewer includes:

  ✅ Features:

  🎯 Core Functionality:
  - URL Parameter Support: Pass ?json=path/to/file.json to load a pattern automatically
  - Manual File Loading: Text input field to enter JSON file paths
  - Interactive Network Visualization: Built with vis-network.js

  🎨 Visual Design:
  - Clean, professional interface with Material Design colors
  - Pattern information display (title, node/edge counts)
  - Responsive layout that works on different screen sizes
  - Error handling with user-friendly messages

  🖱️ Interactive Features:
  - Mouse Controls: Zoom with wheel, pan by dragging, move nodes
  - Node Selection: Click nodes and edges for interaction
  - Keyboard Support: Press Enter in input field to load
  - Auto-fit: Automatically centers and scales the network view

  🔧 Technical Features:
  - All JavaScript Inline: No external dependencies except vis-network.js CDN
  - Error Handling: Validates JSON structure and handles network errors
  - Network Destruction: Properly cleans up previous visualizations
  - Event Logging: Console logs for debugging selected nodes/edges

  📖 Usage Examples:

  1. Direct URL: arch-pattern-viewer.html?json=../../patterns/rag/rag.json
  2. Manual Input: Enter ../../patterns/agentic-orchestration/agentic-orchestration.json
  3. Local Development: Works with any valid relative or absolute path to the JSON files

  The viewer is ready to use and will render beautiful, interactive diagrams of all the architectural patterns you created!

