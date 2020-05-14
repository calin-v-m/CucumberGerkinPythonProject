class NavigationPage:
    url = 'https://www.seleniumeasy.com/'
    maven_tab_element = '.leaf a[href="/maven-tutorials"]'
    expected_url = 'https://www.seleniumeasy.com/maven-tutorials'
    text_field_element = '#edit-search-block-form--2'
    word_to_search = "JUnit"
    search_button = "button[class='btn btn-danger']"
    expected_url2 = 'https://www.seleniumeasy.com/search/node/JUnit'
