from tests.helpers.support_functions import *
from tests.helpers.DataGenerator import *

belt_name = '//*[@id="product-47"]/div[2]/h1'
belt_content = 'product-47'
product_picture = '//*[@id="product-47"]/div[1]/figure/div/img'
zoom_button = '//*[@id="product-47"]/div[1]/a'

cart_button = '//*[@id="content"]/div/div[1]/div/a'
coupon_field = 'coupon_code'
apply_coupon_button = '//*[@id="post-7"]/div/div/form/table/tbody/tr[2]/td/div/button'
coupon_info = '//*[@id="post-7"]/div/div/div[1]'

opinion_field = '//*[@id="tab-title-reviews"]/a'
star_five = '//*[@id="commentform"]/div/p/span/a[5]'
comment = 'comment'
author = 'author'
email = 'email'
submit = 'submit'
opinion_text = 'Lorem ipsum dolor sit amet'
published_opinion = 'comment-229'


def product_name_visible(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, belt_name)
    elem = driver_instance.find_element_by_xpath(belt_name)
    return elem.is_displayed()


def product_content_visible(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, belt_content)
    elem = driver_instance.find_element_by_id(belt_content)
    return elem.is_displayed()


def take_product_screenshot(driver_instance):
    elem = driver_instance.find_element_by_xpath(zoom_button)
    elem.click()
    driver_instance.save_screenshot("C:/Users/Administrator/PycharmProjects/tapsshop-automation/screenshot/belt_picture.png")


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
    wait_for_visibility_of_element_xpath(driver_instance, coupon_info)
    elem3 = driver_instance.find_element_by_xpath(coupon_info)
    value = elem3.text
    if value == 'Kupon został pomyślnie użyty.':
        return True
    else:
        return False


def add_opinion(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, opinion_field)
    opinion = driver_instance.find_element_by_xpath(opinion_field)
    opinion.click()
    star_icon = driver_instance.find_element_by_xpath(star_five)
    star_icon.click()
    comment_field = driver_instance.find_element_by_id(comment)
    comment_field.send_keys(opinion_text)
    author_field = driver_instance.find_element_by_id(author)
    author_field.send_keys(DataGenerator.generateProperName())
    email_field = driver_instance.find_element_by_id(email)
    email_field.send_keys(DataGenerator.generateProperEmail())
    submit_button = driver_instance.find_element_by_id(submit)
    submit_button.click()


