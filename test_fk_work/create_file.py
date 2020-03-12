# coding:utf-8
import unittest
from selenium import webdriver
from test_fk_work.create_method import *
from time import sleep
from config_file import create_config


class WorkOrder(unittest.TestCase):

    def setUp(self):
        print('start')

    def tearDown(self):
        self.driver.quit()
        print('end')

    def test_WorkOrder(self):
        self.driver = webdriver.Chrome()
        self.driver.get(create_config.url)
        self.driver.maximize_window()
        self.driver.find_element_by_id('username').send_keys(create_config.username)
        self.driver.find_element_by_id('password').send_keys(create_config.password)
        # sleep(6)
        self.driver.find_element_by_css_selector('.code_input_login').send_keys(create_config.code)
        clickSpanByText(self.driver, '登 录', 1)
        clickSpanByText(self.driver, '工单管理', 1)
        clickSpanByText(self.driver, '工单系统new', 1)
        clickLiByText(self.driver, '工单管理new', 1)
        clickSpanByText(self.driver, '装机', 2)
        # 装机工单
        inputSendKey(self.driver, '请输入车主姓名', create_config.car_name)
        inputSendKey(self.driver, '请输入车主电话', create_config.car_tel)
        inputSendKey(self.driver, '请输入17位车架号', create_config.car_frame_no)
        inputSendKey(self.driver, '请输入车辆品牌', create_config.car_brand)
        inputSendKey(self.driver, '请输入车辆型号', create_config.car_model)
        department(self.driver, create_config.car_placeholder, create_config.car_shop_name, 1)
        inputSendKey(self.driver, '请选择时间', create_config.car_plan_installTime)
        clickSpanByText(self.driver.find_element_by_css_selector('.el-picker-panel.el-date-picker.el-popper.has-time'), '确定', 1)
        inputSendKey(self.driver, '请输入现场联系人', create_config.car_contact_name)
        inputSendKey(self.driver, '请输入现场联系人身份', create_config.car_contact_status)
        inputSendKey(self.driver, '请输入现场联系人电话', create_config.car_contact_tel)
        deviceInformation(self.driver, create_config.car_wire_equip, create_config.car_wireless_equip, create_config.car_obd_equip)  # 设备信息-有限、无线、OBD
        address(self.driver)    # 工作地址、居住地址、安装地址
        # 信息填写完后，点击提交按钮
        clickSpanByText(self.driver.find_element_by_css_selector('.el-button.el-button--primary.el-button--medium'), '提交', 1)
        # 弹框处理  点击确定:accept()   点击取消:dismiss()
        self.driver.find_element_by_css_selector('.el-button.el-button--default.el-button--small.el-button--primary').click()
        sleep(2)


if __name__ == '__main__':
    unittest.main()
