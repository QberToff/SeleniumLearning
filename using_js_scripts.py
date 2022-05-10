from selenium import webdriver
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"

def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_xpath("//span[@id='input_value']")
    x_value = x.text
    y = calc(x_value)

    answer = browser.find_element_by_xpath("//input[@id='answer']")
    answer.send_keys(y)

    checkbox = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    checkbox.click()

    radio = browser.find_element_by_xpath("//input[@id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
