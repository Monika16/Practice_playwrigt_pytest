from playwright.sync_api import Page

def set_date(page,date, month, year):
    page.locator('.ui-datepicker-month').select_option(month)
    page.locator(".ui-datepicker-year").select_option(year)
    dates = page.locator(".ui-datepicker-calendar tbody tr td").all()
    for dt in dates:
        if dt.inner_text() == date:
            dt.click()
            break

def test_dummy_ticket(page:Page):
    page.goto("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    page.locator("#product_549").click()
    page.locator("#travname").fill("Joseph")
    page.locator("#travlastname").fill("Smith")
    page.locator("#dob").click()
    set_date(page,"21","Jan","1992")
    page.locator("#sex_1").click()
    page.locator("#fromcity").fill("Seattle")
    page.locator("#tocity").fill("Dallas")
    page.locator("#departon").click()
    set_date(page,"21","Jun","2026")
    page.locator("#appoinmentdate").click()
    set_date(page,"28","Jun","2026")
    page.locator("#billing_phone").fill("123456788990")
    page.locator("#billing_email").fill("abc@gmail.com")
    page.locator("#billing_address_1").fill("123 St SE")
    page.locator("#billing_city").fill("Seattle")
    page.locator("#select2-billing_state-container").click()
    states=page.locator(".select2-results__options li").all()
    for state in states:
        if state.inner_text() == "Washington":
            state.click()
            break
    page.locator("#billing_postcode").fill("12345")
    page.wait_for_timeout(3000)
    if page.locator(".order-total .woocommerce-Price-amount bdi").inner_text() == "USD $19.00":
        print("Success !!")
    else:
        print("Fail !!")