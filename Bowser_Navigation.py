# Browser Navigation

# maximize_window()
# get()
# refresh()
# back()
# forward()



import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.XPATH,"//a[text()='A/B Testing']").click()
driver.refresh()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()


print(f"Successfull :{driver.title} ")
