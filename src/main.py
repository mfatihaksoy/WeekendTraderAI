from data.downloader import download_stock
from data.symbols import SYMBOLS
from scout import score_stock

results = []

for symbol in SYMBOLS:
    data = download_stock(symbol)
    score = score_stock(data)

    results.append({
        "symbol": symbol,
        "score": score
    })

results = sorted(results, key=lambda x: x["score"], reverse=True)

print("SCOUT AI SONUÇLARI")
print("=" * 40)

for item in results:
    print(item["symbol"], "Skor:", item["score"])