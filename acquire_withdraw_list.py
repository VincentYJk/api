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
     st=ar1+'&tonce='+ar2+'&secret_key='+ar3
     #print('st:',st)
     import hashlib
     m = hashlib.md5()  # 创建md5对象
     m.update(st.encode())  # 生成加密串，其中password是要加密的字符串
     t=m.hexdigest()
     #print('upper:',t.upper())  # 打印经过md5加密的字符串
     return (t.upper(),ar2)
#call the funcion to get authorization & tonce
(x,y)=get_md5('access_id=7A9D4B9D19604DD5897716XXXX')
#print(x,y)

#get withdraw list
def get_withdraw_list(x,y):
    import requests
    headers = {
        'application': 'json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'authorization': x}
    #print('ar1:', x)
    url = 'https://api.coinex.com/v1/balance/coin/withdraw?access_id=7A9D4B9D19604DD5897716XXXX&tonce=%s' % y
   # print(url)
    r1 = requests.get(url, headers=headers)
    # r1 = requests.get(url)
    return r1.text
    print(r1.text)

my_result=get_withdraw_list(x,y)
print(my_result)
