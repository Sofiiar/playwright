import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
from pom.login_page import LoginPage


@pytest.mark.smoke
def test_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    home_page = HomePage(page)

    page.wait_for_load_state("networkidle")
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(page.locator("[data-test='login-button']")).to_be_hidden(timeout=3000)
    expect(home_page.home_page_title).to_be_visible()

    all_images = page.locator("img")
    for i in range(all_images.count()):
        img_src = all_images.nth(i).get_attribute('src')
        if img_src and '/static' in img_src:
            assert '/media' in img_src


@pytest.mark.regression
def test_login_2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    home_page = HomePage(page)

    page.wait_for_load_state("networkidle")
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(page.locator("[data-test='login-button']")).to_be_hidden(timeout=3000)
    expect(home_page.home_page_title).to_be_visible()

    all_images = page.locator("img")
    for i in range(all_images.count()):
        img_src = all_images.nth(i).get_attribute('src')
        if img_src and '/static' in img_src:
            assert '/media' in img_src


@pytest.mark.integration
def test_login_3(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    home_page = HomePage(page)

    page.wait_for_load_state("networkidle")
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(page.locator("[data-test='login-button']")).to_be_hidden(timeout=3000)
    expect(home_page.home_page_title).to_be_visible()

    all_images = page.locator("img")
    for i in range(all_images.count()):
        img_src = all_images.nth(i).get_attribute('src')
        if img_src and '/static' in img_src:
            assert '/media' in img_src


# ---------------------

    page.close()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_login(playwright)
