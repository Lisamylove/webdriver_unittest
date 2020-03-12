def click_a_text(driver, text):
    # div = driver.find_element_by_css_selector('.container-fluid')
    # print(div)
    list_a = driver.find_elements_by_tag_name('a')
    print(list_a)
    for a in list_a:
        print(a.text)
        if a.text == text:
            a.click()
            break
