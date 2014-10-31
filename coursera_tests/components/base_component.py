from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait


class BaseComponent(object):
    def __init__(self, driver, element=None):
        """
        :type driver: WebDriver
        :type element: WebElement
        """
        self.driver = driver
        self.element = element

