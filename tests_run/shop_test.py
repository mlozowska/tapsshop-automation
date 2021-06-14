import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, shop_page, out_of_stock_page


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

    def test2_out_of_stock_displayed(self):
        main_page.go_to_shop_page(self.driver)
        shop_page.go_to_second_shop_page(self.driver)
        shop_page.click_read_more_vneck_tshirt(self.driver)
        self.assertTrue(out_of_stock_page.out_of_stock_msg_visible(self.driver))

    def test3_go_to_slider_product(self):
        Tests.test2_out_of_stock_displayed(self)
        out_of_stock_page.go_to_slider_product(self.driver)
        self.assertTrue(out_of_stock_page.slider_product_visible(self.driver))


if __name__ == '__main__':
    unittest.main()