import time

# to handle this type of Authentication popup there is a syntax
# https://the-internet.herokuapp.com/basic_auth

# syntax  = https://username:password@test.com
#
# for example:
#
#     http://admin:admin@the-internet.herokuapp.com/basic_auth


from selenium import webdriver

driver  = webdriver.Chrome()

# driver.get("http://the-internet.herokuapp.com/basic_auth")

driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(5)