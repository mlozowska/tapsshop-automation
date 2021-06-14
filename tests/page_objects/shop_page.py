from tests.helpers.support_functions import *


sorting_field = '//*[@id="main"]/div[1]/form/select'
popularity_value = '//*[@id="main"]/div[1]/form/select/option[2]'
popularity_field_down = '//*[@id="main"]/div[2]/form/select/option[2]'

belt_pic = '//*[@id="main"]/ul/li[2]/a[1]/img'
number_two_page = '//*[@id="main"]/div[2]/nav/ul/li[2]/a'
read_more_button = '//*[@id="main"]/ul/li[3]/a[2]'


def sort_products(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, sorting_field)
    elem = driver_instance.find_element_by_xpath(popularity_value)
    elem.click()
    wait_for_visibility_of_element_xpath(driver_instance, popularity_field_down)
    elem2 = driver_instance.find_element_by_xpath(popularity_field_down)
    return elem2.is_displayed()


def go_to_belt_page(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, belt_pic)
    elem = driver_instance.find_element_by_xpath(belt_pic)
    elem.click()


def go_to_second_shop_page(driver_instance):
    elem = driver_instance.find_element_by_xpath(number_two_page)
    elem.click()


def click_read_more_vneck_tshirt(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, read_more_button)
    elem = driver_instance.find_element_by_xpath(read_more_button)
    elem.click()








