import requests
import json
print("success")
headers={'content-type': 'application/json',
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
#r = requests.get('https://api.github.com/events')
#r = requests.get('https://api.coinex.com/')
r=requests.get('https://api.coinex.com/v1/market/list')
print(r.status_code)
print(r.text)
#print(r.json())