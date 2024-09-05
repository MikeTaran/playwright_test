import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://admin.websitewizard.ru/")
    page.goto("https://admin.websitewizard.ru/owners")
    page.goto("https://admin.websitewizard.ru/login")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("mtaran.admin@gmail.com")
    page.get_by_placeholder("Пароль").click()
    page.get_by_placeholder("Пароль").fill("Zxcv1234")
    page.get_by_role("button", name="Войти").click()
    page.locator("#customerId").click()
    page.get_by_text("Test_MT").click()
    page.get_by_role("button", name="Применить").click()
    page.locator("div:nth-child(2) > div > div:nth-child(6) > .flex > .ant-switch").click()
    page.locator("div:nth-child(2) > div > div:nth-child(7) > .flex > .ant-switch").click()
    page.locator("div:nth-child(2) > div > div:nth-child(2) > .ant-select > .ant-select-selector > .ant-select-selection-item").click()
    page.get_by_text("Активный").click()
    page.get_by_label("grid").get_by_title("Активный").click()
    page.locator("div:nth-child(4) > .ant-select-dropdown > div > .rc-virtual-list > .rc-virtual-list-holder > div > .rc-virtual-list-holder-inner > div:nth-child(3) > .ant-select-item-option-content").click()
    page.locator("div:nth-child(2) > div > div:nth-child(6) > .flex > .ant-switch").click()
    page.locator("div:nth-child(2) > div > div:nth-child(7) > .flex > .ant-switch").click()
    page.get_by_role("button", name="Применить").click()
    page.locator(".ant-select-selection-overflow").first.click()
    page.locator("#agentIds").fill("sms")
    page.get_by_title("Test_SMS_agent").locator("div").click()
    page.get_by_role("button", name="Применить").click()
    page.get_by_text("ID", exact=True).click()

    # ---------------------
    context.storage_state(path="auth.json")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
