import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# driver.get("https://demo.nopcommerce.com/")

# for opening link to new tab

# driver.find_element(By.LINK_TEXT,"Register").click()
#
# regiskey = Keys.CONTROL + Keys.ENTER
# driver.find_element(By.LINK_TEXT,"Register").send_keys(regiskey)

# for opening tabs in new window
#
# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.new_window("tab")
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# for opening in new window

# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.new_window("tab")
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


time.sleep(5)
