from hooks.web_factory import get_web
from pages.BasePage import allure_writer
from pages.LoginPage import LoginPage


def before_all(context):
    pass


def after_all(context):
    allure_writer(context)


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_scenario(context, scenario):
    base_url = context.config.userdata.get('base_url', 'https://ix-qa.firestonecompleteautocare.com/')
    browser = context.config.userdata.get('browser', 'firefox')
    web = get_web(browser)
    context.web = web
    web.maximize_window()
    web.open(base_url)
    context.login_page = LoginPage(web)


def after_scenario(context, scenario):
    context.login_page = None  # Reset the login_page instance
    context.web.close()  # Close the browser after each scenario


def before_step(context, step):
    pass


def after_step(context, step):
    if step.status == "failed":
        context.web.take_screenshot()


def before_tag(context, tag):
    pass


def after_tag(context, tag):
    pass
