# Welcome to Python for Water Modellers! 🌊

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mabesa/python-for-water-modellers/main?urlpath=lab/tree/tutorials/00_introduction.ipynb)

**📖 [Read the Tutorial Online](https://mabesa.github.io/python-for-water-modellers/)**

**Learn Python programming tailored specifically for water resources engineers, hydrologists, and hydraulic modellers.**

This hands-on tutorial will take you from complete beginner to confidently writing Python scripts for real-world water engineering tasks—analyzing discharge data, calculating hydraulic parameters, and automating repetitive tasks that currently consume hours of your time.

## Who Is This For?

This tutorial is designed for:
- **Hydraulic engineers** wanting to automate calculations and data processing
- **Hydrologists** analyzing rainfall-runoff data and streamflow time series  
- **Groundwater modellers** working with observation data and water balance calculations
- **Water resources planners** needing to process and visualize large datasets

**No prior programming experience required!** We'll start from the very beginning and build up skills progressively.

## What You'll Learn

By the end of this tutorial series, you'll be able to:

✅ Write Python scripts to automate hydraulic calculations (Manning's equation, pipe flow, etc.)  
✅ Read, process, and analyze hydrological time series data (discharge, rainfall, water levels)  
✅ Create professional visualizations of water resources data  
✅ Use AI assistants (like GitHub Copilot) to accelerate your coding  
✅ Build simple water balance models and flow routing calculations

## Tutorial Structure

This course is organized into focused modules that build on each other:

**Module 0: Introduction & Prerequisites** (👈 Start here!)  
Understand why Python is valuable for water modelling and what you'll need to get started.

**Module 1: Setting Up Your Development Environment**
- **1a: Installing VS Code** - Download and set up your code editor
- **1b: Python Extension** - Add Python support to VS Code

**Module 2: Understanding Python Environment Management**
- **2a: Environment Concepts** - Why virtual environments matter for reproducible science
- **2b: Installing uv** - Set up the modern Python package manager

**Module 3: Python Fundamentals for Water Modellers**
- **3a: Python Basics** - Learn variables, functions, and imports through hydraulic calculations
- **3b: AI-Assisted Coding** - Discover how AI can help you write code faster

**Module 4: Real-World Data Analysis**
- **4a: Getting Hydrological Data** - Access open streamflow datasets programmatically
- **4b: Discharge Analysis** - Analyze real discharge data from CAMELS

**Module 5: Resources & Next Steps**
Find the best learning resources and community support for your continued journey.

## How to Use This Tutorial

### Option 1: Read Online (Easiest)
Simply navigate through the chapters using the sidebar. Each module includes explanations, code examples, and practical exercises.

### Option 2: Run in the Cloud with Binder (No Installation!)
Click the **Launch Binder** badge above to open Module 0 directly in JupyterLab. This lets you run and modify code without installing anything on your computer. The first launch can take a minute or two while Binder builds or wakes up the environment.

Binder is best for previewing one or two notebooks. Public mybinder.org sessions are shared, ephemeral environments with limited memory; the [Binder user guidelines](https://mybinder.readthedocs.io/en/latest/about/user-guidelines.html) describe a 1 GB guaranteed / 2 GB maximum memory range and note that sessions are not guaranteed to stay running indefinitely. If Binder disconnects after several notebooks, close unused notebooks, restart the kernel, or relaunch Binder. For working through the full course, use a local Jupyter installation.

### Option 3: Run Locally with Jupyter Notebooks (Recommended)
If you want the most reliable setup for the whole tutorial:

1. **Install Python 3.12+** from the [official Python downloads page](https://www.python.org/downloads/)
2. **Install uv** using the [official uv installation guide](https://docs.astral.sh/uv/getting-started/installation/)
3. **Clone this repository** and navigate to it
4. **Install dependencies**: `uv sync --all-groups`
5. **Start JupyterLab**: `uv run jupyter lab`
6. **Open notebooks** in the `tutorials/` folder

The project environment installs Jupyter for you. If you want to install Jupyter separately, use the official [Project Jupyter installation guide](https://jupyter.org/install) or the [JupyterLab installation documentation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html).

```bash
git clone https://github.com/mabesa/python-for-water-modellers.git
cd python-for-water-modellers
uv sync --all-groups
uv run jupyter lab
```

Detailed installation instructions are in Module 1 and Module 2.

### Quick Local Checklist

1. **Python installed?** Run `python --version`
2. **uv installed?** Run `uv --version`
3. **Dependencies installed?** Run `uv sync --all-groups`
4. **Jupyter starts?** Run `uv run jupyter lab`

## Why This Tutorial Is Different

🎯 **Domain-Specific**: Every example uses real water engineering problems—no generic programming exercises  
📊 **Real Data**: Work with actual USGS discharge data from CAMELS, not synthetic datasets  
🤖 **AI-Powered**: Learn to leverage modern AI coding assistants from day one  
⚡ **Modern Tools**: Uses current Python tools such as uv, VS Code, and JupyterLab
💡 **Practical Focus**: Build skills you'll use immediately in your daily work

## Prerequisites

- A computer running Windows, macOS, or Linux
- Willingness to learn and experiment
- Basic understanding of water engineering concepts (discharge, catchments, hydraulic calculations)

**No programming experience necessary!**

## Ready to Begin?

👉 **[Start with Module 0: Introduction & Prerequisites](tutorials/00_introduction.ipynb)**

---

## About This Tutorial

This tutorial was developed with AI assistance (Claude) but every module has been carefully curated and reviewed by experienced water modellers and Python practitioners. We've tailored the content specifically to address the real challenges we've observed when helping hydrologists, hydraulic engineers, and groundwater modellers transition to Python—from understanding why virtual environments matter to working with actual streamflow data. We believe in transparency about AI use while ensuring professional-quality, domain-relevant content.

## For Developers & Contributors

If you're interested in contributing to this tutorial or running it locally for development:

- **Repository**: [github.com/mabesa/python-for-water-modellers](https://github.com/mabesa/python-for-water-modellers)
- **Package Manager**: uv ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))
- **Python Version**: 3.12+
- **Build System**: Jupyter Book 2.x with MyST
- **Deployment**: Automated via GitHub Actions on push to main
- **License**: CC-BY 4.0 (content) / MIT (code)

### Automated Maintenance Checks

- **[Binder Health](https://github.com/mabesa/python-for-water-modellers/actions/workflows/binder-health.yml)** launches the public Binder environment for `main`, waits for Jupyter to become responsive, and shuts the test server down. This catches broken Binder builds and obvious connection failures.
- **[Link Check](https://github.com/mabesa/python-for-water-modellers/actions/workflows/link-check.yml)** periodically scans the README, MyST configuration, and tutorial notebooks for external links that have gone missing. Binder launch URLs are checked by Binder Health instead of the link checker.

### Local Development

```bash
# Clone and install
git clone https://github.com/mabesa/python-for-water-modellers.git
cd python-for-water-modellers
uv sync --all-groups

# Start local development server (auto-reloads)
uv run jupyter-book start

# Or build static HTML
uv run jupyter-book build --html
```
