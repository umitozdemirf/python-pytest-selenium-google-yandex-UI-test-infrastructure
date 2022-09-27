import sys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class YandexResultsPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def store_top_results(self):
        sys.stdout.write(f'Storing top results on Yandex\n')
        top_results = list()
        sys_out = list()

        elements = self.driver.find_elements(By.CSS_SELECTOR, '#search-result > li')
        for element in elements:
            item = element.text.split("\n")
            if len(item) == 4:
                data = dict()
                data.update({"title": item[0]})
                data.update({"url": item[1].replace("›", "/")})
                data.update({"desc": item[2]})

                top_results.append(data.copy())
                sys_out.append(item[0])

        sys.stdout.write(f'Yandex Top Results: {sys_out}\n')
        return top_results
