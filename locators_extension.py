from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

EMAIL = "demo@gmail.com"

PASSWORD = "123456"

service_obj = Service(
    r"C:\Users\adaml\Documents\python\
    selenium-python\chromedriver.exe"
)
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys(EMAIL)
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys(
    PASSWORD
)
driver.find_element(By.ID, "confirmPassword").send_keys(PASSWORD)
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
