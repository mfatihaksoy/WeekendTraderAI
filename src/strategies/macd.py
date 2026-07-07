def macd_score(data):
    close = data["Close"]

    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()

    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()

    if float(macd.iloc[-1]) > float(signal.iloc[-1]):
        return 25

    return 0