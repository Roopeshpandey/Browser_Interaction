import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")

time.sleep(5)
#click on download By Link Text
driver.find_element(By.LINK_TEXT,"Digital downloads").click()

#click on download By Partial Link Text
#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital")


#find number of links on page
links = driver.find_elements(By.TAG_NAME,"a")
print("total number of links : ",len(links))

#print link name

for link in links:
    print(link.text)

time.sleep(5)
