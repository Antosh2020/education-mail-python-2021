from base import BaseCase
from ui.locators import basic_locators
import pytest


class TestOne(BaseCase):

    @pytest.mark.skip("SKIP")
    def test_title(self):
        assert "Python" in self.driver.title

    @pytest.mark.parametrize(
        'query',
        [
            pytest.param(
                'pycon'
            ),
            pytest.param(
                'python'
            )
        ]
    )
    @pytest.mark.skip("SKIP")
    def test_search(self, query):
        self.base_page.search(query)
        assert "No results found." not in self.driver.page_source

    def test_negative_search(self):
        self.search_page.search('olololol')
        self.search_page.find(self.search_page.locators.NO_RESULTS_FOUND).is_displayed()

    @pytest.mark.skip("SKIP")
    def test_page_changed(self):
        self.base_page.click(basic_locators.BasePageLocators.GO_LOCATOR)

    @pytest.mark.skip("SKIP")
    def test_carousel(self):
        self.main_page.click(basic_locators.MainPageLocators.COMPREHENSIONS, timeout=15)
