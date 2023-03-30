# import allure_pytest
# import allure
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time
#
# class TestZAMIT:
#     def test_logo(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://www.zamit.one/login")
#         logostatus = self.driver.find_element(By.XPATH,"//header/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]").is_displayed()
#         time.sleep(5)
#         if logostatus == True:
#             assert True
#         else: assert False
#         self.driver.close()
#
#     def test_FBButtonStatus(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://www.zamit.one/login")
#         FBButtonStatus = self.driver.find_element(By.ID,"fb-login").is_displayed()
#         time.sleep(5)
#         if FBButtonStatus == True:
#             assert True
#         else: assert False
#         self.driver.close()
#
#     def test_GoogleButtonStatus(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://www.zamit.one/login")
#         GoogleButtonStatus = self.driver.find_element(By.ID, "fb-login").is_displayed()
#         time.sleep(5)
#         if GoogleButtonStatus == True:
#             assert True
#         else:
#             assert False
#         self.driver.close()
#
#
#
#
#
#
#
