import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
import time
import math

message = ''

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    global message
    print(message)
    browser.quit()

@pytest.mark.parametrize('pages', ['236895','236896','236897','236898','236899','236903','236904','236905'])
def test_for_answer_form(browser, pages):
    global message
    link = f"https://stepik.org/lesson/{pages}/step/1"
    print (f"open link {pages}")
    browser.get(link)
    print('trying to find textarea')
    browser.implicitly_wait(5)
    textarea = browser.find_element(By.XPATH, "//textarea")
    print('textarea was found')
    textarea.send_keys(str(math.log(int(time.time() + 1.4))))
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()
    hint = WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='smart-hints__hint']")))
    correct_message = "Correct!"
    assert hint.text != correct_message
    message += hint.text