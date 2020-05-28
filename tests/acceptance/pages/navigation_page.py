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

    # subscription_se elements
    page_final = "window.scrollTo(0, document.body.scrollHeight);"
    subscription_button = '#mc-embedded-subscribe'
    email_address_field = '#MERGE0'
    first_name_field = '#MERGE1'
    last_name_field = '#MERGE2'
    send_info_button = 'div .formEmailButton'
    expected_subscription_url = 'https://seleniumeasy.us15.list-manage.com/subscribe/post?u=a5d2efe08ad93a8b91b578279&id=5d70235043'
