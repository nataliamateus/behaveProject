from seleniumpagefactory.Pagefactory import PageFactory

import logging


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d %(levelname)s %(name)s.%(funcName)s :: %(message)s',
                    datefmt='%H:%M:%S')

TIMEOUT = 30
HIGHLIGHT = False
MOBILE_TEST = False


class BasePage(PageFactory):

    def __init__(self, driver) -> None:
        self.driver = driver
        self.timeout = TIMEOUT
        self.highlight = HIGHLIGHT
        self.mobile_test = MOBILE_TEST
