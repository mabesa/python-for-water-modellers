# Binder Support Implementation Plan

**Date Created**: 7 December 2024  
**Status**: Not Started  
**Priority**: High (blocks interactive functionality)

## Problem Statement

Jupyter Book's Binder integration allows readers to launch interactive notebooks directly from the documentation. However, relative file paths (`../data/`) that work locally fail in Binder with:

```
FileNotFoundError: [Errno 2] No such file or directory: '../data'
```

**Failing Code Example**:
```python
# Quick check: list files in the data folder
import os

data_files = [f for f in os.listdir('../data') if f.endswith('.csv')]
print("CSV files in data/ folder:")
for f in data_files:
    print(f"  {f}")
```

## Investigation Tasks

### Task 1: Understand Binder's Working Directory
- **Action**: Research how Binder sets up the working directory when launching from Jupyter Book
- **Questions to Answer**:
  - Where does Binder place the user when launching a notebook from a specific chapter?
  - Does Binder clone the entire repo or just specific folders?
  - What is the current working directory (`os.getcwd()`) in a Binder session?
- **Test Approach**: Add a diagnostic cell to print `os.getcwd()` and `os.listdir('.')` in Module 4a
- **Estimated Time**: 30 minutes

### Task 2: Determine File Path Strategy
- **Action**: Decide on the correct path approach for Binder compatibility
- **Options to Evaluate**:
  
  **Option A: Use repo-root relative paths**
  ```python
  # Assumes notebooks know the repo structure
  data_files = os.listdir('data/')  # If cwd is repo root
  ```
  
  **Option B: Use absolute paths from repo root**
  ```python
  import pathlib
  repo_root = pathlib.Path(__file__).parent.parent  # Won't work in notebook
  data_path = repo_root / 'data'
  ```
  
  **Option C: Smart path resolution**
  ```python
  from pathlib import Path
  
  # Try multiple locations
  if Path('../data').exists():
      data_path = Path('../data')  # Local execution
  elif Path('data').exists():
      data_path = Path('data')      # Binder at repo root
  elif Path('../../data').exists():
      data_path = Path('../../data')  # Alternative structure
  else:
      raise FileNotFoundError("Cannot locate data folder")
  ```
  
  **Option D: Environment-based detection**
  ```python
  import os
  from pathlib import Path
  
  # Detect if running in Binder
  if 'BINDER_REQUEST' in os.environ or 'BINDER_LAUNCH_HOST' in os.environ:
      data_path = Path('data')  # Binder path
  else:
      data_path = Path('../data')  # Local path
  ```

- **Recommendation Criteria**:
  - Works both locally (VS Code) and in Binder
  - Clear for students to understand
  - Minimal complexity
  - Good pedagogical value (teaches path handling)
- **Estimated Time**: 45 minutes

### Task 3: Data File Strategy
- **Action**: Decide whether to commit data files or download them dynamically
- **Options**:

  **Option A: Commit data files to repo**
  - **Pros**: 
    - Guaranteed availability in Binder
    - Works offline
    - No API dependencies
    - Faster for students
  - **Cons**: 
    - Repo size increases
    - Data versioning complexity
    - Not realistic workflow for real projects
  - **File to commit**: `data/camels_01013500_discharge.csv` (~50KB based on CAMELS typical size)

  **Option B: Download in notebooks**
  - **Pros**: 
    - Teaches real data acquisition workflow
    - Keeps repo lean
    - Always gets latest data
  - **Cons**: 
    - Requires internet in Binder (should be fine)
    - API rate limits or outages could break tutorials
    - Slower startup time
  - **Implementation**: Module 4a already downloads data; Module 4b checks if exists before loading

  **Option C: Hybrid approach**
  - **Pros**: 
    - Best of both worlds
    - Fallback mechanism
  - **Cons**: 
    - More complex logic
  - **Implementation**:
    ```python
    from pathlib import Path
    
    csv_file = data_path / 'camels_01013500_discharge.csv'
    
    if not csv_file.exists():
        print("Data not found locally. Downloading from CAMELS...")
        # Run pygeohydro download code
    else:
        print("Using local data file")
    ```

- **Recommendation**: Option C (Hybrid) - commit the file but keep download code
- **Files to track**: Add `data/camels_01013500_discharge.csv` to git
- **Estimated Time**: 30 minutes

### Task 4: Update .gitignore
- **Action**: Modify `.gitignore` to allow tracking specific data files
- **Current State**: Check if `data/` is currently ignored
- **Change Required**:
  ```gitignore
  # Track specific tutorial data files
  !data/camels_01013500_discharge.csv
  
  # But ignore user-generated data
  data/*_user.csv
  data/temp_*
  ```
- **Estimated Time**: 10 minutes

## Documentation Tasks

### Task 5: Document Binder Support in README
- **Action**: Add section explaining interactive Binder functionality
- **Content to Include**:
  - What is Binder and why it's useful
  - How to launch notebooks interactively from the tutorial site
  - Note about persistence (changes don't save)
  - Expected behavior and limitations
- **Location**: `README.md` - new section after "Tutorial Structure"
- **Draft Content**:
  ```markdown
  ## Interactive Learning with Binder

  All tutorial notebooks can be run interactively in your browser using Binder, 
  without installing anything locally. Click the rocket icon (🚀) at the top of 
  any tutorial page and select "Binder" to launch an interactive session.

  **Note**: 
  - Binder sessions are temporary - your changes won't be saved
  - First launch may take 2-3 minutes while environment builds
  - Ideal for testing concepts before local setup
  - For serious work, we recommend local installation (Modules 1-2)

  **Limitations**:
  - No persistence between sessions
  - Limited computational resources
  - Requires internet connection
  ```
- **Estimated Time**: 20 minutes

### Task 6: Add Binder Badge/Link to README
- **Action**: Add standard Binder badge for quick access
- **Implementation**:
  ```markdown
  [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mabesa/python-for-water-modellers/main)
  ```
- **Location**: Top of README near other badges
- **Estimated Time**: 5 minutes

### Task 7: Test Binder Configuration
- **Action**: Verify Binder can build and run the environment
- **Steps**:
  1. Commit changes and push to GitHub
  2. Launch Binder from the badge link
  3. Wait for environment build
  4. Test running Module 4a and 4b notebooks
  5. Verify path resolution works
  6. Verify data loading works
- **Expected Issues**: May need to create `environment.yml` or `requirements.txt` for Binder
- **Estimated Time**: 30 minutes + build time

### Task 8: Update Implementation Plan
- **Action**: Document Binder support completion
- **File**: `planning/implementation_plan.md`
- **Updates**:
  - Add Binder support to Module 4 completion criteria
  - Note file path strategy chosen
  - Document testing results
- **Estimated Time**: 15 minutes

## Code Changes Required

### Files to Modify:
1. `tutorials/04a_getting_data.ipynb`:
   - Update file path handling (Task 2 decision)
   - Add diagnostic cell showing `os.getcwd()` for learning
   - Keep download code but make it check for existing file first

2. `tutorials/04b_discharge_analysis.ipynb`:
   - Update file path to match 04a strategy
   - Add error handling if data not found

3. `.gitignore`:
   - Allow tracking `data/camels_01013500_discharge.csv`

4. `README.md`:
   - Add Binder badge
   - Add Interactive Learning section

5. `planning/implementation_plan.md`:
   - Document Binder support completion

6. **Potentially**: Create `environment.yml` or `binder/environment.yml` if Binder needs explicit dependencies

## Success Criteria

- [ ] Binder launches successfully from Jupyter Book
- [ ] File paths work in both local VS Code and Binder
- [ ] Data loads correctly in Module 4b in Binder
- [ ] README clearly explains Binder functionality
- [ ] Students understand path handling concepts
- [ ] No FileNotFoundError in Binder sessions

## Timeline Estimate

**Total Time**: ~3 hours
- Investigation & Testing: 1.5 hours
- Code Changes: 45 minutes
- Documentation: 45 minutes

## Open Questions

1. Does Jupyter Book automatically configure Binder, or do we need manual setup?
2. Should we add Binder button to individual chapter pages via MyST config?
3. Do we want to limit which notebooks are Binder-enabled? (Maybe skip installation modules 1a-2b)
4. Should we add a Module 0b: "Quick Start with Binder" for users who want to try before installing?

## References to Check

- Jupyter Book Binder docs: https://jupyterbook.org/en/stable/interactive/launchbuttons.html
- Binder docs: https://mybinder.readthedocs.io/
- File path handling in notebooks: Python `pathlib` docs
- CAMELS dataset license: Verify redistribution is allowed

---

**Next Steps for Tomorrow**:
1. Start with Task 1 (diagnostic) - add `print(os.getcwd())` to Module 4a and test in Binder
2. Based on findings, choose path strategy (Task 2)
3. Implement chosen strategy across notebooks
4. Commit data file if going hybrid/committed approach
5. Update documentation
6. Test end-to-end in Binder
