Here are more examples using a **Login Page** scenario:

---

## HTML Structure (imagine this is a login page)
```html
<input id="email" name="user-email" class="form-input" type="email" placeholder="Enter Email">
<input id="password" name="user-pass" class="form-input" type="password" placeholder="Enter Password">
<button id="loginBtn" class="btn-login">Login</button>
<a href="/forgot">Forgot Password?</a>
<a href="/register">Create New Account</a>
```

---

## 1. By.ID
```python
driver.find_element(By.ID, "email")
driver.find_element(By.ID, "password")
driver.find_element(By.ID, "loginBtn")
```

---

## 2. By.NAME
```python
driver.find_element(By.NAME, "user-email")
driver.find_element(By.NAME, "user-pass")
```

---

## 3. By.XPATH
```python
# by id
driver.find_element(By.XPATH, "//input[@id='email']")

# by type
driver.find_element(By.XPATH, "//input[@type='password']")

# by placeholder
driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")

# by button text
driver.find_element(By.XPATH, "//button[text()='Login']")
```

---

## 4. By.CLASS_NAME
```python
driver.find_element(By.CLASS_NAME, "btn-login")
driver.find_elements(By.CLASS_NAME, "form-input")  # returns both inputs as list
```

---

## 5. By.TAG_NAME
```python
driver.find_element(By.TAG_NAME, "button")   # finds Login button
driver.find_elements(By.TAG_NAME, "input")   # returns all inputs as list
driver.find_elements(By.TAG_NAME, "a")       # returns all links as list
```

---

## 6. By.LINK_TEXT
```python
driver.find_element(By.LINK_TEXT, "Forgot Password?")
driver.find_element(By.LINK_TEXT, "Create New Account")
```

---

## 7. By.PARTIAL_LINK_TEXT
```python
driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot")       # matches "Forgot Password?"
driver.find_element(By.PARTIAL_LINK_TEXT, "Create")       # matches "Create New Account"
driver.find_element(By.PARTIAL_LINK_TEXT, "Account")      # matches "Create New Account"
```

---

## 8. By.CSS_SELECTOR
```python
driver.find_element(By.CSS_SELECTOR, "#email")                    # by id
driver.find_element(By.CSS_SELECTOR, "#password")                 # by id
driver.find_element(By.CSS_SELECTOR, ".btn-login")                # by class
driver.find_element(By.CSS_SELECTOR, "input[type='email']")       # by attribute
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Password']")
```

---

## Full Login Script using all locators
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://your-login-page.com")
time.sleep(2)

# type email — using ID
driver.find_element(By.ID, "email").send_keys("sabya@gmail.com")

# type password — using NAME
driver.find_element(By.NAME, "user-pass").send_keys("mypassword")

# click login — using XPATH
driver.find_element(By.XPATH, "//button[text()='Login']").click()

time.sleep(3)
driver.quit()
```

---

## Key difference — `find_element` vs `find_elements` 🎯

| Method | Returns | Use when |
|---|---|---|
| `find_element` | Single element | You want one specific element |
| `find_elements` | List of elements | Multiple elements with same locator |