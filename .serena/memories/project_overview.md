# Python for Water Modellers - Project Overview

## Purpose
Educational tutorial for water resources engineers, hydrologists, and hydraulic modellers to learn Python programming. The project targets beginners with no prior programming experience, using real-world water engineering examples.

## Target Audience
- Hydraulic engineers wanting to automate calculations
- Hydrologists analyzing rainfall-runoff data
- Groundwater modellers working with observation data
- Water resources planners processing large datasets

## Tech Stack
| Component | Tool |
|-----------|------|
| Language | Python 3.12 |
| Package Manager | uv |
| IDE | VS Code |
| Tutorial Format | Jupyter Notebooks (.ipynb) |
| Publishing | Jupyter Book 2.x (MyST) → GitHub Pages |
| Version Control | Git + GitHub |
| Data Source | CAMELS-CH (Swiss discharge data) |
| CI/CD | GitHub Actions with uv |

## Core Dependencies
- numpy >= 1.24.0
- pandas >= 2.0.0
- matplotlib >= 3.7.0
- scipy >= 1.10.0

## Dev Dependencies
- jupyter >= 1.0.0
- ipykernel >= 6.25.0
- jupyter-book >= 2.0.0 (v2.x uses MyST format)
- sphinx-design >= 0.5.0
- sphinx-copybutton >= 0.5.0

## Repository Structure
```
python-for-water-modellers/
├── README.md                    # Learner-focused landing page
├── pyproject.toml              # Python dependencies
├── uv.lock                     # Locked dependency versions
├── .python-version             # Python 3.12
├── myst.yml                    # Jupyter Book 2.x configuration
├── .github/
│   ├── copilot-instructions.md # AI coding guidelines
│   └── workflows/deploy.yml    # Auto-deploy to GitHub Pages
├── tutorials/                  # Jupyter notebooks
│   └── 00_introduction.ipynb   # First module (complete)
├── planning/                   # Planning docs
├── src/python_for_water_modellers/  # Package code
└── _build/                     # Build output (gitignored)
```

## Key URLs
- Repository: https://github.com/mabesa/python-for-water-modellers
- GitHub Pages: https://mabesa.github.io/python-for-water-modellers
