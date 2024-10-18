import csv
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)  
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://www.applyboard.com/services/study-canada")

    # let the page to be loaded completely
    page.wait_for_load_state('networkidle')

    # Scroll to load all the elements
    page.evaluate('window.scrollBy(0, document.body.scrollHeight / 2)')  

    page.wait_for_timeout(2000)  

    page.evaluate('window.scrollBy(0, document.body.scrollHeight / 2)')

    # Find course containers!
    page.wait_for_selector('div.elementor-column.elementor-col-33.elementor-top-column.elementor-element')

    # Scrape container's data
    courses = page.query_selector_all('div.elementor-column.elementor-col-33.elementor-top-column.elementor-element')

    print(f"Number of course containers found: {len(courses)}")

    university_names = []

    for course in courses:
        university_element = course.query_selector('p')  # University names are in <p> tags
        if university_element:
            university = university_element.inner_text()
            university_names.append(university)

    with open('universities.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['University Name'])  
        for university in university_names:
            writer.writerow([university])

    print(f"Saved {len(university_names)} university names to universities.csv")

  
with sync_playwright() as playwright:
    run(playwright)
