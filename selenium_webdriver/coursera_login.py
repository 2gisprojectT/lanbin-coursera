from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

__author__ = 'la0rg'


class CourseraLoginTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.my_url = "https://www.coursera.org/"

    def test_site(self):
        driver = self.driver
        driver.get(self.my_url)
        #Input account information
        signin_link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign In"))
        )
        signin_link.click()
        #Email
        signin_email = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "signin-email"))
        )
        signin_email.clear()
        signin_email.send_keys("lanbinaleksey@gmail.com")
        #Password
        signin_password = driver.find_element_by_id("signin-password")
        signin_password.clear()
        signin_password.send_keys("******")
        driver.find_element_by_class_name("coursera-signin-button").click()
        #Check login
        user_name = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.coursera-header-account-name"))
        )
        self.assertEqual(" Aleksey", user_name.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()