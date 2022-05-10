from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element_by_xpath("//h2/span[@id='num1']")
    num1 = int(num1_element.text)

    num2_element = browser.find_element_by_xpath("//h2/span[@id='num2']")
    num2 = int(num2_element.text)
    result = num1 + num2

    select = Select(browser.find_element_by_xpath("//select"))
    select.select_by_value(str(result))

    btn = browser.find_element_by_xpath("//button")
    btn.click()


finally:
    time.sleep(5)
    browser.quit()