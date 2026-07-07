import yfinance as yf

apple = yf.Ticker("AAPL")

bilgi = apple.fast_info

print("Apple")
print(f"Güncel fiyat: {bilgi['lastPrice']} USD")
