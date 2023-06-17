from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(
    r"C:\Users\adaml\Documents\python\
    selenium-python\chromedriver.exe"
)
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "email").send_keys("hello@example.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# CSS - tagname[attribute='value'] -? input[type='submit'], #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Adam")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
# Xpath - //tagname[@attribute='value'] -? //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
msg = driver.find_element(By.CLASS_NAME, "alert-success").text
print(msg)
assert "Success" in msg

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
    "Hello Again!"
)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
