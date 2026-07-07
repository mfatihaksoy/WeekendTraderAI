from ta.momentum import RSIIndicator


def rsi_score(data):
    close = data["Close"]

    rsi = float(RSIIndicator(close=close, window=14).rsi().iloc[-1])

    if 45 <= rsi <= 65:
        return 25

    if 35 <= rsi < 45:
        return 15

    return 0