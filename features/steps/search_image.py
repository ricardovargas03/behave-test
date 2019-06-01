from behave import *
from pynput.keyboard import Key
from selenium.webdriver.common.keys import Keys
import os
import time


@given("I open google images")
def open_google_image(context):
    context.driver.get("https://www.google.com.co/imghp")


@when('I search any "{word}" on google')
def search_google(context, word):
    context.driver.find_element_by_name("q").send_keys(word)
    context.driver.find_element_by_css_selector("svg").click()


@then('I choose the image on the position "{number}"')
def choose_image(context, number):
    context.img = context.driver.find_element_by_xpath("//div[@id='rg_s']/div[" + number + "]/a/img")


@then('I save the image with desire file "{name}"')
def save_image(context, name):
    directory = os.getcwd()

    # Context menu and save image
    context.action.context_click(context.img).perform()
    context.keyboard.press('q')
    context.keyboard.release('q')
    context.keyboard.press(Key.enter)
    context.keyboard.release(Key.enter)
    time.sleep(2)

    # Go to directory
    context.keyboard.press(Key.cmd)
    context.keyboard.press(Key.shift)
    context.keyboard.press('g')
    context.keyboard.release(Key.cmd)
    context.keyboard.release(Key.shift)
    context.keyboard.release('g')
    time.sleep(2)
    context.keyboard.press(Key.delete)
    context.keyboard.release(Key.delete)

    # Type file name
    time.sleep(1)
    context.keyboard.type(directory.lower() + '/images')
    time.sleep(2)
    context.keyboard.press(Key.enter)
    context.keyboard.release(Key.enter)
    time.sleep(2)
    context.keyboard.type(name)
    context.keyboard.press(Key.enter)
    context.keyboard.release(Key.enter)
    time.sleep(1)

    # Assert image saved on dir
    assert (os.path.isfile(directory + '/images/' + name + '.jpeg')), "image not successfully saved"