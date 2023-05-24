import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when(u'open orange hrm homepage')
def open_home_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(1)  # Let the user actually see something!


@then(u'verify that the logo present on page')
def verify_logo(context):
    status = context.driver.find_element(By.CSS_SELECTOR, "div.orangehrm-login-branding").is_displayed()
    assert status is True

