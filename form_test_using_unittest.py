import unittest
from selenium import webdriver

link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'

list = ['First Name', 'Last Name', 'emailsample@gmail.com']
congrat_text = "Congratulations! You have successfully registered!"


def form_test(link):
    browser = webdriver.Chrome()
    browser.get(link)

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

    text_from_page = browser.find_element_by_css_selector('h1')
    return text_from_page.text


class FormTestClass(unittest.TestCase):

    def test_fisrt_form(self):
        actual_text = form_test(link1)
        self.assertEqual(actual_text, congrat_text,
                         f"Expected '{congrat_text}' after successful registation, got {actual_text}")
    def test_second_form(self):
        actual_text = form_test(link2)
        self.assertEqual(actual_text, congrat_text,
                         f"Expected '{congrat_text}' after successful registation, got {actual_text}")


if __name__ == "__main__":
    unittest.main()
