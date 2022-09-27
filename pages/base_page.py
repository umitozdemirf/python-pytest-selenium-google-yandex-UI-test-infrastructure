import sys

from config.base_config import BaseConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all classes"""
"""It contains all the generic methods and utilities for all pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = BaseConfig.DEFAULT_WAIT

    def navigate_to(self, url):
        sys.stdout.write(f'Navigating to {url}\n')
        self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator),
                                                              'ELEMENT IS NOT FOUND OR VISIBLE! => {}'.format(
                                                                  locator))

    def fill_input(self, locator, value):
        self.find_element(locator).send_keys(value)

    def click_element(self, locator):
        self.find_element(locator).click()

    def verify_element(self, locator):
        self.find_element(locator)

    def verify_element_text(self, locator, text):
        assert self.find_element(locator).text == text, "Message isn't equal!"
