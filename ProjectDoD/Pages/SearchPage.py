from selenium.webdriver.support.select import Select
from ProjectDoD.Locators.locators import Locators
import datetime

#This class contains all the objects insite the search page
#The methods inside this class will be used to construct test cases
class searchPage(Locators):

    def __init__(self, driver):
        self.driver = driver

        self.search_method_id         = Locators.search_method_id
        self.award_number_id          = Locators.award_number_id
        self.fiscal_year_id           = Locators.fiscal_year_id
        self.fiscalYear_2016_value    = Locators.fiscalYear_2016_value
        self.effort_from_date_id      = Locators.effort_from_date_id
        self.effort_to_date_id        = Locators.effort_to_date_id
        self.investigator_director_id = Locators.investigator_director_id
        self.recipient_org_id         = Locators.recipient_org_id
        self.amount_min_id            = Locators.amount_min_id
        self.amount_max_id            = Locators.amount_max_id
        self.awarding_office_id          = Locators.awarding_office_id
        self.DARPA_office_value       = Locators.DARPA_office_value
        self.NSA_funding_office_value = Locators.NSA_funding_office_value
        self.funding_agencies_id      = Locators.funding_agencies_id
        self.search_button_id         = Locators.search_button_id
        self.clear_button_id          = Locators.clear_button_id

    #This method displayes all available records
    def search(self):
        self.driver.find_element_by_id(Locators.search_button_id).click()

    #search_fy2016 selects the fiscal year 2016
    def search_fy2016(self):
        select_2016 = Select(self.driver.find_element_by_id(Locators.fiscal_year_id))
        select_2016.select_by_visible_text(Locators.fiscalYear_2016_value)

    #search_by_project_title clears the project title input field and inputs the argument projects_title
    def search_by_project_title(self, project_title):
        self.driver.find_element_by_id(Locators.search_method_id).clear()
        self.driver.find_element_by_id(Locators.search_method_id).send_keys(project_title)

    # search_by_award_number clears the award number input field and inputs the argument award_num
    def search_by_award_number(self, award_num):
        self.driver.find_element_by_id(Locators.award_number_id).clear()
        self.driver.find_element_by_id(Locators.award_number_id).send_keys(award_num)

    # search_by_effort_starting_date clears the starting date input field and inputs the argument from_date
    def search_by_effort_starting_date(self, from_date):

        self.driver.find_element_by_id(Locators.effort_from_date_id).clear()

        #checking if the date format is valid
        try:
            datetime.datetime.strptime(from_date, '%m/%d/%y')
            self.driver.find_element_by_id(Locators.effort_from_date_id).send_keys(from_date)
        except ValueError:
            raise ValueError("Incorrect data format, should be MM/DD/YYYY")

    # search_by_effort_startingDate_to clears the starting date input field and inputs the argument to_date
    def search_by_effort_startingDate_to(self, to_date):

        self.driver.find_element_by_id(Locators.effort_to_date_id).clear()
        # checking if the date format is valid
        try:
            datetime.datetime.strptime(to_date, '%m/%d/%y')
            self.driver.find_element_by_id(Locators.effort_to_date_id).send_keys(to_date)
        except ValueError:
            raise ValueError("Test failed, date format should be MM/DD/YYYY")

    #search_by_investigator_or_director_name clears the Investigator or Director Name input field and inputs the argument dir_name
    def search_by_investigator_or_director_name(self, dir_name):
        self.driver.find_element_by_id(Locators.investigator_director_id).send_keys(dir_name)

    #search_by_recipient_org clears the Recipient Organization input field and inputs the argument org_name
    def search_by_recipient_org(self, org_name):
        self.driver.find_element_by_id(Locators.recipient_org_id).send_keys(org_name)

    #search_by_max_and_min_amount clears the Recipient Organization input field and inputs the argument org_name
    def search_by_max_and_min_amount(self, min_amount, max_amount):
        if max_amount >= min_amount:
            self.driver.find_element_by_id(Locators.amount_min_id).send_keys(min_amount)
            self.driver.find_element_by_id(Locators.amount_max_id).send_keys(max_amount)
        else:
            print("Test failed: The maximum value should be greater or equal to the minimum value")

    #this method selects DARPA Awarding Office
    #this can be repeated for all DoD Awarding Offices
    def search_by_dod_awarding_office(self):
        select_DARPA = Select(self.driver.find_element_by_id(Locators.awarding_office_id))
        select_DARPA.select_by_visible_text(Locators.DARPA_office_value)

    #This methods selects the NSA
    #This can be repeated with all funding agencies
    def search_funding_agency(self):
        select_NSA = Select(self.driver.find_element_by_id(Locators.funding_agencies_id))
        select_NSA.select_by_visible_text(Locators.NSA_funding_office_value)

    #clear_search clears the entered search filteres
    def clear_search(self):
        self.driver.find_element_by_id(Locators.clear_button_id).click()

    #cert_err_bypass ignores the certification error for the browser
    def cert_err_bypass(self):
        self.driver.find_element_by_id("details-button").click()
        self.driver.find_element_by_id("proceed-link").click()