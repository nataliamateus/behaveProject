import csv
import time

from behave import *

from features.pages.users_page import Users

# Define a dictionary to store user data
user_data = {}


@given('I allow the cookies')
def allow_cookies(context):
    context.login_page.clickOnCookiesButton(context)


@given('The user data is read from the CSV file')
def user_reader(context):
    # Read user data from the CSV file and store it in the user_data dictionary
    with open('data/users.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_data[row['username']] = row['password']
    # Attach the user_data dictionary to the context for later use in other steps
    context.user_data = user_data


@given('User enters the "{username}" and "{password}"')
def step_user_enters_credentials(context, username, password):
    # Use the user_data from the context to compare entered credentials
    assert username in context.user_data, f"Username '{username}' not found in user_data"
    assert context.user_data[username] == password, f"Invalid password for username '{username}'"
    context.user_data['current_username'] = username
    context.user_data['current_password'] = password
    context.login_page.signIn(context, username, password)


@given('User fills the "{username}" and "{password}"')
def enter_credentials(context, username, password):
    print(f"Attempting login with username: {username}, password: {password}")
    context.login_page.signIn(context, username, password)


@given('User enters a "{username}" and "{password}" from the users list')
def enter_user_credentials(context, username, password):
    all_users = Users()
    for user in all_users.users_list:
        if user.username == username and user.password == password:
            context.current_user = user
            print(f"login with username: {user.username} and password: {user.password}")
            context.login_page.signIn(context, user.username, user.password)
        else:
            print(f"Attempting login with username: {user.username}, password: {user.password}, doesn't exist")


@when(u'Click on sign in button')
def signin_page(context):
    context.login_page.clickOnSignInButton(context)
    time.sleep(3)  # Let the user actually see something!


@Then(u'The user clicks on account name')
def username_page(context):
    context.login_page.clickOnUserNameLink(context)
    time.sleep(3)  # Let the user actually see something!
