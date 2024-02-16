import time

from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

slider = driver.find_element(By.XPATH,"//span[@class = 'ui-slider-handle ui-corner-all ui-state-default']")

print(slider.location)

act = ActionChains(driver)
act.drag_and_drop_by_offset(slider,100,0).perform()
time.sleep(5)
print(slider.location)



