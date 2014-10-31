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
        cls.driver.implicitly_wait(10)
        cls.page = MainPage(cls.driver)

    def setUp(self):
        self.page.open_in_browser()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_find_valid_course(self):
        #get new page and change current
        self.page = self.page.header.go_courses()
        self.page.save_source()
        self.page.catalog_toolbar.search("algorithm and data structure")
        self.page.wait_for_page_load()
        result = self.page.search_result.find_course_in_result("Algorithms: Design and Analysis, Part 1")
        self.assertEqual(result, True)

    def test_find_invalid_course(self):
        #get new page and change current
        self.page = self.page.header.go_courses()

        #нужно, для проверки загрузки страницы
        self.page.save_source()
        self.page.catalog_toolbar.search("language")
        #ждем загрузки страницы(изменения DOM- дерева)
        self.page.wait_for_page_load()

        result = self.page.search_result.find_course_in_result("Algorithms: Design and Analysis, Part 1")
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
