import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(5000)
    page.goto("https://www.saucedemo.com/")
    page.wait_for_load_state("networkidle")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    # alternative -> page.fill("input:below(:text(\"Swag Labs\"))", "standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"login-button\"]")).to_be_hidden(timeout=3000)
    expect(page.locator("text=Swag Labs")).to_be_visible()

    all_images = page.locator("img")
    for i in range(all_images.count()):
        img_src = all_images.nth(i).get_attribute('src')
        if img_src and '/static' in img_src:
            assert '/media' in img_src

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
