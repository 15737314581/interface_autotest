# coding = utf-8
import requests
from requests_test.po_key.apiDemo import ApiDemo

url = 'http://shop-xo.hctestedu.com/index.php?s=/api/user/login&application=app'
data = {'type':'username','accounts':'admin','pwd':'123456'}
headers = {'content_type':'application/x-www-form-urlencoded'}
r = requests.post(url, json=data,headers=headers)

demo = ApiDemo()
r = demo.request(url,'post',params=data,content_type='application/json')

# print(r.url)
# print(r.text)
print(r)