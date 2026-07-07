import yfinance as yf


def run_backtest(symbol, period="5y"):

    data = yf.download(
        symbol,
        period=period,
        auto_adjust=True,
        progress=False
    )

    if data.empty or len(data) < 250:
        return None

    if hasattr(data.columns, "levels"):
        data.columns = data.columns.get_level_values(0)

    trades = 0
    wins = 0
    losses = 0
    total_r = 0

    for i in range(200, len(data) - 20):

        close = float(data["Close"].iloc[i])
        sma20 = float(data["Close"].iloc[i-19:i+1].mean())
        sma50 = float(data["Close"].iloc[i-49:i+1].mean())

        if close < sma20:
            continue

        if sma20 < sma50:
            continue

        entry = close
        stop = float(data["Low"].iloc[i-5:i+1].min())

        risk = entry - stop

        if risk <= 0:
            continue

        target = entry + risk * 2

        trades += 1

        future = data.iloc[i+1:i+21]

        hit_target = False
        hit_stop = False

        for _, row in future.iterrows():

            low = float(row["Low"])
            high = float(row["High"])

            if low <= stop:
                hit_stop = True
                break

            if high >= target:
                hit_target = True
                break

        if hit_target:
            wins += 1
            total_r += 2

        elif hit_stop:
            losses += 1
            total_r -= 1

    if trades == 0:
        return None

    return {
        "Trades": trades,
        "Wins": wins,
        "Losses": losses,
        "WinRate": round(wins / trades * 100, 2),
        "AverageR": round(total_r / trades, 2)
    }


if __name__ == "__main__":
    result = run_backtest("AAPL")
    print(result)