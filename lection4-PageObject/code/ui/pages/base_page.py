from ui.locators import basic_locators
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CLICK_RETRY = 3


class BasePage(object):

    locators = basic_locators.BasePageLocators

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def search(self, query):
        search = self.find(self.locators.QUERY_LOCATOR)
        search.clear()
        search.send_keys(query)
        go_button = self.find(self.locators.GO_LOCATOR)
        go_button.click()

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY-1:
                    raise
