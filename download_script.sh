#!/bin/bash
#            0       1      2      3      4      5      6      7      8       9       10     11     12     13     14     15      16      17
symbols=( BTCUSDT ETHBTC XRPBTC BCCBTC EOSBTC XLMBTC LTCBTC XMRBTC TRXBTC IOTABTC DASHBTC BNBBTC NEOBTC ETCBTC ICXBTC QTUMBTC LSKBTC NANOBTC )
for i in "${symbols[@]}"
do
    kline-binance -i 1m -s $i -l 500000 -st 01/12/2017 -e 02/10/2018 -o $i
    sleep 10
done

# incomplete: 13 
