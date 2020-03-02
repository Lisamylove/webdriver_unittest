from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


# 点击菜单按钮
def clickSpanByText(driver, text, sleeps=0):
    spans = driver.find_elements_by_tag_name('span')
    for span in spans:
        print(span.text)
        if span.text == text:
            span.click()
            sleep(sleeps)
            break


# 点击子菜单列表按钮
def clickLiByText(driver, text, sleeps=0):
    lis = driver.find_elements_by_tag_name('li')
    for li in lis:
        if li.text == text:
            li.click()
            sleep(sleeps)
            break


# 装机弹框页需要填写的信息
def inputSendKey(driver, placeholder, text, sleeps=0):
    inputs = driver.find_elements_by_tag_name('input')
    for input in inputs:
        if input.get_attribute('placeholder') == placeholder:
            input.send_keys(text)
            sleep(sleeps)
            break


# 所属部门
def department(driver, text, SelectText, sleeps=0):
    inputs = driver.find_elements_by_tag_name('input')
    for input in inputs:
        if input.get_attribute('placeholder') == '请选择所属部门':
            span = input.find_element_by_xpath('../..')
            print(span.get_attribute('class'))
            span.click()
            input.send_keys(text)
            sleep(3)
    ul = driver.find_element_by_css_selector('.el-cascader-menu.el-cascader-menu--flexible')
    print(ul)
    lis = ul.find_elements_by_xpath('li')
    for li in lis:
        print(li.text)
        ActionChains(driver).move_to_element(li).perform()
        if SelectText in li.text:
            li.click()
            sleep(sleeps)
            break


# 设备信息
def deviceInformation(driver, wired=0, wireless=0, obd=0):
    i = 1
    div = driver.find_element_by_css_selector('.installInfo')
    for li in div.find_elements_by_css_selector('.el-col.el-col-4'):
        input = li.find_element_by_tag_name('input')
        if input.get_attribute('role') == 'spinbutton':
            if i == 1:
                input.clear()
                input.send_keys(str(wired))
            if i == 2:
                input.clear()
                input.send_keys(str(wireless))
            if i == 3:
                input.clear()
                input.send_keys(str(obd))
        i += 1


def address(driver, fatherNode):
    placeholders = ['请选择省', '请选择市', '请输入详细地址']
    for index, placeholder in enumerate(placeholders):
        # f'inputplaceholder="请选择省"'   保持原有格式，传入变量的当前实际值
        addressPart = fatherNode.find_element_by_css_selector(f'input[placeholder="{placeholder}"]')
        if index == 2:
                addressPart.send_keys('望京街道')
        else:
            addressPart.click()
            sleep(1)
            options = driver.find_elements_by_css_selector('.el-select-dropdown.el-popper:last-child ul.el-scrollbar__view.el-select-dropdown__list li')
            if options:
                options[randint(0, len(options) - 1)].click()
            sleep(1)





