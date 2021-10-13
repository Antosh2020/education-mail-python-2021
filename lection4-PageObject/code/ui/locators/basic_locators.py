from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.ID, 'id-search-field')
    GO_LOCATOR = (By.ID, 'submit')


class MainPageLocators:
    COMPREHENSIONS = (
        By.XPATH, '//code/span[@class="comment" and contains(text(), "comprehensions")]'
    )


class SearchPageLocators(BasePageLocators):
    NO_RESULTS_FOUND = (
        By.XPATH, "//p[starts-with(text(), 'No results found')]"
    )
