from playwright.sync_api import Page, expect


def test_file_upload(page:Page):
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")
    files = ['upload_files/test1.txt', 'upload_files/test2.txt']
    page.locator('#filesToUpload').set_input_files(files)
    files_uploaded=page.locator('#fileList')
    print(files_uploaded.locator('li').all_inner_texts())
    expect(files_uploaded).to_have_count(1)
    page.wait_for_timeout(3000)
