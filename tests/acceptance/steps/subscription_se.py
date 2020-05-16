from behave import *
from selenium import webdriver
from tests.acceptance.pages.navigation_page import NavigationPage
import time

use_step_matcher('re')


@given('I am on the homepage of SeleniumEasy.com')
def step_impl(self):
    self.driver = webdriver.Chrome()
    self.driver.get(NavigationPage.url)
    self.driver.maximize_window()


@when('I click on the subscription button')
def step_impl(self):
    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    my_button_for_subscription = self.driver.find_element_by_css_selector(NavigationPage.subscription_button)
    my_button_for_subscription.click()
    time.sleep(1)
    pass


@then('it takes me to the correct web page to let me fill all the text fields')
def step_impl(self):
    windows_list = self.driver.window_handles
    self.driver.switch_to.window(windows_list[1])
    # if self.driver.current_url == NavigationPage.expected_subscription_url:
    email = self.driver.find_element_by_css_selector(NavigationPage.email_address_field)
    email.send_keys('someEmailAddress@email.com')
    f_name = self.driver.find_element_by_css_selector(NavigationPage.first_name_field)
    f_name.send_keys('someFirstName')
    l_name = self.driver.find_element_by_css_selector(NavigationPage.last_name_field)
    l_name.send_keys('someLastName')


@then('click submit')
def step_impl(self):
    button = self.driver.find_element_by_css_selector(NavigationPage.send_info_button)
    button.click()
    time.sleep(2)
    self.driver.quit()
