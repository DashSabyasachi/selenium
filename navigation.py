from selenium import webdriver
import time

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
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://amazon.in")
driver.minimize_window()
time.sleep(2)

driver.find_element(By.class, value: 'ap-locale-en_US a-m-us a-aui_72554-c a-aui_template_weblab_cache_333406-c a-meter-animate')

