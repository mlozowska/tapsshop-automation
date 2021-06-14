from tests.helpers.support_functions import *

out_of_stock_info = '//*[@id="product-42"]/div[2]/form/p'
change_color_link = '//*[@id="product-42"]/div[1]/ol/li[2]/img'
slider_element = '//*[@id="product-42"]/nav/a[1]/img'
long_sleeve_tea_content = 'primary'


def out_of_stock_msg_visible(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, out_of_stock_info)
    elem = driver_instance.find_element_by_xpath(out_of_stock_info)
    value = elem.text
    print(value)
    if value == 'Tego produktu nie ma na stanie i jest niedostępny.':
        return True
    else:
        return False


def select_different_product_color(driver_instance):
    elem = driver_instance.find_element_by_xpath(change_color_link)
    elem.click()


def go_to_slider_product(driver_instance):
    elem = driver_instance.find_element_by_xpath(side_movable_element)
    elem.click()


def slider_product_visible(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, long_sleeve_tea_content)
    elem = driver_instance.find_element_by_id(long_sleeve_tea_content)
    return elem.is_displayed()

