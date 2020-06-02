from behave import *
from selenium import webdriver
from tests.acceptance.pages.content_page import ContentPage
from tests.acceptance.utils import utils

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(self):
    self.driver = webdriver.Chrome()
    self.driver.get(ContentPage.url)
    utils.maximize_driver(self)


@then('The title has the text "(.*)"')
def step_impl(self, content):
    title_tag = self.driver.find_element_by_css_selector(ContentPage.title_element)
    assert title_tag.text == content
    utils.close_driver(self)


