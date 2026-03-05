from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
action = ActionChains(driver)
driver.get("https://demo.automationtesting.in/Static.html")
sym=driver.find_element(By.ID,"angular")
drp=driver.find_element(By.ID,"droparea")
action.drag_and_drop(sym,drp).perform()
time.sleep(2)
action.click_and_hold(sym).release(drp).perform()  
