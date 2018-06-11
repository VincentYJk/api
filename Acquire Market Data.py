import requests
import json
#acquire market statistic
r1=requests.get('https://api.coinex.com/v1/market/ticker?market=CETBCH')
print('market statistic:',r1.text)
#acquire market depth
r2=requests.get('https://api.coinex.com/v1/market/depth?market=cetbch&limit=1&merge=0.00000001')
print('market depth',r2.text)
#acquire latest transaction data
r3=requests.get('https://api.coinex.com/v1/market/deals?market=BTCBCH&last_id=1')
print('latest transaction data',r3.text)
#acquire kline
r4=requests.get('https://api.coinex.com/v1/market/kline?market=BTCBCH&type=5min')
print('kline 5 min',r4.text)
