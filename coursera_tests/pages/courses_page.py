from pages.base_page import BasePage


class CoursesPage(BasePage):

    """page of all courses, search"""

    def __init__(self, driver):
        super(CoursesPage, self).__init__(driver)
        self._self_link = "https://coursera.org/courses"
        self._search_result = None
        self._catalog_toolbar = None

    @property
    def catalog_toolbar(self):
        from components.catalog_toolbar import CatalogToolbar

        if self._catalog_toolbar is None:
            self._catalog_toolbar = CatalogToolbar(self.driver, self.driver.find_element_by_css_selector(CatalogToolbar.selectors['self']))
        return self._catalog_toolbar

    @property
    def search_result(self):
        from components.search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver, self.driver.find_element_by_css_selector(SearchResult.selectors['self']))
        return self._search_result


