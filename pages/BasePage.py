from utils.helpers.AllureHelper import allure_environment_writer


def allure_writer(context):
    base_url = context.config.userdata.get('base_url', 'https://ix-qa.firestonecompleteautocare.com/')
    browser = context.config.userdata.get('browser', 'firefox')
    environment_values = {"APPLICATION NAME": "My Firestone ", "ENVIRONMENT": "QA"}
    allure_environment_writer(environment_values)


class BasePage:
    pass
