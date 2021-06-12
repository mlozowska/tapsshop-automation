import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, belt_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Program Files/chromedriver/chromedriver.exe")
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_product_name_visible(self):
        main_page.search_valid_product(self.driver)
        self.assertTrue(belt_page.product_name_visible(self.driver))

    def test2_take_screenshot(self):
        main_page.search_valid_product(self.driver)
        self.assertTrue(belt_page.product_name_visible(self.driver))
        belt_page.take_product_screenshot(self.driver)

    def test2_change_product_quantity(self):
        main_page.search_valid_product(self.driver)
        self.assertTrue(belt_page.product_name_visible(self.driver))
        belt_page.change_product_quantity(self.driver)

    def test3_add_invalid_coupon(self):
        Tests.test2_change_product_quantity(self)
        belt_page.go_to_cart(self.driver)
        self.assertTrue(belt_page.add_invalid_coupon(self.driver))

    def test3_add_valid_coupon(self):
        Tests.test2_change_product_quantity(self)
        belt_page.go_to_cart(self.driver)
        self.assertTrue(belt_page.add_valid_coupon(self.driver))