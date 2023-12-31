from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/documentation/overview/")
Title = driver.title
Url = driver.current_url
page_source = driver.page_source

print(Title)
print(Url)
print(page_source)

