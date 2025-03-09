# Customer-Retention-Analysis

# Customer Retention Analysis

## Overview

This project focuses on analyzing customer retention using various data analysis techniques to gain insights into customer behavior and improve retention strategies.

## Repository Structure

- **data/**: Contains datasets used for analysis.
- **models/**: Stores trained machine learning models.
- **notebooks/**: Jupyter notebooks detailing data analysis and modeling processes.
- **scripts/**: Python scripts for data processing and analysis.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Jupyter Notebook
- Required Python packages listed in `requirements.txt`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NAV2399/Customer-Retention-Analysis.git
   cd Customer-Retention-Analysis

Analysis Details

Cohort Analysis

Groups customers by first purchase month and tracks retention over time.

Uses a heatmap to visualize retention trends.

Churn Prediction Model

Defines churn as customers who haven’t purchased in the last 90 days.

Uses RandomForestClassifier to predict churn probability.

Features include recency, frequency, and monetary values.

Outputs churn probability for each customer.

Customer Segments Distribution Analysis

The project also includes customer segmentation based on purchasing behavior. The distribution is visualized using a pie chart, highlighting the following key segments:

Loyal Customers (35.5%)

The largest segment, indicating a strong customer base that makes frequent and repeated purchases.

Retaining and rewarding this group (e.g., loyalty programs, exclusive offers) is essential.

Potential Loyalists (12.3%)

Customers who have made some repeat purchases but need further engagement to turn into loyal customers.

Strategies like personalized offers and follow-up emails can help increase retention.

Other Smaller Segments (Each ~3-5%)

These represent various customer behaviors, potentially categorized using RFM (Recency, Frequency, Monetary) analysis.

Further segmentation could include:

High-value customers (big spenders)

Frequent but low-spend customers

Churn-prone customers (who might stop purchasing soon)

Actionable Recommendations

For Loyal Customers: Maintain engagement with special rewards and premium offers.

For Potential Loyalists: Encourage repeat purchases through personalized discounts.

For Smaller Segments: Identify which groups are at risk of churn and implement re-engagement campaigns.

Results

Churn probability predictions are saved in rfm_churn_with_probabilities.csv.

Final trained model is stored in models/rfm_churn_model.pkl.
