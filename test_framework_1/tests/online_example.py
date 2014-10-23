#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from helpers.page import Page


class SeleniumTest(TestCase):

    def test_search(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        page.open("http://2gis.ru")
        page.search_bar.search(u'кафе')
        self.assertTrue(int(page.search_result.count) > 0, 'Wrong count of firms')
        driver.close()

    def test_share(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        #input
        page.open("http://2gis.ru")
        page.search_bar.search(u'кафе')
        #get share link
        page.extra_bar.share_click()
        share_link = page.share_result.link
        #open new tab, use received link
        body = driver.find_element_by_tag_name("body")
        body.send_keys(Keys.CONTROL + 't')
        page.open(share_link)
        #check input query
        query = page.search_bar.query
        self.assertEquals(str(query), u"кафе")

        driver.close()

    def test_route(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        page.open("http://2gis.ru")
        page.search_bar.search(u'карла маркса', u'красный проспект')

        time = page.routes_result.time
        self.assertIsNotNone(time)
        driver.close()


if __name__ == '__main__':
    unittest.main()
