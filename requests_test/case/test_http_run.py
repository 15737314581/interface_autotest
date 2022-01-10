# coding = utf-8
from requests_test.http_api.coreHttp import CoreHttp
from requests_test.config.excel_reader import ExcelReader
import jsonpath
import pytest


class TestHttpRun:
    # def do_send_request(self, method, url, data=None, headers=None, content_type=None, extract=None,
    #                     assert_options=None, assert_data=None, assert_value=None, **kwargs):
    #     ch = CoreHttp()
    #     res = ch.send_rquest(method, url, data, headers, content_type, **kwargs)
    #     contentData = {}
    #     if None is not extract and '' is not extract:
    #         for ex in eval(extract):
    #             j_res = jsonpath.jsonpath(res, '$..' + ex)
    #             contentData[ex] = j_res[0]
    #
    #     # 断言
    #     if assert_options == '包含':
    #         assert jsonpath.jsonpath(res,'$..'+assert_data)
    #         print('断言通过')
    #     elif assert_options == '大于':
    #         assert res[assert_data] > assert_value
    #         print('断言通过')
    #     elif assert_options == '大于等于':
    #         assert res[assert_data] >= assert_value
    #         print('断言通过')
    #     elif assert_options == '小于':
    #         assert res[assert_data] < assert_value
    #         print('断言通过')
    #     elif assert_options == '小于等于':
    #         assert res[assert_data] <= assert_value
    #         print('断言通过')
    #     elif assert_options == '等于':
    #         assert res[assert_data] == assert_value
    #         print('断言通过')
    #     else:
    #         print('断言方式有误')
    contentData = {}
    models = ExcelReader().reader()

    @pytest.mark.parametrize('model', models)
    def test_send_request(self, model, **kwargs):

        if int(model.is_need) == 1:  # 是否需要提取值
            if self.contentData:
                for value in eval(model.last_value):
                    data_value = self.contentData[value]
                    model.data = eval(model.data)
                    # model.data[value] = data_value
                    model.data.update({value: data_value})
            else:
                raise Exception('期望有上次结果的值，但是没有对应的数据')
        ch = CoreHttp()
        res = ch.send_rquest(model.method, model.url, model.data, model.headers, model.req_param_type, **kwargs)
        print(res)

        if None is not model.extract and '' != model.extract:
            for ex in eval(model.extract):
                j_res = jsonpath.jsonpath(res, '$..' + ex)
                self.contentData.update({ex: j_res[0]})

        # 断言
        if model.assert_options == '包含':
            try:
                assert jsonpath.jsonpath(res, '$..' + model.assert_data)
                print('断言通过')
            except Exception as e:
                print('断言不通过：实际返回中不包含{0}'.format(res[model.assert_data]))
        elif model.assert_options == '大于':
            try:
                assert res[model.assert_data] > int(model.assert_value)
                print('断言通过')
            except Exception as e:
                print('断言不通过：实际值{0}不大于预期值{1}'.format(res[model.assert_data], int(model.assert_value)))

        elif model.assert_options == '大于等于':
            try:
                assert res[model.assert_data] >= int(model.assert_value)
                print('断言通过')
            except Exception as e:
                print('断言不通过：实际值{0}不大于等于预期值{1}'.format(res[model.assert_data], int(model.assert_value)))
        elif model.assert_options == '小于':
            try:
                assert res[model.assert_data] < int(model.assert_value)
                print('断言通过')
            except Exception as e:
                print('断言不通过：实际值{0}不小于预期值{1}'.format(res[model.assert_data], int(model.assert_value)))
        elif model.assert_options == '小于等于':
            try:
                assert res[model.assert_data] <= int(model.assert_value)
                print('断言通过')
            except Exception as e:
                print('断言不通过：实际值{0}不小于等于预期值{1}'.format(res[model.assert_data], int(model.assert_value)))
        elif model.assert_options == '等于':
            try:
                assert res[model.assert_data] == int(model.assert_value)
                print('断言通过')
            except Exception as e:
                print('断言不通过：实际值{0}与预期值{1}不相等'.format(res[model.assert_data], int(model.assert_value)))

        else:
            print('断言方式有误')


if __name__ == '__main__':
    pytest.main(['./test_http_run.py::TestHttpRun::test_send_request', '--html=../report/report.html'])
