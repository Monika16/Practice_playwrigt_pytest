from playwright.sync_api import Page


def test_pagination_table(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    pages_count = page.locator(".pagination li").all()
    print("No. of pages: ", len(pages_count))
    table = page.locator("#productTable tbody")
    pag = 0
    while pag < len(pages_count):
        page.locator(".pagination li").nth(pag).click()
        rows = table.locator("tr")
        row_count = rows.count()
        for i in range(row_count):
            curr_row = rows.nth(i)
            cols = curr_row.locator("td")
            cols_count = cols.count()
            row_data=[]
            for j in range(cols_count-1):
                row_data.append(cols.nth(j).inner_text())
            print(row_data)
            checkbox = cols.nth(cols_count-1).locator("input[type='checkbox']")
            checkbox.check()
        page.wait_for_timeout(2000)
        print("\n\n")
        pag = pag + 1

