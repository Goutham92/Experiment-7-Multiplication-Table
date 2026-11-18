
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://localhost:8082")

number = driver.find_element(By.ID, "number")
number.send_keys("7")

button = driver.find_element(By.TAG_NAME, "button")
button.click()

result = driver.find_element(By.ID, "result")

assert "7 x 1 = 7" in result.text
assert "7 x 10 = 70" in result.text

print("Selenium Test Passed!")

driver.quit()
