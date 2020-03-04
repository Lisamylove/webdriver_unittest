# coding:utf-8
import unittest
from selenium import webdriver
from testfk3_2_work.ButtonClick import *
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
        self.driver.quit()
        print('end')

    def test_WorkOrder(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url_test)
        # self.driver.maximize_window()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        # sleep(5)
        self.driver.find_element_by_css_selector('.code_input_login').send_keys(code)
        clickSpanByText(self.driver, '登 录', 2)
        clickSpanByText(self.driver, '工单管理', 2)
        clickSpanByText(self.driver, '工单系统new', 2)
        clickLiByText(self.driver, '工单管理new', 3)
        clickSpanByText(self.driver, '装机', 3)
        # 装机工单
        inputSendKey(self.driver, '请输入车主姓名', '车晓VIN1')
        inputSendKey(self.driver, '请输入车主电话', '13252635263')
        inputSendKey(self.driver, '请输入17位车架号', '65S41526352634333')
        inputSendKey(self.driver, '请输入车辆品牌', '品牌')
        inputSendKey(self.driver, '请输入车辆型号', '型号')
        department(self.driver, "广汽", "广汽佛山广爱店", 1)
        inputSendKey(self.driver, '请选择时间', '2020-02-26 18:29:46')
        clickSpanByText(self.driver.find_element_by_css_selector('.el-picker-panel.el-date-picker.el-popper.has-time'), '确定', 1)
        inputSendKey(self.driver, '请输入现场联系人', '哈哈哈')
        inputSendKey(self.driver, '请输入现场联系人身份', '哈哈2')
        inputSendKey(self.driver, '请输入现场联系人电话', '13252635263')
        deviceInformation(self.driver, 1)  # 设备信息-有限、无线、OBD
        address(self.driver)    # 工作地址、居住地址、安装地址
        # 信息填写完后，点击提交按钮
        clickSpanByText(self.driver.find_element_by_css_selector('.el-button.el-button--primary.el-button--medium'), '提交', 1)
        # 弹框处理  点击确定:accept()   点击取消:dismiss()
        self.driver.find_element_by_css_selector('.el-button.el-button--default.el-button--small.el-button--primary').click()
        sleep(10)


if __name__ == '__main__':
    unittest.main()
