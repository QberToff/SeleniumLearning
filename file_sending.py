from selenium import webdriver
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

dir_path = os.path.abspath(os.path.dirname(__file__))
file_name = 'text.txt'

file_path = os.path.join(dir_path, file_name)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_xpath('//input[@name="firstname"]')
    first_name.send_keys('First Name')

    last_name = browser.find_element_by_xpath('//input[@name="lastname"]')
    last_name.send_keys('Last name')

    email = browser.find_element_by_xpath('//input[@name="email"]')
    email.send_keys('simpleemail@asddasd')

    file_input = browser.find_element_by_xpath('//input[@type="file"]')
    file_input.send_keys(file_path)

    btn = browser.find_element_by_xpath('//button[@type="submit"]')
    time.sleep(1)
    btn.click()


finally:
    time.sleep(5)
    browser.quit()