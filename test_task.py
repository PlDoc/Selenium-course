import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]//div[@class="form-group first_class"]//*[@class="form-control first"]')
        input1.send_keys("Biba")
        input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//div[@class="form-group second_class"]//*[@class="form-control second"]')
        input2.send_keys("Bobov")
        input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]//div[@class="form-group third_class"]//*[@class="form-control third"]')
        input3.send_keys("dolboeb@mail.ru")
        button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
        button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "doesnt match")

    def test_abs2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]//div[@class="form-group first_class"]//*[@class="form-control first"]')
        input1.send_keys("Biba")
        input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//div[@class="form-group second_class"]//*[@class="form-control second"]')
        input2.send_keys("Bobov")
        input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]//div[@class="form-group third_class"]//*[@class="form-control third"]')
        input3.send_keys("dolboeb@mail.ru")
        button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
        button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "doesnt match")

if __name__ == "__main__":
    unittest.main()