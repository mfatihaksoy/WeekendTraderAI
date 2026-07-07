def trade_plan(data):
    close = data["Close"]
    high = data["High"]
    low = data["Low"]

    last_close = float(close.iloc[-1])

    support = float(low.tail(20).min())
    resistance = float(high.tail(20).max())

    stop = round(support * 0.98, 2)
    target = round(resistance * 1.05, 2)
    entry = round(last_close, 2)

    risk = entry - stop
    reward = target - entry

    if risk <= 0:
        rr = 0
    else:
        rr = round(reward / risk, 2)

    return {
        "entry": entry,
        "stop": stop,
        "target": target,
        "rr": rr
    }