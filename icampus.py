import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

def wait_for_element(driver, selector, timeout=10):
    for _ in range(timeout*2):
        els = driver.find_elements(By.CSS_SELECTOR, selector)
        if els:
            return els[0]
        time.sleep(0.5)
    raise Exception(f"Element not found: {selector}")

ICAMPUS_LOGIN_URL = "https://icampus.ueab.ac.ke/"
# You need to update URLs below to your institution's actual grades/timetable pages after login
GRADES_PAGE_URL = ICAMPUS_LOGIN_URL + "grades"
TIMETABLE_PAGE_URL = ICAMPUS_LOGIN_URL + "timetable"
ASSIGNMENTS_PAGE_URL = ICAMPUS_LOGIN_URL + "assignments"  # If any

user_id = input("Enter your iCampus Student ID: ")
password = input("Enter your iCampus Password: ")

driver = webdriver.Chrome()  # Make sure chromedriver is installed and in your PATH

output = {"grades": [], "timetable": [], "assignments": []}
try:
    # 1. LOGIN
    driver.get(ICAMPUS_LOGIN_URL)
    time.sleep(2)
    user_field = wait_for_element(driver, 'input[type="text"],input[type="email"]')
    pass_field = wait_for_element(driver, 'input[type="password"]')
    user_field.clear(); user_field.send_keys(user_id)
    pass_field.clear(); pass_field.send_keys(password)
    pass_field.send_keys(Keys.RETURN)
    time.sleep(3)  # Adjust sleep time depending on your connection

    # 2. GRADES
    driver.get(GRADES_PAGE_URL)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    table = soup.find("table")
    if table:
        for row in table.find_all("tr")[1:]:
            cols = [td.get_text(strip=True) for td in row.find_all("td")]
            if len(cols) >= 7:
                output["grades"].append({
                    "name": cols[0], "code": cols[1], "group": cols[2], "grade": cols[3],
                    "credits": cols[4], "semester": cols[5], "status": cols[6]
                })

    # 3. TIMETABLE
    driver.get(TIMETABLE_PAGE_URL)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    table = soup.find("table")
    if table:
        for row in table.find_all("tr")[1:]:
            cols = [td.get_text(strip=True) for td in row.find_all("td")]
            if len(cols) >= 4:
                output["timetable"].append({
                    "course": cols[0], "start": cols[1], "end": cols[2], "location": cols[3]
                })

    # 4. ASSIGNMENTS (optional)
    driver.get(ASSIGNMENTS_PAGE_URL)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    table = soup.find("table")
    if table:
        for row in table.find_all("tr")[1:]:
            cols = [td.get_text(strip=True) for td in row.find_all("td")]
            if len(cols) >= 4:
                output["assignments"].append({
                    "course": cols[0], "title": cols[1], "due": cols[2], "desc": cols[3]
                })

    # -- Save output to JSON
    with open("mydata.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    print("Data saved to mydata.json!")

finally:
    driver.quit()
