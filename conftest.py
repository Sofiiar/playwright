import os

import pytest
from pom.login_page import LoginPage

PASSWORD = os.environ["PASSWORD"]


@pytest.fixture
def set_up(page):
    page.wait_for_load_state("networkidle")
    page.goto("https://www.saucedemo.com/")
    yield page
    page.close()


@pytest.fixture
def login(set_up):
    login_page = LoginPage(set_up)
    login_page.login("standard_user", PASSWORD)
    yield set_up
