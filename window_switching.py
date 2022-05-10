from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    start_button = browser.find_element_by_xpath('//button')
    start_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_xpath('//span[@id="input_value"]')
    y = calc(x.text)

    answer = browser.find_element_by_xpath('//input[@id="answer"]')
    answer.send_keys(y)

    submit_btn = browser.find_element_by_xpath('//button[@type="submit"]')
    submit_btn.click()
finally:
    time.sleep(5)
    browser.quit()