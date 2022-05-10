from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/get_attribute.html'

def calculate(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element_by_css_selector("img[id='treasure']")
    x_value = chest.get_attribute('valuex')
    y = calculate(x_value)

    input = browser.find_element_by_css_selector("input[id='answer']")
    input.send_keys(y)

    checkbox = browser.find_element_by_css_selector("input[type='checkbox']")
    checkbox.click()

    robot_radiobutton = browser.find_element_by_css_selector("input[id='robotsRule']")
    robot_radiobutton.click()

    submit_button = browser.find_element_by_css_selector("button[type='submit']")
    submit_button.click()


finally:
    time.sleep(5)
    browser.quit()