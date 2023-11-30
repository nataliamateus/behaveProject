from selenium import webdriver

from hooks.web import Web


def get_web(browser):
    print("Browser: " + browser)
    if browser == "chrome":
        return Web(webdriver.Chrome())

    elif browser == "firefox":
        return Web(webdriver.Firefox())
