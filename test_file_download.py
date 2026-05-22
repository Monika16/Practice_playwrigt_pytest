from playwright.sync_api import Page


def test_file_download(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/p/download-files_25.html')
    page.locator('#inputText').fill('Welcome Home')
    page.locator('#generateTxt').click()
    page.on("download", lambda download: download.save_as("downloads/test.txt"))
    page.locator('#txtDownloadLink').click()
    page.wait_for_timeout(3000)