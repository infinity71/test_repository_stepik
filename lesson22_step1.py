from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//h2/span[@id='num1']")
    x = x_element.text
    y_element = browser.find_element_by_xpath("//h2/span[@id='num2']")
    y = y_element.text
    print(x)
    print(y)

    def sum(x, y):
        return str(int(x) + int(y))

    result = sum(x, y)
    print(result)
    selected_result = Select(browser.find_element_by_tag_name("select"))
    selected_result.select_by_visible_text(result)

    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(10)

finally:
    time.sleep(10)
    browser.quit()
