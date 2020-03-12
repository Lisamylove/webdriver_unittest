import unittest
from selenium import webdriver
from test_fk_work.create_method import *


test_url = 'http://testkc3.chexiao.co'
username = 'xinxinceshi'
password = '961111'
code = '11'


class DeviceFile(unittest.TestCase):
    def setUp(self):
        print('start')

    def tearDown(self):
        print('end')

    def test_device(self):
        self.driver = webdriver.Chrome()
        self.driver.get(test_url)
        self.driver.maximize_window()
        self.driver.find_element_by_id('username').clear()
        inputSendKey(self.driver, '用户名', username)
        self.driver.find_element_by_id('password').clear()
        inputSendKey(self.driver, '密码', password)
        inputSendKey(self.driver, '验证码', code, 1)
        self.driver.find_element_by_css_selector('.btn.orange.pull-right').submit()
        sleep(3)
        self.driver.find_element_by_css_selector('.sidebar-toggler.hidden-phone').click()
        clickSpanByText(self.driver, '信息管理', 2)
        clickLiByText(self.driver, '设备信息', 2)
        sleep(10)


if __name__ == '__main__':
    unittest.main()
