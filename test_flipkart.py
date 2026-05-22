from playwright.sync_api import Page


def test_flipkart_search(page:Page):
    page.goto("https://www.flipkart.com/")
    page.wait_for_timeout(5000)
    page.keyboard.press("Escape")

    # Assert the search input field
    search_locator = page.locator(".olwU0Z form div div input")
    assert search_locator.is_visible()

    # fill search input with smart
    search_locator.fill("smart")
    page.wait_for_timeout(2000)

    # get full list of suggestion
    suggestion_list = page.locator("._1cisqlf2 .Swx5kP")

    # Print the total number of suggestions
    count = suggestion_list.count()
    print("No. of suggestions: ", count)

    # Assert atleast one suggestion is present
    assert count >= 1

    # Print 5th Suggestion if exists
    if not suggestion_list.count() < 5:
        print("\n 5th suggestion: ",suggestion_list.nth(4).inner_text())

    # Print all the suggestion
    print("\nAll Suggestions:\n")
    for i in range(count):
        print(suggestion_list.nth(i).inner_text())

    # Match suggestion smartphone and click it
    for i in range(count):
        if suggestion_list.nth(i).inner_text() == "smartphone":
            print("\nFound Smartphone\n")
            suggestion_list.nth(i).click()
            break



