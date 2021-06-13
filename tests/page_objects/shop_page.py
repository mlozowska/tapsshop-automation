from tests.helpers.support_functions import *
from time import sleep


sorting_field = '//*[@id="main"]/div[1]/form/select'
popularity_value = '//*[@id="main"]/div[1]/form/select/option[2]'
popularity_field_down = '//*[@id="main"]/div[2]/form/select/option[2]'

belt_pic = '//*[@id="main"]/ul/li[2]/a[1]/img'


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






