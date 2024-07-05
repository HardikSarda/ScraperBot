import os
from selenium import webdriver
import process.constants as const
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
        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def signin_button(self, signin= None):
        try:
            checkbox = self.find_element(By.ID, "close-small")
            checkbox.click()
        except:
            print("No checkbox proceeding...")
        google_signin = self.find_element(By.ID, "container")
        google_signin.click()
        #signin_element = self.find_element(By.CSS_SELECTOR, "nav__button-secondary btn-md btn-secondary-emphasis")
        #signin_element.click()
        #signin_element = self.find_element(By.CLASS_NAME, "nsm7Bb-HzV7m-LgbsSe-MJoBVe")
        #signin_element.click()

