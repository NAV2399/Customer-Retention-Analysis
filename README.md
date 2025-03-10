# Customer Retention Analysis

## Overview
This project analyzes customer retention patterns using cohort analysis and churn prediction modeling. The goal is to identify trends in customer behavior and predict churn likelihood based on historical purchase data.

## Project Structure
- `1_data_cleaning.ipynb`: Cleans and preprocesses raw customer data for analysis.
- `2_cohort_analysis.ipynb`: Performs cohort analysis to visualize customer retention trends.
- `3_rfm_analysis.ipynb`: Conducts Recency-Frequency-Monetary (RFM) analysis for customer segmentation.
- `4_churn_model.ipynb`: Builds a churn prediction model using machine learning.
- `api/`: Contains API scripts for deploying the model.
- `main.py`: Runs the API and serves predictions.
- `data/processed/`: Contains preprocessed datasets used in the analysis.
- `models/`: Stores trained machine learning models.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/NAV2399/Customer-Retention-Analysis.git
   cd Customer-Retention-Analysis
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure data files (`merged_data.parquet`, `rfm_data.csv`) are present in `data/processed/`.
4. Run the notebooks in sequence for insights and predictions.

## Running the API
1. Navigate to the project root and run the API:
   ```bash
   python main.py
   ```
2. If successful, the message **'API is running'** will be displayed.
3. The API can be accessed via endpoints to get churn predictions or customer insights.

## Analysis Details
### Data Cleaning
- Handles missing values, duplicates, and inconsistent data formats.
- Standardizes customer transaction data for accurate analysis.

### Cohort Analysis
- Groups customers by first purchase month and tracks retention over time.
- Uses a heatmap to visualize retention trends.

### RFM Analysis
- Segments customers based on Recency, Frequency, and Monetary value.
- Helps identify key customer groups such as loyal customers, at-risk customers, and big spenders.

### Churn Prediction Model
- Defines churn as customers who haven’t purchased in the last 90 days.
- Uses `RandomForestClassifier` to predict churn probability.
- Features include `recency`, `frequency`, and `monetary` values.
- Outputs churn probability for each customer.

### Customer Segments Distribution Analysis
The project also includes customer segmentation based on purchasing behavior. The distribution is visualized using a pie chart, highlighting the following key segments:

1. **Loyal Customers (35.5%)**  
   - The largest segment, indicating a strong customer base that makes frequent and repeated purchases.
   - Retaining and rewarding this group (e.g., loyalty programs, exclusive offers) is essential.

2. **Potential Loyalists (12.3%)**  
   - Customers who have made some repeat purchases but need further engagement to turn into loyal customers.
   - Strategies like personalized offers and follow-up emails can help increase retention.

3. **Other Smaller Segments (Each ~3-5%)**  
   - These represent various customer behaviors, potentially categorized using RFM (Recency, Frequency, Monetary) analysis.
   - Further segmentation could include:
     - **High-value customers (big spenders)**  
     - **Frequent but low-spend customers**  
     - **Churn-prone customers (who might stop purchasing soon)**  

### Actionable Recommendations
- **For Loyal Customers**: Maintain engagement with special rewards and premium offers.
- **For Potential Loyalists**: Encourage repeat purchases through personalized discounts.
- **For Smaller Segments**: Identify which groups are at risk of churn and implement re-engagement campaigns.

## Results
- Churn probability predictions are saved in `rfm_churn_with_probabilities.csv`.
- Final trained model is stored in `models/rfm_churn_model.pkl`.
- API successfully serves predictions and insights.

![image](https://github.com/user-attachments/assets/eb6ed40f-2ae2-4a93-bd28-e8c55b7be3ee)

![image](https://github.com/user-attachments/assets/1a985ec5-8048-488b-8d1d-dcab589ca282)

![image](https://github.com/user-attachments/assets/6540acba-4a3d-4108-a76b-14316455f149)

## Next Steps
- Improve model performance by fine-tuning hyperparameters.
- Integrate results into a dashboard for business insights.
- Expand API capabilities for real-time customer retention analysis.

For any questions, feel free to reach out!


