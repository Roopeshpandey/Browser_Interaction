import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd()


def Chrome_setup():
    preference  = { "download.default_directory":location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preference)
    driver = webdriver.Chrome(options=ops)
    return driver

def edge_setup():
    preference  = { "download.default_directory":location}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",preference)
    driver = webdriver.Edge(options=ops)
    return driver

def firefox_setup():
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting",False)
    ops.set_preference("browser.download.folderList",2) # 0- Desktop ,1-download folder , 2 -Desired Location
    ops.set_preference("browser.download.dir",location)
    driver = webdriver.Firefox(options=ops)
    return driver

driver = Chrome_setup()
#driver = edge_setup()
# driver= firefox_setup()

driver.implicitly_wait(10)
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
iframe = driver.find_element(By.ID, "aswift_1")
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH,'//tbody/tr[1]/td[5]/a[1]').click()


time.sleep(30)