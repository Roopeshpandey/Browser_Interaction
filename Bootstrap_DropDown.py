import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
countrylist = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countrylist))

for country in countrylist:
    if country.text == "India":
        country.click()
        break


time.sleep(10)