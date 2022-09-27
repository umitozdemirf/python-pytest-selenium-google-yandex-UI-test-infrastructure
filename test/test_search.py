import pytest
import sys

from utils.driver import Driver
from utils.data.data_compare import DataCompare
from pages.google.google_main_page import GoogleMainPage
from pages.google.google_results_page import GoogleResultsPage
from pages.yandex.yandex_main_page import YandexMainPage
from pages.yandex.yandex_results_page import YandexResultsPage

from pages.base_page import BasePage
from config.base_config import BaseConfig as config


class TestSearch:
    """Products test - """

    @pytest.mark.smoke
    def test_login_case1(self):
        driver = Driver("firefox").init_driver()
        driver.delete_all_cookies()

        base_page = BasePage(driver)
        google_main_page = GoogleMainPage(driver)
        google_results_page = GoogleResultsPage(driver)
        yandex_main_page = YandexMainPage(driver)
        yandex_results_page = YandexResultsPage(driver)

        base_page.navigate_to(config.GOOGLE)

        google_main_page.fill_search_input("elma")
        google_main_page.click_search_button()
        google_top_results = google_results_page.store_top_results()

        base_page.navigate_to(config.YANDEX)

        yandex_main_page.fill_search_input("elma")
        yandex_main_page.click_search_button()

        yandex_top_results = yandex_results_page.store_top_results()

        DataCompare.compare_and_merge_dict(google_top_results, yandex_top_results)

        driver.close()
