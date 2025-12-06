# Code Style and Conventions

## Python Style
- Follow PEP 8 style guidelines
- Use descriptive variable names relevant to hydraulic/hydrological engineering
- Include docstrings for all functions with parameter descriptions
- Add comments explaining hydraulic/hydrological formulas and concepts

## Domain-Specific Conventions
- Use SI units (meters, m³/s, etc.) unless otherwise specified
- Document assumptions for hydraulic calculations
- Include references to standard equations (Manning's, Darcy-Weisbach, etc.)
- Provide practical examples relevant to water engineering

## Type Hints
- Use type hints where they improve clarity
- Not required for simple scripts in tutorials

## Naming Conventions
- Variables: `snake_case` (e.g., `discharge_m3s`, `catchment_area_km2`)
- Functions: `snake_case` (e.g., `calculate_flow_velocity()`)
- Classes: `PascalCase` (e.g., `HydraulicModel`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `GRAVITY_MS2 = 9.81`)

## Tutorial Notebook Style
- Clear title and description at top
- Time estimate for completion
- Prerequisites listed
- Learning objectives stated
- Checkpoints throughout
- Troubleshooting section
- Next steps/links at end

## Content Tone
- Beginner-friendly
- Encouraging, not condescending
- Practical over theoretical
- Use "you" language (direct address)
- Short sentences
- No jargon without explanation

## Notebooks
- Commit notebooks WITH outputs (for educational value)
- Code cells should be runnable as-is
- Include water modelling context in every module
