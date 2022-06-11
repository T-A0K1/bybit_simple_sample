## Agenda
bybitから現在及び直近過去の履歴を取得するコードです。

## Purpose
githubの練習

## Required packages
ccxt

## How to use
python myproject/main.py ParamA [ParamB]
- ParamA: 何個前のろうそく足の情報を取得するか。range: 1-200
- ParamB: ろうそく足の間隔(1,3,5,10,15,30)。無記入の場合は1

## sample
- 10本前の15分足を取得  
python myproject/main.py 10 15 

### 出力結果
Time： 2022-06-11 19:00:00  
Mergin： 15 分  
Start: 29066.5  
High : + 53.5  
Low  :  -16.5  
End  : -6.0  