import csv
import time

from behave import *


@given('User enters the "{username}" and "{password}"')
def enter_Credentials(context, username, password):
    user_reader(context)
    for user in context.users:
        username = user['username']
        password = user['password']
    context.login_page.signIn(context, username, password)


@given('User fills the "{username}" and "{password}"')
def enter_Credentials(context, username, password):
    context.login_page.signIn(context, username, password)


@when(u'Click on sign up button')
def signin_page(context):
    context.login_page.clickOnSignInButton(context)
    time.sleep(4)  # Let the user actually see something!


@then(u'User must successfully login to the Dashboard page')
def verify_login(context):
    assert context.login_page.verifyLogIn(context) is True


def user_reader(context):
    with open('src/test/resources/features/users.csv', 'r') as f:
        reader = csv.DictReader(f)
        context.users = [row for row in reader]
        f.seek(0)
