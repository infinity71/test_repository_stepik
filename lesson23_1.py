from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_xpath("//button[@type='submit']")
    button1.click()
    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text

    def calc_x(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    result = calc_x(x)
    input_result = browser.find_element_by_xpath("//input[@id='answer']")
    input_result.send_keys(result)

    button_submit = browser.find_element_by_xpath("//button[@type='submit']")
    button_submit.click()

    time.sleep(10)


finally:
    time.sleep(10)
    browser.quit()
