# coding = utf-8
import requests
import json
url = 'https://m.dianping.com/brandactivity/query/searchShop'
params = "{'config':'35F332DFB91C206AC8D2223CDE7E58B0','start':0,'limit':10,}"
data = eval(params)
print(data)
r = requests.get(url, data,verify=False)
print(r.status_code)
print(r.url)
r.encoding = 'utf-8'
print(r.text)
