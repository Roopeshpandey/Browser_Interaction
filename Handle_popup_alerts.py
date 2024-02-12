
# Alert and popups
#
# myalert = driver.switch_to.alert
#
# myalert.text
# myalert.sendkeys
# myalert.accept()
# mylaert.dismiss()
# <---------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# open alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()

# to handle alert we need to use switch_to method

alert_window = driver.switch_to.alert

# to print alert message
print(alert_window.text)

# to send keys to alert
alert_window.send_keys("welcome")

# to accept and cancel we use
alert_window.accept()
# alert_window.dismiss()
