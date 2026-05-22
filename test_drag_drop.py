from playwright.sync_api import Page, expect


def test_drag_drop(page:Page):
    page.goto("https://demo.guru99.com/test/drag_drop.html")
    bank_source = page.locator("#credit2")
    bank_target = page.locator("#bank")
    bank_source.drag_to(bank_target)

    amount_source = page.locator("#fourth").nth(0)
    amount_target = page.locator("#amt7")
    amount_source.drag_to(amount_target)

    sales_source = page.locator("#credit1")
    sales_target = page.locator("#loan")
    sales_source.drag_to(sales_target)

    amt_source = page.locator("#fourth").nth(1)
    amt_target = page.locator("#amt8")
    amt_source.drag_to(amt_target)

    success_text = page.locator('.table4_result a').inner_text()
    print(success_text)
    assert success_text == "Perfect!"

    page.wait_for_timeout(5000)
