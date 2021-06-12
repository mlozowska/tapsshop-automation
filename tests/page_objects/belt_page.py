from tests.helpers.support_functions import *
from time import sleep

product_name = '//*[@id="product-47"]/div[2]/h1'
product_picture = '//*[@id="product-47"]/div[1]/figure/div/img'
zoom_button = '//*[@id="product-47"]/div[1]/a'
quantity_arrow = 'quantity_60c4ed1d9fed3'
add_to_cart = '//*[@id="product-47"]/div[2]/form/button'
cart_button = '//*[@id="content"]/div/div[1]/div/a'
coupon_field = 'coupon_code'
apply_coupon_button = '//*[@id="post-7"]/div/div/form/table/tbody/tr[2]/td/div/button'
coupon_info = '//*[@id="post-7"]/div/div/div[1]'

def product_name_visible(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, product_name)
    elem = driver_instance.find_element_by_xpath(product_name)
    return elem.is_displayed()


def take_product_screenshot(driver_instance):
    elem = driver_instance.find_element_by_xpath(zoom_button)
    elem.click()
    driver_instance.save_screenshot("C:/Users/Administrator/PycharmProjects/tapsshop-automation/screenshot/belt_picture.png")


def change_product_quantity(driver_instance):
    elem = driver_instance.find_element_by_id(quantity_arrow)
    elem.clear()
    elem.send_keys(3)
    elem2 = driver_instance.find_element_by_xpath(add_to_cart)
    elem2.click()


def go_to_cart(driver_instance):
    elem = driver_instance.find_element_by_xpath(cart_button)
    elem.click()


def add_invalid_coupon(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, coupon_field)
    elem = driver_instance.find_element_by_id(coupon_field)
    elem.send_keys("abc")
    elem2 = driver_instance.find_element_by_xpath(apply_coupon_button)
    elem2.click()
    wait_for_visibility_of_element_xpath(driver_instance, coupon_info)
    elem3 = driver_instance.find_element_by_xpath(coupon_info)
    value = elem3.text
    if value == 'Kupon "abc" nie istnieje!':
        return True
    else:
        return False


def add_valid_coupon(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, coupon_field)
    elem = driver_instance.find_element_by_id(coupon_field)
    elem.send_keys("test")
    elem2 = driver_instance.find_element_by_xpath(apply_coupon_button)
    elem2.click()
    sleep(2)
    wait_for_visibility_of_element_xpath(driver_instance, coupon_info)
    elem3 = driver_instance.find_element_by_xpath(coupon_info)
    sleep(2)
    value = elem3.text
    if value == 'Kupon został pomyślnie użyty.':
        return True
    else:
        return False


