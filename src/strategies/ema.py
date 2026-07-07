def ema_score(data):

    ema20 = data["Close"].ewm(span=20, adjust=False).mean().iloc[-1]
    ema50 = data["Close"].ewm(span=50, adjust=False).mean().iloc[-1]
    ema200 = data["Close"].ewm(span=200, adjust=False).mean().iloc[-1]

    score = 0

    if ema20 > ema50:
        score += 10

    if ema50 > ema200:
        score += 10

    if ema20 > ema200:
        score += 5

    return score