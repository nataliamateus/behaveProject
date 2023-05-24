from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from hooks.web import Web


def get_web(browser):
    if browser == "chrome":
        return Web(webdriver.Chrome(ChromeDriverManager().install()))

    if browser == "firefox":
        return Web(webdriver.Firefox(executable_path=GeckoDriverManager().install()))



