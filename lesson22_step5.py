from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname_input = browser.find_element_by_xpath("//input[@name='firstname']")
    firstname_input.send_keys("Test Name")

    lastname_input = browser.find_element_by_xpath("//input[@name='lastname']")
    lastname_input.send_keys("Test LastName")

    email_input = browser.find_element_by_xpath("//input[@name='email']")
    email_input.send_keys("test@test.io")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")

    add_file = browser.find_element_by_xpath("//input[@name='file']")
    add_file.send_keys(file_path)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()
    time.sleep(10)

finally:
    time.sleep(10)
    browser.quit()
