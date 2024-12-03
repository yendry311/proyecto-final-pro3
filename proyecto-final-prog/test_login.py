from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = 'C:\Program Files\Mozilla Firefox'

driver_path =r"C:\Users\Admin\Desktop\geckodriver-v0.33.0-win64\geckodriver.exe"


service = Service(driver_path)

driver = webdriver.Firefox(service=service, options=options)

driver.get("http://127.0.0.1:5000/login")
print(driver.title)
driver.quit()
