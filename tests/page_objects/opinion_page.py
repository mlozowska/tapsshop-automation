from tests.helpers.support_functions import *

opinion_text = '//*[@id="comments"]/ol'


def opinion_visible(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, opinion_text)
    elem = driver_instance.find_element_by_xpath(opinion_text)
    return elem.is_displayed()