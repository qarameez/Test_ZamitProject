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

    def test_logo(self):
        logostatus = self.driver.find_element(By.XPATH,
                                          "//header/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]").is_displayed()
        time.sleep(5)
        if logostatus == True:
            assert True
        else:
            assert False
        time.sleep(3)

    def test_FBButtonStatus(self):
        FBButtonStatus = self.driver.find_element(By.ID, "fb-login").is_displayed()
        time.sleep(5)
        if FBButtonStatus == True:
            assert True
        else:
            assert False

        time.sleep(3)

    def test_GoogleButtonStatus(self):
        GoogleButtonStatus = self.driver.find_element(By.ID, "fb-login").is_displayed()
        time.sleep(5)
        if GoogleButtonStatus == True:
            assert True
        else:
            assert False
        time.sleep(3)

    def test_MenuBar_EngagementActivities(self):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,"//a[contains(text(),'Students')]")).perform()
        time.sleep(3)
        action.move_to_element(self.driver.find_element(By.XPATH,"//a[contains(text(),'Engagement Activities')]")).click().perform()
        time.sleep(3)
        EngagementActivitiesTitle = self.driver.title
        print(EngagementActivitiesTitle)
        assert EngagementActivitiesTitle in "Zamit | Stream"
        print("Engagement Activities is passed ")
        time.sleep(3)

    def test_MenuBar_championships(self):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,"//a[contains(text(),'Students')]")).perform()
        time.sleep(3)
        action.move_to_element(self.driver.find_element(By.XPATH,"//header/div[2]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[1]/ul[1]/li[2]/a[1]")).click().perform()
        time.sleep(3)
        EngagementActivitiesTitle = self.driver.title
        print(EngagementActivitiesTitle)
        assert EngagementActivitiesTitle in "School Championship Programs – Academic Competitions & Challenges"
        print("test_MenuBar_championships is passed ")
        time.sleep(3)

    def test_MenuBar_EnglishLanguage(self):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//a[contains(text(),'Students')]")).perform()
        time.sleep(3)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//a[contains(text(),'English Language')]")).click().perform()
        time.sleep(3)
        EnglishLanguageTitle = self.driver.title
        print(EnglishLanguageTitle)
        assert EnglishLanguageTitle in "Zamit | International English Language Certification mapped to CEFR"
        print("test_MenuBar_championships is passed ")
        time.sleep(3)

    def test_MenuBar_Internship(self):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//a[contains(text(),'Students')]")).perform()
        time.sleep(3)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//a[contains(text(),'Internship')]")).click().perform()
        time.sleep(3)
        InternshipTitle = self.driver.title
        print(InternshipTitle)
        assert InternshipTitle in "Zamit | Internships for students"
        print("InternshipTitle is passed ")
        time.sleep(3)

    def test_MenuBar_Portfolio(self):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//a[contains(text(),'Students')]")).perform()
        time.sleep(3)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//a[contains(text(),'Portfolio')]")).click().perform()
        time.sleep(3)
        PortfolioTitle = self.driver.title
        print(PortfolioTitle)
        assert PortfolioTitle in "Zamit | Student’s Portfolio of Academic and Non-academic Achievements"
        print("PortfolioTitle is passed ")
        time.sleep(3)


    def test_MenuBar_Analysis(self):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//a[contains(text(),'Students')]")).perform()
        time.sleep(3)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//a[contains(text(),'ZQ Analysis')]")).click().perform()
        time.sleep(3)
        AnalysisTitle = self.driver.title
        print(AnalysisTitle)
        assert AnalysisTitle in "Zamit | Measure and Analyse Student’s Future Readiness with ZQ"
        print("AnalysisTitle is passed ")
        time.sleep(3)

    def test_MenuBar_Teacher(self):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//header/div[2]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]")).perform()
        time.sleep(3)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//a[contains(text(),'CPD Programmes')]")).click().perform()
        time.sleep(3)
        CPDProgrammesTitle = self.driver.title
        print(CPDProgrammesTitle)
        assert CPDProgrammesTitle in "Zamit | Continuous Professional Development for Teachers (CPD)"
        print("CPDProgrammesTitle is passed ")
        time.sleep(3)

    def test_MenuBar_Professional(self):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//header/div[2]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]")).perform()
        time.sleep(3)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//a[contains(text(),'Professional Profile')]")).click().perform()
        time.sleep(3)
        ProfessionalTitle = self.driver.title
        print(ProfessionalTitle)
        assert ProfessionalTitle in "Zamit | Portfolio of Academic and Professional Achievements for Teachers"
        print("ProfessionalTitle is passed ")
        time.sleep(3)



    def test_MenuBar_ResearchGrant(self):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//header/div[2]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]")).perform()
        time.sleep(3)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//a[contains(text(),'Research Grant')]")).click().perform()
        time.sleep(3)
        ResearchGrantTitle = self.driver.title
        print(ResearchGrantTitle)
        assert ResearchGrantTitle in "Zamit | Research grants for teachers for future readiness of students"
        print("ResearchGrantTitle is passed ")
        time.sleep(3)

    def test_MenuBar_TeachingResources(self):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//header/div[2]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]")).perform()
        time.sleep(3)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//a[contains(text(),'Teaching Resources')]")).click().perform()
        time.sleep(3)
        TeachingResourcesTitle = self.driver.title
        print(TeachingResourcesTitle)
        assert TeachingResourcesTitle in "Zamit | Teaching resources to enhance teaching and management skills"
        print("TeachingResourcesTitle is passed ")
        time.sleep(3)

    def test_MenuBar_TERMAnalysis(self):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//header/div[2]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]")).perform()
        time.sleep(3)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//a[contains(text(),'TERM Analysis')]")).click().perform()
        time.sleep(3)
        TermAnalysisTitle = self.driver.title
        print(TermAnalysisTitle)
        assert TermAnalysisTitle in "Zamit | Teaching Excellence and Relevance Management (TERM) analysis across 85+ parameters"
        print("TermAnalysisTitle is passed ")
        time.sleep(3)

    def test_MenuBar_Webinars(self):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//header/div[2]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]")).perform()
        time.sleep(3)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//header/div[2]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[2]/ul[1]/li[6]/a[1]")).click().perform()
        time.sleep(3)
        WebinarsTitle = self.driver.title
        print(WebinarsTitle)
        assert WebinarsTitle in "Zamit | Zamit Originals"
        print("WebinarsTitle is passed ")
        time.sleep(3)

    def test_Marcketplace(self):
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Marketplace')]").click()
        time.sleep(2)
        Marcketplace= self.driver.title
        assert Marcketplace in "Zamit Marketplace- Zamit Marketplace | India&#x27;s first e-commerce platform created to support the school eco-system."
        self.driver.back()

    def test_SearchIcon(self):
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Search')]").click()
        time.sleep(2)
        Marcketplace= self.driver.title
        assert Marcketplace in "School Admissions 2022-23 | Online Nursery School Admission in PAN India"
        self.driver.back()

    def test_ResourceVault(self):
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Resource Vault')]").click()
        time.sleep(2)
        Marcketplace= self.driver.title
        assert Marcketplace in "Zamit | Login"
        self.driver.back()

    def test_Footer_Curricular(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Co-curriculars')]").click()
        time.sleep(2)
        Marcketplace = self.driver.title
        assert Marcketplace in "Extra Curricular Activities Centres for Kids | Experiential Learning Programs"
        self.driver.back()

    def test_Footer_AboutUs(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'About Us')]").click()
        time.sleep(2)
        Marcketplace = self.driver.title
        assert Marcketplace in "Zamit | About Us"
        self.driver.back()


    def test_Valid_login(self,setup):
        self.driver.find_element(By.ID, "loginemail").send_keys("shopcluesqa009@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.ID, "submit-login").click()
        time.sleep(2)

        # To singin
        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('qwerty@123')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//button[@id="submit-login"]').click()
        print("Login succesfully")
        time.sleep(3)


    def test_DashboardItem(self,setup):
        self.driver.find_element(By.ID, "loginemail").send_keys("shopcluesqa009@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.ID, "submit-login").click()
        time.sleep(2)

        # To singin
        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('qwerty@123')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//button[@id="submit-login"]').click()
        print("Login succesfully")
        time.sleep(3)

        #click on View Previous Report
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View Previous Report')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[@id='zq_report']/div[1]/div[1]/div[1]/button[1]").click()
        time.sleep(2)

        # click on Resume button
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Resume')]").click()
        time.sleep(2)
        self.driver.back()

        #General English Certification
        # click on About Button
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[@id='home-diagnostic-tiles']/div[1]/div[2]/div[1]/div[2]/a[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[@id='home-diagnostic-tiles']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
        time.sleep(2)

        # click on Let's Begin Button

        self.driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[@id='home-diagnostic-tiles']/div[1]/div[2]/div[1]/div[2]/a[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[@id='home-diagnostic-tiles']/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]").click()
        time.sleep(2)


        # Content-Based Language Certification

        # About
        self.driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[@id='home-diagnostic-tiles']/div[1]/div[4]/div[1]/div[2]/a[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[@id='home-diagnostic-tiles']/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
        time.sleep(2)


        # Lets Begin
        self.driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[@id='home-diagnostic-tiles']/div[1]/div[4]/div[1]/div[2]/a[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[@id='home-diagnostic-tiles']/div[1]/div[5]/div[1]/div[1]/div[1]/button[1]").click()
        time.sleep(2)


        #Workshops & Webinars
        #
        self.driver.find_element(By.XPATH,"//a[contains(text(),'View & Enrol')]").click()
        time.sleep(2)
        Workshops_Webinars = self.driver.title
        assert Workshops_Webinars in "Zamit | Zamit Originals"
        time.sleep(3)
        self.driver.back()

        # Archieve button
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Archive')]").click()
        # time.sleep(2)
        # Workshops_Archievebutton = self.driver.title
        # assert Workshops_Archievebutton in "Webinar Archive &#8211; Zamit Dashboard"
        time.sleep(2)
        self.driver.back()


        #Competitions & Championships
        self.driver.find_element(By.XPATH,"//a[contains(text(),'View Schedule & Enrol')]").click()
        time.sleep(2)
        Workshops_Championshipsbutton = self.driver.title
        assert Workshops_Championshipsbutton  in "School Championship Programs – Academic Competitions & Challenges"
        time.sleep(2)
        self.driver.back()

        # Book an Appointment
        Option_BookanAppointment = self.driver.find_element(By.XPATH,"//a[contains(text(),'Book an Appointment')]").is_displayed()
        time.sleep(5)
        if Option_BookanAppointment == True:
            assert True
        else:
            assert False

        # Book an Appointment
        Option_Marketplace = self.driver.find_element(By.XPATH,
                                                                "//a[contains(text(),'Browse Marketplace')]").is_displayed()
        time.sleep(5)
        if Option_Marketplace == True:
            assert True
        else:
                assert False


          # Click on Zamit Homepage Icon

        self.driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]").click()






















