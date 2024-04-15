from behave import *


@then(u'User must successfully login to the Dashboard page')
def verify_login(context):
    assert context.login_page.verifyLogIn(context) is True


@then(u'The Vehicles and Service Records title is display')
def verify_vehicles_label(context):
    assert context.login_page.verifyVehiclesLabel(context) is True
