from tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys

taps_logo = '//*[@id="masthead"]/div[1]/div[1]/a/img'
my_account_page_header_link = "menu-item-100"
cart_page_header_link = "menu-item-99"
add_hoodie_to_cart = '//*[@id="post-83"]/div/div[3]/ul/li[3]/div[2]/a'
go_to_cart_under_item = '//*[@id="post-83"]/div/div[3]/ul/li[3]/div[2]/a[2]'
cart_button_header = 'site-header-cart'
search_bar = 'woocommerce-product-search-field-0'
not_found_message = '//*[@id="main"]/p'
shop_page_header_link = '//*[@id="menu-item-102"]/a'


def taps_logo_visible(driver_instance):
    elem = wait_for_visibility_of_element_xpath(driver_instance, taps_logo)
    return elem.is_displayed()


def go_to_login_page(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, my_account_page_header_link)
    elem = driver_instance.find_element_by_id(my_account_page_header_link)
    elem.click()


def add_item_to_cart(driver_instance):
    elem = driver_instance.find_element_by_xpath(add_hoodie_to_cart)
    elem.click()


def go_to_cart_page(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, go_to_cart_under_item)
    elem = driver_instance.find_element_by_xpath(go_to_cart_under_item)
    elem.click()


def search_invalid_product(driver_instance):
    elem = driver_instance.find_element_by_id(search_bar)
    elem.send_keys('test')
    elem.send_keys(Keys.RETURN)
    wait_for_visibility_of_element_xpath(driver_instance, not_found_message)
    elem2 = driver_instance.find_element_by_xpath(not_found_message)
    return elem2.is_displayed()


def search_valid_product(driver_instance):
    elem = driver_instance.find_element_by_id(search_bar)
    elem.send_keys('belt')
    elem.send_keys(Keys.RETURN)


def go_to_shop_page(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, shop_page_header_link)
    elem = driver_instance.find_element_by_xpath(shop_page_header_link)
    elem.click()





