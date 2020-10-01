from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text

    def calc_x(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    input_element = browser.find_element_by_xpath("//input[@id='answer']")
    result = calc_x(x)
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_element)
    input_element.send_keys(result)

    checkbox = browser.find_element_by_xpath("//label[@for='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element_by_xpath("//label[@for='robotsRule']")
    radiobutton.click()

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()


