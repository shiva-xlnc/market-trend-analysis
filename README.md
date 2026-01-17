# AI-Driven Market Trend Analysis and Forecasting

## Project Track
AI for Market Trend Analysis

---

## Abstract
This project explores the application of Artificial Intelligence for analyzing and forecasting market trends using historical stock market data. A Long Short-Term Memory (LSTM) based time-series forecasting model is implemented to capture temporal patterns in stock prices. Additionally, a lightweight Streamlit dashboard is developed to visualize market trends and demonstrate real-world deployment of the analysis.

---

## Problem Statement
Financial markets generate large volumes of time-series data that are difficult to analyze manually due to volatility and noise. The objective of this project is to analyze historical stock price trends and forecast future price movements using AI-based models to support data-driven decision making.

---

## Real-World Relevance
- Stock market trend prediction for investment planning  
- Risk analysis and portfolio management  
- Demand forecasting in financial markets  
- Applicable to stocks, cryptocurrencies, and commodities  

---

## Dataset
- **Source:** Yahoo Finance API  
- **Stocks Used:** AAPL, TSLA, MSFT (example)  
- **Time Period:** 2018 – 2024  
- **Features:** Open, High, Low, Close, Volume  

---

## Methodology
1. Data collection from Yahoo Finance  
2. Exploratory Data Analysis (EDA)  
3. Data preprocessing and feature engineering  
   - Handling missing values  
   - Moving average computation  
4. Time-series modeling using LSTM  
5. Model evaluation using error metrics  
6. Visualization using a Streamlit dashboard  

---

## Model / System Design
- **Model Used:** Long Short-Term Memory (LSTM)  
- LSTM is well-suited for sequential and time-series data  
- Captures long-term dependencies in stock prices  
- Predicts future closing prices based on historical trends  

---

## Evaluation Metrics
- Mean Absolute Error (MAE)  
- Root Mean Squared Error (RMSE)  

The model captures overall price trends effectively but shows limitations during sudden market fluctuations.

---

## Dashboard (UI)
A Streamlit-based dashboard is implemented to visualize:
- Historical stock price trends  
- Moving averages for trend analysis  

The dashboard demonstrates how the analytical model can be integrated into a real-world user interface.  
*(The dashboard is supplementary; the Jupyter Notebook is the primary evaluation artifact.)*

---

## Ethical Considerations & Responsible AI
- The model uses only historical market data  
- Does not consider external factors such as news or economic events  
- Predictions should **not** be treated as financial or investment advice  
- Dataset limitations and model assumptions are clearly stated  

---

## Conclusion
This project demonstrates an end-to-end AI pipeline for market trend analysis, from data collection and preprocessing to modeling, evaluation, and visualization. The results highlight the potential of AI techniques in understanding and forecasting market behavior.

---

## Future Scope
- Integration of news and sentiment analysis  
- Real-time market data forecasting  
- Portfolio-level trend prediction  
- Advanced transformer-based time-series models  

---

## How to Run the Project

### Install dependencies
```bash
pip install -r requirements.txt
