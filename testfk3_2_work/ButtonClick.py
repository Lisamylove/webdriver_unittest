from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from config_file import config


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


# 装机-纯文本框的信息输入
def inputSendKey(driver, placeholder, text, sleeps=0):
    inputs = driver.find_elements_by_tag_name('input')
    for input in inputs:
        if input.get_attribute('placeholder') == placeholder:
            input.send_keys(Keys.ENTER)
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


# 工作地址、居住地址、安装地址
def address(driver, sleeps=0):
    for key in config.data.keys():
        div_class = config.data[key]['div_class']
        province = config.data[key]['province']
        city = config.data[key]['city']
        address = config.data[key]['address']
        divs = driver.find_elements_by_css_selector(div_class)
        for div in divs:
            label_text = div.find_element_by_css_selector('.el-col.el-col-2').text
            if label_text == key:
                inputSendKey(div, '请选择省', province)
                clickLiByText(driver.find_element_by_css_selector('body>div.el-select-dropdown.el-popper'), province, 2)
                inputSendKey(div, '请选择市', city)
                clickLiByText(driver.find_element_by_css_selector('body>div:nth-child(14)'), city, 2)
                inputSendKey(div, '请输入详细地址', address)
    sleep(sleeps)

