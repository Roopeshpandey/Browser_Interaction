import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0)
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/12/2023")  # By send keys
#time.sleep(3)

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
time.sleep(3)


year = "2024"
month = "December"
date = "30"

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon == month and yr==year :
        break
    else:
        driver.find_element(By.XPATH,"//span[normalize-space() = 'Next']").click()
        # driver.find_element(By.XPATH, "//span[normalize-space() = 'Prev']").click()    # For Previous Click

dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")

for ele in dates:
    if ele.text == date:
        ele.click()
        break



time.sleep(10)