from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    text = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '$100'))
    button1 = browser.find_element_by_xpath("//button[@id='book']")
    button1.click()

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    print(x)

    def calc_x(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    result = calc_x(x)
    print(result)
    input_result = browser.find_element_by_xpath("//input[@id='answer']")
    input_result.send_keys(result)

    button_submit = browser.find_element_by_xpath("//button[@type='submit']")
    button_submit.click()

    time.sleep(20)
finally:
    time.sleep(20)
    browser.quit()
