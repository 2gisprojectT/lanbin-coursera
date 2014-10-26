from selenium.webdriver.common.keys import Keys


class Page():
    def __init__(self, driver):

        self.driver = driver
        self._search_bar = None
        self._search_result = None
        self._extra_bar = None
        self._share_result = None
        self._routes_result = None

    @property
    def search_bar(self):
        from helpers.search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def search_result(self):
        from helpers.search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver, self.driver.find_element_by_css_selector(SearchResult.selectors['self']))
        return self._search_result

    @property
    def extra_bar(self):
        from helpers.extra_bar import ExtraBar

        if self._extra_bar is None:
            self._extra_bar = ExtraBar(self.driver, self.driver.find_element_by_css_selector(ExtraBar.selectors['self']))
        return self._extra_bar

    @property
    def share_result(self):
        from helpers.share_result import ShareResult

        if self._share_result is None:
            self._share_result = ShareResult(self.driver, self.driver.find_element_by_css_selector(ShareResult.selectors['self']))
        return self._share_result

    @property
    def routes_result(self):
        from helpers.routes_result import RoutesResult

        if self._routes_result is None:
            self._routes_result = RoutesResult(self.driver, self.driver.find_element_by_css_selector(RoutesResult.selectors['self']))
        return self._routes_result

    def open(self, url):
        self.driver.get(url)

    def open_new_tab(self, url):
        body = self.driver.find_element_by_tag_name("body")
        body.send_keys(Keys.CONTROL + 't')
        self.open(url)

