<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Preview Hacker Toolbox Menu</title>
  <script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg:#0b0f14; --card:#121821; --text:#e6edf3; --muted:#9fb2c7;
      --accent:#00d084; --border:#1f2a36; --disabled:#555;
    }
    body { margin:0; font-family:Inter,system-ui,sans-serif; background:var(--bg); color:var(--text); line-height:1.65; }
    header { padding:28px 24px; border-bottom:1px solid var(--border); background:rgba(18,24,33,0.65); }
    .container { max-width:980px; margin:0 auto; padding:0 24px; }
    h1 { font-size:2rem; margin:0 0 10px; }
    .card { background:var(--card); border:1px solid var(--border); border-radius:14px; padding:28px; margin-top:24px; }
    .btn {
      display:inline-flex; align-items:center; gap:10px;
      padding:12px 16px; border-radius:10px; font-weight:600;
      text-decoration:none; margin-bottom:16px; cursor:pointer;
      border:none;
    }
    .btn.ready { background:var(--accent); color:#00140d; }
    .btn.ready:hover { background:#00e695; }
    .btn.loading { background:var(--disabled); color:#ccc; cursor:not-allowed; }
    pre { background:#0b111a; border:1px solid #162234; border-radius:8px; padding:12px; color:#cde1ff; overflow:auto; }
  </style>
</head>
<body>
  <header>
    <div class="container">
      <h1>Preview Hacker Toolbox Menu</h1>
      <p class="muted">Run <code>Hacker_Menu.py</code> in your browser via WebAssembly.</p>
    </div>
  </header>

  <main class="container">
    <section class="card">
      <button class="btn loading" id="runBtn" disabled>Loading Pyodide...</button>
      <h2>Output</h2>
      <pre id="output">Initializing...</pre>
    </section>
  </main>

  <script>
    let pyodide;

    async function init() {
      const out = document.getElementById("output");
      const btn = document.getElementById("runBtn");

      try {
        pyodide = await loadPyodide();
        out.textContent = "Pyodide loaded. Installing packages...";

        // Install micropip and cryptography
        await pyodide.loadPackage("micropip");
        await pyodide.runPythonAsync(`
import micropip
await micropip.install("cryptography")
        `);

        // Preload your Python files (same path in repo)
        const files = [
          "Hacker_Menu.py",          // preview menu
          "brute_force.py",
          "encryption.py",
          "password_checker.py",
          "port_scanner.py"
        ];
        for (let f of files) {
          const url = "https://raw.githubusercontent.com/adampr0gram/Hacker-Toolbox/main/Hacker%20ToolBox/" + f;
          const resp = await fetch(url);
          if (resp.ok) {
            const code = await resp.text();
            pyodide.FS.writeFile(f, code);
          }
        }

        // Also fetch the preview Hacker_Menu.py from Site/preview
        const previewUrl = "https://raw.githubusercontent.com/adampr0gram/Hacker-Toolbox/main/Site/preview/Hacker_Menu.py";
        const previewCode = await (await fetch(previewUrl)).text();
        pyodide.FS.writeFile("Hacker_Menu.py", previewCode);

        // Enable button
        btn.textContent = "Run Hacker Menu";
        btn.classList.remove("loading");
        btn.classList.add("ready");
        btn.disabled = false;
        out.textContent = "Ready. Click the button to run Hacker_Menu.py.";
      } catch (err) {
        out.textContent = "Initialization error: " + err;
      }
    }

    async function runMenu() {
      const out = document.getElementById("output");
      try {
        // Redirect print() to output
        pyodide.runPython(`
import sys
class StdoutCatcher:
    def write(self, s):
        if s.strip():
            from js import document
            out = document.getElementById("output")
            out.textContent += s + "\\n"
    def flush(self): pass
sys.stdout = StdoutCatcher()
        `);

        out.textContent = "Running Hacker_Menu.py...\n";
        await pyodide.runPythonAsync(`
import sys
sys.path.append(".")
import Hacker_Menu
        `);
      } catch (err) {
        out.textContent = "Error: " + err;
      }
    }

    document.getElementById("runBtn").addEventListener("click", runMenu);

    // Start initialization immediately
    init();
  </script>
</body>
</html>
