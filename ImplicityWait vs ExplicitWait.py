from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# driver.get("https://www.google.co.in/")
#
# driver.find_element(By.XPATH,"//textarea[@id ='APjFqb']").send_keys("selenium")
# driver.find_element(By.XPATH,"//input[@type ='submit']").click()
# driver.find_element(By.XPATH,"//h3[text() ='Selenium']").click()
#
# driver.quit()


# <------------------------------------------------------------------------>

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://www.google.com/")
search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
search_box.send_keys("selenium")

# Use element_to_be_clickable to wait for the search button to be clickable
search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
search_button.click()

search_link = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
search_link.click()

# Close the browser window
driver.quit()







