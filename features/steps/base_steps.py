import time

from behave import *
from assertpy import *


@given('The page loads')
def step_impl(context):
    context.driver.get(context.config.userdata.get("base_url_mf"))
    assert_that(context.driver.title).contains("Tires, Oil Changes & Brakes | Firestone Complete Auto Care")


@when('Allow the cookies')
def step_impl(self):
    self.login_page.clickCookiesButton()


@then('Click on Sign In label')
def step_impl(self):
    self.login_page.clickSignInLabel()


