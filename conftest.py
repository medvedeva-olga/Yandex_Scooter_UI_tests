import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.home_page import HomePage


@pytest.fixture(scope="class")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(options)

    yield driver

    driver.quit()

@pytest.fixture
def home_page(driver):
    page = HomePage(driver)
    page.timeout = 10
    page.open_page()
    return page
