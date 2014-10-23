from helpers.base_component import BaseComponent

__author__ = 'la0rg'


class ExtraBar(BaseComponent):

    selectors = {
        'self': '.extras__group:nth-child(2)',
        'share_btn': '.extras__group .extras__btn.extras__share'
    }

    def share_click(self):
        self.driver.find_element_by_css_selector(self.selectors['share_btn']).click()