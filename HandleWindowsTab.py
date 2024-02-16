import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Every time window ID different
# window_id  = driver.current_window_handle
# print(window_id)    #7DA73601BA139E7EF01EBC3EEFFEE759
                    #00857FA9B1243ACBCEB9922EB4BD4D35
time.sleep(5)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

time.sleep(5)

window_id  = driver.window_handles
# parentid = window_id[0]
# childid = window_id[1]
#
# print(parentid,childid)
#
# driver.switch_to.window(childid)
# print("Title of the child window : ",driver.title)
#
# driver.switch_to.window(parentid)
# print("Title of the parent window : ",driver.title)


# Approach 2
#
# for id in window_id:
#     driver.switch_to.window(id)
#     print(driver.title)

# Approach 3
# for id in window_id:
#     driver.switch_to.window(id)
#     if driver.title == "orange HRM":
#         driver.close()