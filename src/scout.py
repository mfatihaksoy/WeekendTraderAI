def score_stock(data):
    score = 0

    close = float(data["Close"].iloc[-1])
    previous = float(data["Close"].iloc[-2])
    average = float(data["Close"].mean())

    volume = float(data["Volume"].iloc[-1])
    avg_volume = float(data["Volume"].mean())

    if close > average:
        score += 50

    if close > previous:
        score += 25

    if volume > avg_volume:
        score += 25

    return score