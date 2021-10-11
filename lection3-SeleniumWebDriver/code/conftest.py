import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='http://www.python.org')


@pytest.fixture()
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')

    return {'browser': browser, 'url': url}


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
