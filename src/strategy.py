def generate_signals(df):

    df["Signal"] = 0

    df.loc[df["SMA20"] > df["SMA50"], "Signal"] = 1

    df["Position"] = df["Signal"].shift(1)

    return df