import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=5000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com.br/")
    page.get_by_role("combobox", name="Pesquisar").click()
    page.get_by_role("combobox", name="Pesquisar").fill("playwright documentation python")
    page.get_by_role("button", name="Pesquisa Google").first.click()
    page.locator("iframe[name=\"a-1e14ivvgeisy\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
    page.locator("iframe[name=\"c-1e14ivvgeisy\"]").content_frame.locator(".rc-imageselect-tile").first.click()
    page.locator("iframe[name=\"c-1e14ivvgeisy\"]").content_frame.locator("td:nth-child(2)").first.click()
    page.locator("iframe[name=\"c-1e14ivvgeisy\"]").content_frame.locator("tr:nth-child(2) > td").first.click()
    page.locator("iframe[name=\"c-1e14ivvgeisy\"]").content_frame.get_by_role("button", name="Verify").click()
    page.get_by_role("link", name="Playwright Python Playwright https://playwright.dev › docs › api").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
