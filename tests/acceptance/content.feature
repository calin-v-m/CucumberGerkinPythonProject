Feature: Test that pages have the desired content
  Scenario: Selenium easy page has the correct title
    Given I am on the homepage
    Then The title has the text "Selenium Easy"