from components.base_component import BaseComponent
from pages.courses_page import CoursesPage


class Header(BaseComponent):
    """unique component that every page has"""

    selectors = {
        'self': '.coursera-header',
        'courses': '.coursera-header-secondary .coursera-header-link.internal-home'
    }

    #return page that we have to go
    def go_courses(self):
        self.driver.find_element_by_css_selector(self.selectors['courses']).click()
        return CoursesPage(self.driver)
