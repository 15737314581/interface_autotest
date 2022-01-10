# coding = utf-8
import requests
import hashlib
import time
import base64

md5 = hashlib.md5()
token = 'qwsadsdsafsdvsfv'
t1 = str(time.time()*1000)

content = t1 + token
md5.update(content.encode('utf-8'))
print(md5.hexdigest())

base64Str = base64.b64encode(str(md5.hexdigest()).encode('utf-8')).upper()
print(str(base64Str,encoding='utf-8'))


