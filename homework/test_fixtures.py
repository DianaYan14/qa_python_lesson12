import pytest
from selene import browser
from selenium import webdriver

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


@pytest.fixture(params=[(1280, 720), (1980, 1080)])
def precondition_desktop(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield browser
    browser.quit()


@pytest.fixture(params=[(640, 360), (375, 667)])
def precondition_mobile(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield browser
    browser.quit()


def test_desktop(precondition_desktop):
    browser.open('https://github.com/')
    browser.element('a.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()


def test_github_mobile(precondition_mobile):
    browser.open('https://github.com/')
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()

