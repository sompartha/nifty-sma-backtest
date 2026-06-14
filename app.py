import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="NIFTY SMA Dashboard",
    layout="wide"
)

st.title("📈 NIFTY SMA Trading Dashboard")

# Load results
df = pd.read_csv("results/performance_report.csv")

# Latest row
latest = df.iloc[-1]

# Metrics
current_price = latest["Close"]
sma20 = latest["SMA20"]
sma50 = latest["SMA50"]

signal = "BUY" if latest["Signal"] == 1 else "SELL"

# Top metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Current NIFTY", f"{current_price:.2f}")

with col2:
    st.metric("Signal", signal)

with col3:
    st.metric("SMA20", f"{sma20:.2f}")

with col4:
    st.metric("SMA50", f"{sma50:.2f}")

# Equity curve
st.subheader("Strategy Equity Curve")

st.line_chart(
    df["Equity"]
)

# Buy & Hold
st.subheader("Buy & Hold Benchmark")

st.line_chart(
    df["Buy_Hold"]
)

# Recent data
st.subheader("Latest Signals")

st.dataframe(
    df[
        [
            "Close",
            "SMA20",
            "SMA50",
            "Signal",
            "Position",
            "Equity"
        ]
    ].tail(20)
)

st.success("Dashboard Running Successfully")