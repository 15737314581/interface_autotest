# coding = utf-8
from requests_test.case.test_http_run import TestHttpRun
from requests_test.config.excel_reader import ExcelReader
import urllib3
urllib3.disable_warnings()

if __name__ == '__main__':
    # url = 'http://shop-xo.hctestedu.com/index.php?s=/api/user/login&application=app'
    # data = {'type': 'username', 'accounts': 'admin', 'pwd': 123456}
    # method = 'post'
    # headers = {'content_type': 'application/x-www-form-urlencoded'}
    # test_request = HttpRun()
    # res = test_request.do_send_request(method, url, data=data, headers=headers)
    # print(res)
    reader = ExcelReader()
    models = reader.reader()
    run = TestHttpRun()
    run.test_send_request(models=models)
    