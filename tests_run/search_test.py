import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Program Files/chromedriver/chromedriver.exe")
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_search_incorrect_product(self):
        self.assertTrue(main_page.search_invalid_product(self.driver))

    def test2_search_correct_product(self):
        self.assertTrue(main_page.search_valid_product(self.driver))






