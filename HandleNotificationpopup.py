import time

from selenium import  webdriver

# Chrome option specify the browser level setting
# 1 . Handle popups
# 2. headless

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=ops)
driver.get("https://whatmylocation.com/")
driver.maximize_window()
time.sleep(10)
