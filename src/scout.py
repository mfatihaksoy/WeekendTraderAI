from data.downloader import download_stock
from data.get_symbols import get_symbols

from strategies.trend import trend_score
from strategies.macd import macd_score
from strategies.rsi import rsi_score
from strategies.atr import atr_score
from strategies.volume import volume_score
from strategies.adx import adx_score
from strategies.ema import ema_score
from strategies.breakout import breakout_score
from strategies.trade_plan import trade_plan

SYMBOLS = get_symbols()
results = []

for symbol in SYMBOLS:
    try:
        data = download_stock(symbol)

        if len(data) < 200:
            continue

        trend = trend_score(data)
        macd = macd_score(data)
        rsi = rsi_score(data)
        atr = atr_score(data)
        volume = volume_score(data)
        adx = adx_score(data)
        ema = ema_score(data)
        breakout = breakout_score(data)

        plan = trade_plan(data)

        total = trend + macd + rsi + atr + volume + adx + ema + breakout

        if plan["rr"] < 1.5:
            continue

        results.append({
            "symbol": symbol,
            "score": total,
            "trend": trend,
            "macd": macd,
            "rsi": rsi,
            "atr": atr,
            "volume": volume,
            "adx": adx,
            "ema": ema,
            "breakout": breakout,
            "entry": plan["entry"],
            "stop": plan["stop"],
            "target": plan["target"],
            "rr": plan["rr"]
        })

    except Exception:
        continue

results.sort(key=lambda x: x["score"], reverse=True)

print("\nSCOUT AI v11")
print("=" * 145)

for i, item in enumerate(results[:10], start=1):
    print(
        f"{i:2}. "
        f"{item['symbol']:6} "
        f"Skor:{item['score']:3} "
        f"Trend:{item['trend']:2} "
        f"MACD:{item['macd']:2} "
        f"RSI:{item['rsi']:2} "
        f"ATR:{item['atr']:2} "
        f"Hacim:{item['volume']:2} "
        f"ADX:{item['adx']:2} "
        f"EMA:{item['ema']:2} "
        f"BRK:{item['breakout']:2} "
        f"Giriş:{item['entry']} "
        f"Stop:{item['stop']} "
        f"Hedef:{item['target']} "
        f"R/K:{item['rr']}"
    )