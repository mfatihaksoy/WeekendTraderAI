import yfinance as yf


def relative_strength_score(data):
    spy = yf.download("SPY", period="1y", auto_adjust=True, progress=False)

    if spy.empty or len(data) < 126 or len(spy) < 126:
        return 0

    if hasattr(spy.columns, "levels"):
        spy.columns = spy.columns.get_level_values(0)

    stock_close = data["Close"]
    spy_close = spy["Close"]

    stock_return = float(stock_close.iloc[-1]) / float(stock_close.iloc[-126]) - 1
    spy_return = float(spy_close.iloc[-1]) / float(spy_close.iloc[-126]) - 1

    if stock_return > spy_return * 1.20:
        return 25

    if stock_return > spy_return:
        return 15

    return 0