from selenium import webdriver
import time

link = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element_by_xpath("//input[@name='first_name']")
    first_name.send_keys('Ivan')
    last_name = browser.find_element_by_xpath("//input[@name='last_name']")
    last_name.send_keys('Petrov')
    city = browser.find_element_by_xpath("//input[contains(@class,'city')]")
    city.send_keys('Smolensk')
    country = browser.find_element_by_xpath("//*[@id='country']")
    country.send_keys('Russia')
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()


finally:
    time.sleep(10)
    browser.quit()