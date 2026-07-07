def breakout_score(data):

    high20 = data["High"].rolling(20).max().iloc[-2]
    close = float(data["Close"].iloc[-1])

    if close > high20:
        return 25

    if close > high20 * 0.98:
        return 15

    return 0