import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import process.constants as const
from process.filtration import Filtration
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
import time
"""from bs4 import BeautifulSoup
import requests
import lxml"""


class Process(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Drivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Process,  self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def signin_button(self, signin= None):
        try:
            self.get(const.BASE_URL)
            checkbox = self.find_element(By.ID, "close-small")
            checkbox.click()
        except:
            print("No checkbox proceeding...")
        signin_element = self.find_element(By.CLASS_NAME, "nav__button-secondary btn-md btn-secondary-emphasis")
        signin_element.click()
        google_signin = self.find_element(By.ID, "#container")
        google_signin.click()
        login_email = self.find_element(By.ID, "#identifierId")
        login_email.clear()
        login_email.send_keys(const.EMAIL)
        login_next_button = self.find_element(By.CLASS_NAME, ".VfPpkd-vQzf8d")
        login_next_button.click()
        login_password = self.find_element(By.ID, "#password")
        login_password.clear()
        login_password.send_keys(const.PASS)
        login_next_button = self.find_element(By.CLASS_NAME, ".VfPpkd-vQzf8d")
        login_next_button.click()

    def search_box(self):
        html_text = requests.get("https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin").text
        soup = BeautifulSoup(html_text, "lxml")
        search_element = self.find_element(By.ID, "global-nav-typeahead")
        search_element.clear()
        search_element.send_keys(const.SEARCH_BOX)
        search_element.submit()

    def apply_filtration(self):
        filtration = Filtration(driver=self)
        filtration.companies_button()
        filtration.company_size_element()
        filtration.locations_button()


