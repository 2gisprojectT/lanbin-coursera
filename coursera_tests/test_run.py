from unittest import TestCase
from selenium import webdriver
import unittest
from pages.main_page import MainPage
import sys
import os


PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


class CourseraTests(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(20)
        cls.page = MainPage(cls.driver)

    def setUp(self):
        self.page.open_in_browser()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_find_valid_course(self):
        #get new page and change current
        self.page = self.page.header.go_courses()
        self.page.catalog_toolbar.search("algorithm and data structure")
        result = self.page.is_element_present(self.page.search_result.catalog_item)
        self.assertEqual(result, True)

    def test_find_invalid_course(self):
        #get new page and change current
        self.page = self.page.header.go_courses()
        self.page.catalog_toolbar.search("sldfjalsfl12313alkj")
        result = self.page.is_element_present(self.page.search_result.catalog_item)
        self.assertEqual(result, False)

    def test_login(self):
        self.page = self.page.header.go_sign_in()
        self.page = self.page.login_form.go_sign_in('lanbinaleksey@gmail.com', '******')
        present = self.page.is_element_present(self.page.header.account_name)
        self.assertEqual(present, True)

    def test_logout(self):
        self.page.header.go_sign_out()
        present = self.page.is_element_present(self.page.header.account_name)
        self.assertEqual(present, False)

    def test_another_one(self):
        #просто чекаем появился ли список курсов на главной при загрузке
        present = self.page.is_element_present(self.page.header.front_courses)
        self.assertEquals(present, True)

if __name__ == '__main__':
    unittest.main()
