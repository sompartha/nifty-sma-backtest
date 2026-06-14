def run_backtest(df):

    # Daily returns
    df["Returns"] = df["Close"].pct_change()

    # Fill missing positions
    df["Position"] = df["Position"].fillna(0)

    # Strategy returns
    df["Strategy_Returns"] = (
        df["Position"] * df["Returns"]
    )

    # Transaction Costs
    cost = 0.0005

    trades = (
        df["Position"]
        .diff()
        .abs()
        .fillna(0)
    )

    df["Strategy_Returns"] = (
        df["Strategy_Returns"]
        - trades * cost
    )

    # Strategy Equity Curve
    df["Equity"] = (
        1 + df["Strategy_Returns"]
    ).cumprod()

    # Buy & Hold Benchmark
    df["Buy_Hold"] = (
        1 + df["Returns"]
    ).cumprod()

    return df