from selenium.webdriver.common.by import By


class HomePage:

    # Menu Locators
    blog = (By.CSS_SELECTOR, "a[href='/blog/'] span")
    schedule_appointment = (By.CSS_SELECTOR, "div.links a[href*='/appointment'] span")
    request_quote = (By.CSS_SELECTOR, "div.links a[href*='/request'] span")
    contact_us = (By.CSS_SELECTOR, "div.links a[href='/contact/'] span")
    create_account = (By.CSS_SELECTOR, "a[href='/create-account'] span")

    # Account
    create_account_title = (By.CSS_SELECTOR, "")
    first_name = (By.CSS_SELECTOR, "")
    last_name = (By.CSS_SELECTOR, "")
    email = (By.CSS_SELECTOR, "")
    phone_number = (By.CSS_SELECTOR, "")
    password = (By.CSS_SELECTOR, "")

    def __init__(self, context):
        context = context

    def clickOnBlogButton(self, context):
        blog_label = context.browser.find_element(*self.blog)
        blog_label.click()

    def clickOnScheduleAppointmentButton(self, context):
        schedule_appointment_label = context.browser.find_element(*self.schedule_appointment)
        schedule_appointment_label.click()

    def clickOnRequestAQuoteButton(self, context):
        request_quote_label = context.browser.find_element(*self.request_quote)
        request_quote_label.click()

    def clickOnContactUsButton(self, context):
        contact_us_label = context.browser.find_element(*self.contact_us)
        contact_us_label.click()

    def clickOnCreateAnAccountButton(self, context):
        create_account_label = context.browser.find_element(*self.create_account)
        create_account_label.click()
