def calculate_trade_stats(df):

    trades = (
        df["Position"]
        .diff()
        .abs()
        .fillna(0)
    )

    num_trades = int(
        trades.sum()
    )

    return {
        "num_trades": num_trades
    }