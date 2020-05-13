from behave import *
from selenium import webdriver

use_step_matcher('re')


@given('I am on the homepage of Selenium Easy')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.seleniumeasy.com/')
    context.driver.maximize_window()


@given('I am on the homepage that has a search option')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.seleniumeasy.com/')
    context.driver.maximize_window()


@then('I am on the Maven page')
def step_impl(context):
    expected_url = 'https://www.seleniumeasy.com/maven-tutorials'
    print(context.driver.current_url)
    print(expected_url)
    assert context.driver.current_url == expected_url


@then('it shows all the results that include the word searched')
def step_impl(context):
    expected_url = 'https://www.seleniumeasy.com/search/node/JUnit'
    print(context.driver.current_url)
    print(expected_url)
    assert context.driver.current_url == expected_url
