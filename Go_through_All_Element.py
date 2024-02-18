import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")

yr = "2026"
mon = "November"
Date = "19"

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Roopesh Pandey")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Roopeshpandey@gmail.com")
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("123456789")
driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys("Noida")
male_button = driver.find_element(By.XPATH,"//input[@id= 'male']")
if male_button.is_displayed() and male_button.is_enabled() :
    male_button.click()

weekdays =  driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id, 'day')]")

for weekday in weekdays:
    weekname= weekday.get_attribute('id')
    if weekname == "tuesday":
        weekday.click()

dropdown_country = Select(driver.find_element(By.XPATH,"//select[@id='country']"))
dropdown_country.select_by_visible_text("India")

dropdown_colors = Select(driver.find_element(By.XPATH,"//select[@id='colors']"))
dropdown_colors.select_by_visible_text("Blue")


datepicker = driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True :
    month = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    year = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH,"//span[normalize-space() = 'Next']").click()


date = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")
for d in date :
    if d.text == Date:
        d.click()
        break

driver.find_element(By.XPATH,"//button[normalize-space()='Alert']").click()
Alert_popup =  driver.switch_to.alert
Alert_popup.accept()

driver.find_element(By.XPATH,"//button[normalize-space()='Confirm Box']").click()
Confirm_Box =  driver.switch_to.alert
Confirm_Box.dismiss()

driver.find_element(By.XPATH,"//button[normalize-space()='Prompt']").click()
Prompt =  driver.switch_to.alert
Prompt.send_keys("done")
Prompt.accept()

time.sleep(10)

