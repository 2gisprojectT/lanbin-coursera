class BaseComponent(object):
    def __init__(self, driver, element=None):
        """
        :type driver: WebDriver
        :type element: WebElement
        """
        self.driver = driver
        self.element = element

    def find_by_css(self, selector):
        return self.driver.find_element_by_css_selector(self.selectors[selector])

