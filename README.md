Lab and practice files for Agentic AI & Prompt Engineering Class!

## VS Code Setup

### Recommended extensions
- Microsoft Python (ms-python.python)
- Jupyter (ms-toolsai.jupyter)

### Create and activate the virtual environment (for editable install)
- macOS/Linux: `python3 -m venv venv && source venv/bin/activate`
- Windows (PowerShell): `python -m venv venv; .\venv\Scripts\Activate.ps1`
- Then install the project in editable mode: `pip install -e .`

### Install dependencies
- Standard: `pip install -r requirements.txt`
- Editable project install (recommended for notebooks/imports): `pip install -e .`

### Configure VS Code to use the venv
- Open the Command Palette → “Python: Select Interpreter” → choose the interpreter inside `venv`.

### Open the integrated terminal in VS Code
- Shortcut: `Ctrl+`` (macOS: `Cmd+``) to toggle the terminal panel
- Or use menu: View → Terminal
- In the terminal, activate venv if needed: `source venv/bin/activate` (macOS/Linux) or `.\venv\Scripts\Activate.ps1` (Windows PowerShell)
