import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="NIFTY SMA Dashboard",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("results/performance_report.csv")

latest = df.iloc[-1]

current_price = latest["Close"]
sma20 = latest["SMA20"]
sma50 = latest["SMA50"]

signal = "BUY 🟢" if latest["Signal"] == 1 else "SELL 🔴"

# --------------------------------------------------
# PERFORMANCE METRICS
# --------------------------------------------------

SHARPE_RATIO = 0.6032
MAX_DRAWDOWN = -20.17
TOTAL_RETURN = 25.49
NUMBER_OF_TRADES = 19

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📈 NIFTY SMA Trading Dashboard")

st.markdown(
    """
    Live dashboard for a 20/50-day SMA crossover strategy on NIFTY 50.
    Includes walk-forward testing, transaction costs, benchmark comparison,
    and quantitative performance metrics.
    """
)

# --------------------------------------------------
# TOP METRICS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Current NIFTY", f"{current_price:.2f}")

with col2:
    st.metric("Signal", signal)

with col3:
    st.metric("Sharpe Ratio", f"{SHARPE_RATIO:.2f}")

with col4:
    st.metric("Max Drawdown", f"{MAX_DRAWDOWN:.2f}%")

col5, col6 = st.columns(2)

with col5:
    st.metric("Total Return", f"{TOTAL_RETURN:.2f}%")

with col6:
    st.metric("Number of Trades", NUMBER_OF_TRADES)

# --------------------------------------------------
# EQUITY CURVE
# --------------------------------------------------

st.subheader("📊 Strategy Equity Curve")

st.line_chart(df["Equity"])

# --------------------------------------------------
# DRAWDOWN CURVE
# --------------------------------------------------

st.subheader("📉 Drawdown Curve")

rolling_max = df["Equity"].cummax()

drawdown = (
    (df["Equity"] - rolling_max)
    / rolling_max
) * 100

st.line_chart(drawdown)

# --------------------------------------------------
# BUY & HOLD
# --------------------------------------------------

st.subheader("📈 Buy & Hold Benchmark")

st.line_chart(df["Buy_Hold"])

# --------------------------------------------------
# RECENT SIGNALS
# --------------------------------------------------

st.subheader("📋 Latest Signals")

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
    ].tail(20),
    use_container_width=True
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.success("Dashboard Running Successfully ✅")

st.caption(
    "Built using Python, Pandas, Streamlit, and Yahoo Finance data."
)