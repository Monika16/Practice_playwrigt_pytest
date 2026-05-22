from playwright.sync_api import Page


def test_drop_down(page:Page):
    page.goto("https://bstackdemo.com/")
    assert page.locator(".sort select").is_visible()

    page.locator(".sort select").select_option("lowestprice")
    page.wait_for_timeout(5000)

    product_names = page.locator(".shelf-item .shelf-item__title").all_text_contents()
    #print(product_names)

    product_prices = page.locator(".shelf-item .shelf-item__price .val").all_text_contents()
    #print(product_prices)

    product_data = [{
        "product_name": n,
        "price": p
    } for n,p in zip(product_names,product_prices)]

    print("All products:\n")
    for p in product_data:
        print(*p.values(), sep=" : ")


    print("\nFirst Product",*product_data[0].values(), sep=" : ")
    print("\nLast Product" ,*product_data[-1].values(), sep=" : ")