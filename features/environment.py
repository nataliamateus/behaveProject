from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from features.pages.login_page import LogInPage
from allure_commons.types import AttachmentType as aType
from utils.allure_environment import create_allure_environment

import allure


# Before
def before_all(context):
    pass


def before_feature(context, feature):
    pass


def before_tag(context, tag):
    pass


def before_scenario(context, scenario):
    print("Opening Driver")
    browser = context.config.userdata.get("browser_name")

    match browser:
        case "Chrome":
            context.driver = webdriver.Chrome()
        case "Firefox":
            firefox_profile = FirefoxProfile()

            # Allow the location
            firefox_profile.set_preference("geo.enabled", True)
            firefox_profile.set_preference("geo.provider.use_corelocation", True)  # Solo en macOS
            firefox_profile.set_preference("geo.prompt.testing", True)
            firefox_profile.set_preference("geo.prompt.testing.allow", True)

            # Create the Firefox Options and assign the profile
            options = Options()
            options.profile = firefox_profile

            # Initialize the Firefox driver with the specified options
            context.driver = webdriver.Firefox(options=options)

        case "":
            print("Browser not found")

    context.driver.maximize_window()
    context.login_page = LogInPage(context.driver)


def before_step(context, step):
    pass


# After
def after_all(context):
    pass


def after_feature(context, feature):
    pass


def after_tag(context, tag):
    pass


def after_scenario(context, scenario):
    print("Quitting driver")
    context.driver.quit()

    path = context.config.userdata.get("os_name") + "_" + context.config.userdata.get("browser_name")
    values = {
        "os_name": context.config.userdata.get("os_name"),
        "browser_name": context.config.userdata.get("browser_name")
    }
    create_allure_environment(path, values)


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name=step.name, attachment_type=aType.PNG)
