# Text vs GetAttribute

# text
# GetAttribute()

# Text Only return inner text of the element

# GetAttribute()  Returns value of any Attribute of Web Element



from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

Email_box = driver.find_element(By.XPATH,"//input[@id = 'Email']")

Email_box.clear()
Email_box.send_keys("abc@gmai.com")

# Only return inner text of the element
print(f"result of text",Email_box.text)

# Returns value of any Attribute of Web Element
print(f"result of get attribute",Email_box.get_attribute('value'))