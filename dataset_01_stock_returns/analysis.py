# BUSINESS SCIENCE UNIVERSITY
# AI Data Set 1: Stock Return Analysis
# ****

# Analysis Description
# Compare monthly growth for four tech stocks versus the XLK benchmark.
# Save the combined growth series, interactive plot, and min/max summary.

# How you can use AI Agents with this data analysis:
# 1. Report Generation: Use AI agents to generate comprehensive reports based on the analysis, highlighting key insights and trends.
# 2. Automated Alerts: Set up AI agents to monitor stock performance and send alerts when significant changes occur.
# 3. Predictive Analysis: Leverage AI agents to predict future stock performance based on historical data and trends.

# LIBRARIES
from pathlib import Path
import pandas as pd
import pytimetk as tk

# DIRECTORIES
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "analysis_outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# STEP 1: Load monthly stock return data
tech = pd.read_csv(BASE_DIR / "tech_stocks_monthly.csv", parse_dates=["date"])

benchmark = pd.read_csv(BASE_DIR / "benchmark_xlk_monthly.csv", parse_dates=["date"])

# STEP 2: Calculate cumulative monthly growth
combined = pd.concat([tech, benchmark], ignore_index=True)
combined["monthly_growth"] = (
    (1 + combined["monthly.returns"]).groupby(combined["symbol"]).cumprod()
)

combined

# STEP 3: Persist enriched table for downstream work
combined.to_parquet(
    OUTPUT_DIR / "tech_and_benchmark_monthly_growth.parquet", index=False
)

pd.read_parquet(
    OUTPUT_DIR / "tech_and_benchmark_monthly_growth.parquet"
)

# STEP 4: Visualize growth trajectories
growth_fig = combined.groupby("symbol").plot_timeseries(
    date_column="date",
    value_column="monthly_growth",
    facet_ncol=2,
    facet_nrow=2,
    smooth=False,
    engine="plotly",
    title="Monthly Growth | Tech Stocks vs XLK Benchmark",
)
growth_fig

growth_fig.write_html(OUTPUT_DIR / "tech_vs_benchmark_growth.html")

# STEP 5: Summarize growth extremes by symbol
summary = combined.groupby("symbol")["monthly_growth"].agg(["min", "max"]).round(2)

summary.to_csv(OUTPUT_DIR / "growth_extrema.csv")



