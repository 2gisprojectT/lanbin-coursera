from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

__author__ = 'la0rg'


class CourseraSearchTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.my_url = "https://www.coursera.org/"

    def test_site(self):
        driver = self.driver
        driver.get(self.my_url)
        self.assertEquals("Coursera", driver.title)
        #Go to courses
        driver.find_element_by_link_text("Courses").click()
        #Find "algorithm"
        driver.find_element_by_id("coursera-catalog-search-id").click()
        driver.find_element_by_id("coursera-catalog-search-id").send_keys("algorithm", Keys.ENTER)
        self.assertEqual("Stanford University", driver.find_element_by_link_text("Stanford University").text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()