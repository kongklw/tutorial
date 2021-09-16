#coding=utf-8
import unittest
from Flask_day04 import app
class TestCase(unittest.TestCase):
    # 创建测试环境，在测试代码执行前执行
    def setUp(self):
        self.app = app
        # 激活测试标志
        app.config['TESTING'] = True
        self.client = self.app.test_client()

    # 在测试代码执行完成后执行
    def tearDown(self):
        pass

    # 测试代码
    def test_email(self):
        resp = self.client.get('/')
        print resp.data
        self.assertEqual(resp.data,'Sent　Succeed')