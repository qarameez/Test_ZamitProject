from selenium import webdriver
import pytest


@pytest.fixture()
def setup(request):
    request.cls.driver = webdriver.Chrome()
    #request.cls.driver.get("https://www.zamit.one/login")
    #request.cls.driver.get("https://www.zamit.one")   #test_zamit_hp_Item
    request.cls.driver.get("https://zcas.zamit.one/login")
    request.cls.driver.maximize_window()
    yield
    request.cls.driver.close()

