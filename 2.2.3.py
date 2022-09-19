from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID,"num1" )
    y_element = browser.find_element(By.ID,"num2" )
    x1 = x_element.text
    y1 = y_element.text
    x = int(x1)
    y= int(y1)
    z = x + y
    d = str(z)
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(d)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()