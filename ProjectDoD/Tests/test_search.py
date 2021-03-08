from selenium import webdriver
from ProjectDoD.Pages.SearchPage import searchPage
import time
import unittest

#This class contains the test methods to the search functionality
class searchTest(unittest.TestCase):

    #setUp is a class method that will run before every test
    @classmethod
    def setUp(self):
        # self.PATH = "C:\Program Files (x86)\geckodriver.exe"
        self.PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    # This method tests a general search without filters
    def test_search_all(self):
        driver = self.driver
        driver.get("https://dodgrantawards.dtic.mil/grants/index.html#/advancedSearch")
        driver.implicitly_wait(10)
        search = searchPage(driver)
        # you can comment the next line out if the webpage link works without issues
        search.cert_err_bypass()
        search.search()
        time.sleep(5)
        search.clear_search()
        time.sleep(5)

    # This method tests the search functionality for fiscal year 2016
    def test_search_2016fy(self):
        driver = self.driver
        driver.get("https://dodgrantawards.dtic.mil/grants/index.html#/advancedSearch")
        driver.implicitly_wait(10)
        search = searchPage(driver)
        search.cert_err_bypass()
        search.search_fy2016()
        search.search()
        time.sleep(5)
        search.clear_search()
        time.sleep(5)

    # This method tests the search functionality using project title
    def test_search_by_project_title(self):
        title = "Asian Conference On Machine learning 2016"
        driver = self.driver
        driver.get("https://dodgrantawards.dtic.mil/grants/index.html#/advancedSearch")
        driver.implicitly_wait(10)
        search = searchPage(driver)
        search.cert_err_bypass()
        search.search_by_project_title(title)
        search.search()
        time.sleep(5)
        search.clear_search()
        time.sleep(5)

    #This method tests the search functionality using potential period of performance start date
    def test_search_by_effort_starting_date(self):
        from_date = "06/24/2016"
        to_date = "14/02/2016"
        driver = self.driver
        driver.get("https://dodgrantawards.dtic.mil/grants/index.html#/advancedSearch")
        driver.implicitly_wait(10)
        search = searchPage(driver)
        search.cert_err_bypass()
        search.search_by_effort_starting_date(from_date)
        search.search_by_effort_startingDate_to(to_date)
        search.search()
        time.sleep(5)
        search.clear_search()
        time.sleep(5)
    # This method tests the search functionality using the award number
    def test_search_by_award_number(self):
        award_num= "FA23861610004"
        driver = self.driver
        driver.get("https://dodgrantawards.dtic.mil/grants/index.html#/advancedSearch")
        driver.implicitly_wait(10)
        search = searchPage(driver)
        search.cert_err_bypass()
        search.search_by_award_number(award_num)
        search.search()
        time.sleep(5)
        search.clear_search()
        time.sleep(5)

    # This method tests the search functionality using investigator or manager name
    def test_search_by_poc(self):
        poc = "Investigator X"
        driver = self.driver
        driver.get("https://dodgrantawards.dtic.mil/grants/index.html#/advancedSearch")
        driver.implicitly_wait(10)
        search = searchPage(driver)
        search.cert_err_bypass()
        search.search_by_investigator_or_director_name(poc)
        search.search()
        time.sleep(5)
        search.clear_search()
        time.sleep(5)

    # This method tests the search functionality using recipient organization name
    def test_search_by_org_name(self):
        org_name = "Organization X"
        driver = self.driver
        driver.get("https://dodgrantawards.dtic.mil/grants/index.html#/advancedSearch")
        driver.implicitly_wait(10)
        search = searchPage(driver)
        search.cert_err_bypass()
        search.search_by_recipient_org(org_name)
        search.search()
        time.sleep(5)
        search.clear_search()
        time.sleep(5)

    # This method tests the search functionality using the minimum and maximum grant amount
    def test_search_by_award_amount(self):
        min_amount = "100000"
        max_amount = "200000"
        driver = self.driver
        driver.get("https://dodgrantawards.dtic.mil/grants/index.html#/advancedSearch")
        driver.implicitly_wait(10)
        search = searchPage(driver)
        search.cert_err_bypass()
        search.search_by_max_and_min_amount(min_amount, max_amount)
        search.search()
        time.sleep(5)
        search.clear_search()
        time.sleep(5)

    # This method tests the search functionality using the DoD Awarding Office
    def test_search_by_awarding_office(self):
        driver = self.driver
        driver.get("https://dodgrantawards.dtic.mil/grants/index.html#/advancedSearch")
        driver.implicitly_wait(10)
        search = searchPage(driver)
        search.cert_err_bypass()
        search.search_by_dod_awarding_office()
        search.search()
        time.sleep(5)
        search.clear_search()
        time.sleep(5)

    # This method tests the search functionality using the Funding Agency
    def test_search_by_funding_agency(self):
        driver = self.driver
        driver.get("https://dodgrantawards.dtic.mil/grants/index.html#/advancedSearch")
        driver.implicitly_wait(10)
        search = searchPage(driver)
        search.cert_err_bypass()
        search.search_funding_agency()
        search.search()
        time.sleep(5)
        search.clear_search()
        time.sleep(5)

    # This method closes the browser after the test is done
    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
