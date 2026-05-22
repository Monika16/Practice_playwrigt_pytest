from playwright.async_api import Page


def test_demowebshop_logo(page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    page.wait_for_timeout(3000)
    assert page.locator("img[alt='Tricentis Demo Web Shop']").is_visible()


def test_count_computer(page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    page.wait_for_timeout(3000)
    items = page.locator(".item-box .details h2 a:has-text('computer')")
    assert items.count() == 4

def test_first_product(page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    page.wait_for_timeout(3000)
    item_name = page.locator(".item-box").first.locator(".details h2 a").inner_text()
    assert item_name == "$25 Virtual Gift Card"

def test_last_product(page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    page.wait_for_timeout(3000)
    item_name = page.locator(".item-box").last.locator(".details h2 a").inner_text()
    assert item_name == "Simple Computer"

def test_third_product(page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    page.wait_for_timeout(3000)
    item_name= page.locator(".item-box").nth(2).locator(".details h2 a").inner_text()
    print(item_name)

def test_title_of_all_items(page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    page.wait_for_timeout(3000)
    items = page.locator(".item-box .details h2 a").all_text_contents()
    print(items)

def test_footer_links(page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    page.wait_for_timeout(3000)
    links = page.locator(".footer li")
    print("First footer link: ",links.first.inner_text())
    print("Last footer link: ",links.last.inner_text())
    print("6th footer link: ",links.nth(5).inner_text())







