from features.QA_env import BASE_URL_MF
from utils.helpers.AllureHelper import allure_environment_writer


def allure_writer(context):
    base_url_mf = context.config.userdata.get('base_url_mf', BASE_URL_MF)
    browser = context.config.userdata.get('browser', 'chrome')
    environment_values = {"APPLICATION NAME": "My Firestone ", "ENVIRONMENT": "QA"}
    allure_environment_writer(environment_values)


class BasePage:
    pass
