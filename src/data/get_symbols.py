import pandas as pd


def get_symbols():
    url = "https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt"

    df = pd.read_csv(url, sep="|")

    symbols = df["Symbol"].dropna().tolist()

    symbols = [
        s for s in symbols
        if "$" not in s
        and "." not in s
        and len(s) <= 5
    ]

    return symbols[:500]