import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Web(object):
    __TIMEOUT = 5

    def __init__(self, web_driver):
        super(Web, self).__init__()
        self._web_driver_wait = WebDriverWait(web_driver, Web.__TIMEOUT)
        self._web_driver = web_driver

    def open(self, url):
        self._web_driver.get(url)

    def maximize_window(self):
        self._web_driver.maximize_window()

    def title(self):
        return self._web_driver.title

    def curent_url(self):
        return self._web_driver.current_url

    def get_text_xpath(self, xpath):
        return self._web_driver_wait.until(EC.presence_of_element_located((By.XPATH, xpath))).text

    def find_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def finds_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def find_by_xpath_displayed(self, xpath):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).is_displayed()

    def find_by_name(self, name):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def finds_by_name(self, name):
        return self._web_driver_wait.until(EC.presence_of_all_elements_located((By.NAME, name)))

    def find_by_id(self, id):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def find_by_id_displayed(self, id_value):
        return self._web_driver_wait.until(EC.presence_of_element_located((By.ID, id_value))).is_displayed()

    def finds_by_id(self, id):
        return self._web_driver_wait.until(EC.presence_of_all_elements_located((By.ID, id)))

    def find_by_class_name(self, classname):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, classname)))

    def finds_by_class_nam(self, classname):
        return self._web_driver_wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, classname)))

    def find_by_css_selector(self, cssselector):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, cssselector)))

    def finds_by_css_selector(self, cssselector):
        return self._web_driver_wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, cssselector)))

    def switch_frame(self, frame):
        return self._web_driver.switch_to.frame(frame)

    def take_screenshot(self):
        screenshot = self._web_driver.get_screenshot_as_png()
        allure.attach(screenshot, name='screenshot', attachment_type=allure.attachment_type.PNG)

    def close(self):
        self._web_driver.quit()
