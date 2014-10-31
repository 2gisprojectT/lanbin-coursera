from components.base_component import BaseComponent
from selenium.webdriver.common.keys import Keys


class CatalogToolbar(BaseComponent):
    """tool-bar to search courses"""

    selectors = {
        'self': '.coursera-catalog-toolbar-body',
        'input': 'input.coursera-catalog-search'
    }

    def search(self, query):
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(query, Keys.RETURN)

