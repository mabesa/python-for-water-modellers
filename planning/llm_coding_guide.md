# Coding with AI Assistance: A Practical Guide
## For Water Modellers Learning Python

---

## Why Use AI for Coding?

As a water modeller, you're an expert in hydrology or groundwater systems — not necessarily in Python syntax. AI assistants can bridge that gap:

- ✅ **Describe what you need in plain language** → Get working code
- ✅ **Fix errors** without spending hours searching forums
- ✅ **Learn as you go** by asking "why does this work?"
- ✅ **Focus on the science**, not memorizing syntax

> ⚠️ **Critical Limitation:** AI is a coding assistant, not a hydrological expert!
> - ✅ AI can write correct Python syntax
> - ✅ AI can implement equations you specify  
> - ❌ AI **cannot** tell if you're using the wrong equation for your flow regime
> - ❌ AI **cannot** validate your conceptual model
> - ❌ AI **cannot** verify if results are physically plausible
>
> **You must verify:**
> - Are these the right equations for my system?
> - Do the results make physical sense?
> - Are my boundary conditions appropriate?

---

## Getting Started with Claude or ChatGPT

### Free Options
- **Claude.ai** — Free tier at [claude.ai](https://claude.ai)
- **ChatGPT** — Free tier at [chat.openai.com](https://chat.openai.com)

Both work similarly. We'll use Claude in examples, but the approach applies to any AI assistant.

---

## The Art of Prompting: How to Ask for Code

### ❌ Vague Request (Poor Results)
```
Make me a graph of discharge data
```

### ✅ Specific Request (Good Results)
```
Write Python code that:
1. Reads a CSV file called "discharge.csv" with columns "date" and "Q_m3s"
2. Converts the date column to datetime format
3. Creates a line plot showing discharge over time
4. Adds axis labels with units (Date, Discharge m³/s)
5. Saves the plot as PNG at 300 DPI
```

### Key Elements of Good Prompts

| Element | Example |
|---------|---------|
| **Context** | "I'm analyzing daily river discharge data..." |
| **Input format** | "...from a CSV with columns 'date' and 'value'" |
| **Desired output** | "I need a hydrograph plot saved as PNG" |
| **Constraints** | "Use matplotlib, not plotly" |
| **Specifics** | "Show discharge in m³/s, dates on x-axis" |

---

## Practical Example 1: Loading Hydrological Data

### Your prompt:
```
I'm a hydrologist new to Python. I have a CSV file called "station_data.csv" 
with these columns:
- timestamp (format: 2024-01-15 12:00)
- water_level_m
- discharge_m3s

Write Python code to:
1. Load this CSV using pandas
2. Convert timestamp to proper datetime
3. Set timestamp as the index
4. Print the first 5 rows and basic statistics

Include comments explaining each step for a beginner.
```

### What Claude might return:
```python
import pandas as pd

# Load the CSV file into a pandas DataFrame
# A DataFrame is like an Excel spreadsheet in Python
df = pd.read_csv('station_data.csv')

# Convert the 'timestamp' column from text to actual dates
# This allows us to do time-based operations later
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Set timestamp as the index (row labels)
# This makes time-series operations much easier
df.set_index('timestamp', inplace=True)

# Display the first 5 rows to verify data loaded correctly
print("First 5 rows of data:")
print(df.head())
print()

# Show basic statistics (mean, min, max, std, etc.)
print("Basic statistics:")
print(df.describe())
```

---

## Practical Example 2: Asking for Bug Fixes

When your code doesn't work, copy the error message to Claude:

### Your prompt:
```
I'm running this Python code:

df = pd.read_csv('my_data.csv')
df['date'] = pd.to_datetime(df['date'])

But I get this error:

KeyError: 'date'

What's wrong and how do I fix it?
```

### Claude will explain:
- The column 'date' doesn't exist in your CSV
- How to check what columns actually exist (`print(df.columns)`)
- Common causes (typo, different capitalization, extra spaces)

---

## Practical Example 3: Creating a FloPy Model

### Your prompt:
```
I want to create a simple MODFLOW 6 groundwater model using FloPy.
The model should be:
- 10 rows x 10 columns
- Single layer, 10m thick
- Constant head of 100m on the left boundary
- Constant head of 90m on the right boundary
- Hydraulic conductivity of 10 m/day
- Steady-state flow

Please write the complete Python code with comments explaining 
what each section does. I'm new to both FloPy and MODFLOW.
```

---

## When AI Gets It Wrong: Verification Strategies

AI isn't perfect. Here's how to verify code for water modelling:

### 1. Check Units Consistency
```
Ask: "Are the units in this calculation consistent? 
      I have discharge in m³/s and I'm calculating 
      volume in cubic meters over a day."
```

### 2. Sanity Check Results
```
Ask: "The calculated groundwater velocity is 500 m/day. 
      Does this seem physically reasonable for an alluvial aquifer?"
```

### 3. Ask for Validation
```
Ask: "How can I verify this water balance calculation is correct? 
      What should I check?"
```

### 4. Compare with Known Solutions
For analytical problems, ask Claude to compare with known solutions:
```
Ask: "Can you add code to compare this Theis solution result 
      with the analytical equation?"
```

---

## Prompt Templates for Water Modelling

### Template 1: Data Processing
```
I need to process [hydrological/groundwater] data.

Input: [describe your data file, columns, units]
Output: [what you want to produce]
Tools: Use pandas and [other packages]

Please write Python code with comments explaining each step.
```

### Template 2: Visualization
```
Create a [type of plot] showing [what data].

The data is in [format] with columns [list columns].
The plot should include:
- [axis labels with units]
- [title]
- [legend if needed]
- [save format and resolution]

Use matplotlib.
```

**Example:**
```
Create a hydrograph (line plot) showing daily discharge over time.

The data is a pandas DataFrame with columns 'date' and 'Q_m3s'.
The plot should include:
- X-axis: Date
- Y-axis: Discharge (m³/s)
- Title: "Aare River at Untersiggenthal - 2023"
- Blue line, medium thickness
- Save as PNG at 300 DPI

Use matplotlib.
```
- [title]
- [legend if needed]
- [save format and resolution]

Use matplotlib.
```

### Template 3: FloPy Model
```
I need to build a MODFLOW [version] model for [brief description].

Model specifications:
- Grid: [dimensions]
- Layers: [number and thicknesses]
- Boundary conditions: [describe]
- Hydraulic properties: [K, Ss, Sy values]
- Stress periods: [steady/transient, duration]

Write FloPy code with comments for someone new to groundwater modelling.
```

### Template 4: Debugging
```
This code is supposed to [expected behavior]:

[paste your code]

But instead I get [actual behavior or error message]:

[paste error]

What's wrong and how do I fix it? Explain so I can learn.
```

---

## Tips for Learning While Using AI

### 1. Ask "Why?"
After getting working code:
```
"Why did you use enumerate() here instead of a regular for loop?"
```

### 2. Ask for Alternatives
```
"Show me another way to calculate this, and explain when 
each approach is better."
```

### 3. Ask for Explanations
```
"Explain what this line does as if I'm a hydrologist who 
knows nothing about Python: df.groupby('station').agg({'Q': 'mean'})"
```

### 4. Build Understanding Incrementally
Start simple, then add complexity:
1. First: "How do I read a CSV?"
2. Then: "How do I filter for values above a threshold?"
3. Then: "How do I calculate rolling averages?"

---

## Common Pitfalls to Avoid

| Pitfall | Better Approach |
|---------|----------------|
| Accepting code blindly | Test with known data first |
| Copy-pasting without reading | Read comments, understand flow |
| Asking for huge scripts | Break into smaller pieces |
| Not specifying units | Always mention units in prompts |
| Ignoring warnings | Ask about any warnings you see |
| No version control | Save AI-generated code in Git (track what works) |
| Not documenting AI prompts | Keep a log of successful prompts for future reference |

### 💾 Save Your Work

Even if AI wrote the code, **you** should manage it:
- Use Git to track versions
- Document what the code does (AI can help with this too!)
- Save successful prompts - they're reusable
- Share working solutions with colleagues

**Ask AI:**
```
How do I initialize a Git repository for this Python project?
Include .gitignore for Python.
```

---

## Exercise: Try It Yourself

### Task
Use Claude or ChatGPT to write code that:
1. Generates 1 year of synthetic daily discharge data (Q between 5-50 m³/s)
2. Calculates monthly mean discharge
3. Creates a bar plot of monthly means
4. Identifies and prints the month with highest/lowest flow

### Your prompt (fill in the blanks):
```
I'm a hydrology student learning Python. Please write code that...
[describe the task in your own words]

Use pandas, numpy, and matplotlib.
Include comments explaining each step.
```

Compare what you get with what a classmate gets — you'll likely see different but equally valid solutions!

### Follow-Up Questions to Deepen Learning

After getting working code, ask:

1. **Understanding:**
   ```
   "Why did you use np.random.uniform() instead of np.random.normal() 
   for generating discharge values?"
   ```

2. **Alternatives:**
   ```
   "Show me two other ways to calculate monthly means in pandas.
   When would I use each approach?"
   ```

3. **Extension:**
   ```
   "How would I modify this to handle multiple years of data and 
   create a multi-year comparison plot?"
   ```

4. **Validation:**
   ```
   "How can I verify that my monthly aggregation worked correctly?"
   ```

---

## Real-World Application Example

### Scenario
You have 10 years of discharge data from a Swiss river. You need to:
- Calculate annual maximum discharge (for flood frequency analysis)
- Plot the annual maxima time series
- Fit a Gumbel distribution to estimate the 100-year flood

### Iterative Prompting Strategy

**Step 1: Load and explore**
```
I have a CSV file 'rhine_basel.csv' with columns 'date' (YYYY-MM-DD) 
and 'discharge_m3s'. Write code to:
1. Load the data
2. Show the date range
3. Check for missing values
4. Display summary statistics
```

**Step 2: Extract annual maxima** (after step 1 works)
```
From the loaded DataFrame, extract the maximum discharge for each 
hydrological year (Oct 1 - Sep 30). Create a new DataFrame with 
columns 'year' and 'annual_max_m3s'.
```

**Step 3: Visualize** (after step 2 works)
```
Create a plot showing:
1. Annual maximum discharge as bars
2. Trend line (linear regression)
3. X-axis: Year
4. Y-axis: Annual Max Discharge (m³/s)
5. Save as 'annual_maxima.png'
```

**Step 4: Statistical analysis** (after step 3 works)
```
Using the scipy.stats library, fit a Gumbel distribution to the 
annual maxima. Calculate and print:
1. The 100-year flood estimate (Q100)
2. The 95% confidence interval
3. Show how to plot the fitted distribution against observed data
```

### Key Learning: Build Incrementally

❌ **Don't ask:** "Write complete flood frequency analysis code"

✅ **Do ask:** Work step-by-step, verify each stage works before adding complexity

This approach:
- Makes debugging easier
- Helps you understand each component
- Allows you to spot errors early
- Builds your knowledge progressively

---

## Additional Resources

### Prompt Libraries
Save these proven prompts for quick reuse:

**Data cleaning:**
```
I have hydrological time series data with [describe issues]. 
Write Python code to identify and handle [outliers/gaps/duplicates].
Use pandas and explain the approach.
```

**Unit conversion:**
```
Convert discharge data from [unit] to [unit]. 
The data is in a pandas DataFrame column called '[column_name]'.
Add the converted values as a new column.
```

**Comparison plots:**
```
Create a plot comparing [variable] across [number] different stations.
Data is in [format]. Use a legend to identify each station.
Include grid lines and save at 300 DPI.
```

### Community Tips

From experienced water modellers using AI:

1. **"Always test with a tiny dataset first"** - Easier to spot errors
2. **"Ask AI to add assertions"** - Automatic sanity checks in code  
3. **"Request both comments and docstrings"** - Better documentation
4. **"Get AI to write the README too"** - Explain what your script does
5. **"Ask for error handling"** - Robust code that won't crash on bad data