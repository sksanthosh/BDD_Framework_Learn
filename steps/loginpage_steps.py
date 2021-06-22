from behave import *
import time


@given(u'User on Login page')
def step_impl(context):
    element = context.driver.find_element_by_xpath('//a[@href="/login"]')
    if element:
        print("On Log In Screen")


@when(u'User enters email "{email}"')
def step_impl(context, email):
    context.driver.find_element_by_id('email').send_keys(email)


@when(u'User enters password "{password}"')
def step_impl(context, password):
    context.driver.find_element_by_id('password').send_keys(password)


@when(u'User clicks on Login button')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@value="Login"]').click()


@then(u'User should be logged successfully')
def step_impl(context):
    time.sleep(3)
    element = context.driver.find_element_by_xpath('//span[@class="caret"]')
    if element:
        print('Logged Successfully')


@when(u'User enters invalid email "{email}"')
def step_impl(context, email):
    context.driver.find_element_by_id('email').send_keys(email)


@when(u'User enters invalid password "{password}"')
def step_impl(context, password):
    context.driver.find_element_by_id('password').send_keys(password)


@then(u'User Login should fail')
def step_impl(context):
    time.sleep(5)
    element = context.driver.find_element_by_xpath('//span[@class="dynamic-text help-block"]')
    if element:
        print("Login Failed")


@when(u'User clicks on Forgot password link')
def step_impl(context):
    context.driver.find_element_by_link_text('Forgot Password ?').click()


@when(u'User enter valid email "{email}"')
def step_impl(context, email):
    context.driver.find_element_by_id('email').send_keys(email)


@when(u'User clicks on Reset password button')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@value="Send Password Reset Link"]').click()


@then(u'Password reset link should be sent')
def step_impl(context):
    time.sleep(10)
    element = context.driver.find_element_by_xpath('//div[@class="alert alert-success"]')
    if element:
        print("Password reset link is sent")
