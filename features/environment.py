from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from pynput.keyboard import Controller


def before_all(context):
    print("Executing before all")


def before_feature(context, feature):
    print("Before feature\n")


def before_scenario(context, scenario):

    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.implicitly_wait(60)
    context.action = ActionChains(context.driver)
    context.keyboard = Controller()


def after_scenario(context, scenario):
    context.driver.quit()
    print("After scenario\n")


def after_feature(context, feature):
    print("\nAfter feature")


def after_all(context):
    print("Executing after all")