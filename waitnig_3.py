from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from calculation import calc

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser =  webdriver.Chrome()

try:
    browser.get(link)
    hold = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH,'//*[@id="price"]'),"$100"))
    book = browser.find_element_by_xpath('//*[@id="book"]')
    book.click()

    x = browser.find_element_by_xpath('//*[@id="input_value"]')
    y = calc(x.text)

    input = browser.find_element_by_xpath('//*[@id="answer"]')
    input.send_keys(y)

    submit_btn = browser.find_element_by_xpath('//*[@type="submit"]')
    submit_btn.click()

finally:
    time.sleep(20)
    browser.quit()


