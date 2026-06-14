import matplotlib.pyplot as plt

def plot_equity_curve(df):

    plt.figure(figsize=(12, 6))

    plt.plot(
        df["Equity"],
        label="SMA Strategy"
    )

    plt.plot(
        df["Buy_Hold"],
        label="Buy & Hold"
    )

    plt.title(
        "NIFTY SMA Strategy vs Buy & Hold"
    )

    plt.xlabel("Time")

    plt.ylabel("Portfolio Value")

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "results/equity_curve.png"
    )

    plt.show()