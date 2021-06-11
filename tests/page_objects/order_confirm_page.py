from tests.helpers.support_functions import *

confirm_message = '//*[@id="post-8"]/header/h1'


def confirm_order(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, confirm_message)
    elem = driver_instance.find_element_by_xpath(confirm_message)
    return elem.is_displayed()