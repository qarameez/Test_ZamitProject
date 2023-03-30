import allure_pytest
import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
@pytest.mark.usefixtures("setup")

class TestZamit:

    def test_Package_is_not_Activated(self):
        self.driver.find_element(By.ID, "loginemail").send_keys("zamit_user4@yopmail.com")
        time.sleep(2)
        self.driver.find_element(By.ID, "submit-login").click()
        time.sleep(2)

        # To singin
        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('zamit124')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//button[@id="submit-login"]').click()
        print("Login succesfully")
        time.sleep(3)

        dashboard = self.driver.find_element(By.XPATH, "//div[@id='btnPopClose']").is_displayed()
        time.sleep(3)
        if dashboard == True:
            assert True
        else:
            assert False
