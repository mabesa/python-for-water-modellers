# Suggested Commands

## Package Management (uv)

```bash
# Install all dependencies (core + dev)
uv sync --all-groups

# Install only core dependencies
uv sync

# Add a new dependency
uv add <package-name>

# Add a dev dependency
uv add --group dev <package-name>

# Run a Python script
uv run python script.py

# Run a module
uv run python -m module_name
```

## Jupyter Book (Local Development)

```bash
# Start development server (auto-reloads on changes)
uv run jupyter-book start

# Build static HTML
uv run jupyter-book build --html

# Open built site
open _build/html/index.html
```

## Jupyter

```bash
# Start Jupyter Lab
uv run jupyter lab
```

## Git Workflow

```bash
# Stage changes
git add tutorials/XX_module_name.ipynb
git add myst.yml  # if updated TOC

# Commit
git commit -m "Add Module XX: Title"

# Push (triggers auto-deployment)
git push
```

## System Commands (macOS/Darwin)

```bash
# List files
ls -la

# Find files
find . -name "*.ipynb"

# Search in files
grep -r "pattern" .

# Directory navigation
cd path/to/dir
pwd
```

## Publishing Workflow

1. Edit notebooks in `tutorials/`
2. Run cells and save WITH outputs
3. Start dev server: `uv run jupyter-book start`
4. View at http://localhost:3000
5. Commit and push to trigger auto-deployment
6. Check GitHub Actions for deployment status
