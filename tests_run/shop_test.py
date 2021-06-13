import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, shop_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Program Files/chromedriver/chromedriver.exe")
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_sort_products(self):
        main_page.go_to_shop_page(self.driver)
        self.assertTrue(shop_page.sort_products(self.driver))

