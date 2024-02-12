import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# 1) select specific checkbox
#driver.find_element(By.XPATH,"//input[@id='monday']").click()

# 2) select all checkboxes

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

# Approach 1

# for i in range (len(checkboxes)):
#     checkboxes[i].click()

# Approach 2

# for checkbox in checkboxes:
#     checkbox.click()

# Approach select multiple checkbox by choice

for checkbox in checkboxes:
    weekname = checkbox.get_attribute('id')
    if weekname == 'sunday' or weekname == 'monday':
        checkbox.click()


time.sleep(5)