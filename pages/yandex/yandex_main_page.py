import sys

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class YandexMainPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    SEARCH_INPUT = (By.ID, 'text')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.search2__button > button')

    def fill_search_input(self, keyword):
        sys.stdout.write(f'Filling {keyword} on Yandex Search Box\n')

        self.fill_input(self.SEARCH_INPUT, keyword)
        return self

    def click_search_button(self):
        sys.stdout.write(f'Searching keyword on Yandex\n')

        self.click_element(self.SEARCH_BUTTON)
        return self
