from behave import *

use_step_matcher('re')


@when('I click on the link from the Maven tab css "(.*)"')
def step_impl(context, link_css):
    maven_tab = context.driver.find_element_by_css_selector(link_css)
    # maven_tab = context.browser.find_element_by_css('.leaf a[href="/maven-tutorials"]')
    maven_tab.click()


@when('I search for a word with the search text field css "(.*)"')
def step_impl(context, link_css):
    search_field = context.driver.find_element_by_css_selector(link_css)
    search_field.click()
    search_field.clear()
    search_field.send_keys("JUnit")
    search_button = context.driver.find_element_by_css_selector("button[class='btn btn-danger']")
    search_button.click()
