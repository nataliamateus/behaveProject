from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from hooks.web import Web


def get_web(browser):
    print("Browser: " + browser)
    if browser == "chrome":
        # return Web(webdriver.Chrome())
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Configuración para ejecutar en modo headless
        return Web(webdriver.Chrome(options=chrome_options))

    elif browser == "firefox":
        firefox_options = Options()
        firefox_options.add_argument("--headless")  # Configuración para ejecutar en modo headless
        return Web(webdriver.Firefox(options=firefox_options))
