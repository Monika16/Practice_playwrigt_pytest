import re

from playwright.sync_api import Page


def test_dynamic_table(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    table = page.locator("table[id ='taskTable'] tbody")
    rows = table.locator("tr").all()
    for row in rows:
        process_name = row.locator("td").nth(0).inner_text()
        if process_name == 'Chrome':
            cpu_load = row.locator("td:has-text('%')").inner_text()
            print("CPU load of Chrome: ", cpu_load)
            network_speed = row.locator("td:has-text('Mbps')").inner_text()
            print("Network speed of Chrome: ", network_speed)
        if process_name == 'Firefox':
            memory_size = row.locator("td").filter(has_text=re.compile("MB$")).text_content()
            print("Memory size of Firefox: ", memory_size)
            disk_space = row.locator("td:has-text('MB/s')").inner_text()
            print("Disk space of Firefox: ", disk_space)
        page.wait_for_timeout(2000)
