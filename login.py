import time, random
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # headless=False is to watch the process
    context = browser.new_context()

    page = context.new_page()

    # URL
    page.goto("https://accounts.applyboard.com/")

    # fill form
    page.fill('input[name="username"]', 'msa23010@iiitl.ac.in')  
    time.sleep(random.uniform(1.5, 3.0))

    page.fill('input[name="password"]', 'Nishantdeswal@18')  
    time.sleep(random.uniform(1.5, 3.0))
    
    # id selector to click on submit button as normal type value wasn't working!
    page.click('#okta-signin-submit')

    page.wait_for_load_state('networkidle')  # wait till the page is fully loaded!

    # browser.close()

    # To keep the browser idle to confirm whether everything worked or not!
    page.wait_for_timeout(60000)

with sync_playwright() as playwright:
    run(playwright)
