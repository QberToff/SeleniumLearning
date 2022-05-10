from selenium import webdriver
import time

link = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_css_selector("form input")
    for el in elements:
        el.send_keys('F')
    button = browser.find_element_by_css_selector(".btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()