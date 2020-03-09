# coding:utf-8
import unittest
from selenium import webdriver
from testfk3_2_work.ButtonClick import *
from time import sleep
from config_file import config


class WorkOrder(unittest.TestCase):

    def setUp(self):
        print('start')

    def tearDown(self):
        self.driver.quit()
        print('end')

    def test_WorkOrder(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.url)
        self.driver.maximize_window()
        self.driver.find_element_by_id('username').send_keys(config.username)
        self.driver.find_element_by_id('password').send_keys(config.password)
        # sleep(5)
        self.driver.find_element_by_css_selector('.code_input_login').send_keys(config.code)
        clickSpanByText(self.driver, '登 录', 2)
        clickSpanByText(self.driver, '工单管理', 2)
        clickSpanByText(self.driver, '工单系统new', 2)
        clickLiByText(self.driver, '工单管理new', 3)
        clickSpanByText(self.driver, '装机', 3)
        # 装机工单
        inputSendKey(self.driver, '请输入车主姓名', config.car_name)
        inputSendKey(self.driver, '请输入车主电话', config.car_tel)
        inputSendKey(self.driver, '请输入17位车架号', config.car_frame_no)
        inputSendKey(self.driver, '请输入车辆品牌', config.car_brand)
        inputSendKey(self.driver, '请输入车辆型号', config.car_model)
        department(self.driver, "广汽佛", config.car_shop_name, 1)
        inputSendKey(self.driver, '请选择时间', config.car_plan_installTime)
        clickSpanByText(self.driver.find_element_by_css_selector('.el-picker-panel.el-date-picker.el-popper.has-time'), '确定', 1)
        inputSendKey(self.driver, '请输入现场联系人', config.car_contact_name)
        inputSendKey(self.driver, '请输入现场联系人身份', config.car_contact_status)
        inputSendKey(self.driver, '请输入现场联系人电话', config.car_contact_tel)
        deviceInformation(self.driver, config.car_wire_equip, config.car_wireless_equip, config.car_obd_equip)  # 设备信息-有限、无线、OBD
        address(self.driver)    # 工作地址、居住地址、安装地址
        sleep(5)
        # 信息填写完后，点击提交按钮
        clickSpanByText(self.driver.find_element_by_css_selector('.el-button.el-button--primary.el-button--medium'), '提交', 1)
        # 弹框处理  点击确定:accept()   点击取消:dismiss()
        self.driver.find_element_by_css_selector('.el-button.el-button--default.el-button--small.el-button--primary').click()
        sleep(10)


if __name__ == '__main__':
    unittest.main()
