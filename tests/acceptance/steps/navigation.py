from behave import *
from selenium import webdriver
from tests.acceptance.pages.navigation_page import NavigationPage
from tests.acceptance.utils import utils

use_step_matcher('re')


@given('I am on the homepage of Selenium Easy')
def step_impl(self):
    self.driver = webdriver.Chrome()
    self.driver.get(NavigationPage.url)
    utils.maximize_driver(self)


@when('I click on the Maven tab link')
def step_impl(self):
    maven_tab = self.driver.find_element_by_css_selector(NavigationPage.maven_tab_element)
    maven_tab.click()


@then('I am on the Maven page')
def step_impl(self):
    assert self.driver.current_url == NavigationPage.expected_url
    utils.close_driver(self)
