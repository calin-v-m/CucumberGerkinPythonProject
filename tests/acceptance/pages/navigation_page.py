class NavigationPage:

    # navigation elements
    url = 'https://www.seleniumeasy.com/'
    maven_tab_element = '.leaf a[href="/maven-tutorials"]'
    expected_url = 'https://www.seleniumeasy.com/maven-tutorials'

    # navigation2 elements
    text_field_element = '#edit-search-block-form--2'
    word_to_search = "JUnit"
    search_button = "button[class='btn btn-danger']"
    expected_url2 = 'https://www.seleniumeasy.com/search/node/JUnit'

    # navigation3 elements
    google_url = 'https://www.google.com/'
    google_search_text_field = 'input[name="q"]'
    google_input_link = 'http://www.seleniumeasy.com/'
    first_se_element = 'a[href="https://www.seleniumeasy.com/"]'
    expected_url3 = 'https://www.seleniumeasy.com/'