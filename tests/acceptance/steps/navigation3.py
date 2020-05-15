from behave import *
from selenium import webdriver
from tests.acceptance.pages.navigation_page import NavigationPage
from selenium.webdriver.common.keys import Keys

use_step_matcher('re')


@given('I am on the google.com web page')
def step_impl(self):
    self.driver = webdriver.Chrome()
    self.driver.get(NavigationPage.google_url)
    self.driver.maximize_window()


@when('I search for Seleniumeasy.com')
def step_impl(self):
    search_field = self.driver.find_element_by_css_selector(NavigationPage.google_search_text_field)
    search_field.click()
    search_field.clear()
    search_field.send_keys(NavigationPage.google_input_link)
    search_field.send_keys(Keys.RETURN)


@when('I click on the first result')
def step_impl(self):
    search_result = self.driver.find_element_by_css_selector(NavigationPage.first_se_element)
    search_result.click()


@then('it takes me to the desired web page')
def step_impl(self):
    self.driver.current_url == NavigationPage.expected_url3
    self.driver.close()
