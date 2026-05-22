from playwright.sync_api import Page

def set_date(page,month,day,year):
    # Calender next icon
    next_icon = page.locator(".ui-datepicker-next-icon")
    future = True

    # press the next button until you find the desired month and year
    while future:
        current_month = page.locator(".ui-datepicker-title .ui-datepicker-month").inner_text()
        current_year = page.locator(".ui-datepicker-title .ui-datepicker-year").inner_text()
        if current_month == month and current_year == year:
            break
        else:
            next_icon.click()

    # dates list has only the dates that are available
    dates = page.locator(".ui-datepicker-calendar tbody tr td a").all()
    if dates:
        for date in dates:
            # if you find the desired date then click
            if date.inner_text() == day:
                date.click()
                break
        else:#if the desired date is not available
            print("Cannot book on the date selected, choose dates that are available")
    else:#if dates are not available in that particular month
        print("Cannot select the date, choose the month that is available")

def test_irctc_date_picker(page:Page):
    page.goto("https://www.irctc.co.in/nget/train-search")
    # Click the calendar
    page.locator(".ui-calendar").click()
    set_date(page,"June","15","2026")
    page.wait_for_timeout(3000)
