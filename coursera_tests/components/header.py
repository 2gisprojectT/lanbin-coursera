from components.base_component import BaseComponent
from pages.courses_page import CoursesPage
from pages.login_page import SignInPage
from pages.logout_page import SignOutPage
from pages.main_page import MainPage


class Header(BaseComponent):
    """unique component that every page has"""

    selectors = {
        'self': '.coursera-header',
        'courses': '.coursera-header-secondary .coursera-header-link.internal-home',
        'account_name': '.coursera-header-account-name',
        'front_courses': '.coursera-front-courses'
    }

    #return page that we have to go
    def go_courses(self):
        self.find_by_css('courses').click()
        return CoursesPage(self.driver)

    def go_sign_in(self):
        sip = SignInPage(self.driver)
        sip.open_in_browser()
        return sip

    def go_sign_out(self):
        sop = SignOutPage(self.driver)
        sop.open_in_browser()
        #sign out page redirect to the main page
        return MainPage(self.driver)

    @property
    def account_name(self):
        return self.selectors['account_name']

    @property
    def front_courses(self):
        return self.selectors['front_courses']