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
        firstInput = int(argv[1])
        howPast = firstInput if firstInput < 200 else 200 #1~200
        if firstInput > 200:
            print('ろうそく足は最大200個前のデータしか取得できないため、200個前を取得しました')
        if len(argv) >= 3:
            isMerginValueTrueFlg = argv[2] in ['1', '3', '5', '10', '15', '30']
            merginMinutes = argv[2] + 'm' if isMerginValueTrueFlg else '1m'
            if not isMerginValueTrueFlg:
                print(argv[2], '分刻みのろうそく足データは存在しないため、1分足で取得しました。2つ目のパラメータは1,3,5,10,15,30のいずれかにしてください')
        else:
            merginMinutes = '1m'
            
        ohl_hist = bybit.fetch_ohlcv(symbol='BTCUSDT',timeframe=merginMinutes, limit=howPast) #m:1,3,5,10,15,30
        targetCandle = ohl_hist[0]
        printData(targetCandle, merginMinutes)
    
    return 0

def printData(targetCandle, merginMinutes):
    dateTime = fromUNIXmStoDatetime(targetCandle[0])
    s,h,l,e = targetCandle[1:-1]
    print('Time：', dateTime)
    print('Mergin：', merginMinutes[:-1], '分')
    print('Start:', s)
    print('High : +', h-s)
    print('Low  : ', l-s)
    print('End  :', e-s if e-s < 0 else '+ ' + str(e-s))
    

if __name__ == "__main__":
    sys.exit(main(sys.argv))