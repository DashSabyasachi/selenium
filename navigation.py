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


# css and selenium selectors uses
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.maximize_window()
name_box=driver.find_element(By.ID,'autocomplete'
                             )
name_box.send_keys('Australia')
time.sleep(2)

name_box.clear()
time.sleep(1)

name_box.send_keys('India')
driver.find_element(By.XPATH,"//input[@value='radio2']").click()
time.sleep(1)

checkbox=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/fieldset/label[3]/input')
checkbox.click()
time.sleep(1)

heading=driver.find_element(By.TAG_NAME,'h1').text
print(heading)

place_name=name_box.get_attribute('class')
print(place_name)

textbox=driver.find_element(By.ID,'displayed-text')
print('Before hide:',textbox.is_displayed())

driver.find_element(By.ID,'hide-textbox').click()
time.sleep(1)

print('After hide:',textbox.is_displayed())
driver.find_element(By.ID,'show-textbox').click()
time.sleep(1)

print('Textbox enable:',textbox.is_enabled())
print('Checkbox selected:',checkbox.is_selected())
time.sleep(2)
driver.quit()




























