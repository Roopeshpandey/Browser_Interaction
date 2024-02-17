from selenium import webdriver
import os

#src_path = r"C:\Users\Roope\OneDrive\Desktop\Study_Matterial\Python_Projects\Selenium Mini Projects\Browser_Interaction\homepage.png"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")

# this both method work same 
driver.save_screenshot(os.getcwd()+"\\homepage.png")
driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")


# this both method take screenshot as Binary code and we have to convert in Image file by code
driver.get_screenshot_as_png()
driver.get_screenshot_as_base64()