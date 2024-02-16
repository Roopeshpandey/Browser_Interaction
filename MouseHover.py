
# ActionsChains


# Mouse Hover
# Right Click
# Double click
# Drag & Drop





import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



# ----------->>>>>>>>>   Mouse Hover  <<<<<<<<<<<<<<<---------


# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(3)
#
# # login to page
# driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
# driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# time.sleep(3)
#
# # Navigate to Admin <<< user management >>> User
#
# admin = driver.find_element(By.XPATH, "//span[normalize-space()='Admin']")
# user_management = driver.find_element(By.XPATH, "//span[normalize-space()='User Management']")
# users = driver.find_element(By.XPATH, "//a[normalize-space()='Users']")
#
# act = ActionChains(driver)
# act.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()



# ----------->>>>>>>>>    Right Click on element   <<<<<<<<<<<<<<<---------


# driver = webdriver.Chrome()
# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# button = driver.find_element(By.XPATH,"//span[normalize-space()='right click me']")
#
# act = ActionChains(driver)
# act.context_click(button).perform()

# ----------->>>>>>>>>    Double Click on element   <<<<<<<<<<<<<<<---------

# driver = webdriver.Chrome()
# driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")
#
# driver.switch_to.frame("iframeResult")
# doubleClick_button = driver.find_element(By.XPATH,"//button[normalize-space()='Double-click me']")
#
# act  = ActionChains(driver)
# act.double_click(doubleClick_button).perform()
# time.sleep(3)


# ----------->>>>>>>>>    Drag & Drop  element   <<<<<<<<<<<<<<<---------

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

source_ele = driver.find_element(By.XPATH,"//div[@id='draggable']")
target_ele = driver.find_element(By.XPATH,"//div[@id='droppable']")

act = ActionChains(driver)
act.drag_and_drop(source_ele,target_ele).perform()
time.sleep(5)