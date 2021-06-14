import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, belt_page, shop_page, opinion_page


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

    def test3_add_invalid_coupon(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(belt_page.add_invalid_coupon(self.driver))

    def test4_add_valid_coupon(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(belt_page.add_valid_coupon(self.driver))

    def test5_add_opinion(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_belt_page(self.driver)
        belt_page.add_opinion(self.driver)
        self.assertTrue(opinion_page.opinion_visible(self.driver))


if __name__ == '__main__':
    unittest.main()
