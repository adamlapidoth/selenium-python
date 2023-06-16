from selenium import webdriver

# chrome_driver
from selenium.webdriver.chrome.service import Service

service_obj = (
    Service(r"C:\Users\adaml\Documents\python\
    selenium-python\chromedriver.exe")
)
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.close()
