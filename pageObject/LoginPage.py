# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# class LoginPage:
#     # Login Page
#     textbox_username_id = "loginemail"
#     textbox_next_id = "submit-login"
#     textbox_password_id = '//input[@id="password"]'
#     button_login_xpath = '//button[@id="submit-login"]'
#     link_logout_linktext = "Logout"
#
#     def __init__(self,driver):
#         self.driver=driver
#
#
#     def setUserName(self, username):
#         time.sleep(3)
#         self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
#
#     def setNextName(self, nextname):
#         time.sleep(3)
#         self.driver.find_element(By.ID, self.textbox_next_id).send_keys(nextname)
#
#     def setPassword(self, password):
#         time.sleep(3)
#         self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)
#
#     def clickLogin(self):
#         time.sleep(3)
#         self.driver.find_element(By.XPATH,self.button_login_xpath).click()
#
#     def clickLogout(self):
#         self.driver.find_element_by_link_text(self.link_logout_linktext).click()

#######################################################################################
#
# from selenium import webdriver
# import time
# import pytest
# from selenium.webdriver.common.by import By
# from pageObject.LoginPage import LoginPage
#
# class Test_001_Login:
#     baseURL = "https://www.zamit.one/login"
#     username = "shopcluesqa009@gmail.com"
#     password = "qwerty@123"
#     next_id =  "submit-login"
#
#
#     def test_login(self,setup):
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.lp=LoginPage(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.textbox_next_id(self.next_id)
#         self.lp.setPassword(self.password)
#         self.lp.clickLogin()
#         act_title = self.driver.title
#         if act_title == "Junior Dashboard":
#             assert True
#         else:
#             assert False
#         self.driver.close()