import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions


class Driver:

    def __init__(self, driver="chrome"):
        self.driver = driver
        self.web_driver = None

    def init_driver(self):
        sys.stdout.write(f'\nInitializing {self.driver} driver\n')

        match self.driver:
            case 'chrome':
                self.web_driver = webdriver.Chrome(options=ChromeOptions())
                return self.web_driver
            case 'firefox':
                self.web_driver = webdriver.Firefox(options=FirefoxOptions())
                return self.web_driver
            case 'safari':
                self.web_driver = webdriver.Safari(options=SafariOptions())
                return self.web_driver
            case 'remote-chrome':
                self.web_driver = webdriver.Remote(options=ChromeOptions())
                return self.web_driver
            case 'remote-firefox':
                self.web_driver = webdriver.Remote(options=FirefoxOptions())
                return self.web_driver

    def close_driver(self):
        sys.stdout.write(f'Closing driver')
        self.web_driver.close()
