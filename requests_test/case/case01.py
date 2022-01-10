# coding = utf-8
from requests_test.po_key.apiDemo import ApiDemo

api_demo = ApiDemo()
url = 'http://shop-xo.hctestedu.com/index.php?s=/api/user/login&application=app'
data = {'type':'username','accounts':'admin','pwd':123456}
headers = {'content_type':'application/x-www-form-urlencoded'}
r = api_demo.request(url,'post', params=data, headers=headers)
print(r)
assert r['code'] == 0, '断言错误，code不相同'
