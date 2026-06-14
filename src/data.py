import yfinance as yf

nifty = yf.download(
    "^NSEI",
    start="2010-01-01",
    end="2025-01-01",
    auto_adjust=True
)

# Flatten if multi-index columns exist
if hasattr(nifty.columns, "levels"):
    nifty.columns = nifty.columns.get_level_values(0)

nifty.to_csv("data/nifty50.csv")

print(nifty.head())