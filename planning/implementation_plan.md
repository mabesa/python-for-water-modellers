# Python for Water Modellers - Implementation Plan
**Status:** ✅ ALL MODULES COMPLETE
**Last Updated:** 7 December 2025

---

## Project Complete! 🎉

All 10 tutorial modules have been created and are ready for deployment.

### Completed Modules
| Module | Title | Status |
|--------|-------|--------|
| 0 | Introduction & Prerequisites | ✅ Complete |
| 1a | Installing VS Code | ✅ Complete |
| 1b | Python Extension Setup | ✅ Complete |
| 2a | Understanding Environments | ✅ Complete |
| 2b | Installing and Using uv | ✅ Complete |
| 3a | Python Basics for Water Modellers | ✅ Complete |
| 3b | AI-Assisted Coding | ✅ Complete |
| 4a | Getting Hydrological Data | ✅ Complete |
| 4b | Discharge Analysis | ✅ Complete |
| 5 | Resources & Next Steps | ✅ Complete |

### Infrastructure
- ✅ Jupyter Book 2.x with MyST format
- ✅ GitHub Actions auto-deployment
- ✅ Binder support for interactive notebooks
- ✅ PDF export capability configured

---

## Project Overview

**Goal:** Create a comprehensive, beginner-friendly Python tutorial series specifically for water modellers (hydrologists, hydraulic engineers, groundwater modellers).

**Delivery:** Jupyter Book published via GitHub Pages, with PDF export capability for partners.

**Target Audience:**
- Middle-aged professionals transitioning to Python
- Bachelor/master students in water engineering
- Varying technical backgrounds (Excel users → programming beginners)

**Key Differentiators:**
- Water modelling examples from day 1
- Modern tools (uv, AI assistance)
- Real Swiss data (CAMELS-CH)
- Practical focus over theory

---

## Technical Stack (DECIDED)

| Component | Tool/Technology | Why |
|-----------|----------------|-----|
| **Language** | Python 3.12 | Modern, stable, long-term support |
| **Package Manager** | uv | Fast, modern, handles Python installation |
| **IDE** | VS Code | Free, popular, excellent Python support |
| **Tutorial Format** | Jupyter Notebooks (.ipynb) | Interactive, mix code + text, industry standard |
| **Publishing** | Jupyter Book 2.x (MyST) → GitHub Pages | Modern format, professional navigation, free hosting, PDF export |
| **Version Control** | Git + GitHub | Industry standard, enables collaboration |
| **Data Source** | CAMELS-CH | Real Swiss discharge data, open-source |
| **Dependencies** | pyproject.toml + uv.lock | Modern Python packaging, reproducible |
| **CI/CD** | GitHub Actions with uv | Automated deployment on push to main |

---

## Repository Structure (CURRENT)

```
python-for-water-modellers/
├── README.md                          # ✅ Learner-focused landing page
├── pyproject.toml                     # Python dependencies (core + dev)
├── uv.lock                            # Locked dependency versions
├── .python-version                    # Python 3.12
├── myst.yml                          # ✅ Jupyter Book 2.x configuration
├── .github/
│   ├── copilot-instructions.md       # AI coding guidelines
│   └── workflows/
│       └── deploy.yml                # ✅ Auto-deploy to GitHub Pages (uv-based)
├── tutorials/
│   ├── 00_introduction.ipynb         # ✅ COMPLETE
│   ├── 01a_vscode_installation.ipynb # ✅ COMPLETE
│   ├── 01b_python_extension.ipynb    # ✅ COMPLETE
│   ├── 02a_environment_concepts.ipynb # ✅ COMPLETE
│   ├── 02b_installing_uv.ipynb       # ✅ COMPLETE
│   ├── 03a_python_basics.ipynb       # ✅ COMPLETE
│   ├── 03b_ai_assisted_coding.ipynb  # ✅ COMPLETE
│   ├── 04a_getting_data.ipynb        # ✅ COMPLETE
│   ├── 04b_discharge_analysis.ipynb  # ✅ COMPLETE
│   └── 05_resources_next_steps.ipynb # ✅ COMPLETE
├── _build/                            # ✅ Jupyter Book build output (gitignored)
│   ├── html/                          # Static website files
│   └── templates/                     # MyST templates
├── data/                              # ✅ Created
│   └── camels_01013500_discharge.csv # ✅ Sample data (downloaded in Module 3a)
├── examples/                          # For future standalone scripts
├── planning/
│   └── implementation_plan.md        # This file (project status & reference)
├── src/
│   └── python_for_water_modellers/
│       ├── __init__.py
│       ├── main.py
│       └── paths.py                  # ✅ get_data_path() for Binder compatibility
├── binder/
│   └── postBuild                     # ✅ Binder setup script
└── .gitignore
```

---

## Module Breakdown (DETAILED)

### ✅ Module 0: Introduction & Prerequisites (COMPLETE)
**File:** `00_introduction.ipynb`  
**Status:** Complete and reviewed  
**Time:** 10 minutes reading

**Content:**
- Why Python for water modelling?
- What you'll learn in this series
- Essential terminology (glossary)
- What "success" looks like (example code)
- Modern learning approach (AI-assisted)
- Prerequisites & requirements
- FAQ

**Next Action:** None (complete)

---

### Module 3a: Python Basics for Water Modellers (COMPLETE)
**File:** `03a_python_basics.ipynb`  
**Status:** ✅ Complete (formerly Module 2c)  
**Time:** 20-25 minutes

**Content:**
- Understanding notebook cells (markdown vs code)
- First code cell execution and Python interpreter selection
- Variables and calculations (Manning's equation example)
- Basic operators and math operations
- Imports (math module for π, sqrt)
- Functions: anatomy, creating reusable calculations
- Hydraulic examples: pipe discharge, critical depth
- Practice exercise: Froude number calculation
- Engineering best practices: units in docstrings, descriptive names

**Dependencies:** Module 2b complete  
**Deliverables:** Understanding of Python fundamentals needed for data analysis

**Key Features:**
- Natural progression after environment setup
- All examples use hydraulic/hydrological formulas
- Includes both worked examples and practice exercises
- Prepares students for pandas/matplotlib in Module 4

---

### Module 3b: AI-Assisted Coding (COMPLETE)
**File:** `03b_ai_assisted_coding.ipynb`
**Status:** ✅ Complete
**Time:** 20-25 minutes

**Content:**
- **WHAT AI CAN DO:**
  - Write code from descriptions
  - Debug errors
  - Explain existing code
  - Suggest improvements
- **WHAT AI CANNOT DO:**
  - Validate conceptual models
  - Know correct equation for flow regime
  - Verify physical plausibility
  - **Critical warning for water modellers**
- **EFFECTIVE PROMPTING:**
  - Template structure
  - Vague vs. specific examples
  - Domain context (units, water engineering terms)
- **QUICK DEMO:**
  - Take Python basics examples
  - Ask AI to add new calculations
  - Copy, test, verify result
- **VERIFICATION STRATEGIES:**
  - Test with known solutions
  - Sanity checks (units, magnitudes)
  - Compare with analytical equations
  - When to trust vs. verify

**Dependencies:** Module 3a (Python basics)  
**Deliverables:**
- Understanding of AI limitations
- Ability to write effective prompts
- Verification strategies

**Strategic Placement:** Teaching AI assistance early means students can use it when tackling real data in Modules 4a and 4b.

---

### Module 4a: Getting Hydrological Data (COMPLETE)
**File:** `04a_getting_data.ipynb`
**Status:** ✅ Complete (formerly Module 3a)  
**Time:** 25-30 minutes

**Content:**
- **THE DATA CHALLENGE:**
  - Why getting data is often the hardest part
  - Different formats, sources, quality issues
  - The value of standardized datasets
- **OPEN DATA SOURCES:**
  - Global datasets: Caravan, GRDC, GloFAS
  - Regional CAMELS family: CAMELS-US, CAMELS-CH, CAMELS-CL, CAMELS-BR, etc.
  - Brief mention of national databases
- **PRACTICAL: USING PYGEOHYDRO:**
  - Access CAMELS dataset programmatically
  - Explore available stations
  - Filter and select stations by criteria
  - Download streamflow data
  - Understanding file paths (absolute vs relative)
  - Save to CSV for offline use
- **FOR SWISS-SPECIFIC WORK:**
  - CAMELS-CH overview and access (Zenodo)
  - Citation requirements
- **DATA QUALITY CONSIDERATIONS:**
  - Missing values, suspicious values
  - Time series continuity
  - Physical plausibility checks

**Dependencies:** Module 3a (Python basics), Module 3b (AI assistance available)  
**Deliverables:**
- Understanding of open hydrological data landscape
- Ability to fetch CAMELS data via Python
- Local CSV file ready for analysis

**Key Features:**
- Students now have AI assistance for troubleshooting
- Notebook-only workflow (no separate .py files)
- File paths explanation included
- Real CAMELS data downloaded

---

### Module 4b: Your First Water Modelling Script (COMPLETE)
**File:** `04b_discharge_analysis.ipynb`
**Status:** ✅ Complete (formerly Module 3b)  
**Time:** 40-50 minutes (hands-on)

**Content:**
- **DATA VERIFICATION:**
  - Check for downloaded data from Module 4a
  - List available CSV files
- **DATA LOADING:**
  - Load CSV discharge data
  - Initial data exploration
  - Data type verification
- **DATA PREPARATION:**
  - Convert dates to datetime
  - Set date as index for time-series operations
  - Handle missing values
- **STATISTICAL ANALYSIS:**
  - Calculate flow statistics (mean, median, std, min, max)
  - Compute percentiles (Q10, Q90)
  - Monthly summary statistics
- **EXTREME EVENTS:**
  - Identify high and low flow periods
  - Find maximum and minimum events
- **VISUALIZATIONS:**
  - Hydrograph with mean line and high flow markers
  - Monthly distribution boxplot
  - Save plots to files
- **CODE UNDERSTANDING:**
  - Key pandas operations explained
  - Design patterns highlighted
  - Adaptation guidelines for own data

**Dependencies:** Module 4a complete (data downloaded), Module 3b (AI assistance)  
**Deliverables:**
- Complete discharge analysis workflow
- Generated plots and statistics
- Understanding of pandas basics for time series

**Key Features:**
- Capstone project using all learned skills
- Students can use AI for extensions and debugging
- Uses real CAMELS data
- Comprehensive explanations for beginners

---

### Module 5: Resources & Next Steps (COMPLETE)
**File:** `05_resources_next_steps.ipynb`
**Status:** ✅ Complete
**Time:** Reference (browsable)

### ⏭️ Module 1a: Installing VS Code (COMPLETE)
**File:** `01a_vscode_installation.ipynb`  
**Status:** ✅ Complete  
**Time:** 15-20 minutes  
**Format:** Guided notebook with external links

**Content:**
- **WHY:** What is an IDE? Why VS Code?
- **INSTALLATION:** 
  - Link to VS Code official download
  - Link to Getting Started video
  - Platform-specific notes (Windows/Mac/Linux)
- **VERIFICATION:** 
  - Open VS Code
  - Recognize interface (Explorer, Editor, Terminal)
  - Screenshot checkpoints
- **TROUBLESHOOTING:**
  - Installation issues
  - Permissions on work computers
- **WATER MODELLING CONTEXT:**
  - Why text editor vs. GUI software
  - Reproducibility benefits

**Dependencies:** None  
**Deliverables:** Working VS Code installation

---

### Module 1b: Python Extension Setup (COMPLETE)
**File:** `01b_python_extension.ipynb`  
**Status:** ✅ Complete  
**Time:** 10-15 minutes

**Content:**
- **WHY:** What are extensions? Why Python extension?
- **INSTALLATION:**
  - Step-by-step with screenshots
  - Link to Python extension guide
- **VERIFICATION:**
  - Create test.py file
  - See syntax highlighting
  - Test IntelliSense
- **OPTIONAL EXTENSIONS:**
  - Jupyter (for notebooks)
  - Python Indent
  - autoDocstring

**Dependencies:** Module 1a complete  
**Deliverables:** VS Code with Python support

---

### Module 2a: Understanding Environment Management (COMPLETE)
**File:** `02a_environment_concepts.ipynb`  
**Status:** ✅ Complete  
**Time:** 15 minutes (conceptual, no coding)

**Content:**
- **THE PROBLEM:**
  - Python version conflicts
  - Package version conflicts between projects
  - "Works on my machine" syndrome
  - Reproducibility in science
- **THE SOLUTION:**
  - Virtual environments explained
  - Visual analogy: Separate labs for experiments
- **TRADITIONAL VS. MODERN:**
  - pip + venv (manual, slow)
  - conda (heavy, complex)
  - uv (modern, fast, integrated)
- **WHY UV:**
  - One tool for everything
  - Fast (written in Rust)
  - Handles Python installation
  - Industry trend

**Dependencies:** None (pure explanation)  
**Deliverables:** Understanding of why we need uv

---

### Module 2b: Installing & Using uv (COMPLETE)
**File:** `02b_installing_uv.ipynb`  
**Status:** ✅ Complete  
**Time:** 20-30 minutes

**Content:**
- **INSTALLATION:**
  - Link to uv installation guide
  - Platform-specific commands
  - Verification: `uv --version`
- **FIRST PROJECT:**
  - `uv init my-first-project`
  - Understanding created files (pyproject.toml, .venv)
  - Opening in VS Code
- **SELECTING INTERPRETER:**
  - How VS Code finds Python
  - Selecting .venv interpreter
  - Verification in status bar
- **INSTALLING PACKAGES:**
  - `uv add pandas numpy matplotlib`
  - Understanding dependency management
- **RUNNING CODE:**
  - `uv run script.py`
  - Why this ensures correct environment
- **VERIFICATION TEST:**
  - Simple script importing packages
  - Create test plot
- **LINKS:**
  - Real Python uv guide
  - uv docs

**Dependencies:** Modules 1a, 1b, 2a  
**Deliverables:** Working uv setup, first project created

---

## Data Preparation Tasks

### CAMELS-CH Sample Data
**Priority:** High (needed for Module 3)

**Requirements:**
- [ ] Select 2-3 representative stations:
  - Large river (e.g., Aare at Untersiggenthal)
  - Alpine catchment (snowmelt-dominated)
  - Regulated station (hydropower influence)
- [ ] Extract 2-3 years of daily discharge data
- [ ] Format as simple CSV (date, discharge_m3s, station_info)
- [ ] Test data loads correctly in pandas
- [ ] Document:
  - Data source and licensing
  - Station characteristics
  - Download/access instructions
  - Known data quality issues

**Files to create:**
- `data/aare_untersiggenthal_2020_2022.csv`
- `data/alpine_station_2020_2022.csv`
- `data/regulated_station_2020_2022.csv`
- `data/data_sources.md` (metadata and provenance)

---

## Publishing Workflow

### Local Development
```bash
# Create/edit notebook
# Run cells, generate outputs
# Save notebook WITH outputs

# Start development server (auto-reloads on changes)
uv run jupyter-book start

# View at http://localhost:3000
# Make changes, server rebuilds automatically

# For static build (optional):
uv run jupyter-book build --html
open _build/html/index.html
```

### Git Workflow
```bash
# Stage changes
git add tutorials/XX_module_name.ipynb
git add myst.yml  # if updated TOC or config

# Commit with descriptive message
git commit -m "Add Module XX: Title"

# Push to GitHub
git push
```

### Auto-Deployment
1. GitHub Actions triggers on push to main
2. Workflow installs uv, Python 3.12
3. Runs `uv sync --all-groups`
4. Builds Jupyter Book: `uv run jupyter-book build --html`
5. Deploys to GitHub Pages
6. ~2-3 minutes total

### Verification
- Check Actions tab for green checkmark
- Visit: `https://mabesa.github.io/python-for-water-modellers`
- Navigate between modules
- Test search, download buttons

---

## Dependencies & Versions

### Python Version
**Required:** 3.12  
**Managed by:** uv (auto-install)  
**Specified in:** `.python-version`, `pyproject.toml`

### Core Dependencies (Tutorial Content)
```toml
[project.dependencies]
numpy >= 1.24.0
pandas >= 2.0.0
matplotlib >= 3.7.0
scipy >= 1.10.0
```

### Dev Dependencies (Publishing)
```toml
[dependency-groups.dev]
jupyter >= 1.0.0
ipykernel >= 6.25.0
jupyter-book >= 2.0.0  # v2.x uses MyST format
sphinx-design >= 0.5.0
sphinx-copybutton >= 0.5.0
```

### Installation
```bash
# Full install (content + publishing)
uv sync --all-groups

# Just content packages
uv sync
```

---

## Consistency Checklist

Before creating each module, verify:

- [ ] **Python version:** All references to 3.12 (not 3.11)
- [ ] **Package manager:** Use `uv` commands, not `pip`
- [ ] **Dependencies:** Defined in `pyproject.toml`, not requirements.txt
- [ ] **File paths:** Consistent with repository structure
- [ ] **GitHub org:** `mabesa/python-for-water-modellers`
- [ ] **TOC:** Module added to `myst.yml` under `project.toc` with correct path
- [ ] **Jupyter Book version:** 2.x (MyST format), not legacy 1.x
- [ ] **Config file:** Update `myst.yml`, not `_config.yml` or `_toc.yml`
- [ ] **Build command:** `uv run jupyter-book build --html` or `uv run jupyter-book start`
- [ ] **Outputs:** Notebooks committed WITH outputs (for educational value)
- [ ] **Links:** Internal links use relative paths
- [ ] **License:** CC-BY 4.0 mentioned where appropriate
- [ ] **Terminology:** Consistent with Module 0 glossary

---

## Quality Standards

### For Each Notebook

**Structure:**
- Clear title and description at top
- Time estimate
- Prerequisites listed
- Learning objectives stated
- Checkpoints throughout
- Troubleshooting section
- Next steps/links at end

**Content:**
- Water modelling context in every module
- Real examples, not generic
- Explain WHY before HOW
- Use analogies for complex concepts
- Screenshots where helpful
- Code cells runnable as-is
- Outputs visible (plots, results)

**Tone:**
- Beginner-friendly
- Encouraging, not condescending
- Practical over theoretical
- "You" language (direct address)
- Short sentences
- No jargon without explanation

---

## Timeline Estimate

| Module | Content Creation | Testing | Total | Status |
|--------|-----------------|---------|-------|--------|
| 0 | ✅ Complete | ✅ | 2h | ✅ Done |
| Infrastructure | ✅ Complete | ✅ | 3h | ✅ Done (MyST migration) |
| 1a | ✅ Complete | ✅ | 2.5h | ✅ Done |
| 1b | ✅ Complete | ✅ | 1.5h | ✅ Done |
| 2a | ✅ Complete | ✅ | 2h | ✅ Done |
| 2b | ✅ Complete | ✅ | 4h | ✅ Done |
| 3a | ✅ Complete | ✅ | 2h | ✅ Done (Python Basics, formerly 2c) |
| 3b | ✅ Complete | ✅ | 2.5h | ✅ Done (AI-Assisted Coding) |
| 4a | ✅ Complete | ✅ | 5h | ✅ Done (Getting Data, formerly 3a) |
| 4b | ✅ Complete | ✅ | 5h | ✅ Done (Analysis, formerly 3b) |
| 5 | ✅ Complete | ✅ | 2.5h | ✅ Done (Resources & Next Steps) |
| **Completed** | | | **32h** | |
| **Remaining** | | | **0h** | |
| **Total** | | | **~32h** | |

**Current status:** Execute notebooks → Deploy  
**Final review:** +2h (after all modules)  
**Grand total:** ~34 hours (27h completed, ~7h remaining)

---

## Recent Enhancements (Dec 7, 2025 - v1.1)

✅ **Module 3a: Added "Coming from Excel?" section**
- Excel → Python translation table
- Motivates the switch with concrete benefits
- Mindset shift explanation (interactive vs. scripted)
- Placed at start of module to build confidence

✅ **Module 4b: Added Flow Duration Curve section**
- Full explanation of FDC purpose and interpretation
- Working code with log-scale plot
- Q10/Q50/Q90 reference lines
- Flow variability ratio metric
- Catchment characterization guidance

---

## Remaining Tasks

1. ⏭️ Execute all notebooks with outputs (for visual results in published book)
2. ⏭️ Final review and polish

### Future Enhancements (Optional)
- Custom domain for GitHub Pages
- Google Analytics for usage tracking
- Google Colab support
- Video supplements / screen recordings
- Translations to other languages
- Project logo
- Swiss-specific data (CAMELS-CH stations)

---

**Status:** All modules complete and deployed via GitHub Actions!