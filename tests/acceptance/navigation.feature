Feature: Test navigation between pages and when performing an action it takes us to the correct web page

  Scenario: From homepage we can go to another page
    Given I am on the homepage of Selenium Easy
    When I click on the Maven tab link
    Then I am on the Maven page

  Scenario: From homepage we can go to the search bar and perform a search for a word, example JUnit
    Given I am on the homepage that has a search option
    When I search for a word using the search text field
    Then it shows all the results that include the word searched
