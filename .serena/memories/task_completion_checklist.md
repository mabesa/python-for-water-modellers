# Task Completion Checklist

## Before Completing Any Task

### Code Changes
- [ ] Code follows PEP 8 style
- [ ] Type hints added where appropriate
- [ ] Docstrings included for functions
- [ ] SI units used (meters, m³/s)
- [ ] Domain assumptions documented

### Notebook Changes
- [ ] Run all cells and verify outputs
- [ ] Save notebook WITH outputs
- [ ] Test code is runnable as-is
- [ ] Water modelling context included

### Configuration Changes
- [ ] Update `myst.yml` if TOC changed
- [ ] Update `pyproject.toml` if dependencies changed

### Before Committing
- [ ] Python version references 3.12
- [ ] Use `uv` commands, not `pip`
- [ ] Internal links use relative paths
- [ ] Terminology consistent with Module 0 glossary

### Testing Locally
```bash
# Start dev server to test changes
uv run jupyter-book start

# View at http://localhost:3000
```

### Git Workflow
```bash
git add <changed-files>
git commit -m "Descriptive message"
git push  # Triggers auto-deployment
```

### After Push
- Check GitHub Actions tab for green checkmark
- Visit https://mabesa.github.io/python-for-water-modellers to verify

## Consistency Checks
- Python version: 3.12
- Package manager: uv (not pip)
- Config file: myst.yml (not _config.yml)
- Build command: `uv run jupyter-book build --html`
- GitHub org: mabesa/python-for-water-modellers
