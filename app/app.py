import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Market Trend Dashboard", layout="wide")

st.title("📈 AI-Based Market Trend Analysis Dashboard")

# Sidebar
st.sidebar.header("Configuration")
ticker = st.sidebar.selectbox(
    "Select Stock",
    ["AAPL", "TSLA", "MSFT", "GOOGL"]
)

# Load data
data = yf.download(ticker, start="2018-01-01", end="2024-01-01")

# 🔑 FIX: flatten MultiIndex columns
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

data = data[['Close']].dropna()

# Moving averages
data['MA20'] = data['Close'].rolling(20).mean()
data['MA50'] = data['Close'].rolling(50).mean()

st.subheader(f"Historical Price Trend: {ticker}")
st.line_chart(data[['Close', 'MA20', 'MA50']])

st.subheader("Key Insights")
st.write(f"Latest Closing Price: {data['Close'].iloc[-1]:.2f}")
st.write("Moving averages help identify short-term and long-term trends.")

# st.info("⚠️ This dashboard is for educational purposes only. Not financial advice.")
