import pytest
from selenium import webdriver
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.search_page import SearchPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def search_page(driver):
    return SearchPage(driver=driver)


@pytest.fixture(scope='function')
def driver(config):

    browser = config['browser']
    url = config['url']

    if browser == 'chrome':
        browser = webdriver.Chrome(
            executable_path='/home/konstantin-ermakov/drivers/chromedriver'
        )
    elif browser == 'firefox':
        browser = webdriver.Firefox(
            executable_path='/home/konstantin-ermakov/drivers/geckodriver'
        )
    else:
        raise RuntimeError(f'Unsupported browser: {browser}')

    browser.maximize_window()
    browser.get(url)
    # browser.set_window_size(1400, 1000)
    # browser.set_network_conditions(
    #     offline=False,
    #     latency=5,  # additional latency (ms)
    #     download_throughput=500 * 64,  # maximal throughput
    #     upload_throughput=500 * 64
    # )
    yield browser
    browser.close()
