from tests.helpers.support_functions import *

confirm_order_message = 'post-8'
total_price = '//*[@id="post-8"]/div/div/div/ul/li[3]/strong/span/bdi'


def confirm_order_visible(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, confirm_order_message)
    elem = driver_instance.find_element_by_id(confirm_order_message)
    return elem.is_displayed()


def total_price_correct(driver_instance, price):
    wait_for_visibility_of_element_xpath(driver_instance, total_price)
    elem = driver_instance.find_element_by_xpath(total_price)
    amount = elem.text
    print(f"Order confirmation page price: {amount}")
    if price == amount:
        return True
    else:
        return False





