import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

answer = str(math.log(int(time.time())))
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class Testinput():
    @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
    def test_input_time(self, browser, link):
        browser.implicitly_wait(10)
        input1 = browser.find_element(By.ID, "ember90")
        input1.send_keys(answer)
