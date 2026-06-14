# 📈 NIFTY SMA Crossover Backtest Dashboard

A quantitative trading strategy on the NIFTY 50 index using a 20-day and 50-day Simple Moving Average (SMA) crossover.

## 🚀 Live Dashboard

https://nifty-sma-backtest-kxa2y274la2jr6c3tg2f5r.streamlit.app/

## 📊 Strategy Overview

This project implements a trend-following strategy based on SMA crossovers:

* Buy when SMA20 crosses above SMA50
* Sell when SMA20 crosses below SMA50
* Includes transaction costs
* Walk-forward testing to reduce overfitting
* Comparison against Buy & Hold benchmark

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Streamlit
* Yahoo Finance (yfinance)

## 📈 Performance Metrics

### Train Period (2010–2020)

* Total Return: 119.37%
* Sharpe Ratio: 0.7140
* Maximum Drawdown: -28.95%

### Test Period (2021–2025)

* Total Return: 25.49%
* Buy & Hold Return: 68.67%
* Sharpe Ratio: 0.6032
* Maximum Drawdown: -20.17%
* Number of Trades: 19

## 📉 Dashboard Features

* Current NIFTY Price
* Trading Signal (BUY/SELL)
* Sharpe Ratio
* Maximum Drawdown
* Total Return
* Number of Trades
* Equity Curve
* Drawdown Curve
* Buy & Hold Benchmark
* Recent Trading Signals

## 📂 Project Structure

nifty-sma-backtest/

├── data/

│   └── nifty50.csv

├── results/

│   ├── equity_curve.png

│   ├── drawdown_curve.png

│   └── performance_report.csv

├── src/

│   ├── backtester.py

│   ├── indicators.py

│   ├── strategy.py

│   ├── metrics.py

│   ├── drawdown.py

│   ├── trade_stats.py

│   └── plotter.py

├── app.py

├── main.py

├── requirements.txt

└── README.md

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📌 Future Improvements

* Parameter optimization
* Multi-asset backtesting
* Risk-adjusted position sizing
* Portfolio-level backtesting
* Factor investing strategies

## 👨‍💻 Author

Sompartha Sinha

BS in Data Science, IIT Madras
