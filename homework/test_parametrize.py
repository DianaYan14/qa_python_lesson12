import pytest
from selenium import webdriver
from selene import browser

"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""


@pytest.fixture(params=[(1280, 720), (1920, 1080), (360, 740), (393, 851)])
def size_browser(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield browser
    browser.quit()


@pytest.mark.parametrize('size_browser', [(1280, 720), (1920, 1080)], indirect=True)
def test_github_desktop(size_browser):
    browser.open('https://github.com/')
    browser.element('a.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()


@pytest.mark.parametrize('size_browser', [(360, 740), (393, 851)], indirect=True)
def test_github_mobile(size_browser):
    browser.open('https://github.com/')
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()

