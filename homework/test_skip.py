import pytest
from selene import browser
from selenium import webdriver

"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""


@pytest.fixture(params=[(1280, 720), (360, 740), (1920, 1080), (393, 851)])
def window(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.open("https://github.com/")
    yield browser
    browser.quit()


def test_github_desktop(window):
    if browser._config.window_width < 1280:
        pytest.skip('Ширина окна для мобильного теста')
    browser.open('https://github.com/')
    browser.element('a.HeaderMenu-link--sign-in').click()


def test_github_mobile(window):
    if browser._config.window_width > 1279:
        pytest.skip('Ширина окна для десктоп теста')
    browser.open('https://github.com/')
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
