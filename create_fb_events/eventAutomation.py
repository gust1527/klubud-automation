from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from datetime import datetime

import time
from selenium.webdriver.chrome.options import Options
from datetime import datetime

options = Options()
options.add_argument("--disable-notifications")  # Disable pop-up notifications
# Path to your chromedriver
webdriver_service = Service("D:\Programmer\Chrome Driver\chromedriver-win64\chromedriver.exe")

# facebook username and password
username = 'gustavemilholmsimonsen@gmail.com'
password = '010401'
business_page = 'https://www.facebook.com/klubud/'
event_page = 'https://www.facebook.com/klubud/upcoming_hosted_events'


event_to_create_name = input("Input the event name you want to create: ")
start_datetime_str = input("Input the start time of the event (format: dd-mm-yyyy hh:mm): ")
end_datetime_str = input("Input the end time of the event (format: dd-mm-yyyy hh:mm): ")

# Convert the datetime strings to datetime objects
start_datetime = datetime.strptime(start_datetime_str, '%d-%m-%Y %H:%M')
end_datetime = datetime.strptime(end_datetime_str, '%d-%m-%Y %H:%M')

# Save the event to the event map
event_map = {event_to_create_name: {'start_date': start_datetime.strftime('%d-%m-%Y'), 'start_time': start_datetime.strftime('%H:%M'),
                                    'end_date': end_datetime.strftime('%d-%m-%Y'), 'end_time': end_datetime.strftime('%H:%M')}}

start_time = event_map[event_to_create_name]['start_time']
end_time = event_map[event_to_create_name]['end_time']

# Print the event map
print(event_map)
print(event_map[event_to_create_name]['start_date'])
print(event_map[event_to_create_name]['end_time'])

def scroll_to_bottom():
    # Scroll to the bottom of the page
    SCROLL_PAUSE_TIME = 2
    last_height = driver.execute_script("return document.body.scrollHeight")

    # Set a timeout of 15 seconds
    timeout = 30
    start_time = time.time()

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")

        # Exit the loop if we have reached the bottom of the page
        if new_height == last_height and driver.execute_script(
                "return window.pageYOffset + window.innerHeight") >= new_height:
            time.sleep(SCROLL_PAUSE_TIME)
            print("Reached the bottom of the page")

            # Attempt to return to the top of the page
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(SCROLL_PAUSE_TIME)

            # Check if we have successfully scrolled to the top
            if driver.execute_script("return window.pageYOffset") == 0:
                print("Successfully returned to the top of the page")
                break

        last_height = new_height

        # Check the timeout
        if time.time() - start_time > timeout:
            print(f"Timeout reached ({timeout} seconds). Returning to the top of the page.")

            # Scroll to the top of the page
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            break



time.sleep(1)
driver = webdriver.Chrome(options=options, service=webdriver_service)
driver.get('https://www.facebook.com')

# Initialize the wait
wait = WebDriverWait(driver, 10)  # wait for up to 10 seconds

try:
    # Handling cookies pop-up
    time.sleep(1)
    cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Tillad alle cookies')]")))
    cookies_button.click()

    print("Let's Begin")

    # Set the email and password fields using JavaScript
    driver.execute_script("document.getElementById('email').value = '{}';".format(username))
    print("Username Entered")

    driver.execute_script("document.getElementById('pass').value = '{}';".format(password))
    print("Password Entered")

    driver.find_element(By.NAME, 'login').click()
    print("Login Successful..")

    # Wait for the page to load
    time.sleep(5)
    print("Clicking on the 'change account' dropdown")
    driver.execute_script("document.querySelector('[aria-label=\"Din profil\"]').parentNode.click();")

    time.sleep(1)
    print("Clicking on the 'confirm-change-to-KlubUd-account' button")
    confirm_account_switch_button = driver.find_element(By.XPATH, "//span[text()='KlubUd']")
    confirm_account_switch_button.click()

    time.sleep(3)
    print("Now going to the Events page")
    driver.get(event_page)

    scroll_to_bottom()

    # Original XPath expression
    original_xpath_expression = f"//a[.//span[contains(text(), '{event_to_create_name}')]]"

    # Modified XPath expression
    modified_xpath_expression = (
        f"//a[.//span[contains(translate(text(), '–', '-'), '{event_to_create_name.replace('–', '-')}')]]"
    )

    # Using the text content of the span to locate the link
    try:
        event_to_target_container = driver.find_element(By.XPATH, original_xpath_expression)
    except NoSuchElementException:
        print(f"Could not find the event under 'upcoming hosted events': {event_to_create_name}")
        print("Attempting to find the event under 'past hosted events'...")
        driver.get('https://www.facebook.com/klubud/past_hosted_events')
        wait.until(EC.url_matches('https://www.facebook.com/klubud/past_hosted_events'))
        scroll_to_bottom()
        event_to_target_container = driver.find_element(By.XPATH, modified_xpath_expression)

    event_to_target_container.click()
    time.sleep(1)
    print(f"Clicked on the event: {event_to_create_name}")

    # Wait for the event page to load
    time.sleep(5)

    # Click on the 'Mere' button
    dropdown_for_event = driver.find_element(By.XPATH, "//div[@aria-label='Mere']")
    time.sleep(1)
    if dropdown_for_event:
        dropdown_for_event.click()
        print("Clicked on the 'Mere' button")

    time.sleep(2)  # Adjust the sleep time as needed

    # Target the button within the dropdown by its text
    button_in_dropdown = driver.find_element(By.XPATH, "//span[text()='Dubler hændelse']")
    button_in_dropdown.click()
    print("Clicked on the 'Dubler hændelse' button")

    # Wait for the modal to load
    time.sleep(2)

    # Target the input field for the event start date
    event_start_date_input_field = driver.find_element(By.XPATH, "//label[@aria-label='Startdato']")
    if event_start_date_input_field:
        event_start_date_input_field.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        event_start_date_input_field.send_keys(event_map[event_to_create_name]['start_date'])

    time.sleep(1)
    # Target the input field for the event start time
    event_start_time_input_field = driver.find_element(By.XPATH, "//label[@aria-label='Starttidspunkt']")
    if event_start_time_input_field:
        event_start_time_input_field.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        event_start_time_input_field.send_keys(event_map[event_to_create_name]['start_time'])

    time.sleep(1)
    # Target the input field for the event end date
    event_end_date_input_field = driver.find_element(By.XPATH, "//label[@aria-label='Slutdato']")
    if event_end_date_input_field:
        event_end_date_input_field.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        print("Clicked on the input field for the event end date, and cleared the field")
        event_end_date_input_field.send_keys(event_map[event_to_create_name]['end_date'])

    time.sleep(1)
    # Target the input field for the event end time
    event_end_time_input_field = driver.find_element(By.XPATH, "//label[@aria-label='Sluttidspunkt']")
    if event_end_time_input_field:
        event_end_time_input_field.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        event_end_time_input_field.send_keys(event_map[event_to_create_name]['end_time'])

    time.sleep(1)
    # Target the button for saving the event
    save_event_button = driver.find_element(By.XPATH, "//span[text()='Opret begivenhed']")
    if save_event_button:
        print("Clicked on the 'Opret begivenhed' button")

    time.sleep(30)

except NoSuchElementException as e:
    print(f"No such element found for the event: {event_to_create_name}")
    print(f"Exception details: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    driver.quit()
