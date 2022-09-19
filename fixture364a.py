import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class Testinput():
    @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
    def test_input_time(self, browser, links):
        answer = str(math.log(int(time.time())))
        link = links
        browser.get(link)
        browser.implicitly_wait(5)
        input = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea")
        input.send_keys(answer)
        button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button.click()
        browser.implicitly_wait(5)
        message = browser.find_element(By.CLASS_NAME,"smart-hints__hint")
        check = message.text
        example = 'Correct!'
        assert example == check, "Значения разные"