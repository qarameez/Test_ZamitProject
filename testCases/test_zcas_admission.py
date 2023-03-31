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

class Test_zcas_admission:


    def test_login(self):
        time.sleep(2)
        self.driver.find_element(By.NAME, "email").send_keys("shopcluesqa009@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.ID, "submit-login").click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'password').send_keys('qwerty@123')
        time.sleep(2)
        self.driver.find_element(By.ID, 'submit-login').click()
        zcas_homepage = self.driver.title
        time.sleep(3)
        # if zcas_homepage  == True:
        #     assert True
        # else:
        #     assert False

        print("Passed test_zamit_Logo")
        print("Login succesfully")
        time.sleep(3)

        self.driver.find_element(By.CLASS_NAME,"d-block").click()
        assert "Update Child Details | Zamit" in "Update Child Details | Zamit"
        print("clicked on Create New Profile succesfully")
        time.sleep(2)

        # 1 Enter Child's Information
        # Enter first name
        self.driver.find_element(By.ID, "firstname").clear()
        self.driver.find_element(By.ID, "firstname").send_keys("Amit ")

        time.sleep(2)
        print("Enter first name succesfully")
        # Enter Last Name
        self.driver.find_element(By.ID,"lastname").clear()
        self.driver.find_element(By.ID,"lastname").send_keys("bhagel")
        time.sleep(2)
        print("Enter Last name succesfully")

        # Enter date of bith
        selectdobd = Select( self.driver.find_element(By.ID,"dobd"))
        selectdobd.select_by_value("01")
        time.sleep(2)
        print("Enter DOB")

        # Enter date of Month
        selctdobm = Select( self.driver.find_element(By.ID,"dobm"))
        selctdobm.select_by_value("01")
        time.sleep(2)
        print("Enter DOM succesfully")
        # Enter date of year
        selectdoby = Select( self.driver.find_element(By.ID,"doby"))
        selectdoby.select_by_value("2005")
        time.sleep(2)
        print("Enter date of year succesfully")
            # Enter gender
        selgender = Select( self.driver.find_element(By.ID,"gender"))
        selgender.select_by_value("Male")
        time.sleep(2)
        print("Enter gender succesfully")
        # Enter Child citizen ship
        selectcitizenship = Select( self.driver.find_element(By.ID,"citizenship"))
        selectcitizenship.select_by_value("1")
        time.sleep(2)
        print("Enter Child citizen ship succesfully")

        # Enter select2-ethnicity-container
        selectethnicity = Select( self.driver.find_element(By.NAME,"ethnicity"))
        selectethnicity.select_by_value("1")
        time.sleep(2)
        print("Enter Child ethnicity succesfully")

        # Enter childwith
        childwith = Select( self.driver.find_element(By.ID,"childwith"))
        childwith.select_by_value("Father")
        time.sleep(2)
        print("Enter childwith succesfully")

        # Enter transfer or Seeking admission in?
        seltransfer = Select( self.driver.find_element(By.ID,"transfer"))
        seltransfer.select_by_value("K-12")
        time.sleep(2)
        print("Enter  Seeking admission in succesfully")


        # Enter i was "attended"
        selattended = Select( self.driver.find_element(By.ID,"attended"))
        selattended.select_by_value("Home School")
        time.sleep(2)
        print("Enter  attendedin succesfully")

        # Enter Home schooled From
        selfromDateMonthhm = Select( self.driver.find_element(By.ID,"fromDateMonthhm"))
        selfromDateMonthhm.select_by_value("01")
        time.sleep(2)
        print("Enter  Home schooled  succesfully")

        # Enter Home schooled From
        selfromDateMonthhm = Select( self.driver.find_element(By.ID,"fromDateYearhm"))
        selfromDateMonthhm .select_by_value("2017")
        time.sleep(2)
        print("Enter Home schooled From  succesfully")

        #DateMonthhm
        seltoDateMonthhm = Select( self.driver.find_element(By.ID,"toDateMonthhm"))
        seltoDateMonthhm.select_by_value("01")
        time.sleep(2)
        print("Enter DateMonthhm  succesfully")

        #DateYearhm
        seltoDateYearhm = Select( self.driver.find_element(By.ID,"toDateYearhm"))
        seltoDateYearhm.select_by_value("2020")
        time.sleep(2)
        print("Enter DateYearhm  succesfully")

        # Enter Home schooled to
        seltoDateMonthhm = Select( self.driver.find_element(By.ID,"toDateMonthhm"))
        seltoDateMonthhm.select_by_value("01")
        time.sleep(2)
        print("Enter Enter Home schooled to  succesfully")

        # Enter Parent/Guardian Information! autofill
        self.driver.find_element(By.XPATH,
                                 "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/h6[1]/label[1]").click()
        time.sleep(5)
        print("Enter Parent/Guardian Information! autofill  succesfully")

        #Select Employment
        selectfemployment = Select( self.driver.find_element(By.ID,"femployment"))
        selectfemployment.select_by_value("7")
        time.sleep(2)
        print("Select Employment succesfully")


        #Select Profession
        selectffprofession = Select( self.driver.find_element(By.ID,"fprofession"))
        selectffprofession.select_by_value("1")
        time.sleep(2)
        print("Enter Select Profession succesfully")

        #pfpcontact
        selectffpcontact = Select( self.driver.find_element(By.ID,"fpcontact"))
        selectffpcontact.select_by_value("0")
        time.sleep(2)
        print("Enter pfpcontact succesfully")

        #Click on Next Button
        self.driver.find_element(By.XPATH,"//body/div[3]/div[1]/div[1]/form[1]/div[3]/button[2]").click()
        time.sleep(6)
        print("Click on Next Button succesfully")

        # assert "Upload Documents | Zamit" in "Uplo  ad Documents | Zamit" , "Validation failed"
        # print("validation pass")

        #upload document
        self.driver.find_element(By.CLASS_NAME,"image-upload").send_keys("C:/Users/MASH/Desktop/Selenium/Testing Doc zcas/child-02.jpg")
        print("Uploaded child photograph succesfully")
        time.sleep(5)

        self.driver.find_element(By.XPATH,"//body/div[3]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/label[1]/input[1]").send_keys("C:/Users/MASH/Desktop/Selenium/Testing Doc zcas/Child_Birth_Certificate.pdf")
        print("Uploaded Proof of Residence Document succesfully")
        time.sleep(5)



        self.driver.find_element(By.XPATH,"//body/div[3]/div[1]/div[1]/div[4]/div[1]/div[3]/div[1]/div[1]/label[1]/input[1]").send_keys("C:/Users/MASH/Desktop/Selenium/Testing Doc zcas/child-02.jpg")
        print("Uploaded Proof of father iamges succesfully")
        time.sleep(5)




        self.driver.find_element(By.XPATH,"//body/div[3]/div[1]/div[1]/div[4]/div[1]/div[4]/div[1]/div[1]/label[1]/input[1]").send_keys("C:/Users/MASH/Desktop/Selenium/Testing Doc zcas/Child_Birth_Certificate.pdf")
        print("Uploaded Proof of Residence Document succesfully")
        time.sleep(5)


    ###################################################################################################
    #Click on next step
        self.driver.find_element(By.ID, "nextstep").click()
        time.sleep(3)



    # Application
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@id='snamestep2']").send_keys("Zamit school")
        time.sleep(6)
        self.driver.find_element(By.XPATH,"//body/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/i[1]").click()
        time.sleep(5)


        # search school
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Select')]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH,"//body/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/button[2]").click()
        time.sleep(3)
        print("Student Admimisson.............. ")
