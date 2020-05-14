from behave import *
from selenium import webdriver
from tests.acceptance.pages.content_page import ContentPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(self):
    self.driver = webdriver.Chrome()
    self.driver.get(ContentPage.url)
    self.driver.maximize_window()


@then('The title has the text "(.*)"')
def step_impl(self, content):
    title_tag = self.driver.find_element_by_css_selector(ContentPage.title_element)
    assert title_tag.text == content
    self.driver.close()


