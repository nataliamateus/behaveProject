from configparser import ConfigParser

import webdriver_manager


from src.test.python.hooks.web import Web
from src.test.python.hooks.web_factory import get_web
from src.test.python.pages.BasePage import allure_writer
from src.test.python.pages.LoginPage import LoginPage


def before_scenario(context, test):
    web = get_web('chrome')
    context.web = web
    web.maximize_window()
    web.open('https://ix-qa.firestonecompleteautocare.com/')
    context.login_page = LoginPage(web)


def after_scenario(context, test):
    allure_writer()
    context.web.take_screenshot()
    context.web.close()
