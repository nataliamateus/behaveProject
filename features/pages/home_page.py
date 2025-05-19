from features.pages.base_page import BasePage

import logging


class HomePage(BasePage):

    locators = {
        "blogButton": ('CSS', "a[href='/blog/'] span"),
        "scheduleAppointmentButton": ('CSS', "div.links a[href*='/appointment'] span"),
        "requestQuoteButton": ('CSS', "div.links a[href*='/request'] span"),
        "contactUsButton": ('CSS', "div.links a[href='/contact/'] span"),
        "createAccountButton": ('CSS', "a[href='/create-account'] span")
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(self.__class__.__name__)

    def clickBlogButton(self):
        self.blogButton.click_button()
        self.logger.info(f"Click the blog button")

    def clickScheduleAppointmentButton(self):
        self.scheduleAppointmentButton.click_button()
        self.logger.info(f"Click Schedule Appointment button")

    def clickRequestAQuoteButton(self):
        self.requestQuoteButton.click_button()
        self.logger.info(f"Click request a quote button")

    def clickContactUsButton(self):
        self.contactUsButton.click_button()
        self.logger.info(f"Click contact us button")

    def clickCreateAnAccountButton(self):
        self.createAccountButton.click_button()
        self.logger.info(f"Click create an account button")
