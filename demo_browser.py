from selenium import webdriver

# chrome_driver
from selenium.webdriver.chrome.service import Service

service_obj = Service(
    r"C:\Users\adaml\Documents\python\
    selenium-python\chromedriver.exe"
)
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/selemiumPractice/#/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
