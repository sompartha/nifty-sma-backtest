# NIFTY SMA Crossover Strategy Backtest

## Overview

This project implements a quantitative trading strategy on the NIFTY 50 Index using a Simple Moving Average (SMA) crossover system.

The strategy generates buy signals when the 20-day SMA crosses above the 50-day SMA and exits when the condition is no longer satisfied.

The project includes:

* Walk-forward testing
* Transaction costs
* Buy & Hold benchmark comparison
* Sharpe Ratio analysis
* Maximum Drawdown analysis
* Trade statistics
* Performance visualization

---

## Strategy Logic

### Buy Signal

20-Day SMA > 50-Day SMA

### Exit Signal

20-Day SMA <= 50-Day SMA

Positions are shifted by one day to avoid look-ahead bias.

---

## Data Source

NIFTY 50 historical data downloaded using Yahoo Finance (`yfinance`).

Period:

2010-01-01 to 2025-01-01

---

## Walk-Forward Testing

Training Period:

2010 - 2020

Testing Period:

2021 - 2025

This helps evaluate out-of-sample performance and reduces the risk of overfitting.

---

## Performance Results

### Training Period (2010-2020)

* Total Return: 119.37%
* Sharpe Ratio: 0.7140
* Maximum Drawdown: -28.95%

### Testing Period (2021-2025)

* Total Return: 25.49%
* Buy & Hold Return: 68.67%
* Sharpe Ratio: 0.6032
* Maximum Drawdown: -20.17%
* Number of Trades: 19

---

## Generated Outputs

* equity_curve.png
* drawdown_curve.png
* performance_report.csv

---

## Project Structure

nifty-sma-backtest/

data/
src/
results/
main.py
README.md

---

## Future Improvements

* Parameter optimization
* Additional technical indicators
* Risk-adjusted position sizing
* Machine learning based forecasting
* Options-based strategies
* Streamlit dashboard

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Yahoo Finance (yfinance)

---

## Author

Sompartha Sinha

BS in Data Science, IIT Madras
