#Script to launch whatsappweb using selenium

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print (driver.title)
