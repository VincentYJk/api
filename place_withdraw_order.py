# -*- coding:utf-8 -*-
#get tonce
def current_time():
    import datetime
    import time
    t=time.time()
    current=round(t*1000)
    s_current=str(current)
    return(s_current)
    #print(s_current)

my_tonce=current_time()

#get tonce&authorization
def get_md5(ar1,ar2=current_time(),ar3='secret_key'):
     st=ar1+'&actual_amount=0.001&coin_address=192Vrf3A9HZU3BhSYatm4eTeVAadASZpxH&coin_type=bch&tonce='+ar2+'&secret_key='+ar3
     #print('st:',st)
     import hashlib
     m = hashlib.md5()  # 创建md5对象
     m.update(st.encode())  # 生成加密串，其中password是要加密的字符串
     t=m.hexdigest()
     #print('upper:',t.upper())  # 打印经过md5加密的字符串
     return (t.upper(),ar2)
#call the funcion to get authorization & tonce
(x,y)=get_md5('access_id=C16F3EF3EB3A4391B1C1FA64CBBDD70A')
print(x,y)

#place a withdraw order
def withdraw(x,y):
    import requests
    import json
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'authorization': x}
    url = 'https://api.coinex.com/v1/balance/coin/withdraw'
    s = json.dumps({'coin_type': 'bch', 'coin_address': '192Vrf3A9HZU3BhSYatm4eTeVAadASZpxH','actual_amount':'0.001','access_id':'C16F3EF3EB3A4391B1C1FA64CBBDD70A','tonce':y})
    r= requests.post(url,data=s, headers=headers)
    return r.text
my_withdraw=withdraw(x,y)
print(my_withdraw)


