from behave import *
from selenium.webdriver import Chrome
URL = "https://courses.letskodeit.com/login"
driver_path = "./library/chromedriver"


def before_scenario(context, scenario):
    context.driver = Chrome(executable_path=driver_path)
    context.driver.get(URL)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    context.driver.close()

