from ta.trend import ADXIndicator


def adx_score(data):
    adx = ADXIndicator(
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        window=14
    ).adx().iloc[-1]

    if adx >= 40:
        return 25

    if adx >= 30:
        return 20

    if adx >= 25:
        return 15

    return 0