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

    def test_go_to_login_page(self):
        main_page.taps_logo_visible(self.driver)
        self.assertTrue(main_page.go_to_login_page(self.driver))

