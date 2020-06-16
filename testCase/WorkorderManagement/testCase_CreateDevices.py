import unittest
from selenium import webdriver
from testCase.WorkorderManagement.testCase_Method import *
from selenium.webdriver.support.select import Select


test_url = 'http://testkc1.chexiao.co'
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
        sleep(1)
        self.driver.find_element_by_css_selector('.sidebar-toggler.hidden-phone').click()
        clickSpanByText(self.driver, '信息管理', 1)
        clickLiByText(self.driver, '设备信息', 1)
        # 嵌套了ifram
        self.driver.switch_to_frame('rightFrame')
        portlet_title = self.driver.find_element_by_class_name('portlet-title')
        portlet_title.find_element_by_css_selector('div>div:nth-child(3)').click()
        # 输入添加设备的信息
        self.driver.find_element_by_id('deviceNum').send_keys('1029999032')
        self.driver.find_element_by_id('model').send_keys('CX102')
        select = Select(self.driver.find_element_by_id('type'))
        # 0 无线  1有线   2 OBD
        select.select_by_visible_text('无线')
        sleep(4)
        s = Select(self.driver.find_element_by_id('manufacturer'))
        # 1博实结  2好的货  3康凯斯  4沃达孚
        s.select_by_visible_text('好的货')
        self.driver.find_element_by_xpath('//*[@id="inputForm"]/div[5]/div/button[1]').click()


if __name__ == '__main__':
    unittest.main()
