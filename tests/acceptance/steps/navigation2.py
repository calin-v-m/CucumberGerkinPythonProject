from behave import *
from selenium import webdriver
from tests.acceptance.pages.navigation_page import NavigationPage

use_step_matcher('re')


@given('I am on the homepage that has a search option')
def step_impl(self):
    self.driver = webdriver.Chrome()
    self.driver.get(NavigationPage.url)
    self.driver.maximize_window()


@when('I search for a word using the search text field')
def step_impl(self):
    search_field = self.driver.find_element_by_css_selector(NavigationPage.text_field_element)
    search_field.click()
    search_field.clear()
    search_field.send_keys(NavigationPage.word_to_search)
    search_button = self.driver.find_element_by_css_selector(NavigationPage.search_button)
    search_button.click()


@then('it shows all the results that include the word searched')
def step_impl(self):
    assert self.driver.current_url == NavigationPage.expected_url2
    self.driver.quit()
