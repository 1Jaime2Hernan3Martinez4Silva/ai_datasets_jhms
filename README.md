# 10 AI Data Science Datasets

Welcome to the Business Science University practice workspace. This project bundles ten curated datasets and accompanying analyses to help you develop portfolio-ready data science projects in both R and Python. Each dataset folder includes a ready-to-run `analysis.py` script that you can execute cell-by-cell (Shift+Enter in VS Code’s Python Interactive window) or as a standard Python script.

## Why These Datasets Matter

- **Diverse domains:** finance, geospatial, marketing, customer analytics, energy, and more.
- **Real-world formats:** CSV, Parquet, and GeoJSON assets mirror production data scenarios.
- **Hands-on practice:** Each dataset comes with a guided analysis that you can extend into personal portfolio work, blog posts, or demos.

## Quick Start

1. **Clone or download** this repository.
2. **Open the workspace** in VS Code (recommended) or your preferred editor.
3. **Create a Conda environment (once):**
   ```bash
   conda create -n ai-datasets python=3.12 -y
   conda activate ai-datasets
   ```
4. **Install dependencies:**
   ```bash
   pip install pandas pytimetk plotly plotnine geopandas folium rdata shapely
   ```
   > _Tip:_ If you prefer `conda`, many of these packages are also available via `conda-forge`.
5. **Start exploring:**
   - Run the top-level orchestrator to refresh all outputs:
     ```bash
     python dataset_overview.py
     ```
   - Or open an individual `analysis.py` (e.g., `dataset_01_stock_returns/analysis.py`) and step through it with Shift+Enter in VS Code’s Python Interactive window.

## Working in the Conda Environment

- To activate the environment in future sessions:
  ```bash
  conda activate ai-datasets
  ```
- If you add new packages during your explorations, capture them in a `requirements.txt` or `environment.yml` so classmates can reproduce your work.

## Building Portfolio Projects

Each dataset folder contains:

- Raw data files (CSV/Parquet/GeoJSON, etc.).
- An `analysis_outputs/` directory populated when you run the accompanying script.
- A curated `analysis.py` script with clearly labeled sections:
  - **Analysis Description** – the business question addressed.
  - **Libraries and Setup** – imports and directory configuration.
  - **Step-by-Step Analysis** – modular, executable blocks ready for modification.
  - **Conclusions** – prompts to document findings and next steps.

Use the provided scripts as a starting point:

1. Duplicate an analysis file to a new notebook or script (`your_name_project.ipynb`).
2. Extend the analysis with your own models, visualizations, and narratives.
3. Export charts, dashboards, or written summaries into the `analysis_outputs/` subfolders.
4. Document your work in a blog post, portfolio site, or README extension to showcase your process and results.

## Getting Started Fast

- **Need inspiration?** Start with `dataset_01_stock_returns` or `dataset_09_iphone_sales` for quick wins; they feature tidy tabular data and ready-to-use visualizations.
- **Want to dive into spatial analytics?** Head to `dataset_03_geospatial` and explore the Folium map generation—swap in your own basemaps or clustering techniques.
- **Interested in text analytics?** `dataset_05_twitter` and `dataset_08_customer_survey` contain rich textual fields ripe for NLP, topic modeling, or sentiment classification.

## Need Help?

- Review the comments embedded in each `analysis.py` for step-wise guidance.
- Visit the Business Science University Learning Labs for deeper dives into similar projects.
- Reach out to classmates or mentors, sharing your updated scripts and outputs for feedback.

Happy analyzing, and remember to turn your findings into compelling portfolio stories!
