# Setting Up VS Code with uv: A Step-by-Step Guide
## For Water Modellers New to Python

---

## What You'll Learn
By the end of this guide, you'll have a working Python environment ready for water modelling, using modern tools that professionals use today.

**Time required:** ~30 minutes

---

## Step 1: Install VS Code

1. Go to [code.visualstudio.com](https://code.visualstudio.com/)
2. Click the big blue **Download** button
3. Run the installer:
   - **Windows:** Double-click the downloaded `.exe` file
   - **Mac:** Drag the app to your Applications folder
4. Open VS Code

> 💡 **What is VS Code?** It's a free text editor designed for writing code. Think of it like Word, but for programming.

---

## Step 2: Install the Python Extension

1. In VS Code, click the **Extensions** icon in the left sidebar (looks like 4 squares)
2. Type `Python` in the search box
3. Click **Install** on "Python" by Microsoft (the one with millions of downloads)
4. Wait for installation to complete

---

## Step 3: Install uv

**uv** is a modern Python package manager that handles Python installation and project dependencies. It's fast and simple.

### Windows (PowerShell)
1. Press `Win + X`, then click **Terminal** (or **PowerShell**)
2. Paste this command and press Enter:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
3. **Close and reopen** your terminal

### Mac/Linux (Terminal)
1. Open Terminal
2. Paste this command and press Enter:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
3. **Close and reopen** your terminal

### Verify Installation
Type this command:
```bash
uv --version
```
You should see something like `uv 0.5.x` — this means it worked!

> 💡 **What is uv?** It manages Python versions and packages for you. Instead of manually downloading Python and worrying about compatibility, uv handles everything.

---

## Step 4: Create Your First Project

Now we'll create a folder for your water modelling work.

### Create a project folder
1. Open your terminal (PowerShell on Windows, Terminal on Mac)
2. Navigate to where you want your projects:
```bash
cd Documents
```
3. Create and initialize a new project:
```bash
uv init my-water-project
cd my-water-project
```

This creates a folder with:
- `pyproject.toml` — your project's configuration file
- `hello.py` — a sample Python file
- `.python-version` — specifies which Python version to use

---

## Step 5: Open the Project in VS Code

### Method 1: From the terminal
```bash
code .
```

### Method 2: From VS Code
1. File → Open Folder
2. Navigate to your `my-water-project` folder
3. Click **Select Folder**

---

## Step 6: Install Packages for Water Modelling

Water modelling typically needs these packages:
- **pandas** — data manipulation (like Excel, but better)
- **numpy** — numerical calculations
- **matplotlib** — creating plots
- **flopy** — MODFLOW interface (for groundwater modelling)

### Install packages with uv

In your terminal (you can use VS Code's built-in terminal: View → Terminal), type:

```bash
uv add pandas numpy matplotlib
```

For groundwater modelling, also add:
```bash
uv add flopy
```

> 💡 **What happens?** uv downloads these packages and records them in your `pyproject.toml` file. Anyone can recreate your exact setup later!

---

## Step 7: Select the Python Interpreter in VS Code

VS Code needs to know which Python to use.

1. Press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac)
2. Type `Python: Select Interpreter`
3. Choose the one that shows `.venv` in the path — this is your project's virtual environment

If you don't see it, click **Enter interpreter path** and navigate to:
- Windows: `my-water-project\.venv\Scripts\python.exe`
- Mac/Linux: `my-water-project/.venv/bin/python`

---

## Step 8: Run Your First Script

### Create a test file
1. In VS Code, right-click in the Explorer panel → New File
2. Name it `test_setup.py`
3. Paste this code:

```python
# Test that everything works
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("✅ All packages imported successfully!")
print(f"   pandas version: {pd.__version__}")
print(f"   numpy version: {np.__version__}")

# Quick test: create some "discharge" data
dates = pd.date_range('2024-01-01', periods=30, freq='D')
discharge = np.random.uniform(5, 25, 30)  # m³/s

# Plot it
plt.figure(figsize=(10, 4))
plt.plot(dates, discharge, 'b-', linewidth=1)
plt.xlabel('Date')
plt.ylabel('Discharge (m³/s)')
plt.title('Test Hydrograph')
plt.tight_layout()
plt.savefig('test_plot.png', dpi=150)
print("✅ Plot saved as 'test_plot.png'")
```

### Run the script
**Option 1:** Click the ▶️ play button in the top-right corner

**Option 2:** In the terminal, type:
```bash
uv run test_setup.py
```

If you see the checkmarks and a plot file appears, **congratulations — your setup is complete!**

---

## Quick Reference Card

| Task | Command |
|------|---------|
| Create new project | `uv init project-name` |
| Add a package | `uv add package-name` |
| Run a script | `uv run script.py` |
| Update all packages | `uv sync` |
| See installed packages | `uv pip list` |

---

## Understanding Virtual Environments

### 💡 What is a virtual environment (.venv)?

Think of it like a **separate workspace for each project**:

| Without Virtual Environments | With Virtual Environments |
|------------------------------|---------------------------|
| All packages installed globally | Each project has its own packages |
| Package conflicts between projects | Packages isolated per project |
| Hard to share exact setup | Easy to recreate environment |
| "Works on my machine" problems | Reproducible across machines |

**Example scenario:**
- Project A needs pandas version 1.5
- Project B needs pandas version 2.0
- Without virtual environments → conflict!
- With virtual environments → both work fine

**uv automatically creates `.venv` for each project** - you don't need to think about it much, just know it keeps things organized.

---

## Troubleshooting

### "uv is not recognized" (Windows)
→ Close and reopen your terminal after installing uv
→ If still not working, restart your computer
→ Check installation: `where uv` should show a path

### "uv: command not found" (Mac/Linux)
→ Close and reopen terminal
→ Check installation: `which uv` should show a path
→ If not found, try: `source ~/.bashrc` or `source ~/.zshrc`

### "No Python interpreter selected" in VS Code
1. Press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac)
2. Type: `Python: Select Interpreter`
3. Choose the one with `.venv` in the path
4. If none appear, run `uv sync` in terminal first

### "Module not found" error when running script
→ Make sure you ran `uv add package-name` for that package
→ Verify VS Code is using the `.venv` interpreter (bottom right corner)
→ Try running: `uv sync` to refresh environment

### VS Code terminal shows wrong directory
→ File → Open Folder and select your project folder
→ VS Code's terminal should open in the project root
→ You can check with: `pwd` (Mac/Linux) or `cd` (Windows)

### Permission denied errors (Mac/Linux)
→ Don't use `sudo` with uv commands
→ uv installs in your user directory - no admin rights needed

### Packages install but imports fail
→ Check you're running with `uv run script.py` OR
→ Make sure VS Code selected the correct Python interpreter

---

## Quick Reference: Terminal Navigation

New to command-line interfaces? Here are the basics:

| Command | What it does | Example |
|---------|--------------|---------|
| `pwd` | Show current directory | `pwd` |
| `ls` | List files (Mac/Linux) | `ls` |
| `dir` | List files (Windows) | `dir` |
| `cd foldername` | Go into folder | `cd Documents` |
| `cd ..` | Go up one level | `cd ..` |
| `cd ~` | Go to home directory | `cd ~` |

**Tip:** Use Tab key to auto-complete folder/file names!

---

## Next Steps

You're now ready to:
1. **Load real hydrological data** — See the "First Water Script" tutorial
2. **Learn FloPy** — Check out the USGS tutorials
3. **Try LLM-assisted coding** — See the "Coding with AI" guide

---

## Appendix: Common uv Commands

| Task | Command | When to use |
|------|---------|-------------|
| Create new project | `uv init project-name` | Starting fresh |
| Add a package | `uv add pandas` | Need a new library |
| Remove a package | `uv remove pandas` | Don't need it anymore |
| Update packages | `uv sync --upgrade` | Get latest versions |
| Run a script | `uv run script.py` | Execute Python code |
| See what's installed | `uv pip list` | Check environment |
| Create requirements.txt | `uv pip freeze > requirements.txt` | Share exact versions |
| Install from requirements | `uv pip install -r requirements.txt` | Recreate environment |

---

## Getting Help

**uv Documentation:** [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

**Built-in help:**
```bash
uv --help              # General help
uv add --help          # Help for specific command
```

**VS Code Python Help:**
- Press `F1` → type "Python" to see all Python commands
- View → Command Palette → "Python: Show Output" for diagnostic info