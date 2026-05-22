from playwright.sync_api import Page


def test_blaze_demo(page:Page):
    page.goto("https://blazedemo.com/")
    page.wait_for_timeout(2000)
    #departure = page.locator("select[name='fromPort'] option")
    # departure_cities = []
    # for city in departure.all_inner_texts():
    #     departure_cities.append(city)
    # print(departure_cities)

    # destination = page.locator("select[name='toPort'] option")
    # destination_cities =[]
    # for city in destination.all_inner_texts():
    #     destination_cities.append(city)
    # print(destination_cities)

    #************ Set the departure city as Boston ****************#
    page.locator("select[name='fromPort']").select_option("Boston")

    #************ Set the destination city as London ****************#
    page.locator("select[name='toPort']").select_option("London")

    #***************** Click Find Flights *************************#
    page.locator("input[value='Find Flights']").click()
    page.wait_for_timeout(2000)

    #************ Get the prices of all the flights ****************#
    table = page.locator(".table tbody")
    prices = table.locator("tr td:has-text('$')").all_inner_texts()
    sorted_prices = sorted(prices)
    #print(sorted_prices)

    #************ Choose the flight with lowest fare ****************#
    rows = table.locator("tr").all()
    for row in rows:
        price = row.locator("td:has-text('$')").inner_text()
        if price == sorted_prices[0]:
            row.locator("td").nth(0).locator('input[value="Choose This Flight"]').click()
            page.wait_for_timeout(2000)
            break

    page.get_by_placeholder("First Last").fill("Joseph")
    page.locator("#address").fill("123 Main St.")
    page.locator("#city").fill("Anytown")
    page.locator("#state").fill("WA")
    page.locator("#zipCode").fill("12345")
    page.locator("#cardType").select_option("Visa")
    page.locator("#creditCardNumber").fill("2345678453678")
    page.locator("#creditCardYear").fill("2028")
    page.locator("#nameOnCard").fill("Joseph Smith")
    page.locator("input[value='Purchase Flight']").click()
    page.wait_for_timeout(2000)
    if page.locator(".hero-unit h1").inner_text() == "Thank you for your purchase today!":
        print("Success !! Passed")
    else:
        print("Failed")







