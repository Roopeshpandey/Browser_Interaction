import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

# login to page
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)

# Navigate to Admin <<< user management >>> User

driver.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Users']").click()
time.sleep(3)

# total row in a table

rows = len(driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']/div"))
print(rows)

count = 0
for r in range(1,rows+1):
    status= driver.find_element(By.XPATH,"//div[@class='oxd-table-body']/div["+str(r)+"]/div/div[5]").text
    print(status)
    if status == "Disabled":
        count += 1

print("total no of rows : ", rows)
print("total no of Disabled : ", count)
print("total no of enabled : ", rows-count)
