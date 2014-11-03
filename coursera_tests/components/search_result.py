from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from components.base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC


class SearchResult(BaseComponent):
    """list of courses, result of search"""

    selectors = {
        'self': '.coursera-catalog-container.coursera-catalog-listings-courses-container',
        'catalog_element': '.coursera-catalog-listings .coursera-catalog-course-listing-box'
    }

    @property
    def catalog_item(self):
        return self.selectors['catalog_element']

