# switch_to.frame
#
# switch_to.frame(name of the frame)
# switch_to.frame(id of frame)
# switch_to.frame(webelement)
# switch_to.frame(index of frame)

#
# Note : Driver cannot switch to
# one frame to another frame first we need to go to base frame

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.maximize_window()

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.switch_to.default_content()    # it will take you to main page

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"Webdriver").click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"org.openqa.selenium").click()

