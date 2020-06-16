# coding:utf-8
import unittest
from selenium import webdriver
from testCase.WorkorderManagement.testCase_Method import *
from time import sleep
from config import configNewCreate


class WorkOrderCreate(unittest.TestCase):

    def setUp(self):
        print('start')

    def tearDown(self):
        self.driver.quit()
        print('end')

    def test_workOrderCreate(self):
        self.driver = webdriver.Chrome()
        self.driver.get(configNewCreate.url)
        self.driver.maximize_window()
        self.driver.find_element_by_id('username').send_keys(configNewCreate.username)
        self.driver.find_element_by_id('password').send_keys(configNewCreate.password)
        self.driver.find_element_by_css_selector('.code_input_login').send_keys(configNewCreate.code)
        clickSpanByText(self.driver, '登 录', 1)
        clickSpanByText(self.driver, '工单管理', 1)
        # clickSpanByText(self.driver, '工单系统new', 1)
        # clickLiByText(self.driver, '工单管理new', 1)
        clickSpanByText(self.driver, '装机', 2)
        # 装机工单
        inputSendKey(self.driver, '请输入车主姓名', configNewCreate.car_name)
        inputSendKey(self.driver, '请输入车主电话', configNewCreate.car_tel)
        inputSendKey(self.driver, '请输入17位车架号', configNewCreate.car_frame_no)
        inputSendKey(self.driver, '请输入车辆品牌', configNewCreate.car_brand)
        inputSendKey(self.driver, '请输入车辆型号', configNewCreate.car_model)
        department(self.driver, configNewCreate.car_placeholder, configNewCreate.car_shop_name, 1)
        inputSendKey(self.driver, '请选择时间', configNewCreate.car_plan_installTime)
        clickSpanByText(self.driver.find_element_by_css_selector('.el-picker-panel.el-date-picker.el-popper.has-time'), '确定', 1)
        inputSendKey(self.driver, '请输入现场联系人', configNewCreate.car_contact_name)
        inputSendKey(self.driver, '请输入现场联系人身份', configNewCreate.car_contact_status)
        inputSendKey(self.driver, '请输入现场联系人电话', configNewCreate.car_contact_tel)
        deviceInformation(self.driver, configNewCreate.car_wire_equip, configNewCreate.car_wireless_equip, configNewCreate.car_obd_equip)  # 设备信息-有限、无线、OBD
        address(self.driver)    # 工作地址、居住地址、安装地址
        # 信息填写完后，点击提交按钮
        clickSpanByText(self.driver.find_element_by_css_selector('.el-button.el-button--primary.el-button--medium'), '提交', 1)
        # 弹框处理  点击确定:accept()   点击取消:dismiss()
        self.driver.find_element_by_css_selector('.el-button.el-button--default.el-button--small.el-button--primary').click()
        sleep(2)


if __name__ == '__main__':
    unittest.main()
