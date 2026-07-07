from ta.volatility import AverageTrueRange


def atr_score(data):
    high = data["High"]
    low = data["Low"]
    close = data["Close"]

    atr = float(
        AverageTrueRange(
            high=high,
            low=low,
            close=close,
            window=14
        ).average_true_range().iloc[-1]
    )

    if atr > 5:
        return 25

    if atr > 2:
        return 15

    return 5