from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CLASS_NAME, "")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CLASS_NAME, "")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.CLASS_NAME, "")
    input4.send_keys("Russia")
    input5 = browser.find_element(By.CLASS_NAME, "")
    input5.send_keys("Russia")
    button = browser.find_element(By.CLASS_NAME, "")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла