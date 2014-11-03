from components.base_component import BaseComponent
from pages.main_page import MainPage


class SignInForm(BaseComponent):

    selectors = {
        'self': '.coursera-signin-form',
        'email': '.control-group .controls input[id="signin-email"]',
        'password': '.control-group .controls input[id="signin-password"]',
        'submit': '.btn.btn-success.coursera-signin-button'
    }

    def set_email(self, email):
        self.find_by_css('email').send_keys(email)

    def set_password(self, password):
        return self.find_by_css('password').send_keys(password)

    def go_sign_in(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.find_by_css('submit').click()
        return MainPage(self.driver)

