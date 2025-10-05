AI Debugger VS Code extension (minimal)

Usage

1. Start the Flask app locally (default port 5002):

```bash
python3 app.py
```

2. In VS Code, install this extension locally (use `vsce` or run from the Extension Development Host).
3. Run the command `AI Debugger: Open Web UI` from the Command Palette. The extension will try `http://127.0.0.1:5002/health` first; if healthy it opens the UI in a WebView.

Configuration

- You can set the base URL in your VS Code settings under `aiDebugger.url` if you run the Flask app on a different port or host.
