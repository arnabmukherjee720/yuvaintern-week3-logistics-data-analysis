# Week 3 — Advanced Data Analysis and Visualization in Logistics

## Project overview
This project demonstrates exploratory data analysis (EDA) and visualization on a simulated logistics dataset using Python, Pandas, NumPy, and Matplotlib.

## Files
- `week3_eda_visualization.py` — script to calculate descriptive statistics, regional summaries, correlations, and generate charts.
- `week3_logistics_eda_simulated.csv` — simulated data for 180 logistics orders.
- `requirements.txt` — required Python libraries.
- `chart_delivery_time_distribution.png` — delivery-time histogram.
- `chart_distance_vs_cost.png` — distance versus shipping-cost scatter plot.
- `chart_region_delivery.png` — average delivery duration by region.
- `chart_correlation_matrix.png` — correlation matrix for numeric variables.

## How to run
Keep all files in the same folder. Install dependencies:
```bash
pip install -r requirements.txt
```
Run:
```bash
python week3_eda_visualization.py
```
The script prints summary statistics, delivery status percentages, regional summaries, and correlations. It also generates chart images in the same folder.

## Main analysis
The report explores delivery duration, shipping cost, distance, weight, shipment volume, delivery status, and region. It includes descriptive statistics, regional comparisons, and correlation analysis.

## Data note
The dataset is synthetic and intended only for educational demonstration. It does not contain real company or customer records.
