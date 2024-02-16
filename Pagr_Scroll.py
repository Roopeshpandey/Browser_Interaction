import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# 1) Approach Scroll down page by pixel

# driver.execute_script("window.scrollBy(0,3000)","")
# value = driver.execute_script("return window.pageYOffset;")
# print("Page Scroll by pixel : " , value)

# 2) Scroll down the page till element is visible

# flag = driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("Page Scroll by pixel : " , value)
#
# time.sleep(10)

# 3) Scroll down page till end

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)

# Scroll up to starting position

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Page Scroll by pixel : " , value)
time.sleep(5)


