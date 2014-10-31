import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


from helpers.base_component import BaseComponent
__author__ = 'la0rg'


class RoutesResult(BaseComponent):

    selectors = {
        'self': '.online__dataViewer',
        'header_time': '.routeResults__routeHeaderWrap .routeResults__time'
    }

    @property
    def time(self):
        return self.driver.find_element_by_css_selector(self.selectors['header_time']).text
