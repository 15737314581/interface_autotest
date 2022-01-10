# coding = utf-8
from requests_test.po_key.apiDemo import ApiDemo
import unittest
from ddt import ddt, file_data


@ddt()
class CaseDemo(unittest.TestCase):

    @file_data('../data/login.yml')
    def test_login(self, url, method, data, headers, content_type, assert_code):
        api_demo = ApiDemo()
        r = api_demo.request(url, method, params=data, headers=headers, content_type=content_type)
        print(r['code'])
        self.assertEqual(assert_code, r['code'], '断言失败，code不匹配～')


if __name__ == '__main__':
    unittest.main()
