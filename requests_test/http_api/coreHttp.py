# coding = utf-8
import requests
import json


class CoreHttp:
    def send_rquest(self, method, url, data=None, headers=None, req_params_type=None, **kwargs):
        if isinstance(data,str) and data != '':
            try:
                data = eval(data)
            except Exception as e:
                raise Exception("异常：{}_请求体无法转换为JSON格式，请检查你输入参数".format(e))
        if isinstance(headers,str) and headers != '':
            try:
                headers = eval(headers)
            except Exception as e:
                raise Exception("异常：{}_请求头无法转换为JSON格式，请检查你输入参数".format(e))
        if method == 'post':
            if req_params_type == 'json':
                response = getattr(requests, method)(url, json=data, headers=headers,verify=False, **kwargs).json()
            else:
                response = getattr(requests, method)(url, data=data, headers=headers,verify=False, **kwargs).json()
        else:
            response = getattr(requests, method)(url, params=data, headers=headers,verify=False, **kwargs).json()
        return response
