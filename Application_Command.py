
# Application command

# get () - opening the application URL
# title - to capture teh title of the curretn webpage
# current_url - to capture the current url of the webpage
# page_source - to capture source code of the page



from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/documentation/overview/")
Title = driver.title
Url = driver.current_url
page_source = driver.page_source

print(Title)
print(Url)
print(page_source)

