from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class MainPage(BasePage):

    """The main page of coursera"""

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self._self_link = "https://coursera.org/"
        self._header = None

    @property
    def header(self):
        from components.header import Header

        if self._header is None:
            self._header = Header(self.driver, self.driver.find_element_by_css_selector(Header.selectors['self']))
        return self._header
