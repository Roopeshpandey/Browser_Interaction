import time

from selenium import webdriver
from selenium.webdriver.common.by import By

location = r"C:\Users\Roope\OneDrive\Desktop\Study_Matterial\Manual Testing\Software Development Life Cycle (SDLC).docx"
driver = webdriver.Chrome()
driver.get("https://www.4shared.com/")
driver.maximize_window()

upload_files = driver.find_element(By.XPATH,"//*[@id='fid0']").send_keys(location)

time.sleep(10)