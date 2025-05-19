from behave import *
from assertpy import fail
import csv
import time

from features.pages.users_page import Users

# Define a dictionary to store user data
user_data = {}


@given('User fills the "{username}" and "{password}"')
def step_impl(context, username, password):
    print(f"Attempting login with username: {username}, password: {password}")
    context.login_page.fillUsername(username)
    context.login_page.fillPassword(password)


@given('The user data is read from the CSV file')
def step_impl(context):
    # Read user data from the CSV file and store it in the user_data dictionary
    with open('data/users.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_data[row['username']] = row['password']
    # Attach the user_data dictionary to the context for later use in other steps
    context.user_data = user_data


@given('The user enters the "{username}" and "{password}"')
def step_user_enters_credentials(context, username, password):
    # Use the user_data from the context to compare entered credentials
    assert username in context.user_data, f"Username '{username}' not found in user_data"
    assert context.user_data[username] == password, f"Invalid password for username '{username}'"
    # You can use the 'username' and 'password' parameters in your code
    context.user_data['current_username'] = username
    context.user_data['current_password'] = password
    context.login_page.fillUsername(username)
    context.login_page.fillPassword(password)


@when(u'Click on sign in button')
def step_impl(context):
    context.login_page.clickSignInButton()
    time.sleep(3)  # Let the user actually see something!


@Then(u'The user clicks on account name')
def username_page(context):
    context.login_page.clickUserNameLink()
    time.sleep(2)  # Let the user actually see something!