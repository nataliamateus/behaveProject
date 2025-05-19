from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

from hooks.web import Web


def get_web(browser):

    match browser:
        case "Chrome":
            chrome_options = Options()
            # chrome_options.add_argument("--headless")  # Set up to execute headless mode
            return Web(webdriver.Chrome(options=chrome_options))

        case "Firefox":
            firefox_options = Options()
            # firefox_options.add_argument("--headless")  # Set up to execute headless mode
            return Web(webdriver.Firefox(options=firefox_options))
