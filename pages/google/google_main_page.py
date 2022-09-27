import sys

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GoogleMainPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_BUTTON = (By.NAME, 'btnK')

    def fill_search_input(self, keyword):
        sys.stdout.write(f'Filling {keyword} on Google Search Box\n')
        self.fill_input(self.SEARCH_INPUT, keyword)
        return self

    def click_search_button(self):
        sys.stdout.write(f'Searching keyword on Google\n')
        self.click_element(self.SEARCH_BUTTON)
        return self
