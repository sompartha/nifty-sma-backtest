import matplotlib.pyplot as plt

def plot_drawdown(df):

    rolling_max = df["Equity"].cummax()

    drawdown = (
        df["Equity"] - rolling_max
    ) / rolling_max

    plt.figure(figsize=(12,6))

    plt.plot(drawdown)

    plt.title(
        "NIFTY SMA Strategy Drawdown"
    )

    plt.xlabel("Time")

    plt.ylabel("Drawdown")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "results/drawdown_curve.png"
    )

    plt.show()