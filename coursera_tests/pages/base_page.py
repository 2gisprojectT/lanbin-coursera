from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    """Basic Page implements usual behaviors
    """
    def __init__(self, driver):
        self._self_link = None
        self.driver = driver
        self.source = None

    def open_in_browser(self):
        try:
            self.driver.get(self._self_link)
        except:
            print("Can't open page")

    def save_source(self):
        self.source = self.driver.page_source

    def compare_source(self, driver):
        try:
            return self.source != driver.page_source
        except WebDriverException:
            pass

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 5).until(self.compare_source)
