# coding = utf-8
import requests

class ApiDemo(object):

    def __init__(self):
        pass

    def request(self, url, method, headers=None, params=None, content_type=None):
        """
        通用请求工具类
        @param url:
        @param method:
        @param headers:
        @param param:
        @param content_type:
        @return:
        """
        try:
            if method == "get":
                response = requests.get(url=url, headers=headers, params=params).json()
                return response
            elif method == "post":
                if content_type == "application/json":
                    response = requests.post(url=url, headers=headers, json=params).json()
                    return response
                else:
                    response = requests.post(url=url, headers=headers, data=params).json()
                    return response
            else:
                print("http method not allowed")

        except Exception as e:
            print("http请求数据:{0}".format(e))
