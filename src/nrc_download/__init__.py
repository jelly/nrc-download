import os
import os.path
from datetime import datetime

from playwright.sync_api import sync_playwright

# base url
URL = "https://www.nrc.nl/krant/{year}/{month}/{day}/downloads/"


def main():
    username = os.getenv('NRC_USERNAME')
    password = os.getenv('NRC_PASSWORD')
    outputdir = os.getenv('NRC_FOLDER')
    assert username
    assert password
    assert outputdir

    today = datetime.now()
    url = URL.format(year=today.year, month=today.month, day=today.day)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        page.click('a.login-required-message__button')
        page.locator("#username").is_visible()
        page.locator('#username').fill(username)
        page.locator('#password').fill(password)
        page.locator('#password').press('Enter')
        page.locator("section.de-downloads").is_visible()

        with page.expect_download() as download_info:
            # Perform the action that initiates download
            page.get_by_text("ePub").click()
            download = download_info.value

            print(download.suggested_filename)
            # Wait for the download process to complete and save the downloaded file somewhere
            download.save_as(os.path.join(outputdir, download.suggested_filename))

        browser.close()


