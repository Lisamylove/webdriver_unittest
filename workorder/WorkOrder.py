# coding:utf-8
import unittest
from selenium import webdriver
from workorder.ButtonClick import *
from time import sleep

url_test = 'http://testfk3.chexiao.co/'
url_mk = 'http://fk.chexiao.co'
username = 'xinxinceshi'
password = '961111'
code = 'oll'


class WorkOrder(unittest.TestCase):

    def setUp(self):
        print('start')

    def tearDown(self):
        print('end')

    def test_WorkOrder(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url_test)
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        # sleep(5)
        self.driver.find_element_by_css_selector('.code_input_login').send_keys(code)
        clickSpanByText(self.driver, '登 录', 2)
        clickSpanByText(self.driver, '工单管理', 2)
        clickSpanByText(self.driver, '工单系统new', 2)
        clickLiByText(self.driver, '工单管理new', 1)
        clickSpanByText(self.driver, '装机', 3)
        # 装机工单
        inputSendKey(self.driver, '请输入车主姓名', '车晓VIN1')
        inputSendKey(self.driver, '请输入车主电话', '13252635263')
        inputSendKey(self.driver, '请输入17位车架号', 'DAS41526352634333')
        inputSendKey(self.driver, '请输入车辆品牌', '品牌')
        inputSendKey(self.driver, '请输入车辆型号', '型号')
        department(self.driver, "广汽", "福建省瑞骅汽车销售有限公司", 1)
        inputSendKey(self.driver, '请选择时间', '2020-02-26 18:29:46')
        inputSendKey(self.driver, '请输入现场联系人', '哈哈哈')
        inputSendKey(self.driver, '请输入现场联系人身份', '哈哈2')
        inputSendKey(self.driver, '请输入现场联系人电话', '13252635263')
        deviceInformation(self.driver,1)
        sleep(5)


if __name__ == '__main__':
    unittest.main()
