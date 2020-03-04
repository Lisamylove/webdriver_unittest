import unittest
from selenium import webdriver
from testfk3_2_work.ButtonClick import *
from testkc3_1.Device_ButtonClick import *


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
        inputSendKey(self.driver, '用户名', username)
        inputSendKey(self.driver, '密码', password)
        inputSendKey(self.driver, '验证码', code, 1)
        self.driver.find_element_by_css_selector('.btn.orange.pull-right').submit()
        sleep(3)
        self.driver.find_element_by_css_selector('.sidebar-toggler.hidden-phone').click()
        clickSpanByText(self.driver, '信息管理', 2)
        clickLiByText(self.driver, '设备信息', 5)
        # self.driver.find_element_by_xpath('//*[@id="container"]/div[3]/div/div/div[1]/div[3]/a').click()
        sleep(10)


if __name__ == '__main__':
    unittest.main()