from assertpy import assert_that

from features.pages.base_page import BasePage

import logging


class LogInPage(BasePage):
    locators = {
        "cookiesOkButton": ('CLASS_NAME', "cc-submit__btn"),
        "signInLabel": ('CSS', "a[href='/account/sign-in']"),
        "userNameInput": ('ID', "signInEmail"),
        "passwordInput": ('ID', "password"),
        "sigInButton": ('CSS', "button.btn-sign-in"),
        "userLabel": ('CLASS_NAME', "desktopMenuApp"),
        "userNameLink": ('CLASS_NAME', "nav-account-toggle"),
        "vehicleLabel": ('CSS', "a[href='/account/vehicles']")
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(self.__class__.__name__)

    def clickCookiesButton(self):
        self.cookiesOkButton.click_button()
        self.logger.info(f"Click cookies button")

    def clickSignInLabel(self):
        self.signInLabel.click_button()
        self.logger.info(f"Click the sign in button")

    def fillUsername(self, username):
        self.userNameInput.set_text(username)
        self.logger.info(f"Fill the username: <{username}>")

    def fillPassword(self, password):
        self.passwordInput.set_text(password)
        self.logger.info(f"Fill the password: <{password}>")

    def clickSignInButton(self):
        self.sigInButton.click_button()
        self.logger.info(f"Click the sign in button")

    def clickUserNameLink(self):
        self.userNameLink.click_button()
        self.logger.info(f"Click the user name link")

    def verifyLogIn(self):
        return self.userNameLink.get_text()

    def verifyVehiclesLabel(self):
        return self.vehicleLabel.get_text()

