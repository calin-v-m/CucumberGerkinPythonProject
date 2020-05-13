Feature: Test navigation between pages and after executing an action it takes us to the correct one

  Scenario: From homepage we can go to another page
    Given I am on the homepage of Selenium Easy
    When I click on the link from the Maven tab css "li.leaf a[href='/maven-tutorials']"
    Then I am on the Maven page

  Scenario: From homepage we can go to the search bar and perform a search
    Given I am on the homepage that has a search option
    When I search for a word with the search text field css "#edit-search-block-form--2"
    Then it shows all the results that include the word searched
