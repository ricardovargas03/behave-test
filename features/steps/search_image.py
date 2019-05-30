from behave import *
import urllib.request


@given("I open google images")
def open_google_image(context):
    context.driver.get("https://www.google.com.co/imghp")


@when('I search any "{word}" on google')
def search_google(context, word):
    context.driver.find_element_by_name("q").send_keys(word)
    context.driver.find_element_by_css_selector("svg").click()


@then('I choose the image on the position "{number}"')
def choose_image(context, number):
    context.img = context.driver.find_element_by_xpath("//div[@id='rg_s']/div[" + number + "]/a/img").get_attribute("src")


@then('I save the image with desire file "{name}"')
def save_image(context, name):
    urllib.request.urlretrieve(context.img, "images/" + name + ".png")