from behave import *
from selenium import webdriver

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://www.seleniumeasy.com/')
    context.browser.maximize_window()


@then('The title has the text "(.*)"')
def step_impl(context, content):
    title_tag = context.browser.find_element_by_css_selector('#site-name h1').text
    assert title_tag == content
