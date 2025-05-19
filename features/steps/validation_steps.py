from assertpy import assert_that
from behave import *


@then(u'User must successfully login to the Dashboard page')
def verify_login(context):
    assert_that(context.login_page.verifyLogIn()).contains("BSRO")


@then(u'The Vehicles and Service Records title is display')
def verify_vehicles_label(context):
    assert_that(context.login_page.verifyVehiclesLabel()).contains("Vehicles & Service")
