import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")

driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

time.sleep(2)
outer_frame = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame)

time.sleep(2)
inner_frame = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_frame)

time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("welcome")
