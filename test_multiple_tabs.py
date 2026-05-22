from playwright.sync_api import Playwright


def test_multiple_tabs(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    first_page = context.new_page()
    first_page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    first_page.on("popup", lambda page:page.wait_for_load_state())

    first_page.get_by_role("link",name="OrangeHRM, Inc").click()
    first_page.wait_for_timeout(3000)

    all_pages= context.pages
    print("No. of pages: ", len(all_pages))
    print("Title 1st page: ", all_pages[0].title())
    print("Title 2nd page: ", all_pages[1].title())

    login_page=all_pages[0]
    login_page.bring_to_front()
    login_page.get_by_placeholder("Username").fill("Admin")
    login_page.get_by_placeholder("Password").fill("admin123")
    login_page.get_by_role("button",name="Login").click()
    login_page.wait_for_timeout(3000)
    assert "Dashboard" in login_page.locator(".oxd-topbar-header-breadcrumb h6").inner_text()

    second_page=all_pages[1]
    second_page.bring_to_front()
    second_page.locator("//*[@id='navbarNav']/ul[2]/li[3]/a/button").click()
    second_page.wait_for_timeout(3000)
    assert "contact-sales" in second_page.url

    context.close()
    browser.close()

