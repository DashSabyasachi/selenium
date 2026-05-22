
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


## 1. By.ID
# ```python
# driver.find_element(By.ID, "autocomplete")
# driver.find_element(By.ID, "name")
# driver.find_element(By.ID, "alertbtn")
# driver.find_element(By.ID, "confirmbtn")
# ```
#
# ---
#
# ## 2. By.NAME
# ```python
# driver.find_element(By.NAME, "enter-name")
# ```
#
# ---
#
# ## 3. By.XPATH
# ```python
# driver.find_element(By.XPATH, "//input[@id='autocomplete']")
# driver.find_element(By.XPATH, "//input[@name='enter-name']")
# driver.find_element(By.XPATH, "//input[@type='button'][@id='alertbtn']")
# driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']")
# ```
#
# ---
#
# ## 4. By.CLASS_NAME
# ```python
# driver.find_element(By.CLASS_NAME, "inputs")
# ```
#
# ---
#
# ## 5. By.TAG_NAME
# ```python
# driver.find_element(By.TAG_NAME, "input")   # finds first input on page
# driver.find_element(By.TAG_NAME, "select")  # finds the dropdown
# ```
#
# ---
#
# ## 6. By.LINK_TEXT
# ```python
# driver.find_element(By.LINK_TEXT, "Home")
# driver.find_element(By.LINK_TEXT, "Practice")
# ```
#
# ---
#
# ## 7. By.PARTIAL_LINK_TEXT
# ```python
# driver.find_element(By.PARTIAL_LINK_TEXT, "Prac")   # matches "Practice"
# driver.find_element(By.PARTIAL_LINK_TEXT, "Log")    # matches "Login"
# ```
#
# ---
#
# ## 8. By.CSS_SELECTOR
# ```python
# driver.find_element(By.CSS_SELECTOR, "#autocomplete")        # by id
# driver.find_element(By.CSS_SELECTOR, ".inputs")              # by class
# driver.find_element(By.CSS_SELECTOR, "input[name='enter-name']")  # by attribute
# ```
#
# ---
#
# ## Quick Reference 🎯
#
# | Locator | When to use |
# |---|---|
# | `By.ID` | Element has unique id |
# | `By.NAME` | Element has name attribute |
# | `By.XPATH` | Complex/flexible targeting |
# | `By.CLASS_NAME` | Element has class attribute |
# | `By.TAG_NAME` | Find by HTML tag |
# | `By.LINK_TEXT` | Exact anchor text |
# | `By.PARTIAL_LINK_TEXT` | Partial anchor text |
# | `By.CSS_SELECTOR` | CSS-style targeting |