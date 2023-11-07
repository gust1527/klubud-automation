from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service

import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-notifications") # Disable pop-up notifications
# Path to your chromedriver
webdriver_service = Service("D:\Programmer\Chrome Driver\chromedriver-win64\chromedriver.exe")

# Your code here

# facebook username and password
username = 'gustavemilholmsimonsen@gmail.com'
password = '010401'
business_page = 'https://www.facebook.com/klubud/'
event_page = 'https://www.facebook.com/klubud/upcoming_hosted_events'

driver = webdriver.Chrome(options=options, service=webdriver_service)
driver.get('https://www.facebook.com')


# Initialize the wait
wait = WebDriverWait(driver, 10) # wait for up to 10 seconds

try:
    time.sleep(1)
    cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Tillad alle cookies')]")))
    cookies_button.send_keys(Keys.ENTER)


    print("Let's Begin")

    # Set the email and password fields using JavaScript
    driver.execute_script("document.getElementById('email').value = '{}';".format(username))
    print("Username Entered") 

    driver.execute_script("document.getElementById('pass').value = '{}';".format(password))
    print("Password Entered") 

    driver.find_element(By.NAME, 'login').click()
    print("Login Successfull..")

    time.sleep(1)
    print("Going to the Business page now...")
    driver.get(business_page)

    time.sleep(1)
    print("Now going to the Events page")
    driver.get(event_page)

    print("Clicking on the 'change to KlubUd account' button")
    driver.execute_script('document.querySelector(\'[aria-label="Skift"]\').click();')

    print("Getting the 'confirm-change-to-KlubUd-account' button")
    print("Clicking on the 'confirm-change-to-KlubUd-account' button")
    confirm_account_switch_button = driver.execute_script("""
                                                            switchButton = document.querySelector('[aria-label="Switch"]');
                                                            if (switchButton) {
                                                                const clickEvent = new MouseEvent('click', {
                                                                    bubbles: true,
                                                                    cancelable: true,
                                                                    view: window
                                                                });
                                                                switchButton.dispatchEvent(clickEvent);
                                                            }
                                                        """)

    
    print("Clicking on the 'confirm-change-to-KlubUd-account' button")
    "confirm_account_switch_button.click()"
    time.sleep(10)

    time.sleep(2)
    print("Adding event name information")
    eventname= "Automated Coffee For All"
    eventbutton = driver.find_element(By.XPATH,'.//*[@class="_1o0a _55r1 _1488 _58ak _3ct8"]').send_keys(eventname)

    time.sleep(2)
    print("Clicking on the Description field")
    descriptionname = ("We are having an automation coffee blowout")
    descriptionbutton = driver.find_element(By.XPATH,'.//*[@class="_f6a _5yk1"]').click()

    # Click description field
    time.sleep(2)
    print("Clicking on the Description field")
    descriptionname = ("We are having an automation coffee blowout")
    descriptionbutton = driver.find_element(By.XPATH,'.//*[@class="_5rp7"]').click()

    # Enter description info
    time.sleep(2)
    print("Entering Description information")
    descriptionname = ("We are having an automation coffee blowout")
    descriptionbutton = driver.find_element(By.XPATH,'.//*[@class="notranslate _5rpu"]').send_keys(descriptionname)

    # Select Category dropdown
    time.sleep(2)
    print("Click on the Category dropdown")
    categorydropdown = driver.find_element(By.XPATH,".//span[contains(text(), 'Select Category')]").click()

    # Click on sub category dropdown
    time.sleep(2)
    print("Click on the Art Category from dropdown")
    descriptionbutton = driver.find_element(By.XPATH,'.//*[@class="_54nh"]').click()

    # Click on frequency dropdown
    time.sleep(2)
    print("Click on the Frequency dropdown")
    descriptionbutton = driver.find_element(By.XPATH,'.//*[@class="_3r__ _2agf _4o_4 _4jy0 _4jy4 _517h _51sy _42ft _p"]').click()

    # Click on frequency sub dropdown
    time.sleep(2)
    print("Click on the Occurs Weekly from dropdown")
    frequencybutton = driver.find_element(By.XPATH,".//span[contains(text(), 'Occurs Once')]").click()

    # Click on starts calendar
    time.sleep(2)
    print("Click on the Starts Calendar")
    frequencyCalendar = driver.find_element(By.XPATH,'.//*[@class="_3smp"]').click()

    time.sleep(2)
    print("Click on the Start Date")
    frequencyCalendarCalendarSelectDate = driver.find_element(By.XPATH,'.//*[@class="_5c66 _5hpx"]').click()

    # Publish event
    """
    time.sleep(2)
    print("Submit Event")
    submitevent = driver.find_element(By.XPATH,'.//*[@class="_42ft _4jy0 layerConfirm _2pi9 _4jy3 _4jy1 selected _51sy"]').click()
    """
except NoSuchElementException as e:
    print(f"No such element found at line 42: {e.msg}")
