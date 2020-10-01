from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_xpath("//button")
    button1.click()
    handle_window = browser.window_handles[1]
    browser.switch_to.window(handle_window)

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    print(x)

    def calc_x(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    result = calc_x(x)
    print(result)
    input_result = browser.find_element_by_xpath("//input[@id='answer']")
    input_result.send_keys(result)

    button_submit = browser.find_element_by_xpath("//button")
    button_submit.click()

    time.sleep(10)
finally:
    time.sleep(10)
    browser.quit()
