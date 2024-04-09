from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bmi-calculator.azurewebsites.net/")

    page.get_by_label("Feet").click()
    page.get_by_label("Feet").fill("05")
    expect(page.get_by_label("Feet")).to_have_value("5")

    page.get_by_label("Inches").click()
    page.get_by_label("Inches").fill("09")
    expect(page.get_by_label("Inches")).to_have_value("9")

    page.get_by_role("button", name="Convert Height to Inches").click()
    expect(page.get_by_test_id("stVerticalBlock")).to_contain_text(
        "Total Height in Inches: 69"
    )

    page.get_by_label("Weight in lbs").click()
    page.get_by_label("Weight in lbs").fill("150")
    expect(page.get_by_label("Weight in lbs")).to_have_value("150")

    page.get_by_role("button", name="Calculate BMI").click()
    expect(page.get_by_test_id("stVerticalBlock")).to_contain_text("BMI: 22.7")

    page.get_by_role("button", name="Categorize BMI").click()
    expect(page.get_by_test_id("stVerticalBlock")).to_contain_text(
        "BMI Category: Normal weight"
    )

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
