
class LoginPage:

    # Locators
    sign_in = "a[href='/sign-in']"
    email = "signInEmail"
    password = "password"
    sign_in_button = "button.btn-sign-in"
    user_label = "desktopMenuApp"

    def __init__(self, web):
        self.web = web

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

    def verifyLogIn(self, context):
        user_label_test = self.web.find_by_id(self.user_label)
        return user_label_test.is_displayed()
