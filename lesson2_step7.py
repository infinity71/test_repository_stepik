from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    get_tag = browser.find_element_by_tag_name("img")
    x = get_tag.get_attribute("valuex")
    print("get_atribute value is:")
    print(x)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button = browser.find_element_by_tag_name('button')
    button.click()
    time.sleep(10)

finally:
    time.sleep(10)
    browser.quit()

