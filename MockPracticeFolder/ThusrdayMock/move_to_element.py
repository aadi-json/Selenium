from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
action = ActionChains(driver)
driver.get("https://demowebshop.tricentis.com/")
last_ele=driver.find_element(By.LINK_TEXT,"Contact us")
time.sleep(2)
action.move_to_element(last_ele).perform()