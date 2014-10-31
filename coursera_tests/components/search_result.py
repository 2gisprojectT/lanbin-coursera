from selenium.webdriver.support.wait import WebDriverWait
from components.base_component import BaseComponent


class SearchResult(BaseComponent):
    """list of courses, result of search"""

    selectors = {
        'self': '.coursera-catalog-container.coursera-catalog-listings-courses-container',
        'catalog_element': '.coursera-catalog-listing-courselink.internal-home'
    }

    def get_courses(self):
        return self.driver.find_elements_by_css_selector(self.selectors['catalog_element'])

    #поиска совпадения названия с одним из названий курсов в результатах
    def find_course_in_result(self, name):
        for course in self.get_courses():
            if course.text == name:
                return True
        return False

