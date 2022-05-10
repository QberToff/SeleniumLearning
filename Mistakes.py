from selenium import webdriver
import time
link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

    # Ваш код, который заполняет обязательные поля
#first_name = browser.find_element_by_xpath('//div/input[@class="form-control first"]')
first_name=browser.find_element_by_class_name('first')
first_name.send_keys("Aleksandr")
time.sleep(2)
#last_name=browser.find_element_by_xpath('//div/input[@class="form-control second"]')
last_name=browser.find_element_by_class_name('second')
last_name.send_keys("Veselov")
time.sleep(2)
email=browser.find_element_by_class_name('third')
#email=browser.find_element_by_xpath('//div/input[@class="form-control third"]')
email.send_keys("amanda@gmail.com")
time.sleep(2)
#phone=browser.find_element_by_css_selector(input.first[placeholder="Input your phone:"])
#phone=browser.find_element_by_xpath('//div/input[@placeholder="Input your phone:"]')
#phone.send_keys("+6235353535")
time.sleep(2)
address=browser.find_element_by_css_selector('input.second[placeholder="Input your address:"]')    
#address=browser.find_element_by_xpath('//div/input[@placeholder="Input your address:"]')
address.send_keys("Bali Ubud")
time.sleep(2)
    
    # Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
time.sleep(1)

    # находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()