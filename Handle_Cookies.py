import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
cookies  = driver.get_cookies()
print("size of cookies : " , len(cookies))

# for c in cookies:
#     # print(c)
#     print(c.get('name') ,':' , c.get('value'))

# Adding new cookies

driver.add_cookie({"name":"roopesh", "value":"12345"})
cookies  = driver.get_cookies()
print("size of cookies after adding cookies : " , len(cookies))

# delete cookies

driver.delete_cookie("roopesh")
cookies  = driver.get_cookies()
print("size of cookies after deleting cookies : " , len(cookies))

# delete all cookies

driver.delete_all_cookies()
cookies  = driver.get_cookies()
print("size of cookies after deleting cookies : " , len(cookies))