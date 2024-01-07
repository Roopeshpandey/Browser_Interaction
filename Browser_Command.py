# Browser Commands

# close()
# quit()


#  It will close only current tab / or you can say tab on which driver is focused
# close()

# It will kill the process and closed multiple tab as well as Kill the driver
# quit()



import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(5)

# It will close only current tab / or you can say tab on which driver is focused
driver.close()


# It will kill the process and closed multiple tab as well as Kill the driver
driver.quit()

time.sleep(5)