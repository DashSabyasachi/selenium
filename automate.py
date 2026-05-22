from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)

# ---- Element 1: Autocomplete ----
autocomplete = driver.find_element(By.ID, "autocomplete")
autocomplete.send_keys("Ind")   # ← types "Ind" in the box — you'll SEE this!
time.sleep(2)

# ---- Element 2: Name Input ----
name_input = driver.find_element(By.NAME, "enter-name")
name_input.send_keys("Sabya")   # ← types "Sabya" in the box — you'll SEE this!
time.sleep(2)

# ---- Click Alert button ----
driver.find_element(By.ID, "alertbtn").click()   # ← alert popup will appear!
time.sleep(2)
alert = driver.switch_to.alert
print("Alert says:", alert.text)
alert.accept()   # ← clicks OK on the popup

time.sleep(3)
driver.quit()