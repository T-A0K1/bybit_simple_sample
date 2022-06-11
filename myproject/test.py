import ccxt

bybit = ccxt.bybit()

ohl_hist = bybit.fetch_ohlcv(symbol='BTCUSDT',timeframe='1m', limit=1000)

print(len(ohl_hist))