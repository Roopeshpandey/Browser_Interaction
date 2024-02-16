import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")

input1 = driver.find_element(By.XPATH,"//textarea[@id= 'inputText1']")
input2 = driver.find_element(By.XPATH,"//textarea[@id= 'inputText2']")

input1.send_keys("welcome to selenium")

act =ActionChains(driver)
# in multiple line
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

# in single line
#act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# in multiple line
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()


#act.key_down(Keys.CONTROL).send_keys("c").key_down(Keys.CONTROL).perform()

act.send_keys(Keys.TAB).perform()

# in multiple line
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()

#act.key_down(Keys.CONTROL).send_keys("v").key_down(Keys.CONTROL).perform()

time.sleep(5)

