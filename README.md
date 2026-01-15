Telco Customer Churn Analysis Dashboard
This interactive dashboard is designed to help telecommunications companies understand customer behavior and identify the key drivers behind customer attrition (churn).

# Project Objectives
- Analyze churn rates across various segments, including contract types, services, and billing amounts.
- Provide actionable insights through intuitive data visualizations for business stakeholders.
- Identify high-risk customer segments to support targeted retention strategies.

# Key Insights
- Contract Type: Customers on Month-to-month contracts exhibit significantly higher churn rates compared to those on long-term contracts.
- Tenure: New customers (tenure < 5 months) are the most vulnerable group, showing a high early attrition rate.
- Monthly Charges: There is a noticeable trend where customers who churn tend to have higher-than-average monthly charges.

# Tech Stack
- Python: Core programming language.
- Streamlit: Framework for building the interactive web dashboard interface.
- Pandas: Used for data manipulation, cleaning, and preprocessing.
- Plotly: Employed for creating interactive visualizations (Sunburst charts, Histograms, and Boxplots).

# Project Structure
- Churn.py: The main application script for the Streamlit dashboard.
- WA_Fn-UseC_-Telco-Customer-Churn.csv: The raw dataset sourced from Kaggle.
- requirements.txt: List of Python libraries and dependencies required to run the app.
