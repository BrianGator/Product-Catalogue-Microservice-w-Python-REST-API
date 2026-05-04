import os
from behave import fixture, use_fixture
from selenium import webdriver
from service import app

WAIT_SECONDS = int(os.getenv('WAIT_SECONDS', '10'))
BASE_URL = os.getenv('BASE_URL', 'http://localhost:3000')

@fixture
def selenium_browser(context):
    """Fixture for Selenium browser"""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(options=options)
    context.wait_seconds = WAIT_SECONDS
    context.base_url = BASE_URL
    yield context.driver
    context.driver.quit()

def before_all(context):
    """Executed once before all tests"""
    use_fixture(selenium_browser, context)
    context.wait_seconds = WAIT_SECONDS
    context.base_url = BASE_URL
