def trend_score(data):
    close = data["Close"]

    last = float(close.iloc[-1])
    sma20 = float(close.rolling(20).mean().iloc[-1])
    sma50 = float(close.rolling(50).mean().iloc[-1])

    score = 0

    if last > sma20:
        score += 25

    if sma20 > sma50:
        score += 25

    return score