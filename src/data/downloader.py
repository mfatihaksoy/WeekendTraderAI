import yfinance as yf


def download_stock(symbol, period="1y", interval="1d"):
    data = yf.download(symbol, period=period, interval=interval, progress=False)

    if data.empty:
        raise ValueError("Veri bulunamadı")

    if hasattr(data.columns, "levels"):
        data.columns = data.columns.get_level_values(0)

    return data