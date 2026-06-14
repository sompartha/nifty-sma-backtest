import pandas as pd

from src.indicators import add_moving_averages
from src.strategy import generate_signals
from src.backtester import run_backtest
from src.metrics import sharpe_ratio, max_drawdown
from src.trade_stats import calculate_trade_stats
from src.plotter import plot_equity_curve
from src.drawdown import plot_drawdown

# ====================================
# LOAD DATA
# ====================================

df = pd.read_csv("data/nifty50.csv")

# Remove unwanted columns
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Convert Close column
df["Close"] = pd.to_numeric(
    df["Close"],
    errors="coerce"
)

# Remove missing values
df = df.dropna(subset=["Close"])

# ====================================
# WALK-FORWARD SPLIT
# ====================================

train_df = df[
    df["Date"] < "2021-01-01"
].copy()

test_df = df[
    df["Date"] >= "2021-01-01"
].copy()

# ====================================
# TRAIN BACKTEST
# ====================================

train_df = add_moving_averages(train_df)
train_df = generate_signals(train_df)
train_df = run_backtest(train_df)

# ====================================
# TEST BACKTEST
# ====================================

test_df = add_moving_averages(test_df)
test_df = generate_signals(test_df)
test_df = run_backtest(test_df)

# ====================================
# TRADE STATISTICS
# ====================================

stats = calculate_trade_stats(test_df)

# ====================================
# TRAIN METRICS
# ====================================

train_return = (
    train_df["Equity"].iloc[-1] - 1
) * 100

train_sharpe = sharpe_ratio(
    train_df["Strategy_Returns"].dropna()
)

train_mdd = max_drawdown(
    train_df["Equity"]
)

# ====================================
# TEST METRICS
# ====================================

test_return = (
    test_df["Equity"].iloc[-1] - 1
) * 100

test_sharpe = sharpe_ratio(
    test_df["Strategy_Returns"].dropna()
)

test_mdd = max_drawdown(
    test_df["Equity"]
)

buy_hold_return = (
    test_df["Buy_Hold"].iloc[-1] - 1
) * 100

# ====================================
# RESULTS
# ====================================

print("\n" + "=" * 60)
print("NIFTY SMA CROSSOVER BACKTEST")
print("=" * 60)

print("\nTRAIN PERIOD")
print("2010 - 2020")

print(f"Total Return: {train_return:.2f}%")
print(f"Sharpe Ratio: {train_sharpe:.4f}")
print(f"Max Drawdown: {train_mdd:.2%}")

print("\n" + "-" * 60)

print("\nTEST PERIOD")
print("2021 - 2025")

print(f"Total Return: {test_return:.2f}%")
print(f"Buy & Hold Return: {buy_hold_return:.2f}%")
print(f"Sharpe Ratio: {test_sharpe:.4f}")
print(f"Max Drawdown: {test_mdd:.2%}")

print("\n" + "-" * 60)

print(f"\nNumber of Trades: {stats['num_trades']}")

print(
    f"\nFinal Test Portfolio Value: "
    f"{test_df['Equity'].iloc[-1]:.4f}"
)

# ====================================
# LAST 10 ROWS
# ====================================

print("\nLast 10 Rows:\n")

print(
    test_df[
        [
            "Close",
            "SMA20",
            "SMA50",
            "Signal",
            "Position",
            "Equity",
            "Buy_Hold"
        ]
    ].tail(10)
)

# ====================================
# SAVE REPORT
# ====================================

test_df.to_csv(
    "results/performance_report.csv",
    index=False
)

# ====================================
# SAVE CHARTS
# ====================================

plot_equity_curve(test_df)

plot_drawdown(test_df)

print("\nCharts saved to:")
print("results/equity_curve.png")
print("results/drawdown_curve.png")

print("\nReport saved to:")
print("results/performance_report.csv")

print("\nBacktest Completed Successfully!")