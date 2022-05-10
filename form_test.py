from selenium import webdriver
import time

link = 'http://suninjuly.github.io/registration2.html'

list = ['First Name', 'Last Name', 'emailsample@gmail.com']
congrat_text = "Congratulations! You have successfully registered!"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element_by_css_selector('.first_block .first')
    first_name.send_keys(list[0])

    last_name = browser.find_element_by_css_selector('.first_block .second')
    last_name.send_keys(list[1])

    mail = browser.find_element_by_css_selector('.first_block .third')
    mail.send_keys(list[2])

    btn = browser.find_element_by_css_selector("[type='submit']")
    btn.click()

    time.sleep(2)

    text_from_page = browser.find_element_by_css_selector('h1')
    welcome_text_from_page = text_from_page.text

    assert congrat_text == welcome_text_from_page


finally:
    time.sleep(5)
    browser.quit()
