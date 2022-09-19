import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    browser = webdriver.Chrome()
    yield browser
    print(":3", "\n")
    browser.quit()

@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")
    def test_second_smiling_faces(self, prepare_faces):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")