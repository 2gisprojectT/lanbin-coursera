from pages.base_page import BasePage


class SignInPage(BasePage):
    """page to insert login and password"""

    def __init__(self, driver):
        super(SignInPage, self).__init__(driver)
        self._self_link = "https://accounts.coursera.org/signin"
        self._search_result = None
        self._catalog_toolbar = None
        self._login_form = None

    @property
    def login_form(self):
        from components.signin_form_component import SignInForm

        if self._login_form is None:
            self._login_form = SignInForm(self.driver, self.driver.find_element_by_css_selector(SignInForm.selectors['self']))
        return self._login_form



