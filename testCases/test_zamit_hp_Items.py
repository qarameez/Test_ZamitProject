import allure_pytest
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@pytest.mark.usefixtures("setup")
@allure.severity(allure.severity_level.CRITICAL)

class Test_Dashboard1:
    #
    # def test_footerItem(self):
    #     self.driver.find_element(By.ID, "loginemail").send_keys("jai@yopmail.com")
    #     time.sleep(2)
    #     self.driver.find_element(By.ID, "submit-login").click()
    #     time.sleep(2)
    #
    #     # To singin
    #     self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('qwe123')
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, '//button[@id="submit-login"]').click()
    #     print("Login succesfully")
    #     time.sleep(3)
    #
    #
    #
    @allure.severity(allure.severity_level.MINOR)
    def test_zamit_Logo(self):
        time.sleep(2)
        test_zamit_Logo = self.driver.find_element(By.XPATH,
                                                              "//header/nav[1]/div[1]/div[1]/div[1]/a[1]/img[1]").is_displayed()
        time.sleep(3)
        if test_zamit_Logo == True:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="test_zamit_Logo",attachment_type=AttachmentType.PNG)
            assert False
        print("Passed test_zamit_Logo")

    @allure.severity(allure.severity_level.NORMAL)
    def test_header_facebook(self):
        time.sleep(2)
        test_header_facebook = self.driver.find_element(By.XPATH,
                                                              "//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/i[1]").is_displayed()
        time.sleep(3)
        if test_header_facebook == True:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="test_header_facebook",attachment_type=AttachmentType.PNG)
            assert False
        print("Passed test_header_facebook")

    def test_MenuBar_EngagementActivities(self):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,"//header/nav[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[1]/a[1]")).perform()
        time.sleep(3)
        action.move_to_element(self.driver.find_element(By.XPATH,"//a[contains(text(),'Engagement Activities')]")).click().perform()
        time.sleep(3)
        EngagementActivitiesTitle = self.driver.title
        print(EngagementActivitiesTitle)
        assert EngagementActivitiesTitle in "Zamit | Stream"
        self.driver.save_screenshot(".\\Screenshots\\" + EngagementActivitiesTitle)
        print("Engagement Activities is passed ")
        time.sleep(3)

    def test_MenuBar_championships(self):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//header/nav[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[1]/a[1]")).perform()
        time.sleep(3)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//header/nav[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[1]/ul[1]/li[2]/a[1]")).click().perform()
        time.sleep(3)
        EngagementActivitiesTitle = self.driver.title
        print(EngagementActivitiesTitle)
        assert EngagementActivitiesTitle in "School Championship Programs – Academic Competitions & Challenges"
        print("test_MenuBar_championships is passed ")
        time.sleep(3)

    def test_MenuBar_EnglishLanguage(self):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//header/nav[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[1]/a[1]")).perform()
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
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//header/nav[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[1]/a[1]")).perform()
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
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//header/nav[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[1]/a[1]")).perform()
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
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//header/nav[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[1]/a[1]")).perform()
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
                                                        "//header/nav[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[2]/a[1]")).perform()
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
                                                        "//header/nav[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[2]/a[1]")).perform()
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
                                                        "//header/nav[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[2]/a[1]")).perform()
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
                                                        "//header/nav[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[2]/a[1]")).perform()
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
                                                        "//header/nav[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[2]/a[1]")).perform()
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
                                                        "//header/nav[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[2]/a[1]")).perform()
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
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Marketplace')]").click()
        time.sleep(2)
        Marcketplace = self.driver.title
        assert Marcketplace in "Zamit Marketplace- Zamit Marketplace | India&#x27;s first e-commerce platform created to support the school eco-system."
        self.driver.back()

    def test_SearchIcon(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Search')]").click()
        time.sleep(2)
        Marcketplace = self.driver.title
        assert Marcketplace in "School Admissions 2022-23 | Online Nursery School Admission in PAN India"
        self.driver.back()

    def test_ResourceVault(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Resource Vault')]").click()
        time.sleep(2)
        Marcketplace = self.driver.title
        assert Marcketplace in "Zamit | Login"
        self.driver.back()

    def test_Footer_Curricular(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Co-curriculars')]").click()
        time.sleep(2)
        Marcketplace = self.driver.title
        assert Marcketplace in "Extra Curricular Activities Centres for Kids | Experiential Learning Programs"
        self.driver.back()



    def test_button_Get_your_ZQ_Score(self):
        time.sleep(2)
        Get_your_ZQ_Score = self.driver.find_element(By.XPATH,
                                                              "// a[contains(text(), 'Get your ZQ Score')]").is_displayed()
        time.sleep(3)
        if Get_your_ZQ_Score == True:
            assert True
        else:
            assert False
        print("Passed test_Get_your_ZQ_Score")

    def test_button_CPD_for_Teachers(self):
        time.sleep(2)
        CPD_for_Teachers = self.driver.find_element(By.XPATH,
                                                     "//a[contains(text(),'CPD for Teachers')]").is_displayed()
        time.sleep(3)
        if CPD_for_Teachers == True:
            assert True
        else:
            assert False
        print("Passed test_CPD_for_Teachers")



    def test_appterms_of_use(self):
        time.sleep(2)
        mobile_appterms_of_use = self.driver.find_element(By.XPATH,
                                                      "//a[contains(text(),'Mobile App Terms of Use')]").is_displayed()
        time.sleep(3)
        if mobile_appterms_of_use == True:
            assert True
        else:
            assert False
        print("Passed test_appterms_of_use")

    def test_Website_termsofuse(self):
        time.sleep(2)
        Website_termsofuse = self.driver.find_element(By.XPATH,
                                                      "//a[contains(text(),'Website Terms of Use')]").is_displayed()
        time.sleep(3)
        if Website_termsofuse == True:
            assert True
        else:
            assert False
        print("Passed est_Website_termsofuse")

    def test_refundpolicy(self):
        time.sleep(2)
        test_refundpolicy = self.driver.find_element(By.XPATH,
                                                      "//a[contains(text(),'Refund Policy')]").is_displayed()
        time.sleep(3)
        if test_refundpolicy == True:
            assert True
        else:
            assert False
        print("Passed test_refundpolicy")

    def test_privacy_policy(self):
        time.sleep(2)
        privacy_policy = self.driver.find_element(By.XPATH,
                                                      "//a[contains(text(),'Privacy Policy')]").is_displayed()
        time.sleep(3)
        if privacy_policy == True:
            assert True
        else:
            assert False
        print("Passed test_privacy_policy")

    def test_footer_search_Centres(self):
        time.sleep(2)
        test_footer_search_Centres = self.driver.find_element(By.XPATH,
                                                  "//a[contains(text(),'Centres')]").is_displayed()
        time.sleep(3)
        if test_footer_search_Centres == True:
            assert True
        else:
            assert False
        print("Passed test_footer_search_Centres")

    def test_footer_search_school(self):
        time.sleep(2)
        test_footer_search_school = self.driver.find_element(By.XPATH,
                                                  "//body/section[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[4]/a[1]").is_displayed()
        time.sleep(3)
        if test_footer_search_school == True:
            assert True
        else:
            assert False
        print("Passed test_footer_search_school")



    def test_footer_Engagement_NEWS(self):
        time.sleep(2)
        test_footer_Engagement_NEWS = self.driver.find_element(By.XPATH,
                                                  "//body/section[8]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]").is_displayed()
        time.sleep(3)
        if test_footer_Engagement_NEWS == True:
            assert True
        else:
            assert False
        print("Passed test_footer_Engagement_NEWS")


    def test_footer_Original(self):
        time.sleep(2)
        test_footer_Original = self.driver.find_element(By.XPATH,
                                                  "//body/section[8]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]").is_displayed()
        time.sleep(3)
        if test_footer_Original == True:
            assert True
        else:
            assert False
        print("Passed test_footer_Original")

    def test_footer_AboutUs(self):
        time.sleep(2)
        test_footer_Original = self.driver.find_element(By.XPATH,
                                                        "//a[contains(text(),'About Us')]").is_displayed()
        time.sleep(3)
        if test_footer_Original == True:
            assert True
        else:
            assert False
        print("Passed test_footer_Original")

    def test_footer_ContactUs(self):
        time.sleep(2)
        test_footer_Original = self.driver.find_element(By.XPATH,
                                                        "//a[contains(text(),'Contact Us')]").is_displayed()
        time.sleep(3)
        if test_footer_Original == True:
            assert True
        else:
            assert False
        print("Passed test_footer_Original")