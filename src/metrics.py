import numpy as np

def sharpe_ratio(returns):

    return (
        returns.mean()
        / returns.std()
    ) * np.sqrt(252)

def max_drawdown(equity):

    rolling_max = equity.cummax()

    drawdown = (
        equity - rolling_max
    ) / rolling_max

    return drawdown.min()