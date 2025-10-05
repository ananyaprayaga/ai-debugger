const vscode = require('vscode');
const http = require('http');

function checkHealth(url, timeout = 2000) {
  return new Promise((resolve) => {
    const req = http.get(url + 'health', (res) => {
      resolve(res.statusCode === 200);
    });
    req.on('error', () => resolve(false));
    req.setTimeout(timeout, () => {
      req.abort();
      resolve(false);
    });
  });
}

function activate(context) {
  let disposable = vscode.commands.registerCommand('aiDebugger.open', async function () {
    const config = vscode.workspace.getConfiguration('aiDebugger');
    const baseUrl = config.get('url') || 'http://127.0.0.1:5002/';

    const healthy = await checkHealth(baseUrl);
    if (!healthy) {
      vscode.window.showInformationMessage('AI Debugger server not running. Start it with `python3 app.py` and try again.');
      return;
    }

    const panel = vscode.window.createWebviewPanel(
      'aiDebugger',
      'AI Debugger',
      vscode.ViewColumn.Beside,
      {
        enableScripts: true,
        retainContextWhenHidden: true,
      }
    );

    // point webview to the local URL
    panel.webview.html = `<!doctype html><html><body><iframe src="${baseUrl}" style="border:0; width:100%; height:100vh"></iframe></body></html>`;
  });

  context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
  activate,
  deactivate
};
