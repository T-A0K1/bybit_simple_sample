from datetime import date
import sys
import ccxt
from mylib.pkg import fromUNIXmStoDatetime

def main(argv): #argvでコマンドライン引数受け取り
    bybit = ccxt.bybit()
    
    if len(argv) == 1:
        print('test mode')
    else:
        # パラメータ処理
        howPast = int(argv[1]) if int(argv[1]) < 200 else 200 #1~200
        if len(argv) >= 3:
            merginMinutes = argv[2] + 'm' if argv[2] in ['1', '3', '5', '10', '15', '30'] else '1m'
        else:
            merginMinutes = '1m'
            
        print('mergin:', merginMinutes)

        ohl_hist = bybit.fetch_ohlcv(symbol='BTCUSDT',timeframe=merginMinutes, limit=howPast) #m:1,3,5,10,15,30
        targetCandle = ohl_hist[0]
        printData(targetCandle, merginMinutes)
    
    return 0

def printData(targetCandle, merginMinutes):
    dateTime = fromUNIXmStoDatetime(targetCandle[0])
    s,h,l,e = targetCandle[1:-1]
    print('時間：', dateTime)
    print('分足：', merginMinutes[:-1], '分')
    print('Start:', s)
    print('High: +', h-s)
    print('Low : ', l-s)
    print('End :', e-s if e-s < 0 else '+ ' + str(e-s))
    

if __name__ == "__main__":
    sys.exit(main(sys.argv))