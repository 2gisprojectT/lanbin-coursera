#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from helpers.page import Page


class SeleniumTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.page = Page(cls.driver)

    def setUp(self):
        self.page.open("http://2gis.ru")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_search(self):
        self.page.search_bar.search(u'кафе')
        self.assertTrue(int(self.page.search_result.count) > 0, 'Wrong count of firms')

    def test_share(self):
        page = self.page
        page.search_bar.search(u'кафе')
        #get share link
        page.extra_bar.share_click()
        page.open_new_tab(page.share_result.link)
        #check input query
        self.assertEquals(str(page.search_bar.query), u"кафе")

    def test_route(self):
        self.page.search_bar.search_up(u'карла маркса', u'красный проспект')
        time = self.page.routes_result.time
        self.assertIsNotNone(time)


if __name__ == '__main__':
    unittest.main()
