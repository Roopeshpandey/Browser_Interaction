import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

# store XPATH in drpCountry_ele and pass to select class

# drpCountry_ele = driver.find_element(By.XPATH,"//select[@id='input-country']")
# drpCountry = Select(drpCountry_ele)

# we can also directly pass to select class
drpCountry = Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))


#  drpCountry.select_by_visible_text('india')  #by Text
#  drpCountry.select_by_value('10')  #by value
#  drpCountry.select_by_index(10)  #by index

# capture all the options and print them

all_options  = drpCountry.options
print("total options : ", len(all_options))

for options in all_options:
    print(options.text)

# select options from dropdown without using buit in method

for options in all_options:
    if options.text == 'india':
        options.click()
        break

# if in tag name options is not present

all_opt  = driver.find_elements(By.XPATH,"//*[@id='input-country']/option")
print(len(all_opt))


time.sleep(5)

