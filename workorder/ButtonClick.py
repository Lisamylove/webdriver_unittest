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

