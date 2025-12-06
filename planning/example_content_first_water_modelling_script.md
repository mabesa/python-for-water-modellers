# Your First Water Modelling Script
## Analyzing Real Discharge Data with Python

---

## What We'll Build

A complete workflow using real Swiss hydrological data from the CAMELS-CH dataset:
1. Load discharge data from a Swiss gauging station
2. Calculate hydrological flow statistics
3. Create professional hydrographs
4. Analyze seasonal patterns and extreme events
5. Generate monthly summaries

**Data source:** [CAMELS-CH](https://www.camels.ch/) - Catchment Attributes and Meteorology for Large-sample Studies - Switzerland (open data)

**Time required:** 30-40 minutes

---

## Prepare Your Project

Make sure you have a project set up (see VS Code + uv guide).

In your project folder, add the required packages:
```bash
uv add pandas numpy matplotlib
```

---

## Step 1: Get the Data

We'll use discharge data from a Swiss river station. The CAMELS-CH dataset provides quality-controlled daily discharge data.

### Download Sample Data

For this tutorial, we'll provide a pre-processed CSV file from CAMELS-CH station 2486 (Aare at Untersiggenthal):

**Option 1: Download directly**
- Create a file named `aare_untersiggenthal.csv` in your project folder
- Download from: [link to be provided]

**Option 2: Use this Python script to create sample data** (if download not available):

Create `download_sample_data.py`:
```python
"""
Download sample discharge data from CAMELS-CH.
Station: Aare at Untersiggenthal (ID: 2486)
"""
import pandas as pd
import numpy as np

# For this tutorial, we'll create a representative subset
# In practice, you would download from the CAMELS-CH database

print("Creating sample discharge data...")

# Create 2 years of daily data (2022-2023)
dates = pd.date_range('2022-01-01', '2023-12-31', freq='D')

# Aare River: Large river with snowmelt regime + hydropower regulation
# Typical range: 150-600 m³/s, peak in May-June, low in winter
day_of_year = np.arange(len(dates)) % 365

# Seasonal pattern: snowmelt peak in late spring
seasonal = 280 + 200 * np.sin((day_of_year - 80) * 2 * np.pi / 365)

# Add weekly regulation pattern (hydropower)
day_of_week = np.array([d.weekday() for d in dates])
weekly_pattern = np.where(day_of_week < 5, 20, -15)  # Higher on weekdays

# Add weather variability
np.random.seed(42)
weather_noise = np.random.normal(0, 30, len(dates))

# Occasional flood events
floods = np.zeros(len(dates))
flood_events = np.random.choice(len(dates), size=8, replace=False)
floods[flood_events] = np.random.uniform(100, 250, 8)

# Combine (ensure positive)
discharge = np.maximum(seasonal + weekly_pattern + weather_noise + floods, 100)

# Add some missing data (realistic for real datasets)
missing_indices = np.random.choice(len(dates), size=5, replace=False)
discharge[missing_indices] = np.nan

df = pd.DataFrame({
    'date': dates,
    'discharge_m3s': np.round(discharge, 2),
    'station_id': 2486,
    'station_name': 'Aare - Untersiggenthal'
})

df.to_csv('aare_untersiggenthal.csv', index=False)

print(f"✅ Created aare_untersiggenthal.csv")
print(f"   Records: {len(df)} days")
print(f"   Period: {df['date'].min()} to {df['date'].max()}")
print(f"   Discharge range: {df['discharge_m3s'].min():.1f} - {df['discharge_m3s'].max():.1f} m³/s")
print(f"   Missing values: {df['discharge_m3s'].isna().sum()} days")
```

Run it:
```bash
uv run download_sample_data.py
```

---

## Step 2: The Main Analysis Script

Create a file called `analyze_discharge.py`:

```python
"""
Discharge Data Analysis - Swiss CAMELS-CH Dataset
==================================================
Analyze real hydrological time series from Swiss gauging stations.

Data source: CAMELS-CH (https://www.camels.ch/)
Station: Aare at Untersiggenthal (ID: 2486)

Author: [Your Name]
Date: [Today's Date]
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# =============================================================================
# CONFIGURATION
# =============================================================================

INPUT_FILE = 'aare_untersiggenthal.csv'
DATE_COLUMN = 'date'
DISCHARGE_COLUMN = 'discharge_m3s'
STATION_NAME = 'Aare - Untersiggenthal'

# =============================================================================
# LOAD AND PREPARE DATA
# =============================================================================

print("Loading data...")

# Read the CSV file
df = pd.read_csv(INPUT_FILE)

# Convert date column to datetime format
df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN])

# Set date as index (makes time series operations easier)
df.set_index(DATE_COLUMN, inplace=True)

# Quick data quality check
print(f"✅ Loaded {len(df)} records")
print(f"   Period: {df.index.min().strftime('%Y-%m-%d')} to {df.index.max().strftime('%Y-%m-%d')}")

# Check for missing data
missing_count = df[DISCHARGE_COLUMN].isna().sum()
if missing_count > 0:
    print(f"⚠️  Missing data: {missing_count} days ({missing_count/len(df)*100:.1f}%)")
    print(f"   Handling: Will exclude from calculations")

# =============================================================================
# CALCULATE STATISTICS
# =============================================================================

print("\nCalculating statistics...")

# Get discharge series (excluding NaN values)
Q = df[DISCHARGE_COLUMN].dropna()

stats = {
    'Mean Q (m³/s)': Q.mean(),
    'Median Q (m³/s)': Q.median(),
    'Std Dev (m³/s)': Q.std(),
    'Min Q (m³/s)': Q.min(),
    'Max Q (m³/s)': Q.max(),
    'Q10 - Low flow (m³/s)': Q.quantile(0.10),
    'Q50 - Median flow (m³/s)': Q.quantile(0.50),
    'Q90 - High flow (m³/s)': Q.quantile(0.90),
}

print("\n📊 FLOW STATISTICS")
print("-" * 35)
for name, value in stats.items():
    print(f"   {name:25} {value:8.2f}")

# =============================================================================
# IDENTIFY EXTREME EVENTS
# =============================================================================

# Find high flow days (above 90th percentile)
threshold_high = Q.quantile(0.90)
high_flow_days = df[Q > threshold_high]

# Find low flow days (below 10th percentile)  
threshold_low = Q.quantile(0.10)
low_flow_days = df[Q < threshold_low]

print(f"\n⚠️  HIGH FLOW EVENTS (Q > {threshold_high:.1f} m³/s)")
print(f"   {len(high_flow_days)} days identified")
if len(high_flow_days) > 0:
    max_day = Q.idxmax()
    print(f"   Maximum: {Q.max():.1f} m³/s on {max_day.strftime('%Y-%m-%d')}")

print(f"\n🔻 LOW FLOW PERIODS (Q < {threshold_low:.1f} m³/s)")
print(f"   {len(low_flow_days)} days identified")
if len(low_flow_days) > 0:
    min_day = Q.idxmin()
    print(f"   Minimum: {Q.min():.1f} m³/s on {min_day.strftime('%Y-%m-%d')}")

# =============================================================================
# MONTHLY SUMMARY
# =============================================================================

# Calculate monthly statistics
monthly = df.resample('ME').agg({
    DISCHARGE_COLUMN: ['mean', 'min', 'max', 'std']
})
monthly.columns = ['Mean', 'Min', 'Max', 'Std']
monthly.index = monthly.index.strftime('%Y-%m')

print("\n📅 MONTHLY SUMMARY (m³/s)")
print("-" * 50)
print(monthly.round(2).to_string())

# =============================================================================
# CREATE VISUALIZATIONS
# =============================================================================

print("\nCreating plots...")

# Figure with 2 subplots
fig, axes = plt.subplots(2, 1, figsize=(12, 8))

# --- Plot 1: Full Hydrograph ---
ax1 = axes[0]
ax1.plot(df.index, Q, 'b-', linewidth=0.8, label='Daily discharge')
ax1.axhline(y=stats['Mean Q (m³/s)'], color='r', linestyle='--', 
            label=f"Mean ({stats['Mean Q (m³/s)']:.1f} m³/s)")
ax1.fill_between(df.index, 0, Q, alpha=0.3)

# Mark extreme events
ax1.scatter(high_flow_days.index, high_flow_days[DISCHARGE_COLUMN], 
            c='red', s=20, zorder=5, label='High flow events')

ax1.set_ylabel('Discharge (m³/s)')
ax1.set_title(f'{STATION_NAME} - Daily Discharge Hydrograph')
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)

# --- Plot 2: Monthly Box Plot ---
ax2 = axes[1]
df_monthly = df.copy()
df_monthly['month'] = df_monthly.index.month

# Create box plot
box_data = [df_monthly[df_monthly['month'] == m][DISCHARGE_COLUMN].values 
            for m in range(1, 13)]
bp = ax2.boxplot(box_data, labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax2.set_ylabel('Discharge (m³/s)')
ax2.set_xlabel('Month')
ax2.set_title('Monthly Discharge Distribution')
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout()

# Save figure
output_file = 'discharge_analysis.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"✅ Saved plot as '{output_file}'")

# Show plot (comment out if running in headless environment)
plt.show()

print("\n🎉 Analysis complete!")
```

Run it:
```bash
uv run analyze_discharge.py
```

---

## Understanding the Code

### Key Python Concepts Used

| Code | What it does |
|------|--------------||
| `pd.read_csv()` | Loads CSV file into a DataFrame (like an Excel sheet) |
| `pd.to_datetime()` | Converts text to proper date format |
| `.mean()`, `.max()` | Calculate statistics on a column |
| `.quantile(0.90)` | Find the 90th percentile value |
| `.resample('ME')` | Group data by month end |
| `plt.subplots()` | Create a figure with multiple plots |
| `plt.savefig()` | Save plot as image file |

### 💡 Why These Design Choices?

**Why pandas instead of Excel?**
- Reproducible: Run the script again, get same results
- Scalable: Works with 100 rows or 100,000 rows
- Automated: Process multiple stations with one script
- Version controlled: Track changes over time

**Why set date as index?**
```python
df.set_index(DATE_COLUMN, inplace=True)
```
This makes time-based operations much easier:
- Automatic date formatting on plots
- Easy resampling (daily → monthly)
- Simple date range filtering: `df['2022-06':'2022-08']`

**Why dropna()?**
```python
Q = df[DISCHARGE_COLUMN].dropna()
```
Real-world data has gaps (sensor failures, maintenance). Dropping NaN values prevents:
- Statistics calculations failing
- Misleading results from treating gaps as zeros

**Why separate configuration section?**
```python
INPUT_FILE = 'aare_untersiggenthal.csv'
DISCHARGE_COLUMN = 'discharge_m3s'
```
Changing settings in one place makes it easy to:
- Use the script for different stations
- Adapt to different CSV formats
- Share code with colleagues who have different data structures

### How to Modify for Your Own Data

1. **Change input file:**
   ```python
   INPUT_FILE = 'your_station_data.csv'
   STATION_NAME = 'Rhine at Basel'
   ```

2. **Different column names:**
   ```python
   DATE_COLUMN = 'Datum'  # German format
   DISCHARGE_COLUMN = 'Abfluss_m3s'
   ```

3. **Different thresholds:**
   ```python
   threshold_high = Q.quantile(0.95)  # 95th percentile instead
   threshold_low = Q.quantile(0.05)   # 5th percentile
   ```

4. **Filter date range:**
   ```python
   # After loading data:
   df = df.loc['2020-01-01':'2023-12-31']  # Only analyze 2020-2023
   ```

---

## Working with Real Swiss Data

### About CAMELS-CH
The CAMELS-CH dataset provides:
- **Daily discharge data** from 331 Swiss catchments
- **Quality-controlled** measurements from Federal Office for the Environment (FOEN)
- **Catchment attributes**: Area, elevation, land use, geology, climate
- **Open access**: Free for research and educational use

### Accessing More CAMELS-CH Data

1. **Visit:** [https://www.camels.ch/](https://www.camels.ch/)
2. **Download:** Full dataset or individual stations
3. **Format:** CSV files with standardized columns
4. **Documentation:** Metadata explains station characteristics

### Common Data Issues in Real-World Hydrology

| Issue | How to Handle |
|-------|---------------|
| **Missing values** | Use `.dropna()` or interpolate with `.interpolate()` |
| **Ice-affected periods** | Flag winter low flows in Alpine stations |
| **Rating curve changes** | Check for discontinuities in long records |
| **Regulation effects** | Weekday/weekend patterns indicate hydropower |
| **Outliers** | Verify extreme values (floods vs. errors) |

### Example: Handling Missing Data

```python
# Count missing data
missing_pct = df[DISCHARGE_COLUMN].isna().sum() / len(df) * 100

if missing_pct < 5:
    # Few gaps: drop them
    Q = df[DISCHARGE_COLUMN].dropna()
elif missing_pct < 20:
    # Some gaps: interpolate
    Q = df[DISCHARGE_COLUMN].interpolate(method='time')
else:
    # Many gaps: investigate data quality!
    print(f"⚠️ Warning: {missing_pct:.1f}% missing data")
    print("Consider using a different station or time period")
```

---

## Next Steps

### Extend This Script
Ask Claude:
```
I have this discharge analysis script. Can you add:
1. A flow duration curve
2. Annual maximum series extraction
3. Export results to Excel
```

### Work with Your Own Data
- Export data from your database or measurement system as CSV
- Update the column names in the script
- Run the analysis

### Add More Analyses
Common hydrological analyses to request from AI:
- Rating curve fitting
- Baseflow separation
- Recession analysis
- Return period estimation
- Trend analysis (Mann-Kendall test)

---

## Troubleshooting

### "FileNotFoundError: discharge_data.csv"
→ Make sure you ran `create_sample_data.py` first
→ Check you're in the correct folder

### Plot doesn't appear
→ On some systems, `plt.show()` doesn't work in terminal
→ The PNG file is still saved — open it manually

### Dates look wrong
→ Check your CSV date format matches what `pd.to_datetime()` expects
→ You can specify format: `pd.to_datetime(df['date'], format='%d.%m.%Y')`