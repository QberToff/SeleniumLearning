from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/math.html'

def calculate(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector("[id='input_value']")
    x_value = x.text
    y = calculate(x_value)

    input = browser.find_element_by_css_selector('input[required]')
    input.send_keys(y)

    checkbox = browser.find_element_by_css_selector("input[type='checkbox']")
    checkbox.click()

    robot_radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
    robot_radiobutton.click()

    submit_button = browser.find_element_by_css_selector("button[type='submit']")
    submit_button.click()


finally:
    time.sleep(5)
    browser.quit()