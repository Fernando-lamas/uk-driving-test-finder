import os
from dotenv import find_dotenv, load_dotenv
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests, time, threading, random
import undetected_chromedriver as uc


def pushNotification():
    requests.post('https://api.pushover.net/1/messages.json', {
    "token": os.getenv('API_TOKEN'),
    "user": os.getenv('API_USER'),
    "message": "DRIVING TEST FOUND",
    "url" : "https://driverpracticaltest.dvsa.gov.uk/login",
    "priority" : "1"
})
    
def checkForTest():
    driver = uc.Chrome()
    
    driver.get("https://driverpracticaltest.dvsa.gov.uk/login")

    try:
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID,"driving-licence-number"))).send_keys(os.getenv('DRIVING_LICENSE_NUMBER'))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID,"application-reference-number"))).send_keys(os.getenv('DRIVING_TEST_REFERENCENUMBER'))

        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID,"booking-login"))).click()

        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID,"short-notice-slots-view"))).click()

        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID,"postcode-input"))).send_keys(os.getenv('POSTCODE'))

        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID,"test-centres-submit"))).click()
    except:
        print("Imperva blocked this request")
        driver.quit()
        return

    try:
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH, '//section[@class="error-summary formatting"]')))
    except:
        pushNotification()
        print("TEST FOUND as of " +time.ctime())
        
    driver.close()
    driver.quit()
    


def startTimer():
    checkForTest()
    print("Checking for test as of " +time.ctime())
    threading.Timer(random.randint(1800,1900), startTimer).start()


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    startTimer()