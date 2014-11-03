
from pages.base_page import BasePage


class SignOutPage(BasePage):
    """page to sign out of the system"""

    def __init__(self, driver):
        super(SignOutPage, self).__init__(driver)
        self._self_link = "https://www.coursera.org/account/logout"


