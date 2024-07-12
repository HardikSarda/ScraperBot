#This file is to apply filter onto the search done
#The applied filters are Company location, Company Size and Company as a category


from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import process.constants as const


class Filtration:
    def __init__(self, driver: WebDriver):
        self.driver = driver


    def companies_button(self):
        company = self.driver.find_element(By.CLASS_NAME, 'artdeco-pill artdeco-pill--slate artdeco-pill--choice artdeco-pill--2 '
                                         'search-reusables__filter-pill-buttonsearch-reusables__filter-pill-button')
        company.click()

    def locations_button(self):
        location_dropdown = self.driver.find_element(By.ID, "searchFilter_companyHqGeo")
        location_dropdown.click()
        location_searchbox = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder:"Add a location"]')
        location_searchbox.send_keys(const.LOCATION)
        location_list = location_dropdown.find_element(By.ID, 'triggered-expanded-ember6572')
        location_list.click()
        show_result_button = location_dropdown.find_element(By.ID, "ember6462")
        show_result_button.click()

    def company_size_element(self):
        company_size = self.driver.find_element(By.ID, "searchFilter_companySize")
        company_size.click()
        size_selector_1_10 = company_size.find_element(By.CSS_SELECTOR, "span['Filter by 1-10 employees']")
        size_selector_1_10.click()
        size_selector_11_50 = company_size.find_element(By.CSS_SELECTOR, "span['Filter by 11-50 employees']")
        size_selector_11_50.click()
        size_selector_51_200 = company_size.find_element(By.CSS_SELECTOR, "span['Filter by 51-200 employees']")
        size_selector_51_200.click()
        size_selector_201_500 = company_size.find_element(By.CSS_SELECTOR, "span['Filter by 201-500 employees']")
        size_selector_201_500.click()
        size_selector_501_1000 = company_size.find_element(By.CSS_SELECTOR, "span['Filter by 501-1000 employees']")
        size_selector_501_1000.click()
        show_result_button = company_size.find_element(By.ID, "ember6585")
        show_result_button.click()

