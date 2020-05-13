from behave import *
from selenium import webdriver

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.seleniumeasy.com/')
    context.driver.maximize_window()


@then('The title has the text "(.*)"')
def step_impl(context, content):
    title_tag = context.driver.find_element_by_css_selector('#site-name h1')
    assert title_tag.text == content
