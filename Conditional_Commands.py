# Conditional Command

# is_enabled()
# is_displayed()
# is_selected()


# is _selected is generally used for radio button / check box



from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")

searchBox = driver.find_element(By.XPATH,"//input[@id ='small-searchterms' ]")
print (f"Displayed: " , searchBox.is_displayed())
print(f"Enabled: " , searchBox.is_enabled())

rd_male = driver.find_element(By.XPATH,"//input[@id = 'gender-male']")
rd_female = driver.find_element(By.XPATH,"//input[@id = 'gender-female']")

print(f"Default Randio Button Status")

print(f"Male Buttom Status : ", rd_male.is_selected())
print(f"Female Buttom Status : ", rd_female.is_selected())

print(f"Default Randio Button Status After clicking on radio male button")

rd_male.click()

print(f"Male Buttom Status : ", rd_male.is_selected())
print(f"Female Buttom Status : ", rd_female.is_selected())

print(f"Default Randio Button Status After clicking on radio female button")

rd_female.click()

print(f"Male Buttom Status : ", rd_male.is_selected())
print(f"Female Buttom Status : ", rd_female.is_selected())
