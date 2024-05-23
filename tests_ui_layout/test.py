import os
import pytest
from playwright.sync_api import expect

from pom.home_page_elements import HomePage
from pom.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.parametrize("user_name", ["standard_user",
                                       pytest.param("locked_out_user", marks=pytest.mark.xfail),
                                       "problem_user",
                                       "performance_glitch_user",
                                       "error_user",
                                       "visual_user"])
def test_logged_user_can_view_products(set_up, user_name) -> None:
    page = set_up

    home_page = HomePage(page)
    login_page = LoginPage(page)

    login_page.login(user_name, os.environ['PASSWORD'])

    expect(page.locator("[data-test='login-button']")).to_be_hidden(timeout=3000)
    expect(home_page.home_page_title).to_be_visible()

    all_images = page.locator("img")
    for i in range(all_images.count()):
        img_src = all_images.nth(i).get_attribute('src')
        if img_src and '/static' in img_src:
            assert '/media' in img_src


@pytest.mark.regression
def test_logged_user_can_view_products_2(login) -> None:
    page = login

    home_page = HomePage(page)

    expect(page.locator("[data-test='login-button']")).to_be_hidden(timeout=3000)
    expect(home_page.home_page_title).to_be_visible()

    all_images = page.locator("img")
    for i in range(all_images.count()):
        img_src = all_images.nth(i).get_attribute('src')
        if img_src and '/static' in img_src:
            assert '/media' in img_src


@pytest.mark.integration
def test_logged_user_can_view_products_3(login) -> None:
    page = login

    home_page = HomePage(page)

    expect(page.locator("[data-test='login-button']")).to_be_hidden(timeout=3000)
    expect(home_page.home_page_title).to_be_visible()

    all_images = page.locator("img")
    for i in range(all_images.count()):
        img_src = all_images.nth(i).get_attribute('src')
        if img_src and '/static' in img_src:
            assert '/media' in img_src
