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
        self.search(query)
        assert "No results found." not in self.driver.page_source

    @pytest.mark.skip("SKIP")
    def test_negative_search(self):
        self.search('olololol')
        assert "No results found." in self.driver.page_source

    def test_page_changed(self):
        self.click(basic_locators.GO_LOCATOR)
