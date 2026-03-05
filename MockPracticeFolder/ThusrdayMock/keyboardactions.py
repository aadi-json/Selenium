from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
action=ActionChains(driver)
action.key_down(Keys.PAGE_DOWN).perform()
sleep(2)
action.key_down(Keys.PAGE_UP).perform()

for i in range(6):
    action.key_down(Keys.TAB).perform()
action.send_keys("mobile").perform()
