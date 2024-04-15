class LoginPage:
    # Locators
    cookies_ok_button = "cc-submit__btn"
    sign_in = "a[href='/account/sign-in']"
    email = "signInEmail"
    password = "password"
    sign_in_button = "button.btn-sign-in"
    user_label = "desktopMenuApp"
    user_name_link = "nav-account-toggle"
    vehicleLabel = "a[href='/account/vehicles']"

    def __init__(self, web):
        self.web = web

    def clickOnCookiesButton(self, context):
        ok_button = self.web.find_by_class_name(self.cookies_ok_button)
        ok_button.click()

    def signIn(self, context, username, passw):
        sign_in_label = self.web.find_by_css_selector(self.sign_in)
        sign_in_label.click()
        email = self.web.find_by_id(self.email)
        email.send_keys(username)
        password = self.web.find_by_id(self.password)
        password.send_keys(passw)

    def clickOnSignInButton(self, context):
        sign_in_cta = self.web.find_by_css_selector(self.sign_in_button)
        sign_in_cta.click()

    def clickOnUserNameLink(self, context):
        username_cta = self.web.find_by_class_name(self.user_name_link)
        username_cta.click()

    def verifyLogIn(self, context):
        user_label_test = self.web.find_by_id(self.user_label)
        return user_label_test.is_displayed()

    def verifyVehiclesLabel(self, context):
        user_vehicles_label_test = self.web.find_by_css_selector(self.vehicleLabel)
        return user_vehicles_label_test.is_displayed()
