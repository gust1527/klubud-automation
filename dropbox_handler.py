from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = None

def browserSetup(str:url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    wait = WebDriverWait(driver, 60)
    driver.get(url)
    wait.until(EC.url_to_be(url))
    driver.maximize_window()

while(True):
    pass