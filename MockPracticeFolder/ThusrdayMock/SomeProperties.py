from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")

register_ele=driver.find_element(By.LINK_TEXT,"Register")
if register_ele.is_displayed():
    print("Yes element is displayed")
else:
    print("No element is not displayed")

driver.get("https://www.automationtesting.co.uk/buttons.html")
enabled_button=driver.find_element(By.ID,"btn_one")
if enabled_button.is_enabled():
    print("Yes it is enabled")
else:
    print("No it is not enabled")

dis_button=driver.find_element(By.ID,"btn_four")
if dis_button.is_enabled():
    print("Yes it is enabled")
else:
    print("No it is not enabled")

driver.get("https://demowebshop.tricentis.com/")
click_ele=driver.find_element(By.XPATH,"//input[@value='1']")
click_ele.click()
if click_ele.is_selected():
    print("Element is selected")
else:
    print("Element is not selected")
