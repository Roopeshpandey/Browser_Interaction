from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1) Count number of rows and colums

noOfRows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
noOfColoums = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th"))

print(noOfRows)
print(noOfColoums)

# 2) Read specific row & column data - master in selenium
#
# data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text
# print(data)

# 3) Read all rows and column data

# for r in range(2,noOfRows+1):
#     for c in range(1,noOfColoums+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end="              ")
#     print()

# 4) Read data Based on Condition(List book namewhose author is mukesh)
#
# for r in range(2,noOfRows+1):
#     author =driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
#     if author == "Mukesh":
#         bookname = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
#         print( author ,"    ", bookname)
