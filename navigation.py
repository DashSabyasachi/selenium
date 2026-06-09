# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver=webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("https://google.com")
# time.sleep(2)    #to hold an action we use this
#
# driver.get("https://amazon.in")
# driver.minimize_window()
# time.sleep(2)
#
# driver.back()
# time.sleep(2)
#
# driver.forward()
# time.sleep(1)
#
# driver.refresh()
# time.sleep(1)




# ......
# driver=webdriver.Chrome()
# driver.maximize_window()

# driver.get("https://amazon.in")
# driver.minimize_window()
# time.sleep(2)



# # xpath assignment
# driver = webdriver.Chrome()
# driver.maximize_window()
# time.sleep(5)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# autocomplete_xpath  = driver.find_element(By.XPATH,"//input[@id='autocomplete']")
# print("Autocomplete found by XPATH:", autocomplete_xpath.get_attribute("id"))
#
# autocomplete_id = driver.find_element(By.ID, "autocomplete")
# print("Autocomplete found by ID:", autocomplete_id.get_attribute("id"))
#
# time.sleep(2)
#
#
# name_xpath = driver.find_element(By.XPATH,"//input[@id='name']")
# print("Name input found by XPATH:", name_xpath.get_attribute("id"))
#
#
# name_by_name = driver.find_element(By.NAME, "enter-name")
# print("Name input found by NAME:", name_by_name.get_attribute("name"))
#
# time.sleep(2)
#
# driver.quit()


# #css and selenium selectors uses
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get('https://rahulshettyacademy.com/AutomationPractice/')
#
# driver.maximize_window()
# name_box=driver.find_element(By.ID,'autocomplete'
#                              )
# name_box.send_keys('Australia')
# time.sleep(2)
#
# name_box.clear()
# time.sleep(1)
#
# name_box.send_keys('India')
# driver.find_element(By.XPATH,"//input[@value='radio2']").click()
# time.sleep(1)
#
# checkbox=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/fieldset/label[3]/input')
# checkbox.click()
# time.sleep(1)
#
# heading=driver.find_element(By.TAG_NAME,'h1').text
# print(heading)
#
# place_name=name_box.get_attribute('class')
# print(place_name)
#
# textbox=driver.find_element(By.ID,'displayed-text')
# print('Before hide:',textbox.is_displayed())
#
# driver.find_element(By.ID,'hide-textbox').click()
# time.sleep(1)
#
# print('After hide:',textbox.is_displayed())
# driver.find_element(By.ID,'show-textbox').click()
# time.sleep(1)
#
# print('Textbox enable:',textbox.is_enabled())
# print('Checkbox selected:',checkbox.is_selected())
# time.sleep(2)
# driver.quit()



# # # Assignment ( Full automation for Facebook login )
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# # Step 1: Open Chrome
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# # Step 2: Open Facebook login page
# driver.get("https://www.facebook.com/login/")
# time.sleep(3)
#
# # Step 3: Enter email
# email = driver.find_element(By.NAME, "email")
# email.clear()
# email.send_keys("sabyasachidash2017@gmail.com")   # replace with your email
# time.sleep(1)
#
# # Step 4: Enter password
# password = driver.find_element(By.NAME, "pass")
# password.clear()
# password.send_keys("01a4853")       # replace with your password
# time.sleep(1)
#
# # Step 5: Click Login button
# driver.find_element(By.XPATH, "//span[text()='Log in']")
#
# driver.find_element(By.XPATH, "//span[text()='Log in']").click()
# time.sleep(10)
# driver.quit()


# # Your code — just finds element, never clicks!
# driver.find_element(By.XPATH, "//span[text()='Log in']")
#
# # Fix — add .click()
# driver.find_element(By.XPATH, "//span[text()='Log in']").click()






# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# driver=webdriver.Chrome()
# driver.get('https://demoga.com/text-box')
#
# wait=WebDriverWait(driver, 5)
# textbox=wait.until(EC.visibility_of_element_located((By.ID, "userName")))
#
# textbox.send_keys('sankar')
# #time.sleep(2)
# driver.quit()





'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/login/")
time.sleep(3)

# Enter email
email = driver.find_element(By.NAME, "email")
email.clear()
email.send_keys("sabyasachidash2017@gmail.com")
time.sleep(1)

# Enter password
password = driver.find_element(By.NAME, "pass")
password.clear()
password.send_keys("01a4853")
time.sleep(1)

# Click login button
driver.find_element(By.XPATH, "//span[text()='Log in']").click()
time.sleep(5)  # wait for page to load after login

# Check login success or failure
try:
    # This element only appears when logged in
    driver.find_element(By.XPATH, "//div[@aria-label='Facebook']")
    print("✅ Login Successful!")
except NoSuchElementException:
    print("❌ Login Failed! Check email or password.")

time.sleep(3)
driver.quit()
'''

# # 1. Waits
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# # Implicit Wait — applies to all find_element calls globally
# driver.implicitly_wait(10)  # waits max 10 seconds
#
# # Explicit Wait — waits for a specific element
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.presence_of_element_located((By.ID, "autocomplete")))
# print("Element found:", element.get_attribute("id"))



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
# for check single checkbox
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
# checkbox=driver.find_element(By.NAME,"checkBoxOption1")
# checkbox.click()
# print(checkbox.is_selected())
# time.sleep(2)

# for multiple checkbox
# checkboxes=driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
# for checkbox in checkboxes:
# checkbox.click()
# time.sleep(3)
# driver.quit()
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

# https://demo.automationtesting.in/Alerts.html


#
# from selenium.webdriver.support.ui import Select
#
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# dropdown = driver.find_element(By.ID, "dropdown-class-example")
# select = Select(dropdown)
#
# # Select by visible text
# select.select_by_visible_text("Option1")
#
# # Select by index
# select.select_by_index(2)
#
# # Select by value
# select.select_by_value("option2")
#
# print("Selected:", select.first_selected_option.text)





# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# # Type name and click Alert button
# driver.find_element(By.ID, "name").send_keys("Sabya")
# driver.find_element(By.ID, "alertbtn").click()
#
# # Switch to alert and accept
# alert = driver.switch_to.alert
# print("Alert text:", alert.text)
# alert.accept()  # clicks OK
#
# # Type name and click Confirm button
# driver.find_element(By.ID, "name").send_keys("Sabya")
# driver.find_element(By.ID, "confirmbtn").click()
#
# confirm = driver.switch_to.alert
# print("Confirm text:", confirm.text)
# confirm.dismiss()  # clicks Cancel




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get('https://rahulshettyacademy.com/AutomationPractice/')
#
# # Count all rows
# rows = driver.find_elements(By.XPATH, "//table[@name='courses']//tr")
# print('Rows:', len(rows))
#
# # Count all columns
# columns = driver.find_elements(By.XPATH, "//table[@name='courses']//th")
# print('Columns:', len(columns))
#
# # Print entire table
# for row in rows:
#     print(row.text)
#
# # Get specific cell value — row 5, column 3
# cell = driver.find_element(By.XPATH, "//table[@name='courses']//tr[5]/td[3]")
# print("Cell value:", cell.text)
#
# # Print all course names — column 2
# all_course = driver.find_elements(By.XPATH, "//table[@name='courses']//tr/td[2]")
# for course in all_course:
#     print(course.text)
#
# # Print first column data
# first_column_data = driver.find_elements(By.XPATH, "//table[@name='courses']//tr/td[1]")
# for col_data in first_column_data:
#     print(col_data.text)   # ← properly indented
#
# driver.quit()





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# import time
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://demoqa.com/buttons')
# button=driver.find_element(By.ID,"rightClickBtn")
#
# action=ActionChains(driver)
# action.context_click(button).perform()
# time.sleep(3)
#
# message = driver.find_element(By.ID,"rightClickMessage")
# print(message.text)
# driver.quit()




# # For Drag Drop:--→
# # ‌
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
#
# driver=webdriver.Chrome()
# driver.get("https://jqueryui.com/droppable/")
#
# # switch to frame
# frame=driver.find_element(By.CLASS_NAME,"demo-frame")
# driver.switch_to.frame(frame)
#
# drag=driver.find_element(By.ID,"draggable")
#
# drop=driver.find_element(By.ID,"droppable")
#
# actions=ActionChains(driver)
# actions.drag_and_drop(drag,drop).perform()
# time.sleep(2)



# # For File download:-→
# # ‌
# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/download")
#
# driver.find_element(By.LINK_TEXT,"random_data.txt").click()
# time.sleep(3)
#
# file_path=r"C:\Users\Admin\Downloads\random_data.txt"
# print(os.path.exists(file_path))
#
# driver.quit()



# # For Fileupload:--→
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/upload")
#
# driver.find_element(By.ID,"file-upload").send_keys(r"C:\Users\Admin\Documents\19_intro.txt")
# time.sleep(3)
# driver.find_element(By.ID,"file-submit").click()
# time.sleep(3)
# driver.quit()



# #For Screenshot:-→
# # ‌
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
#
# driver.get(
# "https://rahulshettyacademy.com/AutomationPractice/"
# )
#
# # driver.save_screenshot('homepage.png')
# text_box=driver.find_element(By.ID,"name")
# text_box.screenshot(r"C:\Users\Admin\PycharmProjects\PythonProject\screenshot\text.png")
# time.sleep(2)
# driver.quit()


