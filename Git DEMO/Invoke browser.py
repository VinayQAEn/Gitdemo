from selenium import webdriver
driver = webdriver.Chrome()
driver.get("www.google.com")
driver.maximize_window()
driver.implicitly_wait(10)