import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, cart_page, order_page, order_confirm_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Program Files/chromedriver/chromedriver.exe")
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_process(self):
        self.assertTrue(main_page.taps_logo_visible(self.driver))
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.approve_cart(self.driver)
        order_page.proper_fill_all_form_areas(self.driver)
        price = order_page.check_total_price(self.driver)
        order_page.submit_order(self.driver)
        order_confirm_page.confirm_order_visible(self.driver)
        self.assertTrue(order_confirm_page.total_price_correct(self.driver, price))


if __name__ == '__main__':
    unittest.main()




