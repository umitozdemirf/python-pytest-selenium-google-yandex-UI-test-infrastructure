import sys

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GoogleResultsPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def store_top_results(self):
        sys.stdout.write(f'Storing top results on Google\n')
        top_results = list()
        sys_out = list()

        elements = self.driver.find_elements(By.CSS_SELECTOR, '#rso > div')
        for element in elements:
            item = element.text.split("\n")
            if len(item) == 3:
                data = dict()
                data.update({"title": item[0]})
                data.update({"url": item[1].replace(" ", "").replace("›", "/")})
                data.update({"desc": item[2]})

                sys_out.append(item[0])

                top_results.append(data.copy())
        sys.stdout.write(f'Google Top Results: {sys_out}\n')
        return top_results
