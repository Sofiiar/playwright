import pytest

import utils.secret_config
from pom.login_page import LoginPage


@pytest.fixture
def set_up(page):
    page.wait_for_load_state("networkidle")
    page.goto("https://www.saucedemo.com/")
    yield page
    page.close()


@pytest.fixture
def login(set_up):
    login_page = LoginPage(set_up)
    login_page.login("standard_user", utils.secret_config.PASSWORD)
    yield set_up
