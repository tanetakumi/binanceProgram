# Binance Program
program for using binance api 

Python 3.9.4

## RSI
The very first calculations for average gain and average loss are simple
```
              100       (前日までの平均上昇幅x13+直近の上昇幅)÷14
RSI = 100 - -------- = ---------------------------------------- × 100
             1 + RS     (前日までの平均下落幅x13+直近の下落幅)÷14
```


