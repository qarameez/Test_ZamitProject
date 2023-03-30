# import allure_pytest
# import allure
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time
# #
# class TestZamit:
# #
# #
# #     def test_logo(self):
# #         self.driver = webdriver.Chrome()
# #         self.driver.maximize_window()
# #         self.driver.get("https://www.zamit.one/login")
# #         logostatus = self.driver.find_element(By.XPATH,"//header/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]").is_displayed()
# #         time.sleep(5)
# #         if logostatus == True:
# #             assert True
# #         else: assert False
# #         self.driver.close()
# #         time.sleep(3)
# #
# #
# #     def test_FBButtonStatus(self):
# #         self.driver = webdriver.Chrome()
# #         self.driver.maximize_window()
# #         self.driver.get("https://www.zamit.one/login")
# #         FBButtonStatus = self.driver.find_element(By.ID,"fb-login").is_displayed()
# #         time.sleep(5)
# #         if FBButtonStatus == True:
# #             assert True
# #         else: assert False
# #         self.driver.close()
# #         time.sleep(3)
# #
# #     def test_GoogleButtonStatus(self):
# #         self.driver = webdriver.Chrome()
# #         self.driver.maximize_window()
# #         self.driver.get("https://www.zamit.one/login")
# #         GoogleButtonStatus = self.driver.find_element(By.ID, "fb-login").is_displayed()
# #         time.sleep(5)
# #         if GoogleButtonStatus == True:
# #             assert True
# #         else:
# #             assert False
# #         self.driver.close()
# #         time.sleep(3)
# #
# #
# #
# #     def test_MenuBar_Item_Activities(self):
# #         self.driver = webdriver.Chrome()
# #         self.driver.maximize_window()
# #         self.driver.get("https://www.zamit.one/login")
# #         self.driver.find_element(By.XPATH,"//header/div[2]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]").click()
# #         activitiesTitle = self.driver.title
# #         print(activitiesTitle)
# #         assert activitiesTitle in "Zamit | Extracurricular and Co-curricular activities for students"
# #         print("Activities is passed ")
# #         time.sleep(4)
# #         self.driver.back()
# #         self.driver.close()
# #
# #     def test_MenuBar_ZamitOriginal(self):
# #         self.driver = webdriver.Chrome()
# #         self.driver.maximize_window()
# #         self.driver.get("https://www.zamit.one/login")
# #         ZamitOriginal = self.driver.find_element(By.XPATH,"//header/div[2]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]").click()
# #         ZamitOriginalTitle = self.driver.title
# #         print(ZamitOriginalTitle)
# #         assert ZamitOriginalTitle in "Zamit | Zamit Originals"
# #         print("Activities is passed ")
# #         time.sleep(4)
# #         self.driver.back()
# #         self.driver.close()
# #
# #     def test_MenuBar_ZamitCompittition(self):
# #         self.driver = webdriver.Chrome()
# #         self.driver.maximize_window()
# #         self.driver.get("https://www.zamit.one/login")
# #         ZamitCompittition = self.driver.find_element(By.XPATH,
# #                                                      "//header/div[2]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
# #         ZamitCompittitionTitle = self.driver.title
# #         print(ZamitCompittitionTitle)
# #         assert ZamitCompittitionTitle in "School Championship Programs – Academic Competitions & Challenges"
# #         print("ZamitCompittition is passed ")
# #         time.sleep(4)
# #         self.driver.back()
# #         self.driver.close()
# #
# #     def test_MenuBar_ZamitMarketPlace(self):
# #         self.driver = webdriver.Chrome()
# #         self.driver.maximize_window()
# #         self.driver.get("https://www.zamit.one/login")
# #         ZamitMarketPlace = self.driver.find_element(By.XPATH, "//a[contains(text(),'Marketplace')]").click()
# #         ZamitMarketPlaceTitle = self.driver.title
# #         print(ZamitMarketPlaceTitle)
# #         assert ZamitMarketPlaceTitle in "Zamit Marketplace- Zamit Marketplace | India&#x27;s first e-commerce platform created to support the school eco-system."
# #         print("ZamitMarketPlace is passed ")
# #         time.sleep(4)
# #         self.driver.back()
# #         self.driver.close()
# #
# #     def test_MenuBar_ZamitNews(self):
# #         self.driver = webdriver.Chrome()
# #         self.driver.maximize_window()
# #         self.driver.get("https://www.zamit.one/login")
# #         ZamitNews = self.driver.find_element(By.XPATH,
# #                                              "//header/div[2]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]").click()
# #         ZamitNewsTitle = self.driver.title
# #         print(ZamitNewsTitle)
# #         assert ZamitNewsTitle in "Zamit | News"
# #         print("ZamitNews is passed ")
# #         time.sleep(4)
# #         self.driver.back()
# #         self.driver.close()
# #
# #     def test_MenuBar_ZamitStream(self):
# #         self.driver = webdriver.Chrome()
# #         self.driver.maximize_window()
# #         self.driver.get("https://www.zamit.one/login")
# #         ZamitStream = self.driver.find_element(By.XPATH,
# #                                                "//a[contains(text(),'Stream')]").click()
# #         ZamitStreamTitle = self.driver.title
# #         print(ZamitStreamTitle)
# #         assert ZamitStreamTitle in "Zamit | Stream<"
# #         print("ZamitStream is passed ")
# #         time.sleep(4)
# #         self.driver.back()
# #         self.driver.close()
# #
# #     def test_MenuBar_ZamitZQ(self):
# #         self.driver = webdriver.Chrome()
# #         self.driver.maximize_window()
# #         self.driver.get("https://www.zamit.one/login")
# #         ZamitZQ = self.driver.find_element(By.XPATH,
# #                                            "//a[contains(text(),'ZQ')]").click()
# #         time.sleep(5)
# #         ZamitZQTitle = self.driver.title
# #         print(ZamitZQTitle)
# #         assert ZamitZQTitle in "Zamit | ZQ"
# #         print("ZamitZQ is passed ")
# #         time.sleep(4)
# #         self.driver.back()
# #         self.driver.close()
# #
# #
# #     def test_MenuBar_ZamitLoginButton(self):
# #         self.driver = webdriver.Chrome()
# #         self.driver.maximize_window()
# #         self.driver.get("https://www.zamit.one/login")
# #         ZamitLogin = self.driver.find_element(By.XPATH,
# #                                              "//header/div[2]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[8]/a[1]").is_displayed()
# #         time.sleep(3)
# #         if ZamitLogin == True:
# #             assert True
# #         else:
# #             assert False
# #         self.driver.close()
# #         time.sleep(3)
#
#
#     def test_Valid_login(self):
#
#         # Login to zamit
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://www.zamit.one/login")
#         self.driver.find_element(By.ID, "loginemail").send_keys("shopcluesqa009@gmail.com")
#         time.sleep(2)
#         self.driver.find_element(By.ID, "submit-login").click()
#         time.sleep(2)
#
#         # To singin
#         self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('qwerty@123')
#         time.sleep(2)
#         self.driver.find_element(By.XPATH, '//button[@id="submit-login"]').click()
#         print("Login succesfully")
#         time.sleep(3)
#         self.driver.close()
#
#     # def test_Invalid_login(self):
#     #
#     #     # Login to zamit
#     #     self.driver = webdriver.Chrome()
#     #     self.driver.maximize_window()
#     #     self.driver.get("https://www.zamit.one/login")
#     #     self.driver.find_element(By.ID, "loginemail").send_keys("shopcluesqa009@gmail.com")
#     #     time.sleep(2)
#     #     self.driver.find_element(By.ID, "submit-login").click()
#     #     time.sleep(2)
#     #
#     #     # To singin
#     #     self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('qwerty@1233')
#     #     time.sleep(2)
#     #     self.driver.find_element(By.XPATH, '//button[@id="submit-login"]').click()
#     #     ZamitLoginid = self.driver.find_element(By.XPATH,"//p[@id='login_error']").is_displayed()
#     #     time.sleep(3)
#     #     if ZamitLoginid == True:
#     #         assert True
#     #     else:
#     #         assert False
#     #     self.driver.close()
#     #     time.sleep(3)
#     #     print("Pass")
#     #
#     #     time.sleep(3)
#     #     self.driver.close()
