# Libraries
import csv

import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from utils.helpers.AllureHelper import allure_environment_writer


class BasePage:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(driver, 40)


def allure_writer():
    environment_values = {"APPLICATION NAME": "My Firestone ", "ENVIRONMENT": "Testing"}
    allure_environment_writer(environment_values)


def __init__(self, driver, wait):
    self.driver = driver
    self.wait = wait
