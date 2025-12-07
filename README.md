# Welcome to Python for Water Modellers! 🌊

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mabesa/python-for-water-modellers/main)

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
Click the **Launch Binder** badge above to open the notebooks in a free cloud environment. This lets you run and modify code without installing anything on your computer.

### Option 3: Run Locally with Jupyter Notebooks
If you want to follow along by running code yourself:

1. **Install Python 3.12+** and **uv** package manager
2. **Clone this repository** and navigate to it
3. **Install dependencies**: `uv sync --all-groups`
4. **Start Jupyter**: `uv run jupyter lab`
5. **Open notebooks** in the `tutorials/` folder

Detailed installation instructions are in Module 1.

## Why This Tutorial Is Different

🎯 **Domain-Specific**: Every example uses real water engineering problems—no generic programming exercises  
📊 **Real Data**: Work with actual USGS discharge data from CAMELS, not synthetic datasets  
🤖 **AI-Powered**: Learn to leverage modern AI coding assistants from day one  
⚡ **Modern Tools**: Uses the latest Python tools (uv, VS Code) recommended in 2024-2025  
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
- **Package Manager**: uv ([installation guide](https://github.com/astral-sh/uv))
- **Python Version**: 3.12+
- **Build System**: Jupyter Book 2.x with MyST
- **Deployment**: Automated via GitHub Actions on push to main
- **License**: CC-BY 4.0 (content) / MIT (code)

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
