from helpers.base_component import BaseComponent

__author__ = 'la0rg'


class ShareResult(BaseComponent):

    selectors = {
        'self': '.share__popup',
        'input': '.share__popupUrl .share__popupUrlInput'
    }

    @property
    def link(self):
        return self.driver.find_element_by_css_selector(self.selectors['input']).get_attribute("value")