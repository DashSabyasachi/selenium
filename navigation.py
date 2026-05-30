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


















