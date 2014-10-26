from helpers.base_component import BaseComponent


class SearchBar(BaseComponent):

    selectors = {
        'self': '.online__searchBar',
        'input': '.searchBar__form .searchBar__textfield._refbook .suggest__input',
        'submit': '.searchBar__submit._refbook',
        'route_button': '.searchBar__tabs .searchBar__tab.searchBar__rsTab',
        'from': '.searchBar__form .searchBar__textfield._from .suggest__input',
        'to': '.searchBar__form .searchBar__textfield._to .suggest__input'
    }

    def search(self, query):
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    def search_up(self, _from, _to):
        self.driver.find_element_by_css_selector(self.selectors['route_button']).click()
        self.driver.find_element_by_css_selector(self.selectors['from']).send_keys(_from)
        self.driver.find_element_by_css_selector(self.selectors['to']).send_keys(_to)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    @property
    def query(self):
        return self.driver.find_element_by_css_selector(self.selectors['input']).get_attribute("value")

