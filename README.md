# genpark-agent-in-place-canvas-ast-patcher-skill

Fine-grained block AST patcher for in-place canvas editing allowing surgical node updates without full document rebuild.

## Architecture
- **Input**: Canvas document AST, targeted node identifier, field path, and replacement payload.
- **Engine**: In-memory recursive AST walker applying surgical mutations.
- **Output**: Verified patched AST document with diff byte telemetry.
