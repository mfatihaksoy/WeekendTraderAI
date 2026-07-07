import yfinance as yf


def download_stock(symbol, period="1y", interval="1d"):
    """
    Yahoo Finance'tan hisse verisi indirir.
    """

    data = yf.download(
        symbol,
        period=period,
        interval=interval,
        progress=False
    )

    return data