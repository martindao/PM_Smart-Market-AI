# Smart Market AI

## Overview
Smart Market AI ingests influencer, campaign, and social-performance datasets, enriches them with NLP/embedding pipelines, and outputs clustering + visualization artifacts for GTM teams. The repo captures the full workflow—from scraping raw data to publishing dashboards and documentation.

## Repository Layout
- Data Fetching/ – scripts and configs for downloading influencer + competitor feeds.
- Processing Data/ – cleaning utilities, feature builders, and similarity calculations.
- Analysis Module/ – notebooks, clustering experiments, and result CSVs.
- Visualization/ – Plotly/Matplotlib exports and storytelling assets.
- Demonstration/ – walkthrough notebooks + presentation-ready summaries.

## Environment Setup
1. Create/activate an environment and install dependencies:
   `powershell
   conda create -n smart-market python=3.10 pandas numpy scikit-learn plotly
   conda activate smart-market
   pip install sentence-transformers seaborn openpyxl
   `
2. Place API tokens or brand credentials inside .env (if a connector requires it).

## Running Workflows
- Fetch the latest datasets via the scripts in Data Fetching/ (most are Jupyter/py files with documented parameters).
- Execute preprocessing notebooks in Processing Data/ to regenerate the cleaned CSVs consumed by clustering modules.
- Run the analysis notebooks inside Analysis Module/Clustering*/ to produce updated similarity matrices and export them to Analysis Module/Data/.
- Refresh dashboards by re-running the notebooks or using the assets under Visualization/.

## Quality & Automation
- Track large CSVs with Git LFS if they exceed GitHub’s 100 MB limit.
- When updating notebooks, strip outputs (jupyter nbconvert --clear-output) before committing to keep diffs readable.
- Follow the OpenSpec schedule for future commits—late-window work (2021–2022) should focus on transformer upgrades, influencer segmentation, and visualization publishing.
